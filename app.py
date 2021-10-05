import requests

# Configure API request
endpoint = "https://developer.nps.gov/api/v1/parks?stateCode=me&api_key=WqThLdaNfRQFuckXCGLZUqlMI1lPIQ2jm0VcCOPJ"
HEADERS = {"Authorization": "WqThLdaNfRQFuckXCGLZUqlMI1lPIQ2jm0VcCOPJ"}
req = requests.get(endpoint)
# print(req)
a = req.json()
# print(a['data'])
# print(a.get('data',''))

for d in a['data']:
    # print('hello')
    print(d['fullName'])
# print(a['data'][0])


# Additional code would follow
