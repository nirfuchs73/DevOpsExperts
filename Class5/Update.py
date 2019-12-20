import pymysql

# Establishing a connection to DB
conn = pymysql.connect(host='localhost', port=3306,
                       user='root', passwd='1q2w#E$R', db='users')
conn.autocommit(True)

# Getting a cursor from Database
cursor = conn.cursor()

# Updating data inside the table
cursor.execute("UPDATE users.players SET id = '2' WHERE name = 'Nir'")

cursor.close()
conn.close()
