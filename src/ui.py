import utils
import config

def show_welcome_banner():
    print()
    utils.print_header_line() 
    print("\n                                                  ========================================                                                                   ")
    print("                                                   CALCULATING CARBON EMISSION FROM CAR                                                                      ")
    print("                                                  ========================================                                                                   ")
    utils.print_header_line()

def show_error_fuel():
    print("WRONG FUEL TYPE ENTERED")

def show_report(fuel_name, distance, mileage, total_emission):
    print("\n--- Detailed Carbon Emission Report ---")
    print(f"Fuel Source:      {fuel_name}")
    print(f"Distance Traveled: {distance} km")
    print(f"Fuel Economy:     {mileage} km/L")
    print("-" * 30)
    print(f"ESTIMATED Carbon OUTPUT IS: < {total_emission} > kg")

def show_eco_feedback(emission_value):
      utils.print_separator()
    
    if emission_value > config.HIGH_EMISSION_LIMIT:
            print("========================================================================================================================================================")
            print("==================================PLEASE USE PUBLIC TRANSPORT SUCH AS TRAIN OR BUSES OR FLIGHTS FOR LONG DISTANCE TRAVEL==================================")
            print("========================================================================================================================================================")
    
    elif config.MODERATE_EMISSION_LIMIT < emission_value <= config.HIGH_EMISSION_LIMIT:
            print("========================================================================================================================================================")
            print("=================================YOUR CAR IS POLLUTING THE ENVIRONMENT PLEASE PLANT SOME TREES!!!!!!!!!!!!!!!!!!!!======================================")
            print("========================================================================================================================================================")
    
    else:
            print("========================================================================================================================================================")
            print("=================================YOUR VEHICLE IS GOOD FOR USE AND ENVIRONMENT FRIENDLY , KEEP DRIVING  ^_^  ============================================")
            print("========================================================================================================================================================")
    
    utils.print_separator()

def show_goodbye():
    print("\n\n")
    print("                                                          ^_^  HAVE A GOOD RIDE  ^_^                                                                           ")
