def hotel_cost(nights):
  return (140 * nights)

def plane_ride_cost(city):
  if city == "Charlotte":
    return(183)
  elif city == "Tampa":
    return(220)
  elif city == "Pittsburgh":
    return(222)
  elif city == "Los Angeles":
    return(475)

def rental_car_cost(days):
    total = days * 40
    if days >= 7:
        total = total - 50
    elif days in range(3, 7):
        total = total - 20
    return(total)


def trip_cost(city, days, spending_money):
  total_cost = (rental_car_cost(days) + plane_ride_cost(city) + hotel_cost(days)
   + spending_money)
  return(total_cost)

print(trip_cost(city = "Los Angeles", days = 5, spending_money = 600))
