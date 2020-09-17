# 종목기본정보 
# 종목번호(id) / 종목이름 / 시장구분
from utils import df_to_db
import pandas as pd
from db_info import db_info_get
from utils import db_connect

def main():
    ## data download : http://marketdata.krx.co.kr/mdi#document=040601
    kospi_df = pd.read_csv("./data/kospi_data.csv", encoding="utf8") 
    kosdaq_df = pd.read_csv("./data/kosdaq_data.csv", encoding="utf8")

    kospi_df["시장구분"] = "KS"
    kosdaq_df["시장구분"] = "KQ"

    total_df = pd.concat([kospi_df, kosdaq_df], axis=0)
    total_df = total_df[["종목코드", "기업명", "업종코드", "업종"]]
    total_df = total_df.rename(columns={"종목코드":"stock_code", "기업명":"name", "업종코드":"business_code", "업종":"business"})

    def code_to_string(code):
        code = str(code)
        if len(code) == 6:
            return code
        else:
            return "0"*(6-len(code)) + code

    total_df["stock_code"] = total_df["stock_code"].map(lambda x : code_to_string(x))
    total_df["business_code"] = total_df["business_code"].map(lambda x : code_to_string(x))



    # 최초 실행시 table 생성
    db_info = db_info_get("stock")

    db_conn, cursor = db_connect(db_info)

    cursor.execute("drop table if exists stock.stock_master")

    sql = "CREATE table stock.stock_master(\
    stock_code CHAR(6),\
    name CHAR(20),\
    business_code CHAR(6),\
    business CHAR(100),\
    TS TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP,\
    primary KEY(stock_code))\
     ENGINE=InnoDB\
     default CHARSET = utf8\
     collate = utf8_general_ci;"

    cursor.execute(sql)

    db_conn.commit()
    db_conn.close()


    # database 접속 정보 로딩
    db_info = db_info_get("stock")

    df_to_db(total_df, "stock_master", db_info, if_exists="append")
    
    
main()