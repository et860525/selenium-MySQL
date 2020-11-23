import os.path
from getpass import getpass
from configparser import ConfigParser

# Initialize
def init():
    if os.path.exists('database.ini') == False:
        try:
            sql_password = getpass("Please enter your sql password: ")
            settings = f"[mysql]\nhost = localhost\nuser = root \npassword = {sql_password}"
            with open('database.ini', 'xt') as f:
                f.write(settings)
        except IOError:
            #print('Database.ini file is exist.')
            return 0
    else:
        pass

# Add key
def add_key(key, value, section='mysql'):
    cfg = ConfigParser()
    cfg.read('database.ini')

    cfg['mysql'][key] = value
    with open('database.ini', 'w') as configfile:
        cfg.write(configfile)

# Use
def config(filename='database.ini', section='mysql'):
    
    # Create parser
    parser = ConfigParser()

    # Read ini file
    parser.read(filename)

    db = {}
    if parser.has_section(section):
        params = parser.items(section)
        for param in params:
            db[param[0]] = param[1]
    else:
        raise Exception('Section {0} not found in the {1} file'.format(section, filename))

    return db