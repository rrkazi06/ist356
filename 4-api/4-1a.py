# import requests
# uri = "https://portal.app.cent-su.org/api/funnyname/random?n=3"
#     # [https://portal.app.cent-su.org] is URL https:// URL/Resource/Query
#     # [api/funnyname/random] is the resource
#     # [?n=3] is the query string, which is a parameter that specifies how many random names to return
# response = requests.get(uri)
# names = response.json() # python object
# print(names)
# print(names[-1]['first'], names[-1]['last'])

import requests
uri = "https://portal.app.cent-su.org/api/funnyname/random?n=3"
response = requests.get(uri)
if response.ok:
    names = response.json() # python object
    print(names)
    print(names[-1]['first'], names[-1]['last'])
else:
    print("Error:", response.status_code, response.text)