class UniversalOrbitMap():
    def __init__ (self):
        self.orbit_map = {}
        self.checksum = 0
        return
    
    def collect_data(self):
        with open("6_input.txt", 'r') as stream:
            data = stream.readlines()

        self.orbit_map = {}
        for pair in data:
            result = pair.strip().split(")")
            val, key = result[0], result[1]
            self.orbit_map[key] = val
        return
    
    def get_orbit_info(self, key):
        orbit_count = 0
        if key not in self.orbit_map:
            return 0
        else:
            orbit_count += 1
            return orbit_count + self.get_orbit_info(self.orbit_map[key])
    
    def get_checksum(self):
        total_number_of_orbits = 0
        for key in self.orbit_map.keys():
            total_number_of_orbits += self.get_orbit_info(key)
        self.checksum = total_number_of_orbits
        return total_number_of_orbits

    def find_path_for_planet(self, planet):
        path = []
        if planet not in self.orbit_map:
            return []
        else:
            path.append(planet)
            return path + self.find_path_for_planet(self.orbit_map[planet])
    
    def find_closest_path(self, path_a, path_b):
        # return (list(set(path_a).difference(set(path_b))), list(set(path_b).difference(set(path_a))))
        return ([i for i in path_a if i not in path_b], [j for j in path_b if j not in path_a])
    
    def paths_for_you_and_santa(self):
        you_path = self.find_path_for_planet("YOU")
        san_path = self.find_path_for_planet("SAN")
        # print("you_path: ", you_path)
        # print("san_path: ", san_path)
        return (you_path, san_path)


if __name__ == "__main__":
    solution = UniversalOrbitMap()
    solution.collect_data()
    # checksum_result = solution.get_checksum()
    # print ("checksum: ", checksum_result)
    you_path, san_path = solution.paths_for_you_and_santa()
    paths = solution.find_closest_path(you_path, san_path)
    print("result: ", len(paths[0]) + len(paths[1]) -2)