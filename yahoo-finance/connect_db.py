from connection import db_config

import pymysql

'''
Check MySQL is install and database is exsits or not in the first time.
'''

# NOT FINISH
def isDBInstall():
    try:
        params = db_config.config()
        print("Connect MySQL database...")    
        conn = pymysql.connect(**params)      
        cursor = conn.cursor()

        cursor.execute("SELECT VERSION()")
        version = cursor.fetchone()
        
        return version
        conn.close()
    except pymysql.DatabaseError as error:
        print(error)

# Create database
def create_database():
    try:
        params = db_config.config()
        conn = pymysql.connect(**params)
        cursor = conn.cursor()

        # Get all Databases and check stocks is exist or not.
        cursor.execute("SHOW DATABASES LIKE 'stocks'")
        db = cursor.fetchone()
        
        if db == None:
            print('Create db...')
            cursor.execute("CREATE DATABASE stocks") # Create database name stocks
            
            # Write what db use in database.ini
            db_config.add_key('database', 'stocks')
            print(r"'stocks' database is been created.")
        else:
            pass
        conn.close()
    except pymysql.DatabaseError as err:
        print("Something went wrong: {}".format(err))


# Create table
def create_table(table_name='aapl'):    
    try:
        params = db_config.config()
        conn = pymysql.connect(**params)
        cursor = conn.cursor()
    
        cursor.execute(f"SHOW TABLES LIKE '{table_name}'")
        table = cursor.fetchone()

        if table == None:
            cursor.execute('''CREATE TABLE {}(
                id INT AUTO_INCREMENT PRIMARY KEY,
                date VARCHAR(15) NOT NULL,
                open FLOAT(5) NOT NULL,
                high FLOAT(5) NOT NULL,
                low FLOAT(5) NOT NULL,
                close FLOAT(5) NOT NULL,
                adj_close FLOAT(5) NOT NULL, 
                volume INT NOT NULL)'''.format(table_name)
            )
            print('{} is been create.'.format(table_name))            
        else:
            pass
        conn.close()
    except pymysql.DatabaseError as err:
        print("Something went wrong: {}".format(err))


# Insert data
def insert_data(datas, table_name='aapl'):
    try:
        params = db_config.config()
        conn = pymysql.connect(**params)
        cursor = conn.cursor()

        cursor.execute(f"SHOW TABLES LIKE '{table_name}'")
        table = cursor.fetchone()

        if table[0] == table_name:
            for row in datas:
                print(row)
                row[6] = row[6].replace(',', '')
                cursor.execute('''INSERT INTO aapl(date, open, high, low, close, adj_close, volume) VALUES('{}',{},{},{},{},{},{})'''.format(row[0],row[1],row[2],row[3],row[4],row[5],row[6]))
            conn.commit()
        else:
            print(f"'{table_name}' is not exist.")    
        conn.close()            
    except pymysql.DatabaseError as err:
        print("Something went wrong: {}".format(err))


def send_Data2Mysql(datas, stock_name='aapl'):
    if isDBInstall():
        create_database()
        create_table()
        insert_data(datas)
    else:
        print("It is been created")
