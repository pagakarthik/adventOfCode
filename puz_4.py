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

    def naughty_elf_is_happy(self, value):
        digit_cl = flatten(self.get_two_digit_collections(value))
        max_val = 0.0
        dual_list = []
        for element in digit_cl:
            str_element = str(element)
            if str_element[0] == str_element[1]:
                dual_list.append(element)
                if element > max_val:
                    max_val = element
        # if dual_list.count(max_val) > 1:
        #     return False
        # else:
        #     return True

        """
        by using the `.some` method, we only need 1 of the matches
        to not be a part of a larger group
        """
        set_dual = set(dual_list)
        dict_dual  = {}
        for val in set_dual:
            dict_dual[val] = dual_list.count(val)
        
        result = False
        for val, ocrs in dict_dual.items():
            if ocrs == 1:
                result = True
                break
        
        return result


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

    def iterate_over_range_and_solve_naughty_elf(self):
        result = {}
        for key, limits in self.data.items():
            l_limit = limits['L']
            u_limit = limits['U']
            pwd = []
            for val in range(l_limit, u_limit+1):
                if self.is_a_code(val):
                    if self.naughty_elf_is_happy(val):
                        pwd.append(val)
            result[key] = pwd
        return result

if __name__ == "__main__":
    solution = SContainer()
    solution.collect_data()
    # result_old = solution.iterate_over_range_and_solve()
    result_new = solution.iterate_over_range_and_solve_naughty_elf()
    # removed_pwd = []
    # for val in result_old[0]:
    #     if val not in result_new[0]:
    #         removed_pwd.append(val) 
    # print(removed_pwd)
    for key, pwd in result_new.items():
        print("Number of password for key %s is %d"%(str(key), len(pwd)))
        
        


