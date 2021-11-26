from ipywidgets import fixed, interact, interact_manual, interactive
import ipywidgets as widgets
import matplotlib
import matplotlib.pyplot as plt
import streamlit as st
import base64
import gudhi as gd
from pyvis.network import Network
import streamlit.components.v1 as components
import got
from stvis import pv_static
from plotly.subplots import make_subplots

import numpy as np
import gudhi as gd
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
import networkx as nx
from bijection import *

from helpers import cycle, complete, plot_extended_diagram_plotly, plot_levelset_diagram_plotly, threshold, graph_time_series

from visual_features import plot_barcode_LZZ_plotly, plot_extended_barcode_plotly

from st_texts import bijection_explained

    

def interactive_function_EP(space, filtration):
    
    s = gd.SimplexTree()
    
    for edge in eval(space):
        
        s.insert(edge)
        
    for filt in eval(filtration):
        
        s.assign_filtration(filt[0], filt[1])
        
    _ = s.make_filtration_non_decreasing()
        
    real_filtration = list(s.get_filtration())    
    
    s.extend_filtration()
    
    dgms = s.extended_persistence(min_persistence=1e-5)
    
    return dgms

def interactive_function_LZZ(space, filtration):
    
    s = gd.SimplexTree()
    
    for edge in eval(space):
        
        s.insert(edge)
        
    for filt in eval(filtration):
        
        s.assign_filtration(filt[0], filt[1])
        
    _ = s.make_filtration_non_decreasing()
        
    real_filtration = list(s.get_filtration())  
    
    s.extend_filtration()
    
    dgms = s.extended_persistence(min_persistence=1e-5)
    
    B = EP_to_LZZ(real_filtration, dgms)
    
    return B


def interactive_barcodes():
    
    st.header('Computing barcodes')
        
    st.markdown('With this feature, you can choose your own space and filtration. Then, we compute the barcode of your choice with a simple method. More precisely, the extended persistence barcode (1) is computed via the GHUDI library, and the levelset zigzag persistence barcode is computed by applying the bijective mapping to barcode (1).')


    user_space = st.text_input("Choose a simplicial complex, as in the example below (default filtrated space) - e.g. add the edge [0,1] to your space.", [[0,1], [1,2], [1,3], [2,4], [3,4], [4,5], [2,6], [3,7], [4,7], [5,7], [1,8], [2,8], [1,9]])

    user_filtration = st.text_input("Choose a filtration, of the form below (default filtration) - e.g. assign to vertex [6] the value 0.5.", [([0],0),([1],1),([2],2),([3],3),([4],4),([5],5),([6],0.5),([7],4.5),([8],5),([9],6)])

    g = st.checkbox('Begin computation')

    if g:

        G = nx.Graph()

        for edge in eval(user_space):

            G.add_edge(*edge)

        with st.expander("See your simplicial complex."):

            time_series = graph_time_series(user_space, user_filtration)
            
            display_filt_complex(time_series)
        
        st.markdown("Now, you can choose between plotting diagrams or barcodes.")

        d = st.checkbox("Display persistence diagrams")
        b = st.checkbox("Display persistence barcodes")
        
        dgms = interactive_function_EP(user_space,user_filtration)
        B = interactive_function_LZZ(user_space,user_filtration)

        l,r = st.columns(2)
        
        filt = [v[1] for v in eval(user_filtration)]

        if d:
            
            fig_ = make_subplots(
                rows=2, cols=4,
                subplot_titles = ['Ordinary PD',
                                'Relative PD',
                                'Closed-open LZZ PD',
                                'Open-closed LZZ PD',
                                 'Extended+ PD',
                                 'Extended- PD',
                                 'Closed-closed LZZ PD',
                                 'Open-open LZZ PD'],
                                x_title = 'Birth',
                                y_title = "Death"
                )
            
            plot_extended_diagram_plotly(fig_, dgms, filt)
            plot_levelset_diagram_plotly(fig_, dgms, filt)
            
            fig_['layout'].update({
                'width': 1000,
                'height': 600,
            })
            
            st.plotly_chart(fig_)

        if b:
            
            fig = make_subplots(
                rows=1, cols=2,
                subplot_titles = ['Extended persistence barcode',
                                'Levelset zigzag persistence barcode']
                )
            
            plot_extended_barcode_plotly(fig, dgms, filt)
            plot_barcode_LZZ_plotly(fig, B)
            fig['layout'].update({
                'width': 1000,
                'height': 500,
            })
            
            st.plotly_chart(fig)
            
            bijection_explained()
            
            
            
            
        


