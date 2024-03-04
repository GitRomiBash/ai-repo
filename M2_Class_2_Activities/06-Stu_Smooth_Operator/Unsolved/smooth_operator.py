# Declare variables
budget = 2000
cities = ["Rome", "Nairobi", "Phnom Penh", "Santiago", "Toronto", "Rotorua"]
cities_daily_cost = [150, 70, 60, 80, 110, 125]
days = input("How many days can you travel? ")
city_to_visit = input("What city would you like to visit? ")

# Check if days is a number, and convert it to an integer if it is
if days.isdigit():
    days = int(days)
    print("Number of days converted to integer successfully.")
# Else print an error
else:
    print("Error: The input is not a valid number.")

# Check if budget and days are integers, and if so, calculate the daily budget
#if budget.isdigit() and days.isdigit():
if type(budget) is int and type(days) is int:
   daily_budget = budget / days
   print(f"Daily budget: ${daily_budget}")
   #print(float("Daily budget: ", daily_budget))

# Else print an error
else:
    print("Error: Budget and days should be integers.")

# Check if the city_to_visit is in the cities list, and if so,
# get the daily cost for the city
if city_to_visit in cities:
    # Get the daily cost for the city
    city_index = cities.index(city_to_visit)
    city_daily_cost = cities_daily_cost[city_index]
# Else set the city_daily_cost to 0 to be used for error checking
else:
    city_daily_cost = 0




# Check if the city_daily_cost is greater than 0 and equal to or less than the
# daily budget, and if so, tell the traveler they can afford the vacation
if city_daily_cost > 0 and city_daily_cost <= daily_budget:
    print(f"You can afford the trip to {city_to_visit} for {days} with"
          + f"your daily budget of ${daily_budget} because the daily cost is $"
          + str(cities_daily_cost)
    )

# Else if the city_daily_cost is greater than 0 and greater than the daily budget,
# calculate and print out how much more per day the traveler needs

# Else print an error
