import random

total = 200

pattern = ""
for i in range(total):
    if random.random() > 0.5:
        pattern += "H"
    else:
        pattern += "T"

res = ""
res += pattern[:3]

for i, c in enumerate(pattern[3:], start=3):
    if pattern[i-3: i+1] == "THTH":
        res += "<font color=red>H</font>"
    elif pattern[i-3: i+1] == "HTHH":
        res += "<font color=green>H</font>"
    else:
        res += pattern[i]

print(res)
