F = open("sample.txt", "r")
x = F.readlines()
script = ''
for val in x:
    script += '' + val.strip() + '' + ','

print script[0:-1]
