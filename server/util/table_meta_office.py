import pandera.pandas as pa
import pandas as pd
from pandera.typing import Series
from datetime import datetime

# 오피스 칼럼 변수명은 다음 사이트 참고
# https://realestateagent-story.tistory.com/entry/%EB%B6%80%EB%8F%99%EC%82%B0%EC%98%81%EC%96%B4-%EC%8B%A4%EB%AC%B4%EB%A5%BC-%ED%95%98%EB%A9%B4%EC%84%9C-%EB%A7%8E%EC%9D%B4-%EC%93%B0%EB%8A%94-%EC%98%81%EC%96%B4%EB%8B%A8%EC%96%B4-%EB%A6%AC%EC%8A%A4%ED%8A%B8

# 오피스_임대_Raw_data(마켓 db)는 2024년 1분기부터 Column 수가 달라짐 (공실면적 제외)
# 오피스_임대_Raw_data 만 사용

class OfficeTable1(pa.DataFrameModel):
    # 시트: 임대시장통계(5구분)
    year: Series[int]  # 연도
    quarter: Series[str]  # 분기
    district: Series[str]  # 큰 지역 구분 / 서울, GBD, 등
    size: Series[str]  # 오피스 크기 
    deposit: Series[float]
    rent: Series[float]
    utility: Series[float]
    vacancy_inclusive: Series[float]  # 공실률 신축 포함
    vacancy_exclusive: Series[float]  # 공실률 신축 제외
    noc: Series[float]


class OfficeTable2(pa.DataFrameModel):
    # 시트: 임대시장통계(3구분)
    year: Series[int]  # 연도
    quarter: Series[str]  # 분기
    district: Series[str]  # 큰 지역 구분 / 서울, GBD, 등
    size: Series[str]  # 오피스 크기 
    deposit: Series[float]
    rent: Series[float]
    utility: Series[float]
    vacancy_inclusive: Series[float]  # 공실률 신축 포함
    vacancy_exclusive: Series[float]  # 공실률 신축 제외
    noc: Series[float]


class OfficeTable3(pa.DataFrameModel):
    # 시트: 임대차사례
    demand_type: Series[str]  # 수요형태
    contract_yq: Series[str]  # 계약시기(분기)
    tenant: Series[str]
    from_district: Series[str]  # 권역
    from_gu: Series[str]
    from_dong: Series[str]
    from_address: Series[str]
    from_build_name: Series[str]
    from_leasable_area: Series[float]  # 전용면적
    to_district: Series[str]  # 권역
    to_gu: Series[str]
    to_dong: Series[str]
    to_address: Series[str]
    to_build_name: Series[str]
    to_leasable_area: Series[float]  # 전용면적    
    area_change: Series[float]
    note: Series[str]
    company_subcategory: Series[str]
    company_category: Series[str]


class OfficeTable4(pa.DataFrameModel):
    # 임대지수
    year: Series[int]
    quarter: Series[str]
    cbd: Series[float]
    gbd: Series[float]
    ybd: Series[float]
    others: Series[float]
    bbd: Series[float]
    seoul: Series[float]
    seoul_bbd: Series[float]
    

class OfficeTable5(pa.DataFrameModel):
    # 공급기장통계
    year: Series[int]
    quarter: Series[str]
    cbd: Series[float]
    gbd: Series[float]
    ybd: Series[float]
    others: Series[float]
    seoul: Series[float]


class OfficeTable6(pa.DataFrameModel):
    # 당분기 신규공급사례
    no: Series[int]
    type: Series[str]
    build_name: Series[str]
    pnu: Series[str]
    bjd_code: Series[str]
    land_code: Series[str]
    bjd_address: Series[str]
    bjd_sido: Series[str]
    district: Series[str]
    sido: Series[str]
    gu: Series[str]
    dong: Series[str]
    main_no: Series[int]
    sub_no: Series[int]
    gross_floor_area_sqm: Series[float]  # 언면적
    gross_floor_area_py: Series[float]  # 연면적 (평)
    land_area_sqm: Series[float]  # 대지면적
    land_area_py: Series[float]  # 대지면적 (평)
    floor_area_sqm: Series[float]  # 건축면적
    site_coverage_ratio: Series[float]  # 건폐율
    floor_area_ratio_calc_area: Series[float]  # 용적률 계산용 연면적
    floor_area_ratio: Series[float]  # 용적률
    law_floor_area_ratio_cap: Series[float]  # 법적 용적률 상한
    office_area_sqm: Series[float]  # 오피스 면적
    office_area_py: Series[float]  # 오피스 면적 (평)
    efficiency_rate: Series[float]
    ground_floor: Series[int]
    basement: Series[int]
    main_usage: Series[str]
    height: Series[float]
    structure: Series[str]
    elevator: Series[str]
    owner: Series[str]
    construct_permission_date: Series[datetime]
    construction_date: Series[datetime]
    usage_permission_date: Series[datetime]
    completion_year: Series[int]
    completion_quarter: Series[str]
    construction_phase: Series[str]
    note: Series[str]


