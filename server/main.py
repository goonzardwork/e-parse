from fastapi import FastAPI, UploadFile, File
from fastapi.middleware.cors import CORSMiddleware
import pandas as pd
import pandera as pa
import util.table_meta_office as office_obj
import util.table_parse as office_fn
from typing import Dict, Tuple, Callable
from pathlib import Path
import io

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

FILENAME_MAP: Dict[
    str, 
    Tuple[
        pa.DataFrameModel, 
        Callable[[pd.DataFrame, pa.DataFrameModel], pd.DataFrame]
    ]
] = {
    # 시트: 임대시장통계(5구분)
    "오피스_0.csv": (office_obj.OfficeTable1, office_fn.office_parse_1),
    
    # 시트: 임대시장통계(3구분)
    "오피스_1.csv": (office_obj.OfficeTable2, office_fn.office_parse_2),

    # 시트: 임대차사례
    "오피스_2.csv": (office_obj.OfficeTable3, office_fn.office_table_3),
    
    # 시트: 임대지수
    "오피스_3.csv": (office_obj.OfficeTable4, office_fn.office_table_4),
    
    # 시트: 공급시장통계
    "오피스_4.csv": (office_obj.OfficeTable5, office_fn.office_table_4),
    "오피스_5.csv": (office_obj.OfficeTable5, office_fn.office_table_4),
    "오피스_6.csv": (office_obj.OfficeTable5, office_fn.office_table_4),
    "오피스_7.csv": (office_obj.OfficeTable5, office_fn.office_table_4),
    "오피스_8.csv": (office_obj.OfficeTable5, office_fn.office_table_4),
    "오피스_9.csv": (office_obj.OfficeTable5, office_fn.office_table_4),
    "오피스_10.csv": (office_obj.OfficeTable5, office_fn.office_table_4),
    
    # 시트: 당분기 신규공급사례
    "오피스_11.csv": (office_obj.OfficeTable6, office_fn.office_table_5),
    
    # 시트: 공급예정물량
    "오피스_12.csv": None, # office.OfficeTable7

    # 시트: 매매시장통계
    "오피스_13.csv": (office_obj.OfficeTable8_1, office_fn.office_table_4),
    "오피스_14.csv": (office_obj.OfficeTable8_1, office_fn.office_table_4),

    "오피스_15.csv": (office_obj.OfficeTable8_2, office_fn.office_table_5),
    "오피스_16.csv": (office_obj.OfficeTable8_2, office_fn.office_table_5),

    "오피스_17.csv": (office_obj.OfficeTable8_3, office_fn.office_table_4),
    
    "오피스_18.csv": (office_obj.OfficeTable8_4, office_fn.office_table_5),
    
    "오피스_19.csv": (office_obj.OfficeTable8_5, office_fn.office_table_4),
    "오피스_20.csv": (office_obj.OfficeTable8_5, office_fn.office_table_4),

    "오피스_21.csv": (office_obj.OfficeTable8_6, office_fn.office_table_4),
    
    # 시트: 당분기 매매사례
    "오피스_22.csv": (office_obj.OfficeTable9, office_fn.office_table_5),

    # 시트: 경제지표
    "오피스_23.csv": (office_obj.OfficeTable10_1, office_fn.office_table_4),

    "오피스_24.csv": (office_obj.OfficeTable10_2, office_fn.office_table_4),

    "오피스_25.csv": (office_obj.OfficeTable10_3, office_fn.office_table_4),

    # 시트: 오피스 임대_Raw data
    "오피스_26.csv": (office_obj.OfficeTable11, office_fn.office_table_6),
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
        dtype, fn = proc
        result = fn(df, dtype)
        
    except Exception as e:
        return {"status": f"not saved: {e}", "filename": None}

    path = Path("saved") / filename
    path.parent.mkdir(exist_ok=True)
    result.to_csv(path, index=False)

    return {"status": "saved", "filename": filename}