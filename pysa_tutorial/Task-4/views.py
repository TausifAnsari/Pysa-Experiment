import requests
from collections import defaultdict

def solve(value):
    if value in {"+", "-", "*", "/"}:
        result = eval(f"8 {value} 4")
        return result
    else:
        return -1

base_url = 'https://pysa-api-2598d-default-rtdb.firebaseio.com/opr.json'
operators = requests.get(base_url)
opr_json = operators.json()
operator = opr_json["mul"]

d = defaultdict(list)
d[1].append(operator)
operators = d[1]

result = solve(operator)

print(result)