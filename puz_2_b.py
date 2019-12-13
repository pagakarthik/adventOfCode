from puz_2 import GravityAssist

if __name__ == "__main__":
    solution = GravityAssist()

    for i_1 in range(100):
        for i_2 in range(100):
            solution.solve(i_1, i_2)
            if solution.final_solution() == 19690720:
                print("%d, %d"%(i_1, i_2))
                break
            else:
                # print("%d, %d, %d"%(i_1, i_2, solution.final_solution()))
                solution.reset_memory()