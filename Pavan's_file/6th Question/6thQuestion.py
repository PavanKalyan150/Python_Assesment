people = [
{'name': 'John', 'age': 25},
{'name': 'Jane', 'age': 30},
{'name': 'Alice', 'age': 25},
{'name': 'Bob', 'age': 30}]
d={}
for idx in people:
    if(idx['age'] in d):
        d[idx['age' ]].append(idx['name'])
    else:
        d[idx['age']]=[idx['name' ]]
print(d)