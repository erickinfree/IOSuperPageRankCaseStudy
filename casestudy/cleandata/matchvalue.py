import pandas as pd
import numpy as np
import networkx as nx
import copy

namelist = ['202012.xlsx',
            '202101.xlsx','202102.xlsx','202103.xlsx','202104.xlsx','202105.xlsx','202106.xlsx',
            '202107.xlsx','202108.xlsx','202109.xlsx','202110.xlsx','202111.xlsx','202112.xlsx',
            '202201.xlsx','202202.xlsx','202203.xlsx','202204.xlsx','202205.xlsx','202206.xlsx',
            '202207.xlsx','202208.xlsx','202209.xlsx','202210.xlsx','202211.xlsx','202212.xlsx',
            '202301.xlsx','202302.xlsx','202303.xlsx','202304.xlsx','202305.xlsx','202306.xlsx',
            '202307.xlsx','202308.xlsx','202309.xlsx','202310.xlsx','202311.xlsx']

adj_list = []
for ele in namelist:
    data = pd.read_excel(ele)
    G = nx.DiGraph()
    for startname, endname, qty in zip(data['startname'], data['endname'], data['Qty']):
        G.add_edge(startname, endname, weight=qty)
    adj_matrix = nx.to_numpy_matrix(G)
    adj_list.append(copy.deepcopy(adj_matrix))

print(adj_list)

#Different networks output different files: crudeoil.npy, lightoil.npy, fabric.npy.
np.save('fabric.npy',adj_list)
