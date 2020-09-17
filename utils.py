import pymysql
import pandas as pd
from sqlalchemy import create_engine

# connector 세팅 : select 
def db_connect(db_info):
    db_conn = pymysql.connect(
            host = db_info["host"],
            port = db_info["port"], 
            user = db_info["user"], 
            passwd = db_info["passwd"], 
            db = db_info["db"], 
            charset = db_info["charset"])

    # cursor 세팅
    cursor = db_conn.cursor(pymysql.cursors.DictCursor)
    
    return db_conn, cursor


#connector 세팅

# MySQL Connector using pymysql


def df_to_db(df, table_name, db_info, if_exists="append"):
    
    pymysql.install_as_MySQLdb()

    engine_info = "mysql+mysqldb://{user}:{passwd}@{host}/{db}".format(user = db_info["user"],
                                                                       passwd = db_info["passwd"], 
                                                                       host = db_info["host"],
                                                                       db = db_info["db"])
    db = create_engine(engine_info, encoding='utf-8')
    conn = db.connect()

    df.to_sql(name=table_name, con=conn, if_exists =if_exists, index=False)
    
    conn.close()
    db.dispose()
    
    


    


    
    
    