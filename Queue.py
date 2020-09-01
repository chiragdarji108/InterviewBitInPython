
class queue:
    def __init__(self):
        self.s1=[]
        self.s2=[]
    
    def enQueue(self,x):
        self.s1.append(x)

    def deQueue(self):
        if(len(self.s2)==0):

            if(len(self.s1)==0):
                print("Queue is Empty")

            while(len(self.s1)!=0): 
                self.s2.append(self.s1[-1])
                self.s1.pop()

        x=self.s2[-1]
        self.s2.pop()
        return x

if __name__ == '__main__': 
    q = queue() 
    q.enQueue(1)  
    q.enQueue(2)  
    q.enQueue(3)  
  
    print(q.deQueue()) 
    print(q.deQueue()) 
    print(q.deQueue()) 
    
