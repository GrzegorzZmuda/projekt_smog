import numpy as np
import matplotlib.pyplot as plt

#wykresik z kolorkami
def chart(A,x,y):
    z = np.array(A)
    Z = z.reshape(x, y)
    plt.imshow(Z, interpolation='bilinear')
    plt.show()