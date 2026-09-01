def ft_plant_age():
    day = 60
    plant = int(input("Enter plant age in days: "))
    if plant > day:
        print("Plant is ready to harvest!")
    else:
        print("Plant need more time to grow")
