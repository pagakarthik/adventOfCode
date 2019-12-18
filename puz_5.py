class TEST(object):
    def __init__(self):
        self.parser = {"1": self.add, "2": self.multiply, "3": self.write_to, "4": self.read_from}
        self.increment = {"1": 4, "2": 4, "3": 2, "4": 2, "99": 0}
        self.number_of_operands = {"1": 2, "2": 2, "3": 1, "4": 1, "99": 0}
        self.data = []
        return

    def write_to(self, addr):
        val = int(input("Enter the input"))
        print ("addr: ", addr )
        self.data[addr] = str(val)
        return
    
    def read_from(self, addr):
        val = self.data[addr]
        print("Value at addr %d is %d"%(addr, val))
        return

    def collect_data(self):
        with open("5_input.txt", 'r') as stream:
            data = stream.readlines()
        self.data = []
        for line in data:
            self.data += line.strip().split(",")
        return

    def add(self, i_1, i_2):
        return int(i_1) + int(i_2)
    
    def multiply(self, i_1, i_2):
        return int(i_1) * int(i_2)
# can use decorator
    # def add(self, i_1, i_2, op_loc):
    #     self.data[op_loc] = int(i_1) + int(i_2)
    #     return
    
    # def multiply(self, i_1, i_2):
    #     self.data[op_loc] = int(i_1) * int(i_2)
    #     return

    def get_val(self, op_tuple):
        print ("op tuple: ", op_tuple)
        if op_tuple[0] == 0:
            return int(self.data[op_tuple[1]])
        elif op_tuple[0] == 1:
            return int(op_tuple[1])
        else:
            print("Operand tuple (param_code, operand): ", op_tuple)
            raise ValueError("Unknown param code")
        return

    
    def execute_instruction(self, cur_addr):
        operation = self.data[cur_addr][-2:]
        op_code = str(int(operation))
        n_operands = self.number_of_operands[op_code]
        operands = {}
        for oprnd_id in range(1, n_operands+1):
            loc_back = 2 + oprnd_id
            operand = int(self.data[cur_addr + oprnd_id])
            try:
                param_mode = int(self.data[cur_addr][-1*loc_back])
            except IndexError:
                param_mode = 0
            
            if op_code in ["3", "4"]:
                param_mode = 1
            operands[oprnd_id] = (param_mode, operand)
        print("op_code and operands: ", op_code, "&& ", operands)
        print("type of op code: ", type(op_code))
        if op_code in ["1", "2"]:
            print ("Running add mul instruction")
            out = int(self.data[cur_addr+3])
            self.data[out] = str(self.parser[op_code](self.get_val(operands[1]), self.get_val(operands[2])))
        elif op_code in ["3", "4"]:
            print("running i/o instruction")
            self.parser[op_code](self.get_val(operands[1]))
        else:
            print("sending key error")
            raise KeyError

        return

    def digest_data(self):
        current_cmd = 0
        while(len(self.data) != 0 and self.data[current_cmd][-2:] != "99"):
            try:
                increment = self.increment[str(self.data[current_cmd])[-2:]]
            except KeyError:
                print ("last increment: ", increment)
                print("Key error at increment: ", current_cmd)
                break
            try:
                self.execute_instruction(current_cmd)
            except KeyError:
                print ("breaking out: ", current_cmd, ", ", self.data[current_cmd])
                break
            # print ("Expected increment: ", increment)
            current_cmd =  current_cmd + increment
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
    print(len(solution.data))
    print (solution.data[0])
    result = solution.digest_data()
    # print ("result: ", result)

    

