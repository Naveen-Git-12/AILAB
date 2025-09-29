import numpy as np
import skfuzzy as fuzz
x = np.linspace(0, 10, 100)
A = fuzz.trimf(x, [0, 2, 5])
B = fuzz.trimf(x, [3, 5, 8])
A_and_B = np.fmin(A, B)   # Fuzzy AND (min)
A_or_B  = np.fmax(A, B)   # Fuzzy OR  (max)
print("Sample AND values:", A_and_B[:10])
print("Sample OR values:", A_or_B[:10])
