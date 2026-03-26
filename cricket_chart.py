import matplotlib.pyplot as plt
import numpy as np
overs=np.arange(1,21)
scores=[2,2,4,8,10,3,4,8,8,9,11,5,5,8,10,4,4,3,2,8,]
plt.bar(overs,scores,color="green")
plt.title("India score for all overs !! ")
plt.xlabel("overs(1-20)")
plt.ylabel("runs for every over")
plt.xticks(overs)
plt.grid(axis="y",linestyle="--")
plt.show()