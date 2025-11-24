import formula
def get_emission_factor_for_fuel(fuel_type):
   fuel_type_input = fuel_type.lower().strip()
   if fuel_type_input == "1":
       return 2.31 
   elif fuel_type_input == "2":
       return 2.68
   else:
       return None
