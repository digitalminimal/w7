from flask import Flask
from flask_restful import Api, Resource


#step1 wrapper our app
app=Flask(__name__)
api=Api(app)  


#2-design our API design
class HelloWorld(Resource):
    def get(self):
        return{"Hello":"World"}

#3-endpoints
api.add_resource(HelloWorld,'/HelloWorld')

#4-running API/
if __name__ == '__main__':
    app.run(debug=True)



