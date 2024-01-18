import numpy as np
import networkx as nx
import matplotlib.pyplot as plt
import pandas as pd
from MIOcalculate import IOSuperPageRank as IOS


crudeoil = np.load("crudeoil.npy",allow_pickle=True)
print([crudeoil[i].shape for i in range(len(crudeoil))])
print(type(crudeoil))
lightoil = np.load("lightoil.npy",allow_pickle=True)
print([lightoil[i].shape for i in range(len(crudeoil))])
print(type(lightoil))
fabric = np.load("fabric.npy",allow_pickle=True)
print([fabric[i].shape for i in range(len(crudeoil))])
print(type(fabric))
block_matrix_seq = [np.array([[crudeoil[i], lightoil[i]],
                    [np.zeros((131, 131)), fabric[i]]])
                    for i in range(len(crudeoil))]
print(block_matrix_seq)

tempio_seq = []

#
for i in range(0,len(block_matrix_seq)-1):
    tempio_value = IOS.IOSuperPageRank(block_matrix_seq[i],block_matrix_seq[i+1])
    tempio_seq.append(tempio_value)

print(tempio_seq)
seq = [ele.MIO() for ele in tempio_seq]
#
print(seq)

crudeoildata = [ele[0][0] for ele in seq]
print(crudeoildata)
np.save('crudelist.npy',crudeoildata)

lightoildata = [ele[1][0] for ele in seq]
print(lightoildata)
np.save('lightlist.npy',lightoildata)

fabricdata = [ele[1][1] for ele in seq]
print(fabricdata)
np.save('fabriclist.npy',fabricdata)



