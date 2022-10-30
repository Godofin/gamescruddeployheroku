import mysql.connector
from mysql.connector import errorcode

print("Conecting...")
try:
      conn = mysql.connector.connect(
            host='crud-python.mysql.database.azure.com',
            user='crudpython',
            password='Pikachu25'
      )
except mysql.connector.Error as err:
      if err.errno == errorcode.ER_ACCESS_DENIED_ERROR:
            print('Existe algo errado no nome de usuário ou senha')
      else:
            print(err)

cursor = conn.cursor()

cursor.execute("DROP DATABASE IF EXISTS `gamelib`;")

cursor.execute("CREATE DATABASE `gamelib`;")

cursor.execute("USE `gamelib`;")

# create tables
TABLES = {}
TABLES['Games'] = ('''
      CREATE TABLE `Games` (
      `id` int(11) NOT NULL AUTO_INCREMENT,
      `name` varchar(50) NOT NULL,
      `category` varchar(40) NOT NULL,
      `console` varchar(20) NOT NULL,
      `asin` varchar(10) NOT NULL,
      `language` varchar(20) NOT NULL,
      PRIMARY KEY (`id`)
      ) ENGINE=InnoDB DEFAULT CHARSET=utf8 COLLATE=utf8_bin;''')

for table_name in TABLES:
      table_sql = TABLES[table_name]
      try:
            print('Creating table {}:'.format(table_name), end=' ')
            cursor.execute(table_sql)
      except mysql.connector.Error as err:
            if err.errno == errorcode.ER_TABLE_EXISTS_ERROR:
                  print('Just Exists')
            else:
                  print(err.msg)
      else:
            print('OK')

# inserindo jogos
games_sql = 'INSERT INTO games (name, category, console, asin, language) VALUES (%s, %s, %s, %s, %s)'
games = [
      ('Tetris', 'Puzzle', 'Atari', 'itjjrwpyut', 'English'),
      ('God of War', 'Hack n Slash', 'PS2', 'ujenyabgse', 'English'),
      ('Mortal Kombat', 'Luta', 'PS2', 'fzozpufmuo', 'English'),
]
cursor.executemany(games_sql, games)

cursor.execute('select * from gamelib.games')
print(' -------------  Games:  -------------')
for game in cursor.fetchall():
    print(game[1])

# commitando se não nada tem efeito
conn.commit()

cursor.close()
conn.close()