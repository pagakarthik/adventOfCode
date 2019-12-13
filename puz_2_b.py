from puz_2 import GravityAssist

import time

if __name__ == "__main__":
    solution = GravityAssist()
    start = time.time()
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
    print ("compute time: ", time.time() -start)
    print ("Final solution: ", 100*i_1 + i_2)
