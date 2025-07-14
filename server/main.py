from fastapi import FastAPI, UploadFile, File
from fastapi.middleware.cors import CORSMiddleware
from dotenv import load_dotenv
import pandera as pa
import pandas as pd

from typing import List, Dict, Tuple, Callable, Optional
from pathlib import Path
import io
import os

import util.table_meta_office as office_obj
import util.table_parse as office_fn
from util.db_mod import RsquareFeeder

load_dotenv(".env.server")
app = FastAPI()
feeder = RsquareFeeder(
    user=os.getenv("ID"),
    password=os.getenv("PW"),
    host=os.getenv("HOST"),
    port=os.getenv("PORT"),
    dbname=os.getenv("DBNAME")
)

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

FILENAME_MAP: Dict[
    str, 
    Optional[Tuple[
        pa.DataFrameModel,  # Model for dataframe
        Callable[[pd.DataFrame, pa.DataFrameModel], pd.DataFrame],  # CSV parsing function
        str,  # Schema
        str,  # Table name
        List[str],  # PKs
    ]]
] = {
    # 시트: 임대시장통계(5구분)
    # "오피스_0.csv": (office_obj.OfficeTable1, office_fn.office_parse_5size, "rsquare", "rsquare_office_0", ["year", "quarter", "district", "size"]),
    
    # 시트: 임대시장통계(3구분)
    # "오피스_1.csv": (office_obj.OfficeTable2, office_fn.office_parse_3size, "rsquare", "rsquare_office_1", ["year", "quarter", "district", "size"]),

    # 시트: 임대차사례
    "오피스_2.csv": (office_obj.OfficeTable3, office_fn.office_table_universal, "rsquare", "rsquare_office_2", None),
    
    # 시트: 임대지수
    "오피스_3.csv": (office_obj.OfficeTable4, office_fn.office_table_yearffill, "rsquare", "rsquare_office_3", ["year", "quarter"]),
    
    # 시트: 공급시장통계
    "오피스_4.csv": (office_obj.OfficeTable5, office_fn.office_table_yearffill, "rsquare", "rsquare_office_4", ["year", "quarter"]),
    "오피스_5.csv": (office_obj.OfficeTable5, office_fn.office_table_yearffill, "rsquare", "rsquare_office_5", ["year", "quarter"]),
    "오피스_6.csv": (office_obj.OfficeTable5, office_fn.office_table_yearffill, "rsquare", "rsquare_office_6", ["year", "quarter"]),
    "오피스_7.csv": (office_obj.OfficeTable5, office_fn.office_table_yearffill, "rsquare", "rsquare_office_7", ["year", "quarter"]),
    "오피스_8.csv": (office_obj.OfficeTable5, office_fn.office_table_yearffill, "rsquare", "rsquare_office_8", ["year", "quarter"]),
    "오피스_9.csv": (office_obj.OfficeTable5, office_fn.office_table_yearffill, "rsquare", "rsquare_office_9", ["year", "quarter"]),
    "오피스_10.csv": (office_obj.OfficeTable5, office_fn.office_table_yearffill, "rsquare", "rsquare_office_10", ["year", "quarter"]),
    
    # 시트: 당분기 신규공급사례
    "오피스_11.csv": (office_obj.OfficeTable6, office_fn.office_table_universal, "rsquare", "rsquare_office_11", None),
    
    # 시트: 공급예정물량
    "오피스_12.csv": None, # office.OfficeTable7

    # 시트: 매매시장통계
    "오피스_13.csv": (office_obj.OfficeTable8_1, office_fn.office_table_yearffill, "rsquare", "rsquare_office_13", ["year", "quarter"]),
    "오피스_14.csv": (office_obj.OfficeTable8_1, office_fn.office_table_yearffill, "rsquare", "rsquare_office_14", ["year", "quarter"]),
    "오피스_15.csv": (office_obj.OfficeTable8_2, office_fn.office_table_drop_col, "rsquare", "rsquare_office_15", ["year"]),
    "오피스_16.csv": (office_obj.OfficeTable8_2, office_fn.office_table_drop_col, "rsquare", "rsquare_office_16", ["year"]),
    "오피스_17.csv": (office_obj.OfficeTable8_3, office_fn.office_table_yearffill, "rsquare", "rsquare_office_17", ["year", "quarter"]),
    "오피스_18.csv": (office_obj.OfficeTable8_4, office_fn.office_table_drop_col, "rsquare", "rsquare_office_18", ["year"]),
    "오피스_19.csv": (office_obj.OfficeTable8_5, office_fn.office_table_yearffill, "rsquare", "rsquare_office_19", ["year", "quarter"]),
    "오피스_20.csv": (office_obj.OfficeTable8_5, office_fn.office_table_yearffill, "rsquare", "rsquare_office_20", ["year", "quarter"]),
    "오피스_21.csv": (office_obj.OfficeTable8_6, office_fn.office_table_yearffill, "rsquare", "rsquare_office_21", ["year", "quarter"]),
    
    # 시트: 당분기 매매사례
    "오피스_22.csv": (office_obj.OfficeTable9, office_fn.office_table_universal, "rsquare", "rsquare_office_22", None),

    # 시트: 경제지표
    "오피스_23.csv": (office_obj.OfficeTable10_1, office_fn.office_table_yearffill, "rsquare", "rsquare_office_23", ["year", "quarter"]),
    "오피스_24.csv": (office_obj.OfficeTable10_2, office_fn.office_table_yearffill, "rsquare", "rsquare_office_24", ["year", "quarter"]),
    "오피스_25.csv": (office_obj.OfficeTable10_3, office_fn.office_table_yearffill, "rsquare", "rsquare_office_25", ["year", "quarter"]),

    # 시트: 오피스 임대_Raw data
    "오피스_26.csv": (office_obj.OfficeTable11, office_fn.office_table_rent, "rsquare", "rsquare_office_26", ["year", "quarter", "code_specify"]),
}

@app.post("/upload_csv/")
async def upload_csv(file: UploadFile = File(...)):
    contents = await file.read()
    df = pd.read_csv(io.StringIO(contents.decode("utf-8")), header=None)

    filename = file.filename  # 원본 파일 이름 사용

    try:
        proc = FILENAME_MAP.get(filename, None)
        if proc is None:
            return {"status": "not processed. no handlers", "filename": filename}
        dtype, fn, schema, table_name, pks = proc
        result = fn(df, dtype)
    
    except Exception as e:
        path = Path("saved") / f"not_parsed_{filename}"
        path.parent.mkdir(exist_ok=True)
        df.to_csv(path, index=False)

        return {"status": f"not parsed: {e}", "filename": f"not_parsed_{filename}"}
    
    else:
        path = Path("saved") / filename
        path.parent.mkdir(exist_ok=True)
        # result.to_csv(path, index=False)
        feeder.update_panel(result, schema, table_name, pks)

    return {"status": "saved", "filename": filename}