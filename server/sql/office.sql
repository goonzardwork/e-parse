CREATE TABLE IF NOT EXISTS rsquare.rsquare_office_0 (
    year                int4,
    quarter             varchar,
    district            varchar,
    size                varchar,
    deposit             float4,
    rent                float4,
    utility             float4,
    vacancy_inclusive   float4,
    vacancy_exclusive   float4,
    noc                 float4,
    PRIMARY KEY (year, quarter, district, size)
);

CREATE TABLE IF NOT EXISTS rsquare.rsquare_office_1 (
    year               int4,
    quarter            varchar,
    district           varchar,
    size               varchar,
    deposit            float4,
    rent               float4,
    utility            float4,
    vacancy_inclusive  float4,
    vacancy_exclusive  float4,
    noc                float4,
    PRIMARY KEY (year, quarter, district, size)
);

CREATE TABLE IF NOT EXISTS rsquare.rsquare_office_2 (
    demand_type          varchar,
    contract_yq          varchar,
    tenant               varchar,
    from_district        varchar,
    from_gu              varchar,
    from_dong            varchar,
    from_address         varchar,
    from_build_name      varchar,
    from_leasable_area   float4,
    to_district          varchar,
    to_gu                varchar,
    to_dong              varchar,
    to_address           varchar,
    to_build_name        varchar,
    to_leasable_area     float4,
    area_change          float4,
    note                 varchar,
    company_subcategory  varchar,
    company_category     varchar
);

CREATE TABLE IF NOT EXISTS rsquare.rsquare_office_3 (
    year        int4,
    quarter     varchar,
    cbd         float4,
    gbd         float4,
    ybd         float4,
    others      float4,
    bbd         float4,
    seoul       float4,
    seoul_bbd   float4,
    PRIMARY KEY (year, quarter)
);

CREATE TABLE IF NOT EXISTS rsquare.rsquare_office_4 (
    year    int4,
    quarter varchar,
    cbd     float4,
    gbd     float4,
    ybd     float4,
    others  float4,
    seoul   float4,
    PRIMARY KEY (year, quarter)
);

CREATE TABLE IF NOT EXISTS rsquare.rsquare_office_5 (
    year    int4,
    quarter varchar,
    cbd     float4,
    gbd     float4,
    ybd     float4,
    others  float4,
    seoul   float4,
    PRIMARY KEY (year, quarter)
);

CREATE TABLE IF NOT EXISTS rsquare.rsquare_office_6 (
    year    int4,
    quarter varchar,
    cbd     float4,
    gbd     float4,
    ybd     float4,
    others  float4,
    seoul   float4,
    PRIMARY KEY (year, quarter)
);

CREATE TABLE IF NOT EXISTS rsquare.rsquare_office_7 (
    year    int4,
    quarter varchar,
    cbd     float4,
    gbd     float4,
    ybd     float4,
    others  float4,
    seoul   float4,
    PRIMARY KEY (year, quarter)
);

CREATE TABLE IF NOT EXISTS rsquare.rsquare_office_8 (
    year    int4,
    quarter varchar,
    cbd     float4,
    gbd     float4,
    ybd     float4,
    others  float4,
    seoul   float4,
    PRIMARY KEY (year, quarter)
);

CREATE TABLE IF NOT EXISTS rsquare.rsquare_office_9 (
    year    int4,
    quarter varchar,
    cbd     float4,
    gbd     float4,
    ybd     float4,
    others  float4,
    seoul   float4,
    PRIMARY KEY (year, quarter)
);

CREATE TABLE IF NOT EXISTS rsquare.rsquare_office_10 (
    year    int4,
    quarter varchar,
    cbd     float4,
    gbd     float4,
    ybd     float4,
    others  float4,
    seoul   float4,
    PRIMARY KEY (year, quarter)
);

