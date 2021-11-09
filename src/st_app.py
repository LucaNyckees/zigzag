import matplotlib
import matplotlib.pyplot as plt
import streamlit as st
#from pyvis.network import Network
import numpy as np
import pandas as pd
from datetime import datetime
import os
import matplotlib
import base64
import gudhi as gd

from st_functions import main, reference, interactive_function_EP, interactive_function_LZZ
from bijection import *



st.set_page_config(layout='wide')

st.markdown("<h1 style='text-align: center;'> On Computing Levelset Zigzag Homology</h1>",
            unsafe_allow_html=True)


MODES = ['Choose your data','A simple example']

st.sidebar.header('Options')

INFO = st.sidebar.radio("Content",('Project description', 'Whole survey', 'Interactive part', 'References'))
    

if INFO == 'Project description':
    

    st.header('Introduction')

    st.markdown('Hey there! This app is developped in the context of a project supervised by [Nicolas Berkouk](https://people.epfl.ch/nicolas.berkouk) and [Prof. Kathryn Hess Bellwald](https://people.epfl.ch/kathryn.hess) at EPFL, within the *Laboratory for Topology and Neuroscience*.')
    
    st.header('Context')
    
    st.markdown("Topological data analysis is a branch in the field of applied mathematicsthat has rapidly grown in the past few years. It offers toolboxes to study theshape of data and finds applications in various domains of machine learning.Key concepts in topological data analysis are the notion ofpersistent homology and its extended versions, namely extended persistent homology and zigzag homology, which offer a way of analysing the behavior of topological features along a diagram of spaces built from data.")
    
    st.header('Description')

    st.markdown('Zigzag persistence, as introduced by Carlsson and De Silva, offers a way to better understand the behavior of topological features observed in a family of spaces or pointclouds by generalizing the setting of persistent homology. An interesting case is the one of *levelset zigzag persistence*, that encodes more information than standard persistence and offers an alternative intuition to extended persistence. A bijection between the extended persistence barcode and the zigzag barcode can be established via so-called "diamond moves", involving the presence of relative Mayer-Vietoris diamonds, illustrated in the animation below. ')
    
    
    #st.markdown("![Alt Text](https://github.com/LucaNyckees/ParametricMorseTheory/blob/main/pyramid_zigzag.gif)")
    
    _left, _right = st.columns(2)
    with _right: 
        st.image("../figures/pyramid_zigzag.gif")
        
    _left.markdown('The precise statement is formulated as the Strong Diamond Principle - sometimes called the Pyramid Theorem. The whole process relies on consecutive transformations between two sequences of spaces that differ only at one point, so that the difference can be expressed by a relative Mayer-Vietoris diamond.')
    
    st.markdown("""In the animated diagram above, we consider a function $f\in \mathrm{Map}(\mathbb{X},\mathbb{R})$ and look at the spaces defined as $\mathbb{X}_i^j = f^{-1}([s_i,s_j]),$ where the values $s_k$ are regular values of the pair $(\mathbb{X},f)$. If follows that here, all arrows are inclusions of spaces.
                """)

    st.header('Our Goal')
    st.markdown('In this project, we aim at providing a tool to compute levelset zigzag persistence. We deduce the results from computations on extended persistence, which are already implemented in C++. To this end, we make use of Python bindings. This way, we develop an efficient computational tool to add to the general data science toolbox.')
        
    st.header('Key-concepts')
    st.markdown("""
        * zigzag persistence \n 
        * extended persistence \n
        * barcodes \n
        * strong diamond principle \n
        * relative Mayer-Vietoris diamonds \n
        * pyramid theorem \n 
        * combinatorial bijective mapping
        """)
    
    #st.header('Contact')
    
    #st.markdown('We are students in the [mathematics department](https://www.epfl.ch/schools/sb/research/math/fr/) at EPFL.')
    #st.markdown('If you happen to have any question or comment on this project, we are happy to answer - you can find our #contacts in the sidebar.')
    

elif INFO == 'Whole survey':
    
    main()
    
    with open("../reports/report.pdf", "rb") as file:
        btn = st.sidebar.download_button(
            label="Download report",
            data=file,
            file_name="report.pdf",
            mime="report/pdf"
        )
        
        
        
