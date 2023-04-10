import requests

def solve(value):
    num1 = 100
    num2 = 11
    result = num1 * num2
    return result

base_url = 'https://pysa-api-2598d-default-rtdb.firebaseio.com/opr.json'
operators = requests.get(base_url)
opr_json = operators.json()
operator = opr_json["mul"]

result = solve(operator)

print(result)
