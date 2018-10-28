from flask import Flask
from flask_cors import CORS
from flask_restful import Resource, Api, reqparse
import werkzeug

app = Flask(__name__)
CORS(app)
api = Api(app)


class UploadImage(Resource):
    def post(self):
        parser = reqparse.RequestParser()
        parser.add_argument(
            'image', type=werkzeug.datastructures.FileStorage, location='files')
        args = parser.parse_args()
        imagefile = args['image']
        imagefile.save("assets/image.jpg")


class Poem(Resource):
    def get(self):
        return {"data": "这是诗词"}


class Description(Resource):
    def get(self):
        return {"data": "这是文本描述"}


class Message(Resource):
    def get(self):
        return {"data": "这是名言"}


api.add_resource(UploadImage, '/api/uploadImage')
api.add_resource(Poem, '/api/poem')
api.add_resource(Description, '/api/description')
api.add_resource(Message, '/api/message')

if __name__ == '__main__':
    app.run(debug=True)