def computing_barcodes():
    
    st.header('Computing barcodes')
        
    st.markdown('In this example, we consider fixed choices of space and filtration, based on symmetric graphs with natural height functions. Then, we compute the barcode of your choice with a simple method. The extended persistence barcode (1) is computed via GHUDI, and the levelset zigzag persistence barcode is computed by applying the bijective mapping to barcode (1).')

    st.markdown('This feature is essentially designed to allow for better intuition on how extended persistence and levelset zigzag barcodes behave, through working with simple simplicial complexes and height functions as filtrating tools.')


    choice = st.selectbox('What space do you want to look at?', ('The circle as a 6-cycle', 
                                         'The complete graph on 8 nodes'))

    go = st.checkbox('Begin computation')

    if go:

        if choice == 'The circle as a 6-cycle':

            trio = cycle()
            
            space = trio[0]
            filtration = trio[1]
            G = trio[2]

        elif choice == 'The complete graph on 8 nodes':
            
            trio_ = complete()
            
            space = trio_[0]
            filtration = trio_[1]
            G = trio_[2]

        with st.expander("See your simplicial complex."):

            time_series = graph_time_series(space, filtration)
            
            display_filt_complex(time_series)



        dgms = interactive_function_EP(space,filtration)
        B = interactive_function_LZZ(space,filtration)

        d = st.checkbox("Display persistence diagrams")
        b = st.checkbox("Display persistence barcodes")
        
        filt = [v[1] for v in eval(filtration)]
        
        if d:
            
            fig_ = make_subplots(
                rows=2, cols=4,
                subplot_titles = ['Ordinary PD',
                                'Relative PD',
                                'Closed-open LZZ PD',
                                'Open-closed LZZ PD',
                                 'Extended+ PD',
                                 'Extended- PD',
                                 'Closed-closed LZZ PD',
                                 'Open-open LZZ PD'],
                                x_title = 'Birth',
                                y_title = "Death"
                )
            
            plot_extended_diagram_plotly(fig_, dgms, filt)
            plot_levelset_diagram_plotly(fig_, dgms, filt)
            
            fig_['layout'].update({
                'width': 1000,
                'height': 600,
            })
            
            st.plotly_chart(fig_)

        if b:
            
            fig = make_subplots(
                rows=1, cols=2,
                subplot_titles = ['Extended persistence barcode',
                                'Levelset zigzag persistence barcode']
                )
            
            plot_extended_barcode_plotly(fig, dgms, filt)
            plot_barcode_LZZ_plotly(fig, B)
            fig['layout'].update({
                'width': 1000,
                'height': 500,
            })
            
            st.plotly_chart(fig)




def bijection_vis():
    
    st.header("A simple example")
    st.sidebar.header("Bijection visualization")

    st.markdown("#### Visualizing the bijection of intervals between levelset zigzag and extended barcodes.")
    st.markdown("")

    __left,__right = st.columns(2) 
    __left.image("../figures/bij_viz1.png")
    __right.image("../figures/bij_viz2.png")

    with st.expander("See explanation"):
        
        st.write("""Barcodes of levelset zigzag persistence and extended persistence are denoted by $\mathbb{B}_{LZZ}$ and $\mathbb{B}_{EP(+)}$ respectively. In the extended persistence barcode, the central vertical segment separates points living in $\mathbb{R}$ from points living in $\mathbb{R}^\circ=(\mathbb{R},\geq)$. Intervals of the same color are in correspondence via the bijective mapping. We provide an instance of the mapping for each type of intervals (there are four in total).
        """)
        

def display_filt_complex(time_series):
    
    values = [v[1] for v in time_series]
    graphs = [v[0] for v in time_series]
    
    t = st.slider("Filtration threshold", min(values), max(values), max(values))
    
    index = values.index(t)
    
    pv_static(graphs[index])

    

    
    
    
    
    