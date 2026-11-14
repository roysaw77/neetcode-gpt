class Solution:
    def get_minimizer(self, iterations: int, learning_rate: float, init: int) -> float:
        # Objective function: f(x) = x^2
        # Derivative:         f'(x) = 2x
        # Update rule:        x = x - learning_rate * f'(x)
        # Round final answer to 5 decimal places
        
        if iterations==0:
            return round(init, 5)
        
        new_iterations=iterations-1

        fx=init**2
        der=2*init
        x_new = init - (learning_rate * der)

        return self.get_minimizer(
            new_iterations,
            learning_rate,
            x_new
        )
