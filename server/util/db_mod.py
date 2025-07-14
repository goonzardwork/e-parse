from abc import ABC
from typing import List, Optional
import pandas as pd
from sqlalchemy import text
from sqlalchemy import create_engine
from sqlalchemy.dialects.postgresql import insert


class FileDbConnectorBase(ABC):
    def __init__(self, 
                 user, 
                 password, 
                 host, 
                 port, 
                 dbname, 
                 verbose: bool = True,
                 **kwargs):
        
        if "schema" not in kwargs:
            kwargs["schema"] = "file"
        for k,v in kwargs.items():
            setattr(self, k, v)

        self.engine = create_engine(f'postgresql://{user}:{password}@{host}:{port}/{dbname}')
        self.verbose = verbose

    # DB
    def select_sql_dataframe(self, query: str) -> pd.DataFrame:
        """SQL 쿼리를 실행하고 결과를 pandas DataFrame으로 반환합니다."""
        return pd.read_sql(query, self.engine)

    # DB
    def insert_data_frame(self, schema: str, table: str, conflict_columns: Optional[list[str]], data: pd.DataFrame, chunksize: int = 10000):
        def fn(table, conn, keys, data_iter):
            self.postgres_upsert(table, conn, keys, data_iter, index_elements=conflict_columns)

        if conflict_columns is not None:
            data.to_sql(
                table, 
                self.engine, 
                schema=schema, 
                if_exists='append', 
                index=False,
                method=fn,
                chunksize=chunksize
            )
        else:
            data.to_sql(
                table,
                self.engine,
                schema=schema,
                if_exists='replace',
                index=False,
                chunksize=chunksize
            )

    @staticmethod
    def postgres_upsert(table, conn, keys, data_iter, index_elements):
        data = [dict(zip(keys, row)) for row in data_iter]

        insert_statement = insert(table.table).values(data)
        upsert_statement = insert_statement.on_conflict_do_update(
            index_elements=index_elements,
            set_={c.key: c for c in insert_statement.excluded},
        )
        conn.execute(upsert_statement)


class RsquareFeeder(FileDbConnectorBase):
    def __init__(self, 
                 user, 
                 password, 
                 host, 
                 port, 
                 dbname, 
                 verbose: bool = True, 
                 **kwargs):
        super().__init__(
            user, 
            password, 
            host, 
            port, 
            dbname, 
            verbose=verbose,
            **kwargs
        )

    def execute_multiline_sql(self, sql: str):
        for stmt in sql.strip().split(";"):
            stmt = stmt.strip()
            if stmt:
                with self.engine.begin() as conn:
                    conn.execute(text(stmt))

    def update_panel(self, 
                     df: pd.DataFrame,
                     schema: str, 
                     table_name: str,
                     primary_key: List[str],
                     chunksize: int = 10_000):
        
        self.insert_data_frame(
            schema=schema,
            table=table_name,
            conflict_columns=primary_key,
            data=df,
            chunksize=chunksize
        )
    