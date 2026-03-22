def ft_water_reminder():
	water_day = 2
	x = int(input("Days since last watering: "))
	if x > water_day:
		print("Water the plant!")
	else:
		print("Plants are fine")