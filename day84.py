from datetime import datetime

str = "12-07-2022"
fecha = datetime.strptime(str, "%d-%m-%Y")
time_stamp = fecha.timestamp()
print(time_stamp)