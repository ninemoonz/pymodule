def ft_count_harvest_recursive():
	day = int(input("Days until harvest: "))
	recursive_helper(1, day)

def recursive_helper(count, day):
	if count > day:
		print("Harvest time!")
	else:
		print("Day", count)
		recursive_helper(count + 1, day)