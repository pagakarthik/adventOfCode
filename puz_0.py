import numpy as np
from puz_1 import Fuel_Counter as p_1


def main():
    print("This is Advent!")
    solution_1 = p_1()
    solution_1.collect_data()
    solution_1.calculate_fuel()
    fuel = solution_1.total_fuel_needed()
    r_fuel = solution_1.recursive_fuel_needed()
    print("Final answer: ", fuel)
    print ("Recursive fuel: ", r_fuel)
    return

if __name__ == "__main__":
    main()