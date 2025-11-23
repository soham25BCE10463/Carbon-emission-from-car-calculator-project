import sys

def get_fuel_choice():
  return input("Enter which type of fuel your car uses (1 for Petrol / 2 for Diesel): ")

def get_trip_details():
   
    try:
        dist = float(input("Input the total distance you would cover in car (in kilometers): "))
        eff = float(input("Enter your car's fuel efficiency (Km/L): "))
        return dist, eff
    except ValueError:
        print("\n[INPUT ERROR] Please ensure you enter valid numerical values (digits only).")
        sys.exit()
