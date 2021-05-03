from flask import Flask, jsonify, request, abort, make_response
from flask.json import JSONEncoder
import pymysql

class Room:
    def __init__(self, id, name, description):
        self.id = id
        self.name = name
        self.description = description

    def __str__(self):
        return self.id + ' ' + self.name + ' ( ' + self.description + ')'


class BookJSONEncoder(JSONEncoder):
    def default(self, obj):
        if isinstance(obj, Room):
            return {
                'id': obj.id,
                'name': obj.name,
                'description': obj.description
            }
        else:
            return super(BookJSONEncoder, self).default(obj)


class RoomService:
    def __init__(self, rooms=[]):
        self.rooms = rooms

    def get(self, id):
        if int(id) > len(self.rooms):
            abort(404)
        return list(filter(lambda b: b.isbn == id, self.rooms))[0]

    def add_room(self, room):
        self.rooms.append(room)

    def delete_room(self, id):
        self.rooms = list(filter(lambda b: b.isbn != id, self.rooms))


room_service = RoomService()
connection = None


def setup_database_connection():
    global connection
    # Open database connection
    connection = pymysql.connect('localhost', 'user', 'user123', 'room_monitoring')


def load_rooms_from_db():
    # prepare a cursor object using cursor() method
    cursor = connection.cursor()
    # execute SQL query using execute() method.
    cursor.execute('SELECT * FROM rooms')

    data = cursor.fetchall()
    for row in data:
        print(row)
        room_service.add_room(Room(int(row[0]), row[1], row[2]))

    # disconnect from server
    connection.close()


def update_room_in_db(room):
    # prepare a cursor object using cursor() method
    connection.autocommit(False)
    cursor = connection.cursor()
    try:
        update_string = "UPDATE rooms "
        update_string = update_string + "SET name = '" + str(room.name) + "' "
        update_string = update_string + "SET description = '" + str(room.description) + "' "
        update_string = update_string + "WHERE id = " + str(room.id)
        cursor.execute(update_string)
        connection.commit()
    except:
        # Something went wrong
        # rollback the changes
        connection.rollback()


def save_room_in_db(room):
    # prepare a cursor object using cursor() method
    connection.autocommit(False)
    cursor = connection.cursor()
    try:
        insert_string = "INSERT INTO rooms (id, name, description) VALUES ("
        insert_string = insert_string + "'" + str(room.id) + "', "
        insert_string = insert_string + "'" + str(room.name) + "', "
        insert_string = insert_string + "'" + str(room.description) + "')"
        cursor.execute(insert_string)
        connection.commit()
    except:
        # Something went wrong
        # rollback the changes
        connection.rollback()


def delete_room_in_db(room):
    connection.autocommit(False)
    cursor = connection.cursor()
    try:
        delete_string = "DELETE FROM students WHERE id = " + str(room.id)
        cursor.execute(delete_string)
        connection.commit()
    except:
        # Something went wrong
        # rollback the changes
        connection.rollback()


def create_rooms_service():
    app = Flask(__name__)
    app.json_encoder = BookJSONEncoder


    @app.route('/room/list', methods=['GET'])
    def get_rooms():
        return jsonify({'rooms': room_service.rooms})


    @app.route('/room/<int:isbn>', methods=['GET'])
    def get_room(isbn):
        room = room_service.get(isbn)
        return jsonify({'room': room})


    @app.route('/room', methods=['POST'])
    def create_room():
        print('create room')
        if not request.json or not 'id' in request.json:
            abort(400)
        room = Room(request.json['id'],
                    request.json['name'],
                    request.json.get('description', ""))
        # Add the room the cache
        room_service.add_room(room)
        # Permanently save it to the database
        save_room_in_db(room)
        return jsonify({'room': room}), 201


    @app.route('/room', methods=['PUT'])
    def update_room():
        if not request.json or not 'id' in request.json:
            abort(400)
        id = request.json['id']
        room = room_service.get(id)
        room.title = request.json['name']
        room.author = request.json['description']
        update_room(room)
        return jsonify({'room': room}), 201


    @app.route('/room/<int:isbn>', methods=['DELETE'])
    def delete_room(id):
        delete_room(room_service.get(id))
        room_service.delete_room(id)
        return jsonify({'result': True})


    @app.errorhandler(400)
    def not_found(error):
        return make_response(jsonify({'room': 'Not found'}), 400)

    return app


if __name__ == '__main__':
    setup_database_connection()
    load_rooms_from_db()
    app = create_rooms_service()
    app.run(debug=True)
