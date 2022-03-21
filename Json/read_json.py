import json
f=open("assistant.json","r")
s=f.read()
print(s)
assistant=json.loads(s)
print(type(assistant))
print(assistant['siri']['product'])
for x in assistant:
    print(assistant[x])