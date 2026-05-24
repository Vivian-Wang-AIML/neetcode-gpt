class Solution:
    def get_minimizer(self, iterations: int, learning_rate: float, init: int) -> float:
        # Objective function: f(x) = x^2
        # Derivative:         f'(x) = 2x
        # Update rule:        x = x - learning_rate * f'(x)
        # Round final answer to 5 decimal places
        res = init
        def update_rule(x: float) -> float:
            x_new = x - learning_rate*2*x
            return x_new
        for i in range(iterations):
            res = update_rule(res)
        return round(res, 5)
