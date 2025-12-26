''''
explore the possibility of writing contraint optimization problems in python to better understand the concept
of optimization and how it can be applied to machine learning problems.
'''
import numpy as np
class Optimize:
    def __init__(self, constraint):
        self.constraint = constraint
        
    
    def optimize(self, x0: np.ndarray, method: str = 'SLSQP', bounds: list = None, constraints: list = None) -> np.ndarray:
        pass