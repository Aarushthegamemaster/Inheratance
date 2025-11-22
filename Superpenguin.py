class Bird:
    def __init__(self):
        print("The bird is ready")
    
    def whoisthis(self):
        print("Bird")
    
    def swim(self):
        print("Swim faster")

class Penguin(Bird):

    def __init__(self):
        super().__init__()
        print("The Penguin is ready")

    def whoisthis(self):
        print("Penguin")
    
    def run(self):
        print("Run faster")
peggy = Penguin()
peggy.whoisthis()
peggy.run()
peggy.swim()