from flask import Flask, jsonify, request, abort, make_response

from flask.json import JSONEncoder


class Book:
    def __init__(self, isbn, title, author, price):
        self.isbn = isbn
        self.title = title
        self.author = author
        self.price = price

    def __str__(self):
        return self.title + ' by ' + self.author + ' @ ' + str(self.price)


class BookJSONEncoder(JSONEncoder):
    def default(self, obj):
        if isinstance(obj, Book):
            return {
                'isbn': obj.isbn,
                'title': obj.title,
                'author': obj.author,
                'price': obj.price
            }
        else:
            return super(BookJSONEncoder, self).default(obj)


class Bookshop:
    def __init__(self, books):
        self.books = books

    def get(self, isbn):
        if int(isbn) > len(self.books):
            abort(404)
        return list(filter(lambda b: b.isbn == isbn, self.books))[0]

    def add_book(self, book):
        self.books.append(book)

    def delete_book(self, isbn):
        self.books = list(filter(lambda b: b.isbn != isbn, self.books))


bookshop = Bookshop([Book(1, 'XML', 'Gryff Smith', 10.99),
                     Book(2, 'Java', 'Phoebe Cooke', 12.99),
                     Book(3, 'Scala', 'Adam Davies', 11.99),
                     Book(4, 'Python', 'Jasmine Byrne', 15.99)])

def create_bookshop_service():
    app = Flask(__name__)
    app.json_encoder = BookJSONEncoder


    @app.route('/book/list', methods=['GET'])
    def get_books():
        return jsonify({'books': bookshop.books})


    @app.route('/book/<int:isbn>', methods=['GET'])
    def get_book(isbn):
        book = bookshop.get(isbn)
        return jsonify({'book': book})


    @app.route('/book', methods=['POST'])
    def create_book():
        print('create book')
        if not request.json or not 'isbn' in request.json:
            abort(400)
        book = Book(request.json['isbn'],
                    request.json['title'],
                    request.json.get('author', ""),
                    float(request.json['price']))
        bookshop.add_book(book)
        return jsonify({'book': book}), 201


    @app.route('/book', methods=['PUT'])
    def update_book():
        if not request.json or not 'isbn' in request.json:
            abort(400)
        isbn = request.json['isbn']
        book = bookshop.get(isbn)
        book.title = request.json['title']
        book.author = request.json['author']
        book.price = request.json['price']
        return jsonify({'book': book}), 201


    @app.route('/book/<int:isbn>', methods=['DELETE'])
    def delete_book(isbn):
        bookshop.delete_book(isbn)
        return jsonify({'result': True})


    @app.errorhandler(400)
    def not_found(error):
        return make_response(jsonify({'book': 'Not found'}), 400)

    return app

if __name__ == '__main__':
    app = create_bookshop_service()
    app.run(debug=True)
