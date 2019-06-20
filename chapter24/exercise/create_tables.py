import pymysql

# Open database connection
connection = pymysql.connect('localhost', 'user', 'password', 'accounts')

# prepare a cursor object using cursor() method
cursor = connection.cursor()

try:
    # Execute CREATE command
    cursor.execute("CREATE TABLE acc_info (idacc_info INT NOT NULL, name VARCHAR(255) NOT NULL, PRIMARY KEY (idacc_info))")
    cursor.execute("CREATE TABLE transactions (idtransactions INT NOT NULL, type VARCHAR(45) NOT NULL, amount VARCHAR(45) NOT NULL, account INT NOT NULL, PRIMARY KEY (idtransactions))")

    # Commit the changes to the database
    connection.commit()
except:
    # rollback the changes if an exception / error
    connection.rollback()

# Close the database connection
connection.close()
