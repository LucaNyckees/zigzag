import streamlit as st
import base64


def description():
    
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
    
    
def whole_story():
    
    main()
    
    with open("../reports/report.pdf", "rb") as file:
        btn = st.sidebar.download_button(
            label="Download report",
            data=file,
            file_name="report.pdf",
            mime="report/pdf"
        )
        
        
def references():
    
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
        
        
        
def github():
    
    st.sidebar.markdown("The entire code of the project, from source code to notebooks, is available at our GitHub repo [here](https://github.com/LucaNyckees/zigzag). Have a look!")
        
        
def contacts():
    
    st.sidebar.markdown("""
        * Luca Nyckees ([EPFL](https://people.epfl.ch/luca.nyckees), [GitHub](https://github.com/LucaNyckees))\n
        * Nicolas Berkouk [EPFL](https://people.epfl.ch/nicolas.berkouk), [Site](https://nberkouk.github.io/)
        """)
    
    
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
    
    
def bijection_explained():
    
    with st.expander("See explanation"):
        
        st.markdown("The one-to-one correspondence between extended persistence intervals and levelset zigzag intervals in the barcodes above can is drawn from the bijection below, introduced in [[1]](https://www.mrzv.org/publications/zigzags/socg09/).")
        
        st.latex(r'''
\text{Type I : } [a_i,a_j)\leftrightarrow [a_i,a_j)\\
\text{Type II : } [\bar{a}_j,\bar{a}_i)^+\leftrightarrow (a_i,a_j]\\
\text{Type III : } [a_i,\bar{a}_j)\leftrightarrow [a_i,a_j]\\
\text{Type IV : } [a_j,\bar{a}_i)^+\leftrightarrow (a_i,a_j)
        ''')
        
        st.markdown("This is a bijective mapping that preserves the homological dimension of features in most cases, with exceptional degree-shifts of $\pm 1$. On the left, we have the intervals appearing in the extended persistence barcode and their mapped version as levelset zigzag persistence interals on the right. Here, the bar symbol on a value $a_i$ denotes the copy of the critical value $a_i$ in the opposite real line, corresponding to the relative homology case. In other words, what we do is extend the basic input filtration $T = [t_1,t_2]$ to an extended filtration $$E(T) = [t_1,t_2]\cup [t_2,2t_2-t_1]$$ and define")
        
        st.latex(r'''\bar{t}=t+t_2-t_1 \text{ for any } t\in [t_1,t_2].''')
        
       