import re
date = "2020-11-11"
date_secure=re.compile(r"(\d+)-(\d+)-(\d+)")
matches = date_secure.findall(date)
print(f"{matches[0][2]}-{matches[0][1]}-{matches[0][0]}")
