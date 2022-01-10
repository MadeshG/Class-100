class car(object):
    def __init__(self,model,color,speed_limit,company):
        self.color=color
        self.model=model
        self.speed_limit=speed_limit
        self.company=company
    def start(self):
        print("started")
    def stop(self):
        print("stop")
    def accelerate(self):
        print("accelerate")
car1 = car("sedan","blue","100","honda")
car1.start()
car1.accelerate()
car1.model

car2 = car("coupe","black","175","mazda")
car2.start()