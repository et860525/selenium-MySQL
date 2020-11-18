from connection.db_config import config

import pymysql

def create_database():

    params = config()
    conn = pymysql.connect(**params)

    cursor = conn.cursor()
    cursor.execute("Show databases")

    dbs = cursor.fetchall()
    
    #print([db[0] for db in dbs])
    
    # Check 'stocks' database exist or not
    if 'stocks' not in [db[0] for db in dbs]:
        cursor.execute("CREATE DATABASE stocks") # Create database name stocks
        print(r"'stocks' database is been created.")

        try:
            cursor.execute("")
        except pymysql.DatabaseError. as err:
            print("Something went wrong: {}".format(err))

    else:
        print(r"'stocks' database exist.")

        

    conn.close()

create_database()

