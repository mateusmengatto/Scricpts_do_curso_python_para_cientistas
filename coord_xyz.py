# -*- coding: utf-8 -*-
"""
Created on Tue Nov  9 10:47:43 2021

@author: mateus mengatto
"""


def file_to_plot3d(arquivo_path):
    import matplotlib.pyplot as plt
    from mpl_toolkits.mplot3d import Axes3D
      
    with open(arquivo_path) as f:
        f_data = f.readlines()
        f.closed
        
    linhas =[]
    
    for i in range(len(f_data)):
        linhas.append(f_data[i].split(','))
    
    coordenadas = {}
    coordenadas['X'] = []
    coordenadas['Y'] = []
    coordenadas['Z'] = []
        
    for i in range(len(linhas)):
        x = float(linhas[i][3])
        y = float(linhas[i][4])
        z = float(linhas[i][5])
        
        coordenadas['X'].append(x)
        coordenadas['Y'].append(y)
        coordenadas['Z'].append(z)
        
        
        fig = plt.figure() #abri uma figura
        ax = fig.add_subplot(111,projection ='3d')
        
        x=coordenadas['X']
        y=coordenadas['Y']
        z=coordenadas['Z']
        
        ax.scatter(x,y,z)

