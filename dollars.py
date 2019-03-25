import re
x="i have withdrawn $10.00 from bank"
y=re.findall('/$[0-9.]+')
print(y)
