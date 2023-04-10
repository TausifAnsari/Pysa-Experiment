import requests

def solve(value):
    result = eval(f"100 {value} 5")
    return result

base_url = 'https://pysa-api-2598d-default-rtdb.firebaseio.com/opr.json'
operators = requests.get(base_url)
opr_json = operators.json()
operator = opr_json["div"]

result = solve(operator)

print(result)

