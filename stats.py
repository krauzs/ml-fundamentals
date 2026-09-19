import numpy as np

scores = np.array([10,20,30,40,50,60])
print(f"{scores.mean()}")
print(f"{scores.min()}")
print(f"{scores.max()}")
print(f"{scores.shape}")
print(scores[:3])
scores1 = scores
scores1 = scores1 + 5
print(scores1)
