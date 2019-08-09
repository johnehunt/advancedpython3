import pymysql

print('Open database connection')
connection = pymysql.connect('localhost', 'user', 'password', 'uni-database')
print('connection:', connection)

print('prepare a cursor object using cursor() method')
cursor = connection.cursor()
print('cursor:', cursor)

# ... perform database operations

print('disconnect from database server')
connection.close()
print('Done')