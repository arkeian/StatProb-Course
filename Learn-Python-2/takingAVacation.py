# Page 1
def answer():
  return 42

# Page 2 - 7
"""
(ID) Dari Page 2 ke 7, kodenya ditambahkan sedikit demi sedikit sampai terbentuk suatu program yang kohesif.
(EN) From Page 2 to 7, the code is added gradually until a complete program is constructed.
"""
def hotel_cost(nights):
  return 140 * nights

def plane_ride_cost(city):
  if city == "Charlotte":
    return 183
  elif city == "Tampa":
    return 220
  elif city == "Pittsburgh":
    return 222
  elif city == "Los Angeles":
    return 475

def rental_car_cost(days):
  cost = 40 * days
  if days >= 7:
    cost -= 50
  elif days >= 3:
    cost -= 20
  return cost

def trip_cost(city, days, spending_money):
  return hotel_cost(days - 1) + plane_ride_cost(city) + rental_car_cost(days) + spending_money

print(trip_cost("Los Angeles", 5, 600))