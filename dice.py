import random 

class Dice  : 
    def __init__(self) : 
        self.dice = []        
        self.makeDice()
    
    def makeDice(self) :
        for i in range(1,7,1): 
            self.dice.append(i)
         
    def rolDice (self) :
        self.randomNum = random.randrange(len(self.dice))
        print(self.randomNum)

def main () :
    d = Dice()
    d.rolDice()  

main() 
