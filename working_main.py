import psycopg2
import sys
connection_parametters = {
            "database"  : "None",
            "user"      : "None",
            "password"  : "None",
            "host"      : "None",
            "port"      : "None"
        } 

def make_param_dic(database, user, password, host, port) -> dict:

    param_dic = {
            "database"  : "None",
            "user"      : "None",
            "password"  : "None",
            "host"      : "None",
            "port"      : "None"
        } 
    param_dic.update({"database"  : database,
                        "user"      : user,
                        "password"  : password,
                        "host"      : host,
                        "port"      : port})
    
    return param_dic

def connect(params_dic):
    """ Connect to the PostgreSQL database server """
    conn = None
    try:
        # connect to the PostgreSQL server
        print('Connecting to the PostgreSQL database...')
        conn = psycopg2.connect(**params_dic)
    except (Exception, psycopg2.DatabaseError) as error:
        print(error)
        sys.exit(1)
    return conn

def single_insert(conn, insert_req):
    """ Execute a single INSERT request """
    cursor = conn.cursor()
    try:
        cursor.execute(insert_req)
        conn.commit()
    except (Exception, psycopg2.DatabaseError) as error:
        print("Error: %s" % error)
        conn.rollback()
        cursor.close()
    cursor.close()
    return 'commited'
