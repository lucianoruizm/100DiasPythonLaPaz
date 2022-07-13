from datetime import datetime

fecha = datetime.today()
formato = fecha.strftime("%d %B %Y, %I:%M:%S %p")
print(formato)