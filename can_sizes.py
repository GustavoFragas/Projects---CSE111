"""
Instructions: 

In many countries, food is stored in steel cans (also known as tin cans) that are shaped like cylinders. There are many different sizes of steel cans. The storage efficiency of a can tells us how much a can stores versus how much steel is required to make the can. Some sizes of cans require a lot of steel to store a small amount of food. Other sizes of cans require less steel and store more food. A can size with a large storage efficiency is considered more friendly to the environment than a can size with a small storage efficiency.
The storage efficiency of a steel can is computed by dividing the volume of a can by its surface area.
storage_efficiency = volume / surface_area
In other words, the storage efficiency of a can is the space inside the can divided by the amount of steel required to make the can. The formulas for the volume and surface area of a cylinder are:
volume = π*radius**2*height
surface_area = 2*π*radius*(radius + height)
π is the constant PI, the ratio of the circumference of a circle divided by its diameter (use math.pi)
radius is the radius of the cylinder
height is the height of the cylinder

We have the need to create five classes called: main, compute_storage_efficiency, compute_cost_efficiency, compute_volume and compute_surface_area.

Work along with your instructor to write a Python program that computes and prints the storage efficiency for each of the following 12 steel can sizes. Then visually examine the output and answer this question, “Which can size has the highest storage efficiency?”

Name, Radius(centimeters), Height(centimeters), Cost per Can(U.S. dollars)
#1 Picnic,	6.83,	10.16,	$0.28
#1 Tall,	7.78,	11.91,	$0.43
#2,	8.73,	11.59,	$0.45
#2.5,	10.32,	11.91,	$0.61
#3 Cylinder,	10.79,	17.78,	$0.86
#5,	13.02,	14.29,	$0.83
#6Z,	5.40,	8.89,	$0.22
#8Z short,	6.83,	7.62,	$0.26
#10,	15.72,	17.78,	$1.53
#211,	6.83,	12.38,	$0.34
#300,	7.62,	11.27,	$0.38
#303,	8.10,	11.11,	$0.42

Requirements:
Your program must compute the volume of all 12 can sizes.
Your program must compute the surface area of all 12 can sizes.
Your program must compute and print the storage efficiency of all 12 can sizes.
Enhancements
Here is a list of enhancements that you could make to the program. Your instructor will walk you through at least one of them. Feel free to complete others.

Add another function named compute_storage_efficiency to your program. This function should call the compute_volume and compute_surface_area functions and then compute and return the storage efficiency of a steel can size. Replace code in the main function with a call to the compute_storage_efficiency function as appropriate. Did adding and calling the compute_storage_efficiency function reduce the number of lines of code in your program?
The table of can sizes that appears in the Assignment section above includes a column that contains the cost per can of each steel can size. Add another function to your program named compute_cost_efficiency that computes and returns the volume of a steel can divided by its cost. Write code to call the compute_cost_efficiency function and print the cost efficiency for each can size. Then visually examine the output and answer this question, “Which can size has the highest cost efficiency?”
If you remember how to use lists and a for loop from CSE 110, rewrite your main function so that it uses a list or lists that contain the can size names and dimensions. Then write a loop that processes the values in the list.
Add if statements inside the loop to automatically determine which can size has the best storage efficiency and which can size has the best cost efficiency.

How the program needs to look in the input:
> python can_sizes.py
#1 Picnic 2.04
#1 Tall 2.35
#2 2.49
#2.5 2.76
#3 Cylinder 3.36
#5 3.41
#6Z 1.68
#8Z short 1.80
#10 4.17
#211 2.20
#300 2.27
#303 2.34
"""

import math

def main():

    can_sizes = [
        ("#1 Picnic", 6.83, 10.16, 0.28),
        ("#1 Tall", 7.78, 11.91, 0.43),
        ("#2", 8.73, 11.59, 0.45),
        ("#2.5", 10.32, 11.91, 0.61),
        ("#3 Cylinder", 10.79, 17.78, 0.86),
        ("#5", 13.02, 14.29, 0.83),
        ("#6Z", 5.40, 8.89, 0.22),
        ("#8Z short", 6.83, 7.62, 0.26),
        ("#10", 15.72, 17.78, 1.53),
        ("#211", 6.83, 12.38, 0.34),
        ("#300", 7.62, 11.27, 0.38),
        ("#303", 8.10, 11.11, 0.42)
    ]

    for can in can_sizes:
        name, radius_main, height_main, cost_main = can
        storage_efficiency_main = compute_storage_efficiency(radius_main, height_main)
        cost_efficiency_main = compute_cost_efficiency(storage_efficiency_main, cost_main)
        print(f"{name} {storage_efficiency_main:.2f} and the cost efficiency is {cost_efficiency_main:.2f}")

def compute_storage_efficiency(radius_storage_efficiency, height_storage_efficiency):
    storage_efficiency = compute_volume(radius_storage_efficiency, height_storage_efficiency) / compute_surface_area(radius_storage_efficiency, height_storage_efficiency)
    return storage_efficiency
    
def compute_cost_efficiency(volume_cost_efficiency, cost_cost_efficiency):
    cost_efficiency = volume_cost_efficiency / cost_cost_efficiency
    return cost_efficiency

def compute_surface_area(radius, height):
    surface_area = 2 * math.pi * radius * (radius + height)
    return surface_area

def compute_volume(radius, height):
    volume = math.pi * radius**2 * height
    return volume

if __name__ == "__main__":
    main()