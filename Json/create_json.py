import json
assistant={}
assistant['siri']={
    'name' : 'siri',
    'product' : 'apple'
}
assistant['alexa']={
    'name' : 'alexa',
    'product' : 'amazon'
}
s=json.dumps(assistant)
print(s)
with open("assistant.json","w") as f:
    f.write(s)