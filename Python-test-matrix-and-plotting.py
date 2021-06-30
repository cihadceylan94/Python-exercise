import matplotlib.pyplot as plt
import numpy as np
print("Hello world")
m1 = [[2,3,1],
      [0,2,4],
      [6,3,5]]
for i in range(3):
    print(m1[i])
print()
m2 = [[5,3,2],
      [1,3,3],
      [1,3,1]]
for i in range(3):
    print(m2[i])
print()

m3 = [[0,0,0],
      [0,0,0],
      [0,0,0]]
print()
for i in range(3):
    for j in range(3):
        m3[i][j] = m1[i][j] + m2[i][j]
    print(m3[i])

for i in range(3):
    for j in range(3):
        plt.plot( m3[i],m3[j])
plt.show()
