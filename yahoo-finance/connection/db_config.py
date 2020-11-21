from configparser import ConfigParser

# Initialize
def init():
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