CREATE TABLE IF NOT EXISTS rsquare.rsquare_office_11 (
    no                             int4,
    type                           varchar,
    build_name                     varchar,
    pnu                            varchar,
    bjd_code                       varchar,
    land_code                      varchar,
    bjd_address                    varchar,
    bjd_sido                       varchar,
    district                       varchar,
    sido                           varchar,
    gu                             varchar,
    dong                           varchar,
    main_no                        int4,
    sub_no                         int4,
    gross_floor_area_sqm          float4,
    gross_floor_area_py           float4,
    land_area_sqm                 float4,
    land_area_py                  float4,
    floor_area_sqm                float4,
    site_coverage_ratio           float4,
    floor_area_ratio_calc_area    float4,
    floor_area_ratio              float4,
    law_floor_area_ratio_cap      float4,
    office_area_sqm               float4,
    office_area_py                float4,
    efficiency_rate               float4,
    ground_floor                  int4,
    basement                      int4,
    main_usage                    varchar,
    height                        float4,
    structure                     varchar,
    elevator                      varchar,
    owner                         varchar,
    construct_permission_date     timestamp,
    construction_date             timestamp,
    usage_permission_date         timestamp,
    completion_year               int4,
    completion_quarter            varchar,
    construction_phase            varchar,
    note                          varchar
);

CREATE TABLE IF NOT EXISTS rsquare.rsquare_office_13 (
    year        int4,
    quarter     varchar,
    cbd         float4,
    gbd         float4,
    ybd         float4,
    others      float4,
    seoul       float4,
    bbd         float4,
    seoul_bbd   float4,
    seoul_3m    float4,
    PRIMARY KEY (year, quarter)
);

CREATE TABLE IF NOT EXISTS rsquare.rsquare_office_14 (
    year        int4,
    quarter     varchar,
    cbd         float4,
    gbd         float4,
    ybd         float4,
    others      float4,
    seoul       float4,
    bbd         float4,
    seoul_bbd   float4,
    seoul_3m    float4,
    PRIMARY KEY (year, quarter)
);

CREATE TABLE IF NOT EXISTS rsquare.rsquare_office_15 (
    year        int4,
    cbd         float4,
    gbd         float4,
    ybd         float4,
    others      float4,
    seoul       float4,
    bbd         float4,
    seoul_bbd   float4,
    PRIMARY KEY (year)
);

CREATE TABLE IF NOT EXISTS rsquare.rsquare_office_16 (
    year        int4,
    cbd         float4,
    gbd         float4,
    ybd         float4,
    others      float4,
    seoul       float4,
    bbd         float4,
    seoul_bbd   float4,
    PRIMARY KEY (year)
);

CREATE TABLE IF NOT EXISTS rsquare.rsquare_office_17 (
    year     int4,
    quarter  varchar,
    cbd      float4,
    gbd      float4,
    ybd      float4,
    others   float4,
    seoul    float4,
    bbd      float4,
    PRIMARY KEY (year, quarter)
);

CREATE TABLE IF NOT EXISTS rsquare.rsquare_office_18 (
    year    int4,
    cbd     float4,
    gbd     float4,
    ybd     float4,
    others  float4,
    seoul   float4,
    bbd     float4,
    PRIMARY KEY (year)
);

CREATE TABLE IF NOT EXISTS rsquare.rsquare_office_19 (
    year     int4,
    quarter  varchar,
    cbd      float4,
    gbd      float4,
    ybd      float4,
    others   float4,
    seoul    float4,
    bbd      float4,
    PRIMARY KEY (year, quarter)
);

CREATE TABLE IF NOT EXISTS rsquare.rsquare_office_20 (
    year     int4,
    quarter  varchar,
    cbd      float4,
    gbd      float4,
    ybd      float4,
    others   float4,
    seoul    float4,
    bbd      float4,
    PRIMARY KEY (year, quarter)
);

CREATE TABLE IF NOT EXISTS rsquare.rsquare_office_21 (
    year                    int4,
    quarter                 varchar,
    cap_rate_seoul_nominal float4,
    cap_rate_seoul_real    float4,
    seoul_office_index     float4,
    kr3                    float4,
    spread                 float4,
    PRIMARY KEY (year, quarter)
);

