from ipywidgets import fixed, interact, interact_manual, interactive
import ipywidgets as widgets
import matplotlib
import matplotlib.pyplot as plt
import streamlit as st
import base64

import numpy as np
import gudhi as gd
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
import networkx as nx
from bijection import *

def main():
    
    st.title("The Whole Story")
    st.subheader("This is the project report, containing all the details of our data analysis.")
    st.write("You have the possibility to download it - to do this, please check the sidebar.")
    
    with open("../reports/report.pdf","rb") as f:
        base64_pdf = base64.b64encode(f.read()).decode('utf-8')
        pdf_display = f'<embed src="data:application/pdf;base64,{base64_pdf}" width="700" height="1000" type="application/pdf">'
        
    st.markdown(pdf_display, unsafe_allow_html=True)
    
    
def reference(file):
    
    with open(file,"rb") as f:
        base64_pdf = base64.b64encode(f.read()).decode('utf-8')
        pdf_display = f'<embed src="data:application/pdf;base64,{base64_pdf}" width="700" height="1000" type="application/pdf">'
        
    st.markdown(pdf_display, unsafe_allow_html=True)
    

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
        
        
    
    

    
    
    
    
    