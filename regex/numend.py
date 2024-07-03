import re
string = "klhwtb5csyg54"
number_end=re.compile(r".*[^0-9](\d+)")
matches = number_end.findall(string)
print(matches[0])