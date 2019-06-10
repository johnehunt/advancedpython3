from flask import Flask, jsonify, abort


class Book:
    """ Represents a book in the bookshop"""

    def __init__(self, isbn, title, author, price):
        self.isbn = isbn
        self.title = title
        self.author = author
        self.price = price

    def __str__(self):
        return self.title + ' by ' + self.author + ' @ ' + str(self.price)

    def to_json(self):
        return {
            'isbn': self.isbn,
            'title': self.title,
            'author': self.author,
            'price': self.price
        }


class Bookshop:
    """Represents the bookshop within the service"""

    def __init__(self, books):
        self.books = books

    def get(self, isbn):
        if isbn > len(self.books):
            abort(404)
        return list(filter(lambda b: b.isbn == isbn, self.books))[0]

    def add_book(self, book):
        self.books.append(book)

    def delete_book(self, isbn):
        self.books = list(filter(lambda b: b.isbn != isbn, self.books))


# Global value used to hold the Bookshop object
bookshop = Bookshop([Book(1, 'XML', 'Gryff Smith', 10.99),
                     Book(2, 'Java', 'Phoebe Cooke', 12.99),
                     Book(3, 'Scala', 'Adam Davies', 11.99),
                     Book(4, 'Python', 'Jasmine Byrne', 15.99)])


def configure_bookshop_service():
    """Configures the Flask Application Object
    for the bookshop service"""
    app = Flask(__name__)

    @app.route('/book/list', methods=['GET'])
    def get_books():
        return jsonify({'books': [b.to_json() for b in bookshop.books]})

    @app.route('/book/<int:isbn>', methods=['GET'])
    def get_book(isbn):
        book = bookshop.get(isbn)
        return jsonify({'book': book.to_json()})

    return app


if __name__ == '__main__':
    app = configure_bookshop_service()
    app.run(debug=True)
