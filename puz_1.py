class Fuel_Counter(object):

    def __init__(self):
        self.data = []
        self.total_fuel = 0.0
        self.recursive_fuel = 0.0
        return
    
    def collect_data(self):
        with open("1_input.txt", 'r') as f:
            self.data = f.readlines()
            # self.data.append(float(x))
        print ("Completed reading file. #elements: ", len(self.data))
        # print ("Data: ", self.data)
        return

    def fuel_operation(self, val):
        return int(float(val)//3.0 - 2.0)
    
    def fuel_recursor(self, val):
        interim_sum = val
        if val <= 0:
            return 0
        else:
            return interim_sum + self.fuel_recursor(self.fuel_operation(val))
    
    def calculate_fuel(self):
        for item in self.data:
            self.total_fuel += float(item)//3.0 - 2.0
            self.recursive_fuel += self.fuel_recursor(float(item)//3.0 - 2.0)
    
    def total_fuel_needed(self):
        return int(self.total_fuel)
    
    def recursive_fuel_needed(self):
        return int(self.recursive_fuel)

        

