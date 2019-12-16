import itertools

def flatten(z):
    data = []
    if type(z) == type(1):
        data.append(z)
    else:
        for val in z:
            if type(z) == type([]):
                data = data + flatten(val)
    return data
class SContainer(object):
    def __init__(self):
        self.data = {}
        return
    
    def collect_data(self):
        with open("4_input.txt", 'r') as stream:
            data = stream.readlines()
        
        limits = {}
        for itr, line in enumerate(data):
            rng = line.strip().split("-")
            limits["L"] = int(rng[0])
            limits["U"] = int(rng[1])
            self.data[itr] = limits
        return

    def get_two_digit_collections(self, val):
        data = []
        if val < 9.0:
            return data
        else:
            data.append(val%100)
            new_val = self.get_two_digit_collections(val//10)
            if len(new_val) != 0:
                data.append(new_val)
            return  data


    def is_a_code(self, value):
        last_seen_digit = 0
        for digit in str(value):
            if int(digit) < last_seen_digit:
                return False
            last_seen_digit = int(digit)
        
        digit_cl = flatten(self.get_two_digit_collections(value))

        for element in digit_cl:
            str_element = str(element)
            if str_element[0] == str_element[1]:
                return True
        
        return False

    def iterate_over_range_and_solve(self):
        result = {}
        for key, limits in self.data.items():
            l_limit = limits['L']
            u_limit = limits['U']
            pwd = []
            for val in range(l_limit, u_limit+1):
                if self.is_a_code(val):
                    pwd.append(val)
            result[key] = pwd
        return result


if __name__ == "__main__":
    solution = SContainer()
    solution.collect_data()
    result = solution.iterate_over_range_and_solve()
    for key, pwd in result.items():
        print("Number of password for key %s is %d"%(str(key), len(pwd)))
        
        


