def get_sql_uri():
    host = "localhost"
    password = "D3v3L0p"
    username = "root"
    dataBase = "fersanun_pedidos"
    return F"mysql+pymysql://{username}:{password}@{host}/{dataBase}"
