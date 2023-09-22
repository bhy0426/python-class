import requests

#response = requests.get("http://localhost:8080", data=[("a","b")])
response = requests.get("https://www.bible.ac.kr")

d_result = response.json()
#print(type(d_result))
result = f"""{d_result["method"]}
"""

#result = f"""{response.json()=}
#"""

#print(result)
print(response.json())
#print(response.status_code)

if(response.status_code != 200):
    raise Exception()