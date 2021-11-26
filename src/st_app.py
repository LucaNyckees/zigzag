import matplotlib
import matplotlib.pyplot as plt
import streamlit as st
import networkx as nx
import numpy as np
import pandas as pd
from datetime import datetime
import os
import matplotlib
import base64
import gudhi as gd
from pyvis.network import Network
import streamlit.components.v1 as components
import got
from stvis import pv_static

from st_texts import description, whole_story, main, reference, references, github, contacts
from st_functions import *
from bijection import *

plt.style.use('fivethirtyeight')
matplotlib.rcParams.update({'font.size': 10})



st.set_page_config(layout='wide')

st.markdown("<h1 style='text-align: center;'> On Computing Levelset Zigzag Homology</h1>",
            unsafe_allow_html=True)


MODES = ['Choose your data', 'Fixed graphs', 'Barcode bijection']

st.sidebar.header('Options')

INFO = st.sidebar.radio("Content",('Project description', 'Whole survey', 'Interactive part', 'References'))
    

if INFO == 'Project description':
    
    description()

    

elif INFO == 'Whole survey':
    
    whole_story()
        
        
        
elif INFO == "References":
    
    references()
    
    
    
elif INFO == 'Interactive part':

    SELECTED_MODE = st.sidebar.selectbox("Visualization mode", MODES, index=0)
    if SELECTED_MODE == MODES[0]:
        
        interactive_barcodes()


    elif SELECTED_MODE == MODES[1]:
        
        computing_barcodes()
        

    elif SELECTED_MODE == MODES[2]:
        
        bijection_vis()
            

if st.sidebar.button("GitHub"):

    github()

if st.sidebar.button("Contacts"):
    
    contacts()
    

                