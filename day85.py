# from datetime import datetime

# print(datetime.utcnow())

#Solución Python La Paz
from datetime import datetime, timezone

utc = datetime.now(timezone.utc)
print(utc)