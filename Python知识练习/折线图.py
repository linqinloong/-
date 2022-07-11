import matplotlib.pyplot as plt
import numpy as np
from pylab import mpl

"""a = np.arange(10)
plt.plot(a,a*1.5,a,a*2.5,a,a*3.5,a,a*4.5)
plt.show()"""


import numpy as np
import matplotlib.pyplot as plt
from pylab import mpl

mpl.rcParams['font.sans-serif'] = ['FangSong']
mpl.rcParams['axes.unicode_minus'] = False
x = np.linspace(-4, 4, 200)
f1 = np.power(10, x)
f2 = np.power(np.e, x)
f3 = np.power(2, x)
plt.plot(x, f1, 'r', ls='-', linewidth=2, label='$10^x$')
plt.plot(x, f2, 'b', ls='--', linewidth=2, label='$e^x$')
plt.plot(x, f3, 'g', ls=':', linewidth=2, label='$2^x$')
plt.axis([-4, 4, -0.5, 8])
plt.text(1, 7.5, r'$10^x$', fontsize=16)
plt.text(2.2, 7.5, r'$e^x$', fontsize=16)
plt.text(3.2, 7.5, r'$2^x$', fontsize=16)
plt.title('幂函数曲线', fontsize=16)
plt.legend(loc='upper left')
plt.show()