class OfficeTable7(pa.DataFrameModel):
    # 공급예정물량
    expected_completion_year: Series[int]
    expected_completion_quarter: Series[str]
    build_name: Series[str]
    pnu: Series[str]
    bjd_code: Series[str]
    land_code: Series[str]
    bjd_address: Series[str]
    bjd_sido: Series[str]
    district: Series[str]
    sido: Series[str]
    gu: Series[str]
    dong: Series[str]
    main_no: Series[int]
    sub_no: Series[int]
    construction_type: Series[str]
    land_area_sqm: Series[float]
    floor_area_sqm: Series[float]
    gross_floor_area: Series[float]
    basement: Series[int]
    ground_floor: Series[int]
    main_usage: Series[str]
    construction_date: Series[datetime]
    construct_permission_date: Series[datetime]
    tenant_yn: Series[str]
    multi_owned_yn: Series[str]
    expected_demand_type: Series[str]
    owner: Series[str]
    beneficiary: Series[str]
    construction_company: Series[str]
    construction_phase: Series[str]
    status_board_yn: Series[str]  # 현황판 여부
    phase_info: Series[str]
    note1: Series[str]  # 비고
    note2: Series[str]  # 참고


class OfficeTable8_1(pa.DataFrameModel):
    # 매매시장통계
    year: Series[int]
    quarter: Series[str]
    cbd: Series[float]
    gbd: Series[float]
    ybd: Series[float]
    others: Series[float]
    seoul: Series[float]
    bbd: Series[float]
    seoul_bbd: Series[float]
    seoul_3m: Series[float]


class OfficeTable8_2(pa.DataFrameModel):
    # 매매시장통계
    year: Series[int]
    cbd: Series[float]
    gbd: Series[float]
    ybd: Series[float]
    others: Series[float]
    seoul: Series[float]
    bbd: Series[float]
    seoul_bbd: Series[float]


class OfficeTable8_3(pa.DataFrameModel):
    # 매매시장통계
    year: Series[int]
    quarter: Series[str]
    cbd: Series[float]
    gbd: Series[float]
    ybd: Series[float]
    others: Series[float]
    seoul: Series[float]
    bbd: Series[float]


class OfficeTable8_4(pa.DataFrameModel):
    # 매매시장통계
    year: Series[int]
    cbd: Series[float]
    gbd: Series[float]
    ybd: Series[float]
    others: Series[float]
    seoul: Series[float]
    bbd: Series[float]


class OfficeTable8_5(pa.DataFrameModel):
    # 매매시장통계
    year: Series[int]
    quarter: Series[str]
    cbd: Series[float]
    gbd: Series[float]
    ybd: Series[float]
    others: Series[float]
    seoul: Series[float]
    bbd: Series[float]


class OfficeTable8_6(pa.DataFrameModel):
    # 매매시장통계
    year: Series[int]
    quarter: Series[str]
    cap_rate_seoul_nominal: Series[float]
    cap_rate_seoul_real: Series[float]
    seoul_office_index: Series[float]
    kr3: Series[float]  # 국고채 3년
    spread: Series[float]


