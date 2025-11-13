"""
Exceeding the Requirements
If your program fulfills the requirements for this assignment as described above, your program will earn 93% of the possible points. In order to earn the remaining 7% of points, you will need to add one or more features to your program so that it exceeds the requirements. Use your creativity to add features. Add a comment to the top of your code that explains your enhancement(s). Here are a few suggestions for additional features.

Inside the functions of your water_flow.py program, you may have typed numbers for Earth’s acceleration of gravity, the density of water, and the dynamic viscosity of water. Instead of using the numbers inside your functions, define the following constants outside your functions. Then use the constant names in place of the numbers inside your functions.

The functions that you wrote for this assignment, calculate water pressure in kilopascals (kPa). In the United States, water pressure is usually expressed in pounds per square inch (psi). Write a function in your water_flow.py program that converts kPa to psi. Then at the bottom of your main function, add code that calls your conversion function and prints the final pressure value in both kPa and psi.

Add a test function to your test_water_flow.py file that verifies that your psi-from-kPa conversion function works correctly. In your test function, call your conversion function multiple times so that your test function is a rigorous test.
"""

PVC_SCHED80_INNER_DIAMETER = 0.28687 # (meters)  11.294 inches
PVC_SCHED80_FRICTION_FACTOR = 0.013  # (unitless)
SUPPLY_VELOCITY = 1.65               # (meters / second)
HDPE_SDR11_INNER_DIAMETER = 0.048692 # (meters)  1.917 inches
HDPE_SDR11_FRICTION_FACTOR = 0.018   # (unitless)
HOUSEHOLD_VELOCITY = 1.75            # (meters / second)
WATER_DENSITY=998.2000000             # density of water (998.2 kilogram / meter^3)      
WATER_DYNAMIC_VISCOSITY = 0.0010016     # (pascal seconds
EARTH_ACCELERATION_OF_GRAVITY = 9.8066500  # (meters / second^2)       

def main():
    tower_height = float(input("Height of water tower (meters): "))
    tank_height = float(input("Height of water tank walls (meters): "))
    length1 = float(input("Length of supply pipe from tank to lot (meters): "))
    quantity_angles = int(input("Number of 90° angles in supply pipe: "))
    length2 = float(input("Length of pipe from supply to house (meters): "))
    
    water_height = water_column_height(tower_height, tank_height)
    pressure, pressure_psi = pressure_gain_from_water_height(water_height)
    diameter = PVC_SCHED80_INNER_DIAMETER
    friction = PVC_SCHED80_FRICTION_FACTOR
    velocity = SUPPLY_VELOCITY
    reynolds = reynolds_number(diameter, velocity)
    loss = pressure_loss_from_pipe(diameter, length1, friction, velocity)
    pressure += loss
    loss = pressure_loss_from_fittings(velocity, quantity_angles)
    pressure += loss
    loss = pressure_loss_from_pipe_reduction(diameter,
            velocity, reynolds, HDPE_SDR11_INNER_DIAMETER)
    pressure += loss
    diameter = HDPE_SDR11_INNER_DIAMETER
    friction = HDPE_SDR11_FRICTION_FACTOR
    velocity = HOUSEHOLD_VELOCITY
    loss = pressure_loss_from_pipe(diameter, length2, friction, velocity)
    pressure += loss
    print(f"Pressure at house: {pressure:.1f} kilopascals")
    print(f"Pressure at house: {pressure_psi:.1f} psi")

def water_column_height(tower_height, tank_height):
    return tower_height + 3 * tank_height / 4

def pressure_gain_from_water_height(height):
    pressure_in_kilopascals = WATER_DENSITY * EARTH_ACCELERATION_OF_GRAVITY * height / 1000
    converted_to_psi = convert_kPa_to_psi(pressure_in_kilopascals)
    return pressure_in_kilopascals, converted_to_psi

def pressure_loss_from_pipe(pipe_diameter, pipe_length, friction_factor, fluid_velocity):
    numerator = -friction_factor * pipe_length * WATER_DENSITY * fluid_velocity ** 2
    denominator = 2000 * pipe_diameter
    return numerator / denominator

def pressure_loss_from_fittings(fluid_velocity, quantity_fittings):
    return -0.04 * WATER_DENSITY * fluid_velocity ** 2 * quantity_fittings / 2000

def reynolds_number(hydraulic_diameter, fluid_velocity):
      value =  WATER_DENSITY * hydraulic_diameter * fluid_velocity / WATER_DYNAMIC_VISCOSITY
      return value

def pressure_loss_from_pipe_reduction(larger_diameter, fluid_velocity, reynolds_number, smaller_diameter):
    k=(.1 + 50 / reynolds_number) * ((larger_diameter / smaller_diameter) ** 4 - 1)
    return -k * WATER_DENSITY * fluid_velocity ** 2 / 2000

def convert_kPa_to_psi(pressure_in_kilopascals):
    return pressure_in_kilopascals * 0.14503773773

if __name__ == "__main__":
    main()