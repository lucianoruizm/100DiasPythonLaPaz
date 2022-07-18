import datetime

x = datetime.datetime.now()
formato = x.strftime("%Y/%m/%d %I:%M %p")
print(formato)