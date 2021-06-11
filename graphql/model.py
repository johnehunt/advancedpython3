from ariadne import MutationType
from ariadne import QueryType


class Book:
	def __init__(self, isbn, title, author, category, price):
		self.isbn = isbn
		self.title = title
		self.author = author
		self.category = category
		self.price = price


query = QueryType()
mutation = MutationType()

# Data held by server
books = [Book('123', 'Python Naturally', 'John Smith', "TECHNICAL", 12.99)]


@query.field("hello")
def resolve_hello(_, info):
	return "Hi there"


# query {
#   hello
# }

@query.field("books")
def resolve_books(_, info):
	return books


# query {
#   books {
#     isbn
#     title
#     author
#     price
#   }
# }

@query.field("book")
def resolve_book(*_, isbn):
	print(isbn)
	return Book(isbn, 'A title', 'An author', 'TECHNICAL', 1.99)


# query {
#  book(isbn: "123") {
#        isbn
#        title
#        author
#        price
#  }
# }

@mutation.field("addBook")
def resolve_add_book(_, info, isbn, title, author, category, price):
	newBook = Book(isbn, title, author, category, price)
	books.append(newBook)
	return newBook

# mutation  {
#   addBook (
#     isbn : "345"
#     title: "Advanced Python"
#     author: "Bill Smith"
#     price: 15.55
#   ) {
#     isbn
#   }
# }
