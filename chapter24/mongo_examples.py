import pymongo

print('Establishing a connection')
client = pymongo.MongoClient()

print('Obtain bookshop database')
db = client.bookshop
print(db)

print('Access the books collection')
books = db.books

print('Create a book "document"')
book = {
    'author': 'Adam Cooke',
    'title': 'Python Is Great',
    'price': 12.99
}

print('Insert book')
result = books.insert_one(book)
print('Inserted book with id:', result.inserted_id)

print('Select a book')
result = books.find_one({'author': 'Adam Cooke'})
print(result)

results = books.find({'author': 'Adam Cooke'})
for book in results:
    print('book:', book)

print('Deleting a document')
result = books.delete_one({'author': 'Adam Cooke'})
print('Deleted', result.deleted_count, 'books')

print('Closing connection')
client.close()