CREATE TABLE IF NOT EXISTS rsquare.rsquare_office_22 (
    type                              varchar,
    build_name                        varchar,
    pnu                               varchar,
    bjd_code                          varchar,
    land_code                         varchar,
    bjd_address                       varchar,
    sido                              varchar,
    district                          varchar,
    is_bundang                        varchar,
    size_class                        varchar,
    si                                varchar,
    gu                                varchar,
    dong                              varchar,
    main_no                           int4,
    sub_no                            int4,
    add_lot_yn                        varchar,
    add_lot_no                        varchar,
    add_lot_count                     int4,
    add_build                         varchar,
    add_build_count                   varchar,
    gross_floor_area_sqm             float4,
    gross_floor_area_py              float4,
    land_area_sqm                    float4,
    land_area_py                     float4,
    trade_gross_floor_area_sqm       float4,
    trade_gross_floor_area_py        float4,
    trade_land_area_sqm              float4,
    trade_land_area_py               float4,
    ground_floor                     int4,
    basement                         int4,
    completion_year                  int4,
    renovation_yn                    varchar,
    renovation_year                  int4,
    renovation_note                  varchar,
    contract_date                    timestamp,
    payment_date                     timestamp,
    payment_year                     int4,
    payment_month                    int4,
    payment_quarter                  varchar,
    price_1000                       float4,
    price_py                         float4,
    seller                           varchar,
    seller_category                  varchar,
    seller_location                  varchar,
    buyer                            varchar,
    buyer_category                   varchar,
    buyer_location                   varchar,
    buyer_invester                   varchar,
    purpose                          varchar,
    vehicle                          varchar,
    vehicle_note                     varchar,
    buy_all_yn                       varchar,
    transaction_type                 varchar,
    transcation_note                 varchar,
    cost_of_capital                  varchar,
    im_yn                            varchar,
    rent_area                        float4,
    real_price                       float4,
    deposit_1000                     float4,
    rent_1000                        float4,
    utility_1000                     float4,
    efficiency_rate                  float4,
    rent_free                        float4,
    vacancy                          float4,
    district_vacancy                 float4,
    kr5                              float4,
    marketed_noi                     float4,
    marketed_operate_noi_ratio       float4,
    operate_noi                      float4,
    real_noi                         float4,
    marketed_stabilized_nominal_cap float4,
    operate_stabilized_nominal_cap  float4,
    stabilized_real_cap              float4,
    asis_nominal_cap                 float4,
    asis_real_cap                    float4,
    im_cap                           varchar,
    cap_note                         varchar
);

CREATE TABLE IF NOT EXISTS rsquare.rsquare_office_23 (
    year      int4,
    quarter   varchar,
    cp_3m     float4,
    cd_3m     float4,
    kr1       float4,
    kr3       float4,
    kr5       float4,
    kr10      float4,
    aa3       float4,
    bbb3      float4,
    PRIMARY KEY (year, quarter)
);

CREATE TABLE IF NOT EXISTS rsquare.rsquare_office_24 (
    year             int4,
    quarter          varchar,
    kospi            float4,
    kospi_delta      float4,
    kosdaq           float4,
    kosdaq_delta     float4,
    usdkrw           float4,
    usdkrw_delta     float4,
    eurkrw           float4,
    eurkrw_delta     float4,
    PRIMARY KEY (year, quarter)
);

CREATE TABLE IF NOT EXISTS rsquare.rsquare_office_25 (
    year                   int4,
    quarter                varchar,
    cpi_korea              float4,
    cpi_korea_delta        float4,
    cpi_seoul              float4,
    cpi_seoul_delta        float4,
    gdp_nominal            float4,
    gdp_nominal_delta      float4,
    gdp_real               float4,
    gdp_real_delta         float4,
    unemployed             float4,
    unemployed_delta       float4,
    unemploment_ratio      float4,
    PRIMARY KEY (year, quarter)
);

