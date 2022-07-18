from calendar import monthcalendar

semanas = [len(monthcalendar(2022, x)) for x in range(1, 13)]
print(semanas)