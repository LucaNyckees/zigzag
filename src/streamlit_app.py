import numpy as np
import pandas as pd
import streamlit as st

st.title('Computing Levelset Zigzag Persistence')

st.header('Who are we?')

st.markdown("""Hey there! This app is developped in the context of a project supervised by Prof. Kathryn Hess Bellwald, from the [Laboratory of Topology and Neuroscience at EPFL](https://www.epfl.ch/labs/hessbellwald-lab/). You can contact us here :
[Nicolas Berkouk](https://people.epfl.ch/nicolas.berkouk) and [Luca Nyckees](https://people.epfl.ch/luca.nyckees).""") 

st.header('A bit of context...')

st.markdown("""Zigzag persistence, as introduced by Carlsson and De Silva [[1]](https://arxiv.org/abs/0812.0197), offers a way to better understand the persistence of topological features observed in a family of spaces or pointclouds by generalizing the setting of persistent homology. The goal of this app is
to help you compute levelset zigzag persistence in an intuitive and efficient way.""")

st.markdown("![Alt Text](https://github.com/LucaNyckees/zigzag/blob/main/figures/11-Figure2-1.png)")

st.header('The main idea')

st.markdown("""The idea is to deduce the results from computations on extended persistence. A bijection between the extended persistence barcode and the zigzag barcode can be established via so-called "diamond moves", 
involving the presence of relative Mayer-Vietoris diamonds, illustrated in the animation below. The precise statement is formulated as the 
*Strong Diamond Principle* - sometimes called the *Pyramid Theorem* - in [[1]](https://arxiv.org/abs/0812.0197). The whole process relies 
on consecutive transformations between two sequences of spaces that differ only at one point, so that the difference can be expressed 
by a relative Mayer-Vietoris diamond.""")

st.markdown("![Alt Text](https://github.com/LucaNyckees/zigzag/blob/main/figures/pyramid_zigzag.gif)")
