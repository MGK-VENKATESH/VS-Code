feet=int(input("enter a length in feet:"))
print("""""    MENU:
        press 1 to convert into inches,
        press 2 to convert into yards,
        press 3 to convert into miles,
        press 4 to convert into millimeters,
        press 5 to convert into centimeters,
        press 6 to convert into meters,
        press 7 to convert into km""""" )
choice=int(input("enter a choice"))
inches=feet*12
yards=feet*0.33333
miles=feet*0.0001893939
millimeters=feet*304.8
centimeters=feet*30.48
meters=feet*0.3048
kilometers=feet*0.0003048
convert=[feet, inches,yards,miles,millimeters,centimeters,meters,kilometers]
print(convert[choice])