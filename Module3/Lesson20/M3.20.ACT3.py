def hotel_cost (n):
    return 140 * n

def plane_ride_cost(city):
    if city == "Charlotte":
        return 183
    elif city =="Tampa":
        return 220
    elif city == "Pittsburgh":
        return 222
    else:
        return 475
    
def rental_car_cost(days):
    if days >= 7:
        return 40 * days - 50
    elif days >= 3:
        return 40 *days -20
    return 40 * days

def trip_cost(city, days, money):
    return hotel_cost(days) + plane_ride_cost(city) + rental_car_cost(days) + money

print(rental_car_cost(5))
print(plane_ride_cost("Los Angeles"))
print (hotel_cost(7))
print(trip_cost("Los Angeles", 7, 500))