import pandas as pd
import pandera.pandas as pa
from pandera.typing import Series
from typing import get_args, get_origin


def office_parse_1(df: pd.DataFrame, dm: pa.DataFrameModel) -> pd.DataFrame:
    if dm is None:
        raise RuntimeError("no parsing function for `df`")

    df.replace({".": None, "-": None}, inplace=True)

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
    my_df = my_df.astype(type_map)

    return my_df


def office_parse_2(df: pd.DataFrame, dm: pa.DataFrameModel) -> pd.DataFrame:
    if dm is None:
        raise RuntimeError("no parsing function for `df`")

    df.replace({".": None, "-": None}, inplace=True)

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
    my_df = my_df.astype(type_map)

    return my_df


def office_table_3(df: pd.DataFrame, dm: pa.DataFrameModel) -> pd.DataFrame:
    if dm is None:
        raise RuntimeError("no parsing function for `df`")

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
    df = df.astype(type_map)
    return df


def office_table_4(df: pd.DataFrame, dm: pa.DataFrameModel) -> pd.DataFrame:
    if dm is None:
        raise RuntimeError("no parsing function for `df`")
    
    df.replace({".": None, "-": None}, inplace=True)

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
    df = df.astype(type_map)
    return df


def office_table_5(df: pd.DataFrame, dm: pa.DataFrameModel) -> pd.DataFrame:
    if dm is None:
        raise RuntimeError("no parsing function for `df`")
    
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
    df = df.astype(type_map)
    return df


def office_table_6(df: pd.DataFrame, dm: pa.DataFrameModel) -> pd.DataFrame:
    if dm is None:
        raise RuntimeError("no parsing function for `df`")
    
    df.replace({".": None, "-": None}, inplace=True)

    # Common section
    common_section = 20
    columns = list(dm.__annotations__.keys())
    common_columns = columns[:common_section]
    common_df = df.iloc[:, :20]
    common_df.columns = common_columns

    # Repeated section
    y, q = 2022, 4
    repeatc = ["deposit", "rent", "utility", "rent_free", "vacant_area", "vacancy", "noc"]
    yq_count = (df.columns - 20 - 1) / 7  # 20개의 고정된 Column. 1개의 비고 Column

    col_ptr = 20
    segs = list()
    for _ in range(yq_count):
        seg = df.iloc[:, col_ptr : col_ptr + 7].copy()
        seg.columns = repeatc
        seg['year'] = y
        seg['quarter'] = f"{q}Q"

        # Update quarter and year
        q += 1
        if q > 4:
            q = 1
            y += 1
        
        segs.append(pd.concat([common_df, seg], axis=1))

    my_df = pd.concat(segs)

    type_map = {}
    for col, col_type in dm.__annotations__.items():
        if get_origin(col_type) is Series:
            inner_type = get_args(col_type)[0]
            type_map[col] = inner_type

    # 3. Apply type coercion
    my_df = my_df.astype(type_map)
        
    return my_df        
