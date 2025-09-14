def totalfare(distance):
    return (distance * 10) + 50

strtrips = input("Trips= ")
listtrips = [int(x.strip()) for x in strtrips.split(",")]

count = 0
total_fare = 0

for distance in listtrips:
    count += 1
    fare = totalfare(distance)
    print(f"Trip {count}: ${fare}")
    total_fare += fare

print(f"Total Fare: ${total_fare}")
