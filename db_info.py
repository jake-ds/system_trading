db_info = {
    "stock" : {
        "host" : "localhost",
        "port" : 3306,
        "user" : "root",
        "passwd" : "2wldmsdl@@",
        "db" : "stock",
        "charset" : "utf8"
    }

}

def db_info_get(db_name):
    return db_info[db_name]