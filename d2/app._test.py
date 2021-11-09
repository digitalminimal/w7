import requests as r

base_url =  'http://127.0.0.1:5000' #base url local host


response  = r.get(base_url + 'helloworld')


if response.status_code == 200:
    print(".....")
    print("request successful")
    print("...")

    print(response.json())
else:
    print('request failed')