CREATE TABLE IF NOT EXISTS rsquare.rsquare_office_26 (
    row_id              int4,
    build_name          varchar,
    build_name_specify  varchar,
    code                varchar,
    code_specify        varchar,
    pnu                 varchar,
    bjd_code            varchar,
    land_code           varchar,
    bjd_address         varchar,
    bjd_sido            varchar,
    district            varchar,
    sido                varchar,
    gu                  varchar,
    dong                varchar,
    main_no             int4,
    sub_no              int4,
    gross_floor_area    float4,
    office_area         float4,
    efficiency_rate     float4,
    completion_year     int4,
    year                int4,
    quarter             varchar,
    deposit             float4,
    rent                float4,
    utility             float4,
    rent_free           float4,
    vacant_area         float4,
    vacancy             float4,
    noc                 float4,
    PRIMARY KEY (year, quarter, code_specify)
);

COMMENT ON TABLE rsquare.rsquare_office_1 IS '임대시장통계(5구분)';
COMMENT ON TABLE rsquare.rsquare_office_2 IS '임대시장통계(3구분)';
COMMENT ON TABLE rsquare.rsquare_office_3 IS '임대차사례';
COMMENT ON TABLE rsquare.rsquare_office_4 IS '임대지수';
COMMENT ON TABLE rsquare.rsquare_office_5 IS '공급시장통계 - 공실률';
COMMENT ON TABLE rsquare.rsquare_office_6 IS '공급시장통계 - 임대면적';
COMMENT ON TABLE rsquare.rsquare_office_7 IS '공급시장통계 - 흡수면적';
COMMENT ON TABLE rsquare.rsquare_office_8 IS '공급시장통계 - 순흡수면적';
COMMENT ON TABLE rsquare.rsquare_office_9 IS '공급시장통계 - 흡수율';
COMMENT ON TABLE rsquare.rsquare_office_10 IS '공급시장통계 - 누적공급면적';
COMMENT ON TABLE rsquare.rsquare_office_11 IS '공급시장통계 - 신규공급면적';
COMMENT ON TABLE rsquare.rsquare_office_12 IS '당분기 신규공급사례';
COMMENT ON TABLE rsquare.rsquare_office_13 IS '공급예정물량';
COMMENT ON TABLE rsquare.rsquare_office_14 IS '매매시장통계 - Cap rate 추이. 분기별 Stabilized 명목 Cap';
COMMENT ON TABLE rsquare.rsquare_office_15 IS '매매시장통계 - Cap rate 추이. 분기별 Stabilized 실질 Cap';
COMMENT ON TABLE rsquare.rsquare_office_16 IS '매매시장통계 - Cap rate 추이. 연도별 Stabilized 명목 Cap';
COMMENT ON TABLE rsquare.rsquare_office_17 IS '매매시장통계 - Cap rate 추이. 연도별 Stabilized 실질 Cap';
COMMENT ON TABLE rsquare.rsquare_office_18 IS '매매시장통계 - 평당거래가 분기별 추이';
COMMENT ON TABLE rsquare.rsquare_office_19 IS '매매시장통계 - 평당거래가 연도별 추이';
COMMENT ON TABLE rsquare.rsquare_office_20 IS '매매시장통계 - 거래시장 규모';
COMMENT ON TABLE rsquare.rsquare_office_21 IS '매매시장통계 - 거래건수';
COMMENT ON TABLE rsquare.rsquare_office_22 IS '매매시장통계 - 매매지수';
COMMENT ON TABLE rsquare.rsquare_office_23 IS '당분기 매매사례';
COMMENT ON TABLE rsquare.rsquare_office_24 IS '경제지표 - 금리';
COMMENT ON TABLE rsquare.rsquare_office_25 IS '경제지표 - 주식시장 환율';
COMMENT ON TABLE rsquare.rsquare_office_26 IS '경제지표 - 거시경제지표';
COMMENT ON TABLE rsquare.rsquare_office_27 IS '오피스 임대';