elif INFO == "References":
    
    st.title("Related articles and references")
    st.subheader("We give a list of the main references and articles linked to this project.")
    st.write("You can choose an article here and read it!")
    
    elt = st.selectbox('What article do you want to see?', ('Zigzag Persistence', 
                                             'Structure and Interleavings of Relative Interlevel Set Cohomology',
                                             'Zigzag Persistent Homology and Real-valued Functions',
                                             'Computing Optimal Persistent Cycles for Levelset Zigzag on Manifold-like Complexes'))
    
    if elt == 'Zigzag Persistence':
        
        reference('../articles/FODAVA-08-03.pdf')
        
    elif elt == 'Structure and Interleavings of Relative Interlevel Set Cohomology':
        
        reference('../articles/interlevelsets_magnus.pdf')
        
    elif elt == 'Zigzag Persistent Homology and Real-valued Functions':
        
        reference('../articles/morozov.pdf')
        
    elif elt == 'Computing Optimal Persistent Cycles for Levelset Zigzag on Manifold-like Complexes':
        
        reference('../articles/tamal_dey.pdf')
            
    
    
    
elif INFO == 'Interactive part':

    SELECTED_MODE = st.sidebar.selectbox("Visualization mode", MODES, index=0)
    if SELECTED_MODE == MODES[0]:
        
        st.header('Computing barcodes')
        
        st.markdown('With this feature, you can choose your own space and filtration. Then, we compute the barcode of your choice with a simple method. More precisely, the extended persistence barcode (1) is computed via the GHUDI library, and the levelset zigzag persistence barcode is computed by applying the bijective mapping to barcode (1).')
        
        
        user_space = st.text_input("Choose a simplicial complex, as in the example below (default space) - e.g. add the edge [0,1] to your space.", [[0,1], [1,2], [1,3], [2,4], [3,4], [4,5], [2,6], [3,7]])
        
        user_filtration = st.text_input("Choose a filtration, of the form below (default filtration) - e.g. assign to vertex [6] the value 0.5.", [([0],0),([1],1),([2],2),([3],3),([4],4),([5],5),([6],0.5),([7],4.5)])
        
        barcode = st.radio("Now, you can pick a barcode of your choice.", ["Extended persistence barcode", "Levelset persistence barcode"])
        
        
        if barcode == "Extended persistence barcode":
            
            dgms = interactive_function_EP(user_space,user_filtration)
        
            
            fig, axs = plt.subplots(2, 2, figsize=(10,10))
            axs[0,0].scatter([dgms[0][i][1][0] for i in range(len(dgms[0]))], [dgms[0][i][1][1] for i in range(len(dgms[0]))])
            axs[0,0].plot([0,5],[0,5])
            axs[0,0].set_title("Ordinary persistence diagram")
            axs[0,1].scatter([dgms[1][i][1][0] for i in range(len(dgms[1]))], [dgms[1][i][1][1] for i in range(len(dgms[1]))])
            axs[0,1].plot([0,5],[0,5])
            axs[0,1].set_title("Relative persistence diagram")
            axs[1,0].scatter([dgms[2][i][1][0] for i in range(len(dgms[2]))], [dgms[2][i][1][1] for i in range(len(dgms[2]))])
            axs[1,0].plot([0,5],[0,5])
            axs[1,0].set_title("Extended+ persistence diagram")
            axs[1,1].scatter([dgms[3][i][1][0] for i in range(len(dgms[3]))], [dgms[3][i][1][1] for i in range(len(dgms[3]))])
            axs[1,1].plot([0,5],[0,5])
            axs[1,1].set_title("Extended- persistence diagram")
            
            st.pyplot(fig)
            
            
            
        elif barcode == "Levelset persistence barcode":
            
            B = interactive_function_LZZ(user_space,user_filtration)
            
            width = st.sidebar.slider("plot width", 5, 20, 11)
            height = st.sidebar.slider("plot height", 5, 20, 3)
 
            st.pyplot(plot_barcode_LZZ(B,width,height)[0])

        # Temporal cursor

        #plot_stats_window(years,df,"Mean temperature")



    #elif SELECTED_MODE == MODES[1]:

    elif SELECTED_MODE == MODES[1]:
        
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
            
            
            
        

if st.sidebar.button("GitHub"):

    st.sidebar.markdown("The entire code of the project, from source code to notebooks, is available at our GitHub repo [here](https://github.com/LucaNyckees/zigzag). Have a look!")

if st.sidebar.button("Contacts"):
    
    st.sidebar.markdown("""
        * Luca Nyckees ([EPFL](https://people.epfl.ch/luca.nyckees), [GitHub](https://github.com/LucaNyckees))\n
        * Nicolas Berkouk [EPFL](https://people.epfl.ch/nicolas.berkouk), [Site](https://nberkouk.github.io/)
        """)
    

                