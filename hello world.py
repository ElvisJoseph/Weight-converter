weight = int(input("Weight: "))
unit = input("K(gs) or l(bs):")

if unit == "K":
    converted = weight / 0.45
    print("Weight in lbs:" + str(converted))
else:
    converted = weight * 0.45
    print("Weight in Kgs: " + str(converted))