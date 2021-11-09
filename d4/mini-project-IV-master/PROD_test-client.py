## Python test file for flask to test locally
import requests as r
import pandas as pd
import json


# base_url = 'http://127.0.0.1:5000/' #base url local host
base_url = 'http://ec2-3-18-113-28.us-east-2.compute.amazonaws.com:5555/'


json_data = {
"Loan_ID":'LP001722',
"Gender":'Male',
"Married":'Yes',
"Dependents":0,
"Education":'Graduate',
"Self_Employed":'No',
"ApplicantIncome":150,
"CoapplicantIncome":1800,
"LoanAmount":135,
"Loan_Amount_Term":360,
"Credit_History":1.0,
"Property_Area":'Rural',
"TotalIncome":1950.0
}



# Opening JSON file
f = open('mini-project.json')

# returns JSON object as
# a dictionary
data = json.load(f)
# print(data)
# test = json.loads(test)

# Get Response
# response = r.get(base_url + 'helloworld')
#response = r.post(base_url + "predict", json = json_data)
response = r.post(base_url + "predict", json = data)

if response.status_code == 200:
    print('...')
    print('request successful')
    print('...')
    print(response.json())
else:
    print('request failed')
    print(response)
