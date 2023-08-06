from flask import Flask, request
from flask_restful import Resource, Api

app = Flask(__name__)
api = Api(app)

class Multiply(Resource):
    def get(self, a, b):
        return {"result": a * b}

api.add_resource(Multiply, '/<int:a>/<int:b>')

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=5053)