class OfficeTable9(pa.DataFrameModel):
    # 당분기 매매사례
    type: Series[str]
    build_name: Series[str]
    pnu: Series[str]
    bjd_code: Series[str]
    land_code: Series[str]
    bjd_address: Series[str]
    sido: Series[str]
    district: Series[str]
    is_bundang: Series[str]
    size_class: Series[str]
    si: Series[str]
    gu: Series[str]
    dong: Series[str]
    main_no: Series[int]
    sub_no: Series[int]
    add_lot_yn: Series[str]  # 추가필지 여부
    add_lot_no: Series[str]  # 추가필지
    add_lot_count: Series[int]  # 추가필지 수
    add_build: Series[str]  # 기타빌딩
    add_build_count: Series[str]  # 기타빌딩 수
    gross_floor_area_sqm: Series[float]
    gross_floor_area_py: Series[float]
    land_area_sqm: Series[float]
    land_area_py: Series[float]
    trade_gross_floor_area_sqm: Series[float]
    trade_gross_floor_area_py: Series[float]
    trade_land_area_sqm: Series[float]
    trade_land_area_py: Series[float]
    ground_floor: Series[int]
    basement: Series[int]
    completion_year: Series[int]
    renovation_yn: Series[str]
    renovation_year: Series[int]
    renovation_note: Series[str]
    contract_date: Series[datetime]
    payment_date: Series[datetime]
    payment_year: Series[int]
    payment_month: Series[int]
    payment_quarter: Series[str]
    price_1000: Series[float]  # 거래가(천원)
    price_py: Series[float]  # 평당가(천원)
    seller: Series[str]
    seller_category: Series[str]
    seller_location: Series[str]
    buyer: Series[str]
    buyer_category: Series[str]
    buyer_location: Series[str]
    buyer_invester: Series[str]
    purpose: Series[str]
    vehicle: Series[str]
    vehicle_note: Series[str]
    buy_all_yn: Series[str]
    transaction_type: Series[str]  # 거래 종류: 실물/선매입 등등
    transcation_note: Series[str]
    cost_of_capital: Series[str]  # 대출금리
    im_yn: Series[str]  # IM 확보
    rent_area: Series[float]
    real_price: Series[float]  # 순매입가
    deposit_1000: Series[float]
    rent_1000: Series[float]
    utility_1000: Series[float]
    efficiency_rate: Series[float]
    rent_free: Series[float]
    vacancy: Series[float]
    district_vacancy: Series[float]
    kr5: Series[float]
    marketed_noi: Series[float]
    marketed_operate_noi_ratio: Series[float]  # 운용임대료 / 마케팅 임대료
    operate_noi: Series[float]  # 운용 NOI
    real_noi: Series[float]  # 실질 NOI
    marketed_stabilized_nominal_cap: Series[float]
    operate_stabilized_nominal_cap: Series[float]
    stabilized_real_cap: Series[float]
    asis_nominal_cap: Series[float]
    asis_real_cap: Series[float]
    im_cap: Series[str]
    cap_note: Series[str]


class OfficeTable10_1(pa.DataFrameModel):
    # 경제지표
    year: Series[int]
    quarter: Series[str]
    cp_3m: Series[float]
    cd_3m: Series[float]
    kr1: Series[float]
    kr3: Series[float]
    kr5: Series[float]
    kr10: Series[float]
    aa3: Series[float]  # 회사채 aa 3년
    bbb3: Series[float]  # 회사채 bbb 3년


class OfficeTable10_2(pa.DataFrameModel):
    # 경제지표
    year: Series[int]
    quarter: Series[str]
    kospi: Series[float]
    kospi_delta: Series[float]
    kosdaq: Series[float]
    kosdaq_delta: Series[float]
    usdkrw: Series[float]
    usdkrw_delta: Series[float]
    eurkrw: Series[float]
    eurkrw_delta: Series[float]


class OfficeTable10_3(pa.DataFrameModel):
    # 경제지표
    year: Series[int]
    quarter: Series[str]
    cpi_korea: Series[float]
    cpi_korea_delta: Series[float]
    cpi_seoul: Series[float]
    cpi_seoul_delta: Series[float]
    gdp_nominal: Series[float]
    gdp_nominal_delta: Series[float]
    gdp_real: Series[float]
    gdp_real_delta: Series[float]
    unemployed: Series[float]  # 실업자(천명)
    unemployed_delta: Series[float]
    unemploment_ratio: Series[float]  # 실업률


class OfficeTable11(pa.DataFrameModel):
    # 오피스 임대_Raw data
    row_id: Series[int]
    build_name: Series[str]
    build_name_specify: Series[str]
    code: Series[str]
    code_specify: Series[str]  # PK
    pnu: Series[str]
    bjd_code: Series[str]
    land_code: Series[str]
    bjd_address: Series[str]
    bjd_sido: Series[str]
    district: Series[str]
    sido: Series[str]
    gu: Series[str]
    dong: Series[str]
    main_no: Series[int]
    sub_no: Series[int]
    gross_floor_area: Series[float]
    office_area: Series[float]
    efficiency_rate: Series[float]
    completion_year: Series[int]
    # 분기별 반복 Column
    year: Series[int]
    quarter: Series[str]
    deposit: Series[float]  # 원/평
    rent: Series[float]  # 원/평
    utility: Series[float]  # 원/평
    rent_free: Series[float]  # 원/평
    vacant_area: Series[float]  # 공실 면적
    vacancy: Series[float]  # 공실률
    noc: Series[float]