import numpy as np

v = np.array([2,2])
A = np.array([[2,2],
             [0,1]])

result = A @ v 
print(result)

i_hat_new = np.array([2, 0])   # where i-hat landed (first column of A)
j_hat_new = np.array([2, 1])   # where j-hat landed (second column of A)

manual_result = v[0] * i_hat_new + v[1] * j_hat_new
print(manual_result)

