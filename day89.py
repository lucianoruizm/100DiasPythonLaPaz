from calendar import monthcalendar

lunes = [s[0] for s in monthcalendar(2022, 7) if s[0] != 0]
print(lunes)