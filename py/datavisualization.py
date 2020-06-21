import matplotlib.pyplot as plt
#matplotlib.org basically matlab graphs in python
import data as d

purchases = d.selectAllPurchases() #return list of dictionary

costs = list(map(lambda m: float(m.get('Cost')), purchases))
category = list(map(lambda m: m.get('CategoryName')[0:10], purchases))

print(costs[0])
plt.figure(figsize=(40,3))
plt.bar(category, costs)
plt.show()
