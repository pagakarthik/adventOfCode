class GravityAssist(object):
    def __init__(self):
        self.parser = {"1": self.add, "2": self.multiply}
        self.data = []
        return

    def collect_data(self):
        with open("2_input.txt", 'r') as stream:
            data = stream.readlines()

        for line in data:
            self.data += line.strip().split(",")
        return

    def add(self, i_1, i_2):
        return int(i_1) + int(i_2)
    
    def multiply(self, i_1, i_2):
        return int(i_1) * int(i_2)
    

    def digest_data(self):
        current_cmd = 0
        while(len(self.data) != 0 and self.data[current_cmd] != "99"):
            i_1 = int(self.data[current_cmd+1])
            i_2 = int(self.data[current_cmd+2])
            out = int(self.data[current_cmd+3])
            self.data[out] = self.parser[self.data[current_cmd]](self.data[i_1], self.data[i_2])
            current_cmd =  current_cmd + 4
        return self.data

    def solve(self, input_1, input_2):
        self.collect_data()
        if len(self.data) != 0:
            self.data[1] = input_1
            self.data[2] = input_2
        
        self.digest_data()

        return self.data
    
    def reset_memory(self):
        self.collect_data()
        return
    
    def final_solution(self):
        return self.data[0]


    

