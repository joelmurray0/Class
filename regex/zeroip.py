import re
ip_address = input("Enter IP address")
remove_zero = re.compile(r"([1-9](\d*\.){3}\d+)")
matches = remove_zero.findall(ip_address)
print(matches[0][0])