import datetime

str = "12-07-2022"
format = datetime.datetime.strptime(str, "%d-%m-%Y")
time_stamp = datetime.datetime.timestamp(format)
print(time_stamp)