from flask import Flask
from flask_restful import Resource, Api

app = Flask(__name__)
api = Api(app)

class Exp(Resource):
    def get(self, n1: int, n2: int):
        result = n1 ** n2
        return {'result': result}

api.add_resource(Exp, '/<int:n1>/<int:n2>')

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=5056)
