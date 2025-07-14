import pandas as pd
import pandera.pandas as pa
from pandera.typing import Series
from typing import get_args, get_origin
from datetime import datetime


def excel_serial_to_datetime(series: pd.Series) -> pd.Series:
    """
    Convert a Series of Excel serial dates (with possible missing or dirty values)
    to pandas datetime, allowing for NaNs and coercing errors.
    """
    # Step 1: Coerce to numeric (turns ".", "-", "", "NaN" into np.nan)
    numeric = pd.to_numeric(series, errors="coerce")

    # Step 2: Convert to datetime (NaNs remain as NaT)
    return pd.to_datetime(numeric, unit="D", origin="1899-12-30", errors="coerce")


def office_parse_1(df: pd.DataFrame, dm: pa.DataFrameModel) -> pd.DataFrame:
    if dm is None:
        raise RuntimeError("no parsing function for `df`")

    df = df.map(lambda x: x.strip() if isinstance(x, str) else x)
    df.replace({".": None, "-": None, "": None}, inplace=True)

    # 1. Target column names
    columns = list(dm.__annotations__.keys())
    
    district = ["서울", "CBD", "GBD", "YBD", "Others", "BBD"]
    size = ["전체", "초대형", "대형", "중대형", "중형", "소형"]

    yqc = ["year", "quarter"]
    repeatc = ["deposit", "rent", "utility", "vacancy_inclusive", "vacancy_exclusive", "noc"]

    # 2. Pointers that point to appropriate column numbers
    col_ptr = 2  # 0: year, 1: quarter
    segs = list()
    for d in district:
        for s in size:
            # Year and Quarter Column
            yq = df.iloc[:, 0 : 2]  
            yq.columns = yqc
            
            # Repeated Column
            seg = df.iloc[:, col_ptr : col_ptr + 6]  
            seg.columns = repeatc
            seg['size'] = s
            seg['district'] =d
            
            seg = pd.concat([yq, seg], axis=1)
            seg['year'] = seg['year'].ffill()

            segs.append(seg)
            col_ptr += 6

    my_df = pd.concat(segs)

    # 2. Coerce column types using inner_type
    type_map = {}
    for col, col_type in dm.__annotations__.items():
        if get_origin(col_type) is Series:
            inner_type = get_args(col_type)[0]
            type_map[col] = inner_type

    # 3. Apply type coercion
    for col, dtype in type_map.items():
        if dtype in [datetime, pd.Timestamp]:
            my_df[col] = excel_serial_to_datetime(my_df[col])
        elif dtype == int:
            my_df[col] = pd.to_numeric(my_df[col], errors="coerce").astype(pd.Int64Dtype())
        else:
            my_df[col] = my_df[col].astype(dtype)

    return my_df


def office_parse_2(df: pd.DataFrame, dm: pa.DataFrameModel) -> pd.DataFrame:
    if dm is None:
        raise RuntimeError("no parsing function for `df`")

    df = df.map(lambda x: x.strip() if isinstance(x, str) else x)
    df.replace({".": None, "-": None, "": None}, inplace=True)

    # 1. Target column names
    columns = list(dm.__annotations__.keys())
    
    district = ["서울", "CBD", "GBD", "YBD", "Others", "BBD"]
    size = ["전체", "대형", "중형", "소형"]

    yqc = ["year", "quarter"]
    repeatc = ["deposit", "rent", "utility", "vacancy_inclusive", "vacancy_exclusive", "noc"]

    # 2. Pointers that point to appropriate column numbers
    col_ptr = 2  # 0: year, 1: quarter
    segs = list()
    for d in district:
        for s in size:
            # Year and Quarter Column
            yq = df.iloc[:, 0 : 2].copy()
            yq.columns = yqc
            
            # Repeated Column
            seg = df.iloc[:, col_ptr : col_ptr + 6].copy()
            seg.columns = repeatc
            seg['size'] = s
            seg['district'] =d
            
            seg = pd.concat([yq, seg], axis=1)
            seg['year'] = seg['year'].ffill()

            segs.append(seg)
            col_ptr += 6

    my_df = pd.concat(segs)

    # 2. Coerce column types using inner_type
    type_map = {}
    for col, col_type in dm.__annotations__.items():
        if get_origin(col_type) is Series:
            inner_type = get_args(col_type)[0]
            type_map[col] = inner_type

    # 3. Apply type coercion
    for col, dtype in type_map.items():
        if dtype in [datetime, pd.Timestamp]:
            my_df[col] = excel_serial_to_datetime(my_df[col])
        elif dtype == int:
            my_df[col] = pd.to_numeric(my_df[col], errors="coerce").astype(pd.Int64Dtype())
        else:
            my_df[col] = my_df[col].astype(dtype)

    return my_df


