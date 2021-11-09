
import networkx as nx
import gudhi as gd
import numpy as np
import matplotlib.pyplot as plt
from simplicial import *
from scipy.stats import bernoulli


def get_skel(K,p):
    
    """
    Args: 
        K : gudhi.SimplexTree(), a simplicial complex
        p : int, a dimension
    Returns: 
        skel_new : list, a list of all p-simplices of K
    """
    
    skel = list(K.get_skeleton(p))
    skel_new = []
    for simplex in skel:
        if len(simplex[0]) == p+1:
            skel_new.append(simplex)
    return skel_new


    
def EP_to_LZZ(filtration, dgms):
    
    """This function translates the extended persistence barcode output of a 
    filtration on the simplicial complex X to its levelset zigzag barcode. 
    
    Args : 
        filtration : basic filtration on X
        dgms : output diagrams as returned by extended_persistence()
    Returns : 
        barcode_LZZ : corresponding levelset zigzag barcode
    """
    
    barcode_LZZ = []
    
    types = ["ORD","REL","EP+","EP-"]

    for t in range(4):
        
        for (dim,interval) in dgms[t]:
            
            TYPE = types[t]
            
            if t == 0 or t == 2:
                S_i = interval[0]
                S_j = interval[1]
            elif t == 1 or t == 3:
                S_i = interval[1]
                S_j = interval[0]
                
            diff_i = [x[1]-S_i for x in filtration]
            diff_j = [x[1]-S_j for x in filtration]
            index_i = diff_i.index(min(diff_i))
            index_j = diff_j.index(min(diff_j))
            s_i = filtration[index_i][1]
            s_j = filtration[index_j][1]
            i = [x[1] for x in filtration].index(s_i)
            j = [x[1] for x in filtration].index(s_j)+1
            
            if t == 0:
                c = [(i-1,i),(j-1,j-1)]
                new_interval = [filtration[i][1],filtration[j-1][1]]
            elif t == 1:
                c = [(i,i),(j,j-1)]
                new_interval = [filtration[i][1],filtration[j-1][1]]
            elif t == 2:
                c = [(i-1,i),(j-1,j)]
                new_interval = [filtration[i][1],filtration[j][1]]
            elif t == 3:
                c = [(i,i),(j-1,j-1)]
                new_interval = [filtration[i][1],filtration[j-1][1]]
                
            barcode_LZZ.append((TYPE,dim,new_interval))

    return barcode_LZZ



def plot_barcode_LZZ(barcode_LZZ, width, height):
    
    fig, ax = plt.subplots(figsize=(width, height))

    i = 0

    for bar in barcode_LZZ:

        if bar[0]=='ORD':
            ax.plot([bar[2][0],bar[2][1]],[i,i],color='darkturquoise',linewidth=3)
            ax.plot(bar[2][1],i,'x',color='darkturquoise')
            ax.plot(bar[2][0],i,'o',color='darkturquoise')
        elif bar[0]=='REL':
            ax.plot([bar[2][0],bar[2][1]],[i,i],color='aquamarine',linewidth=3)
            ax.plot(bar[2][0],i,'x',color='aquamarine')
            ax.plot(bar[2][1],i,'o',color='aquamarine')
        elif bar[0]=='EP+':
            ax.plot([bar[2][0],bar[2][1]],[i,i],color='cornflowerblue',linewidth=3)
            ax.plot([bar[2][0],bar[2][1]],[i,i],'o',color='cornflowerblue')
        elif bar[0]=='EP-':
            ax.plot([bar[2][0],bar[2][1]],[i,i],color='violet',linewidth=3)
            ax.plot([bar[2][0],bar[2][1]],[i,i], 'x',color='violet')
        i+=1
        
    ax.set_title("Levelset zigzag barcode")
    ax.set_xlabel("Filtration value")
    ax.set_ylabel("Topological feature")
    ax.set_yticks(range(i))

    return (fig, ax)
    
    

    
    

    





