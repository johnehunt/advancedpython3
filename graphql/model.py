# Import the Query and Mutation types from Ariadne
from ariadne import MutationType
from ariadne import QueryType

query = QueryType()
mutation = MutationType()


# Define class used to hold data to be return
class Book:
	""" Simple representation of a book """
	def __init__(self, isbn, title, author, category, price):
		self.isbn = isbn
		self.title = title
		self.author = author
		self.category = category
		self.price = price


# Initial data held by server
books = [Book('123', 'Python Naturally', 'John Smith', "TECHNICAL", 12.99)]


# Map field hello in a query to this
# resolver function - could also be a method on a class
@query.field("hello")
def resolve_hello(_, info):
	return "Hi there"

# To invoke this resolver use this query in the GraphiQL browser
# query {
#   hello
# }


# Map the books field of a query to this resolver function
# It will return the current list of books
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

# Handles a request for a particular book
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


# Defines a mutation resolver. The function takes the data supplied
# by the mutation request. The info parameter contains the context which
# is supplied with the request is processed. The resolver creates a new book
# which is added to the list of books and the new book is returned
@mutation.field("addBook")
def resolve_add_book(_, info, isbn, title, author, category, price):
	newBook = Book(isbn, title, author, category, price)
	books.append(newBook)
	return newBook

# mutation  {
#   addBook(
#      isbn : "345"
#      title: "Advanced Python"
#      author: "Bill Smith"
#      category: TECHNICAL
#      price: 15.55
#    ) {
#      isbn
#    }
# }