def office_table_3(df: pd.DataFrame, dm: pa.DataFrameModel) -> pd.DataFrame:
    if dm is None:
        raise RuntimeError("no parsing function for `df`")

    df = df.map(lambda x: x.strip() if isinstance(x, str) else x)
    df.replace({".": None, "-": None}, inplace=True)

    # 1. Target column names
    columns = list(dm.__annotations__.keys())
    df.columns = columns

    # 2. Coerce column types using inner_type
    type_map = {}
    for col, col_type in dm.__annotations__.items():
        if get_origin(col_type) is Series:
            inner_type = get_args(col_type)[0]
            type_map[col] = inner_type

    # 3. Apply type coercion
    for col, dtype in type_map.items():
        if dtype in [datetime, pd.Timestamp]:
            df[col] = excel_serial_to_datetime(df[col])
        elif dtype == int:
            df[col] = pd.to_numeric(df[col], errors="coerce").astype(pd.Int64Dtype())
        else:
            df[col] = df[col].astype(dtype)
    return df


def office_table_4(df: pd.DataFrame, dm: pa.DataFrameModel) -> pd.DataFrame:
    if dm is None:
        raise RuntimeError("no parsing function for `df`")
    
    df = df.map(lambda x: x.strip() if isinstance(x, str) else x)
    df.replace({".": None, "-": None, "": None}, inplace=True)

    # 1. Target column names
    columns = list(dm.__annotations__.keys())
    df.columns = columns
    df["year"] = df["year"].ffill()

    # 2. Coerce column types using inner_type
    type_map = {}
    for col, col_type in dm.__annotations__.items():
        if get_origin(col_type) is Series:
            inner_type = get_args(col_type)[0]
            type_map[col] = inner_type

    # 3. Apply type coercion
    for col, dtype in type_map.items():
        if dtype in [datetime, pd.Timestamp]:
            df[col] = excel_serial_to_datetime(df[col])
        elif dtype == int:
            df[col] = pd.to_numeric(df[col], errors="coerce").astype(pd.Int64Dtype())
        else:
            df[col] = df[col].astype(dtype)

    return df


def office_table_5(df: pd.DataFrame, dm: pa.DataFrameModel) -> pd.DataFrame:
    # Used for universal purpose - no column operation needed
    if dm is None:
        raise RuntimeError("no parsing function for `df`")
    
    df = df.map(lambda x: x.strip() if isinstance(x, str) else x)
    df.replace({".": None, "-": None, "": None}, inplace=True)

    # 1. Target column names
    columns = list(dm.__annotations__.keys())
    df.columns = columns

    # 2. Coerce column types using inner_type
    type_map = {}
    for col, col_type in dm.__annotations__.items():
        if get_origin(col_type) is Series:
            inner_type = get_args(col_type)[0]
            type_map[col] = inner_type

    # 3. Apply type coercion
    for col, dtype in type_map.items():
        if dtype in [datetime, pd.Timestamp]:
            df[col] = excel_serial_to_datetime(df[col])
        elif dtype == int:
            df[col] = pd.to_numeric(df[col], errors="coerce").astype(pd.Int64Dtype())
        else:
            df[col] = df[col].astype(dtype)

    return df


def office_table_6(df: pd.DataFrame, dm: pa.DataFrameModel) -> pd.DataFrame:
    if dm is None:
        raise RuntimeError("no parsing function for `df`")
    
    df = df.map(lambda x: x.strip() if isinstance(x, str) else x)
    df.replace({".": None, "-": None, "": None}, inplace=True)

    # Common section
    common_section = 20
    columns = list(dm.__annotations__.keys())
    common_columns = columns[:common_section]
    common_df = df.iloc[:, :20]
    common_df.columns = common_columns

    # Repeated section
    y, q = 2022, 4
    repeatc = ["deposit", "rent", "utility", "rent_free", "vacant_area", "vacancy", "noc"]
    yq_count = (len(df.columns) - 20 - 1) // 7  # 20개의 고정된 Column. 1개의 비고 Column
    yq_count_check = (len(df.columns) - 20 - 1) % 7 == 0
    if not yq_count_check:
        raise ValueError(f"Wrong column count; (Total {len(df.columns)} - 20 - 1) % 7")

    col_ptr = 20
    segs = list()
    for _ in range(yq_count):
        seg = df.iloc[:, col_ptr : col_ptr + 7].copy()
        seg.columns = repeatc
        seg['year'] = y
        seg['quarter'] = f"{q}Q"

        segs.append(pd.concat([common_df, seg], axis=1))
        print(y, q)

        # Update quarter and year
        q += 1
        if q > 4:
            q = 1
            y += 1
        
    my_df = pd.concat(segs).reset_index(drop=True)

    type_map = {}
    for col, col_type in dm.__annotations__.items():
        if get_origin(col_type) is Series:
            inner_type = get_args(col_type)[0]
            type_map[col] = inner_type

    # 3. Apply type coercion
    for col, dtype in type_map.items():
        if dtype in [datetime, pd.Timestamp]:
            my_df[col] = excel_serial_to_datetime(my_df[col])
        elif dtype == int:
            my_df[col] = pd.to_numeric(my_df[col], errors="coerce").astype(pd.Int64Dtype())
        else:
            my_df[col] = my_df[col].astype(dtype)
        
    return my_df        
