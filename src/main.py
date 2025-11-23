import sys
import inputs
import logic
import ui

def run_carbon_app():
    ui.show_welcome_banner()
    fuel_choice = inputs.get_fuel_choice()
    emission_factor, fuel_name = logic.get_emission_factor_for_fuel(fuel_choice)

    if emission_factor is None:
        ui.show_error_fuel()
        sys.exit()

    distance, mileage = inputs.get_trip_details()

    final_emission = logic.compute_carbon_emission(distance, mileage, emission_factor)

    ui.show_report(fuel_name, distance, mileage, final_emission)
    ui.show_eco_feedback(final_emission)

if __name__ == "__main__":
    run_carbon_app()
    ui.show_goodbye()
