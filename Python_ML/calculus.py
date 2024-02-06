class Calculus:

   def __init__(self):
     self.power_result = "dy/dx = "
   
   def power_rule(self, n, power):
     print(f"the derivative of y = {n}x^{power} is")
    #if y = f(x) then y' = f'(x)
     #example inputs	
     #y = x^2 -> y' = 2x
     #y = (2x^3)
     #"y = (3x^2 + 2x + 1)
    
     if type(power) != int and type(n) != int:
      raise TypeError("the input for n and power must be integers.")
     if n < 1:
       raise ValueError("the formula input must be a positive integer.")
     n = power
     power = power - 1
     formula = self.power_result+str(n)+"x^"+str(power)+""
     return formula

test_power_rule = Calculus()
print("here's an example of the power rule:")
user_n = int(input("enter a number for x: "))
user_power = int(input("enter a number for the power of x: "))

result = test_power_rule.power_rule(user_n, user_power)
print(result)
      
      
     

     
