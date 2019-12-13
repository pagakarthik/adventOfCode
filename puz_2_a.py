from puz_2 import GravityAssist


if __name__ == "__main__":
    solution = GravityAssist()
    solution.solve(12, 2)
    output = solution.final_solution()

    print(output)