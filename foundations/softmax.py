import numpy as np
from numpy.typing import NDArray


class Solution:

    def softmax(self, z: NDArray[np.float64]) -> NDArray[np.float64]:
        # z is a 1D NumPy array of logits
        # Hint: subtract max(z) for numerical stability before computing exp
        # return np.round(your_answer, 4)
        max_z = max(z)
        def helper(x):
            return np.exp(x - max_z)
        val = []
        for x in z:
            val.append(helper(x))
        sum_val = sum(val)
        res = []
        for v in val:
            res.append(np.round(v/sum_val, 4))
        return res
