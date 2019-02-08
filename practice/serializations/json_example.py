import json
a = {'key': 123, "key_bool": True, "key1": None}

print(json.dumps(a))

r = json.dumps(a)

print(r)

print(json.loads(r))
