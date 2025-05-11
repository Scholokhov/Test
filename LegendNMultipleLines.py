import numpy as np
import matplotlib.pyplot as plt

stock_a = [100, 102, 99, 101, 101, 100, 102]
stock_b = [90, 95, 102, 104, 105, 103, 109]
stock_c = [110, 115, 100, 105, 100, 98, 101]
     
plt.plot(stock_a, label = "A",color = "black")
plt.plot(stock_b, label = "B", color = "blue")
plt.plot(stock_c, label = "C", color = "red")


plt.legend(loc="lower center")#can be used in other chart types too especially pie charts
plt.show()