import time
from puz_2 import GravityAssist
from puz_3 import Crossing
from puz_4 import SContainer
from puz_5 import TEST
from puz_6 import UniversalOrbitMap

def timer(func):

    def inner(*args, **kwargs):
         start = time.time()
         func(*args, **kwargs)
         print("compute time for %s is: %7f"%(func.__name__, time.time()-start))

    return inner

@timer
def puz_2_b():
    solution = GravityAssist()
    for i_1 in range(100):
        for i_2 in range(100):
            solution.solve(i_1, i_2)
            if solution.final_solution() == 19690720:
                print("%d, %d"%(i_1, i_2))
                break
            else:
                solution.reset_memory()
        else: # for -else construct of python
            continue
        break
    print ("Final solution: ", 100*i_1 + i_2)
    return

@timer
def puz_3_a():
    solution = Crossing()
    solution.collect_data()
    # print (len(solution.data))
    solution.find_crossings()
    final_result = solution.crossing_closest_to_central_port()
    print (final_result)
    # print("Final result: ", abs(final_result.values()[0].real) + abs(final_result.values()[0].imag))

@timer
def puz_3_b():
    solution = Crossing()
    solution.collect_data()
    # print (len(solution.data))
    solution.find_crossings()
    final_result = solution.minimal_signal_delay()
    print (final_result)
    # print("Final result: ", abs(final_result.values()[0].real) + abs(final_result.values()[0].imag))


@timer
def puz_4_a():
    solution = SContainer()
    solution.collect_data()
    result = solution.iterate_over_range_and_solve()
    for key, pwd in result.items():
        print("Number of password for key %s is %d"%(str(key), len(pwd)))

@timer
def puz_4_b():
    solution = SContainer()
    solution.collect_data()
    result = solution.iterate_over_range_and_solve_naughty_elf ()
    for key, pwd in result.items():
        print("Number of password for key %s is %d"%(str(key), len(pwd)))

@timer
def puz_5():
    solution = TEST()
    solution.collect_data()
    result = solution.digest_data()
    return

@timer
def puz_6_a():
    solution = UniversalOrbitMap()
    solution.collect_data()
    checksum_result = solution.get_checksum()
    print ("checksum: ", checksum_result)
    return checksum_result

@timer
def puz_6_b():
    solution = UniversalOrbitMap()
    solution.collect_data()
    you_path, san_path = solution.paths_for_you_and_santa()
    paths = solution.find_closest_path(you_path, san_path)
    print("result: ", len(paths[0]) + len(paths[1]) -2)
    return paths

if __name__ == "__main__":
    # puz_2_b()
    # puz_3_a()
    # puz_3_b()
    # puz_4_a()
    # puz_4_b()
    # puz_5() # enter 1 for 5_a and 5 for 5_b
    puz_6_b()