import requests
URL = "http://127.0.0.1:5000/scoring"

json_data = {'alcohol': 14.23,
 'malic_acid': 1.71,
 'ash': 2.43,
 'alcalinity_of_ash': 15.6,
 'magnesium': 127.0,
 'total_phenols': 2.8,
 'flavanoids': 3.06,
 'nonflavanoid_phenols': 0.28,
 'proanthocyanins': 2.29,
 'color_intensity': 5.64,
 'hue': 1.04,
 'od280/od315_of_diluted_wines': 3.92,
 'proline': 1065.0}

# sending get request and saving the response as response object 
r = requests.post(url = URL, json = json_data) 

print(r.json())