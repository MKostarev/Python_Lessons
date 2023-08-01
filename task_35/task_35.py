catalog = {}
s = ''
for i in range(3):
    n = input()
    x = int(input())
    if n in catalog:
        catalog[n] = catalog[n] + x
    else:
        
        catalog[n] = x
for k, v in catalog.items():
    s = s + (k + ':' + str(v)) + '\n'
    print(k + ':' + str(v))
with open('task_35.txt', 'w') as f:
    f.write(s)
