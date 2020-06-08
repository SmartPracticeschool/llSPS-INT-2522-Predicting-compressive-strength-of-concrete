import requests

url = 'http://localhost:5000/predict_api'
r = requests.post(url,json={'cement':205.0, 'blast_furnace_slag':133.4, 'fly_ash':0.0,
                            'water':195.0, 'superplasticizer':0.0, 'coarse_aggregate': 990.4,
                            'fine_aggregate': 825.5, 'age': 350})

print(r.json())



