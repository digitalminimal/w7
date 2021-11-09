#Import the required plugins
from flask import Flask, request, jsonify
from flask_restful import Api, Resource 
import pickle
import pandas as pd
import joblib

#Step 1: Wrapping our app
app = Flask(__name__)
api = Api(app) #Wrapping o ur app in a restful API

#Step 1.5: Load the model
#load pipeline
model = joblib.load('pipe.joblib')

#Step 2: Define our API Resources
class HelloWorld(Resource):
    
    def get(self):
        return {"hello":"world"}

class Predict(Resource):

    def post(self): #post request
        json_data = request.get_json()
        print(json_data)
        #For 1 observation 
        # df = pd.DataFrame(json_data.values(), 
        #                 index = json_data.keys()).transpose()

        # How to take multiple observation
        df = pd.DataFrame.from_records(json_data)
        print('==============================')
        print(df)
        # result = model.predict(df)
        
        #for one observation
        print(df.iloc[[0]])
        result = model.predict(df.iloc[[0]])
        print(result)
        qqq = model.predict_proba(df.iloc[[0]])
        print("Soft Probability of : ")
        print(qqq[0][1].tolist())
        # #TO DO, MANY OBSERVATION 
        # print(df.iloc[[0]])
        # result = model.predict(df.iloc[[0]])
        # print(result)
        if result == 'Y':
            message = f"Soft Approval with score of : {str(qqq[0][1])}"
        else:
            message = f"Soft Dissaproval with score of : {str(qqq[0][0])}"
        return_this= [result.tolist(),qqq[0][1].tolist()]
        return message#result.tolist(),qqq[0][1].tolist()


#Step 3: Assign our endpoints
api.add_resource(HelloWorld, '/helloworld')
api.add_resource(Predict,'/predict')



#Step 4: Runing our api app
if __name__ == '__main__': 
    # app.run(debug=True)
    app.run(host="ec2-3-18-113-28.us-east-2.compute.amazonaws.com", port=5555)
