import pymysql

# Establishing a connection to DB
conn = pymysql.connect(host='localhost', port=3306,
                       user='root', passwd='1q2w#E$R', db='users')
conn.autocommit(True)

# Getting a cursor from Database
cursor = conn.cursor()

# Deleting data into table
cursor.execute("DELETE FROM users.players WHERE name = 'john'")

cursor.close()
conn.close()
