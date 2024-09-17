# Page 1
from datetime import datetime

# Page 2
from datetime import datetime

now = datetime.now()
print(now)

# Page 3
from datetime import datetime

now = datetime.now()

print(now.year)
print(now.month)
print(now.day)

# Page 4
from datetime import datetime
now = datetime.now()

print("%02d/%02d/%d" % (now.month, now.day, now.year))

# Page 5
from datetime import datetime
now = datetime.now()

print('%02d:%02d:%02d' % (now.hour, now.minute, now.second))

# Page 6
from datetime import datetime
now = datetime.now()

print("%02d/%02d/%04d %02d:%02d:%02d" % (now.month, now.day, now.year, now.hour, now.minute, now.second))