# import Flask and jsonify
from flask import Flask, jsonify, request
# import Resource, Api and reqparser
from flask_restful import Resource, Api, reqparse
import pandas as pd
import numpy
import pickle


calculator_app = Flask(__name__)
api = Api(calculator_app)


class Add(Resource):
    #def __init__(self, feats):
    #self.feats = feats

    def get(self):
        # create request parser
        parser = reqparse.RequestParser()

        # create argument 'name'
        parser.add_argument('number1', type=int)
        parser.add_argument('number2', type=int)
        
        # parse 'name'
        number1 = parser.parse_args().get('number1')
        number2 = parser.parse_args().get('number2')
        sum = number1 + number2
        sum = f'sum of {number1}+{number2} is exactly {sum}'
        return jsonify(sum)

class Substract(Resource):
    def get(self):
        # create request parser
        parser = reqparse.RequestParser()

        # create argument 'name'
        parser.add_argument('number1', type=int)
        parser.add_argument('number2', type=int)
        
        # parse 'name'
        number1 = parser.parse_args().get('number1')
        number2 = parser.parse_args().get('number2')
        sub = number1-number2

        return jsonify(sub=sub)


class Multiply(Resource):
   def get(self):
        # create request parser
        parser = reqparse.RequestParser()

        # create argument 'name'
        parser.add_argument('number1', type=int)
        parser.add_argument('number2', type=int)
        
        # parse 'name'
        number1 = parser.parse_args().get('number1')
        number2 = parser.parse_args().get('number2')
        mul = number1*number2

        return jsonify(mul=mul)


class Divide(Resource):
     def get(self):
        # create request parser
        parser = reqparse.RequestParser()

        # create argument 'name'
        parser.add_argument('number1', type=int)
        parser.add_argument('number2', type=int)
        
        # parse 'name'
        number1 = parser.parse_args().get('number1')
        number2 = parser.parse_args().get('number2')
        div = number1/number2

        return jsonify(div=div)


# assign endpoint
api.add_resource(Add, '/add')
api.add_resource(Substract, '/substract')
api.add_resource(Multiply, '/multiply')
api.add_resource(Divide, '/divide')


if __name__ == '__main__':
    calculator_app.run(host="ec2-18-191-255-83.us-east-2.compute.amazonaws.com", port=5555)

    