import re
from collections import defaultdict

def norm(value):
    return value.replace("<td>", "").replace("</td>", "").replace("</tr>", "").replace("</b>", "")

def norm1(value):
    return ''.join(char for char in value if char.isalnum())

with open("1.html", "r", encoding="UTF-8") as file:
    lines = file.readlines()

raw = lines[lines.index("</center>\n") + 1:lines.index("</table>\n")]

slid = [raw[i:i+3] for i in range(0, len(raw), 3)]

data_map = defaultdict(list)

for vec in slid:
    v = list(map(norm, vec))
    key = v[1]
    f = v[0]
    s = [x.strip() for x in v[2].split(",")]

    for x in s:
        data_map[key].append((int(f), int(x)))

enc = [(norm1(key.lower()), values) for key, values in sorted(data_map.items())]

for key, vec in enc:
    with open(f"{key}.txt", "w") as out_file:
        lines = [f"{x[0]} {x[1]}\n" for x in vec]
        out_file.writelines(lines)
