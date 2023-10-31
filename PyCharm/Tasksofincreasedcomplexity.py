import math
y = float(input("Введите угол часовой стрелки (в радианах): "))
angle_minutes = math.degrees(y) * 30
full_hours = y / (2 * math.pi) * 12
full_minutes = y / (2 * math.pi) * 60
print("Угол для минутной стрелки:", angle_minutes, "градусов")
print("Полные часы:", full_hours)
print("Полные минуты:", full_minutes)