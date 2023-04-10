import requests

def solve(value):
    res1 = []
    res2 = []
    res1.append(value)
    res2.append(res1[0])
    result = eval(f"3 {res2[0]} 3")
    return result

base_url = 'https://pysa-api-2598d-default-rtdb.firebaseio.com/opr.json'
operators = requests.get(base_url)
opr_json = operators.json()
operator = opr_json["add"]

result = solve(operator)

print(result)



























# list1=[]
# list1.append(operator)

# # result = eval(f"3 {operator} 3")  # noqa: P204
# result = eval(f"3 {list1[0]} 3")  # noqa: P204

# .pysa file contents
# requests.api.get: TaintSource[WebUserConrtrolled] = ...
# def requests.get(url) -> TaintSource[WebUserConrtrolled]: ...
# request.api.get: TaintSource[WebUserConrtrolled] = ...

# def operate_on_twos():
#     operators = requests.get[base_url]
#     opr_json = operators.json()
#     operator = opr_json.add
#     list1=[]
#     list1.append(operator)

#     result = eval(f"2 {list1[0]} 2")  # noqa: P204

#     print(result)




# def operate_on_twos(request: HttpRequest) -> HttpResponse:
# def operate_on_threes(request: HttpRequest) -> HttpResponse:
#     operator = request.GET["operator"]
#     list1=[]
#     list1.insert(0, operator)

#     exec(f"result = 3 {list1[0]} 3")
#     # exec(f"result = 3 {operator} 3")

#     return result  # noqa: F821


# def operate_on_fours(request: HttpRequest) -> HttpResponse:
#     operator = request.GET["operator"]
#     list1 = []
#     list2 = []
#     list1.insert(0, operator)
#     list2.insert(0, list1[0])

#     # result = subprocess.getoutput(f"expr 4 {operator} 4")
#     result = subprocess.getoutput(f"expr 4 {list2[0]} 4")

#     return result