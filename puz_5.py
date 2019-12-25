class TEST(object):
    def __init__(self):
        self.parser = {"1": self.add, "2": self.multiply, "3": self.write_to, "4": self.read_from, "5": self.jump_if_true,
                        "6": self.jump_if_false, "7": self.less_than, "8": self.equals}
        self.increment = {"1": 4, "2": 4, "3": 2, "4": 2, "5":3, "6":3, "7":4, "8":4, "99": 0}
        self.number_of_operands = {"1": 3, "2": 3, "3": 1, "4": 1, "5":2, "6":2, "7":3, "8":3, "99": 0}
        self.data = []
        return

    def less_than(self, i_1_loc, i_2_loc, op_loc):
        i_1 = self.data[int(i_1_loc)]
        i_2 = self.data[int(i_2_loc)]
        if i_1 < i_2:
            self.data[int(op_loc)] = str(1)
        else:
            self.data[int(op_loc)] = str(0)

        self.current_cmd = self.current_cmd + self.increment['7'] 
        return
    
    def equals(self, i_1_loc, i_2_loc, op_loc):
        i_1 = self.data[int(i_1_loc)]
        i_2 = self.data[int(i_2_loc)]
        if i_1 == i_2:
            self.data[int(op_loc)] = str(1)
        else:
            self.data[int(op_loc)] = str(0)

        self.current_cmd = self.current_cmd + self.increment['8'] 
        return 
    
    def jump_if_true(self, i_1_loc, i_2_loc):
        i_1 = self.data[int(i_1_loc)]
        i_2 = self.data[int(i_2_loc)]
        if int(i_1) != 0:
            self.current_cmd = int(i_2)
        else:
            # neglect current instruction and proceed
            self.current_cmd = self.current_cmd + self.increment['5']        
        return
    
    def jump_if_false(self, i_1_loc, i_2_loc):
        i_1 = self.data[int(i_1_loc)]
        i_2 = self.data[int(i_2_loc)]
        if int(i_1) == 0:
            self.current_cmd = int(i_2)
        else:
            # neglect current instruction and proceed
            self.current_cmd = self.current_cmd + self.increment['6']         
        return

    def write_to(self, addr):
        val = int(input("Enter the input"))
        # print ("addr: ", addr )
        self.data[int(addr)] = str(val)
        self.current_cmd = self.current_cmd + self.increment['3'] 
        return
    
    def read_from(self, addr):
        val = self.data[int(addr)]
        print("Value at addr %s is %s"%(str(addr), str(val)))
        self.current_cmd = self.current_cmd + self.increment["4"] 
        return

    def collect_data(self):
        with open("5_input.txt", 'r') as stream:
            data = stream.readlines()
        self.data = []
        for line in data:
            self.data += line.strip().split(",")
        return

    def add(self, i_1_loc, i_2_loc, op_loc):
        # print ("op_loc: ", op_loc)
        i_1 = self.data[int(i_1_loc)]
        i_2 = self.data[int(i_2_loc)]
        self.data[int(op_loc)] = str(int(i_1) + int(i_2))
        self.current_cmd = self.current_cmd + self.increment["1"] 
        return
    
    def multiply(self, i_1_loc, i_2_loc, op_loc):
        i_1 = self.data[int(i_1_loc)]
        i_2 = self.data[int(i_2_loc)]
        self.data[int(op_loc)] = str(int(i_1) * int(i_2))
        self.current_cmd = self.current_cmd + self.increment["2"] 
        return
    
    def execute_instruction(self, cur_addr):
        operation = self.data[cur_addr][-2:]
        op_code = str(int(operation))
        n_operands = self.number_of_operands[op_code]
        operands = []
        for oprnd_id in range(1, n_operands+1):
            loc_back = 2 + oprnd_id
            # the input code needs to complete
            # systems exists in case of any error other than index
            try:
                param_mode = int(self.data[cur_addr][-1*loc_back])
            except IndexError:
                param_mode = 0 
            if param_mode == 1:
                # send the param address
                operand = int(cur_addr + oprnd_id)
            else:
                # send the value at the param addres
                operand = int(self.data[cur_addr + oprnd_id])
            operands.append(operand)
        self.parser[op_code](*operands)
        return

    def digest_data(self):
        self.current_cmd = 0
        # the loop is expected to terminte by itself (with the Key error)
        while(len(self.data) != 0 and self.data[self.current_cmd][-2:] != "99"):
            try:
                # print ("current_operation: ", self.data[self.current_cmd][-2:])
                self.execute_instruction(self.current_cmd)
                # print("new_data: ", self.data)
            except KeyError:
                # print ("breaking out: ", self.current_cmd, ", ", self.data[self.current_cmd])
                break
        return self.data

    def solve(self):
        self.collect_data()
        self.digest_data()

        return self.data
    
    def reset_memory(self):
        self.collect_data()
        return
    
    def final_solution(self):
        return self.data[0]

if __name__ == "__main__":
    solution = TEST()
    solution.collect_data()
    # print(len(solution.data))
    # print (solution.data[0])
    result = solution.digest_data()
    # print ("result: ", result)

    

