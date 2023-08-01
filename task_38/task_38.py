import json

fake_dict = {
    'key': 'Любая строка'
}
s = json.dumps(fake_dict, ensure_ascii=False)
print(s)
result = json.loads(s)
print(result)