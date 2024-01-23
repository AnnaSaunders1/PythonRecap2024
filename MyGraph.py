##remember that python is an open source coding platform

##steps to create a virtual environment
    ##  1. create the virtual environment
    ##      py -3 -m venv name (this is the command to create the environment that is put in the terminal)
    ##  2. Activate the virtual environment
    ##      .\myvenv\Scripts\activate
    ##  3. Install 3rd party library/module
    ##      pip3 install 'module name'

import matplotlib.pyplot as plt
import numpy as np

x = np.linspace(0, 20, 100)
plt.plot(x, np.sin(x))

plt.show()

print("Hello World!")
