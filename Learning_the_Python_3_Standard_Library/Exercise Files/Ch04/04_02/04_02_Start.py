# Getting more control over formatting
from datetime import datetime

now = datetime.now()

print(now.strftime("%a %A %d"))
print(now.strftime("%b %B %m"))
print(now.strftime("%a %d %B %Y"))

print(now.strftime("%H %M %S %p"))

print(now.strftime("%y %Y"))