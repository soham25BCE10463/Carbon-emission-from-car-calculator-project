import fueltype
def compute_carbon_emission(travel_distance_km, vehicle_mileage_kml, emission_factor_value):

    if vehicle_mileage_kml <= 0:

        return 0.0

    fuel_used_liters = travel_distance_km / vehicle_mileage_kml

    total_carbon_emission = fuel_used_liters * emission_factor_value

    return round(total_carbon_emission, 2)
