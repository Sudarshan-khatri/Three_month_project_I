import re
result=re.match(r'\d+','123abc')
print(result.group()) #output:123

result=re.search(r'abc','123abc456')
print(result.group()) #output:123

result=re.findall(r'\d+','abc123def456')
print(result)