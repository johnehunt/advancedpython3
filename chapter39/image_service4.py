import os

from flask import Flask, jsonify, request, send_from_directory, make_response
from werkzeug.utils import secure_filename

PROJECT_HOME = os.path.dirname(os.path.realpath(__file__))
UPLOAD_FOLDER = '{}/uploads/'.format(PROJECT_HOME)


def create_new_folder(local_dir):
    new_path = local_dir
    if not os.path.exists(new_path):
        os.makedirs(new_path)
    return new_path


def create_image_service():
    app = Flask(__name__)
    app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER
    app.config['UPLOAD_EXTENSIONS'] = ['.jpg', '.png', '.gif']


    @app.route('/api/image/<string:file>', methods=['GET'])
    def get_image(file):
        img_name = secure_filename(file)
        return send_from_directory(app.config['UPLOAD_FOLDER'], img_name, as_attachment=True)


    @app.route('/api/image', methods=['POST'])
    def upload_image():
        print('upload_image()')
        if request.files['file']:
            print(app.config['UPLOAD_FOLDER'])
            img = request.files['file']
            img_name = secure_filename(img.filename)
            print('Secure version of image name ', img_name)
            create_new_folder(app.config['UPLOAD_FOLDER'])
            saved_path = os.path.join(app.config['UPLOAD_FOLDER'], img_name)
            print("saving to " + str(saved_path))
            img.save(saved_path)
            # Return a url to the image
            # return send_from_directory(app.config['UPLOAD_FOLDER'], img_name, as_attachment=True)
            return 'Success'
        else:
            return "Where is the image?"

    @app.errorhandler(400)
    def not_found(error):
        return make_response(jsonify({'file': 'Error'}), 400)

    return app


if __name__ == '__main__':
    app = create_image_service()
    app.run(debug=True)
