import itertools as it
import numpy as np

class Crossing(object):
    def __init__(self):
        self.compass = {"R": 1, "L": -1, "U":1j, "D":-1j}
        self.data = {}
        self.wire_crosses = {}
        self.closest_crosses = {}
        self.data_steps = {}
        self.optimal_crosses = {}
        return
    
    def collect_data(self):
        with open("3_input.txt", 'r') as stream:
            data = stream.readlines()

        self.data = {}
        for line_id, line in enumerate(data):
            wire_stream = line.strip().split(",")
            point = 0
            wire = [point]
            wire_steps = {point:0}
            step_cnt = 0
            for element in wire_stream:
                direction, distance = element[0], int(element[1:])
                for _ in range(distance):
                    point += self.compass[direction]
                    step_cnt += 1
                    wire.append(point)
                    if point not in wire_steps:
                        wire_steps[point] = step_cnt
            self.data[line_id] = wire
            self.data_steps[line_id] = wire_steps
        return
    
    def find_crossings(self):
        wire_keys = self.data.keys()
        u_combinations = it.combinations(wire_keys, 2)
        for key_pair in u_combinations:
            self.wire_crosses[key_pair] = set(self.data[key_pair[0]]) & set(self.data[key_pair[1]])
        return
    
    def crossing_closest_to_central_port(self):
        for key, points in self.wire_crosses.items():
            closest_cross = 0
            proximity = np.Inf
            # print (points)
            for pt in points:
                dist = abs(pt.real) + abs(pt.imag)
                if dist != 0.0 and dist < proximity:
                    closest_cross = pt
                    proximity = dist
            self.closest_crosses[key] = closest_cross
            print(" For wire combination %s, closest_cross is: %s"%(str(key), str(closest_cross)))
        return self.closest_crosses

    def minimal_signal_delay(self):
        for key, points in self.wire_crosses.items():
            optimal_cross = 0
            loss = np.Inf
            for pt in points:
                loss_fn = self.data_steps[key[0]][pt] + self.data_steps[key[1]][pt]
                if loss_fn != 0 and loss_fn < loss:
                    optimal_cross = pt
                    loss = loss_fn
            self.optimal_crosses[key] = optimal_cross
            print(" For wire combination %s, optimal_cross is: %s and the minimal signal delay is: %d"%(str(key), str(optimal_cross), loss))
        return self.optimal_crosses


    
if __name__ == "__main__":
    solution = Crossing()
    solution.collect_data()
    # print (len(solution.data))
    solution.find_crossings()
    # final_result = solution.crossing_closest_to_central_port()
    # final_result_b = solution.minimal_signal_delay()
    # print(final_result_b)