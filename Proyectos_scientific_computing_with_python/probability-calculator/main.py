# This entrypoint file to be used in development. Start by reading README.md
import prob_calculator
from unittest import main

prob_calculator.random.seed(95)


#print(hat.contents)
hat = prob_calculator.Hat(blue=3,red=2,green=6)
#probability = prob_calculator.experiment(hat=hat, expected_balls={"blue":2,"green":1}, num_balls_drawn=4, num_experiments=1000)
#actual = probability
#hat = prob_calculator.Hat(red=5,blue=2)
actual = hat.draw(2)
print(actual)
print("Probability:", actual)
'''
# Run unit tests automatically
main(module='test_module', exit=False)
'''