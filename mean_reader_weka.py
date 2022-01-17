
with open("myk2") as f:
    str = f.readlines()
"""
with open("myk3") as f:
    str = f.readlines()

"""

"""
with open("myk4") as f:
    str = f.readlines()
"""


cluster1_mean = []
cluster2_mean = []
#cluster3_mean = []
#cluster4_mean = []

for line in str:
    lst = line.split()
    lst = lst[2:]
    if (len(lst) >= 3):
        cluster1_mean.append(float(lst[0]))
        cluster2_mean.append(float(lst[1]))
        #cluster3_mean.append(float(lst[2]))
        #cluster4_mean.append(float(lst[2]))

print(cluster1_mean)
print(cluster2_mean)
#print(cluster3_mean)
#print(cluster4_mean)
