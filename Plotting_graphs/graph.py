import matplotlib.pyplot as plt
import numpy as np
import math

length=int(input("Enter the length of well (in A): "))
n=int(input("Enter the energy state: "))

x1 = np.arange(0, length, 0.001)
y1 = (math.sqrt(2/length))*np.sin((np.pi)*x1*n/length)
plt.plot(x1, y1)


x2 = [0,2,length]
y2 = [0,0,0]
plt.plot(x2, y2,color='red')

x3 = [0,0,0]
y3 = [0,1,1]
plt.plot(x3, y3,color='red')

x4 = [length,length,length]
y4 = [0,1,1]
plt.plot(x4, y4, color='red')

x5 = np.arange(0, length, 0.0001)
y5 = ((math.sqrt(2/length))*np.sin((np.pi)*x5*n/length))**2
plt.plot(x5, y5,color='green')

plt.xlabel('length')
plt.ylabel('$\psi$ and |$\psi$|^2 ')
plt.title('Wave function and probability density for particles in an infinite potential well')
plt.show()

e=((6.626*(10**-34))**2)/(8*9.1*10**-31*length**2)
print("The energy of the given particle in the state is",e)