import config

def get_emission_factor_for_fuel(fuel_choice):
  
    clean_choice = fuel_choice.strip()
    
    if clean_choice == config.OPTION_PETROL:
        return config.PETROL_FACTOR, "Petrol"
    elif clean_choice == config.OPTION_DIESEL:
        return config.DIESEL_FACTOR, "Diesel"
    else:
        return None, "Unknown"

def compute_carbon_emission(distance, mileage, factor):
   
    if mileage <= 0:
        return 0.0

    fuel_used = distance / mileage
    total_emission = fuel_used * factor
    
    return round(total_emission, 2)
