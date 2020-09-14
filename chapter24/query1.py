import pymysql

# Open database connection
connection = pymysql.connect('localhost', 'user', 'password', 'uni-database')

# prepare a cursor object using cursor() method
cursor = connection.cursor()

# execute SQL query using execute() method.
cursor.execute('SELECT * FROM students')

print('cursor.rowcount', cursor.rowcount)
print('cursor.description', cursor.description)

# Fetch all the rows and then iterate over the data
data = cursor.fetchall()
for row in data:
    print('row:', row)

# disconnect from server
connection.close()
