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

if __name__ == "__main__":
    solution = UniversalOrbitMap()
    solution.collect_data()
    checksum_result = solution.get_checksum()
    print ("checksum: ", checksum_result)
