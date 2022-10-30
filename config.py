SQLALCHEMY_DATABASE_URI = \
    '{SGBD}://{usuario}:{senha}@{servidor}/{database}'.format(
        SGBD = 'mysql+mysqlconnector',
        usuario = 'crudpython',
        senha = 'Pikachu25',
        servidor = 'crud-python.mysql.database.azure.com',
        database = 'gamelib'
    )