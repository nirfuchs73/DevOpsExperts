import pymysql

# Establishing a connection to DB
conn = pymysql.connect(host='remotemysql.com', port=3306,
                       user='aBteND6icD', passwd='f4NaXA5rUt', db='aBteND6icD')
conn.autocommit(True)

# Getting a cursor from Database
cursor = conn.cursor()


# 2. Insert 3 dogs with different values
def insert():
    cursor.execute(
        "INSERT into aBteND6icD.dogs (name, age, breed) VALUES ('Bella', 7, 'Golden Retriever')")
    cursor.execute(
        "INSERT into aBteND6icD.dogs (name, age, breed) VALUES ('Charlie', 8, 'Labrador Retriever')")
    cursor.execute(
        "INSERT into aBteND6icD.dogs (name, age, breed) VALUES ('Luna', 9, 'Siberian Husky')")


# 3. Update second dog age from one value to another
def update():
    cursor.execute(
        "UPDATE aBteND6icD.dogs SET age = '6' WHERE name = 'Charlie'")


# 4. Delete the third dog from table
def delete():
    cursor.execute("DELETE FROM aBteND6icD.dogs WHERE name = 'Luna'")


# 5. Query table and print all dogs names.
def query():
    cursor.execute("SELECT * FROM aBteND6icD.dogs;")
    for row in cursor:
        print(row[0])


def main():
    # insert()
    # update()
    # delete()
    query()

    cursor.close()
    conn.close()


if __name__ == "__main__":
    main()
