import pymysql

# Establishing a connection to DB
conn = pymysql.connect(host='localhost', port=3306,
                       user='root', passwd='1q2w#E$R', db='users')
conn.autocommit(True)

# Getting a cursor from Database
cursor = conn.cursor()

# Inserting data into table
cursor.execute("INSERT into users.players (name, id) VALUES ('Fuchs', 1)")

cursor.close()
conn.close()
