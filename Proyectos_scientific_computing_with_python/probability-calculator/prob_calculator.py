import copy
import random
# Consider using the modules imported above.


class Hat:
    def __init__(self, **kwargs):
        self.contents = []
        self.hat = {}
        for key, value in kwargs.items():
            self.hat[key] = value
            for val in range(value):
                self.contents.append(key)
        
        
    def draw(self, n):
        if len(self.contents) < n:
            return self.contents
        
        else:
            lista = [] 
            for k in range(n):
                random.shuffle(self.contents)
                lista.append(self.contents.pop())
            return lista
    
                
    


def experiment(hat, expected_balls, num_balls_drawn, num_experiments):
    count = 0
    for i in range(num_experiments):
        hat_copy = copy.deepcopy(hat)   
        balls = hat_copy.draw(num_balls_drawn)
        activador = True 
      
        for key in expected_balls.keys():
            if not key in balls:
                activador = False
                break
            else:
                if balls.count(key)< expected_balls[key]:
                    activador = False
                    break
        if activador:
            count += 1
    probablity = count / num_experiments
    
            
    
    return probablity
