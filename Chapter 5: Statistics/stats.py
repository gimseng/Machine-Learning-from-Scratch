import matplotlib.pyplot as plt
from collections import Counter, defaultdict


num_friends=[1,1,1,2,3,4,4,4,4,6,1,1,1,2,10]
friend_counts=Counter(num_friends)
xs=range(max(num_friends))
ys = [friend_counts[x] for x in xs]
plt.bar(xs,ys)
plt.axis([0,max(num_friends)+1,0,25])
plt.show()
