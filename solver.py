import time
from puz_2 import GravityAssist

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

if __name__ == "__main__":
    puz_2_b()