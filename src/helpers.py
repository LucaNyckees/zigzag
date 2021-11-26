import networkx as nx
import matplotlib.pyplot as plt
import plotly.graph_objects as go
import streamlit as st
from pyvis.network import Network



def cycle():
    
    G = nx.Graph()
    G.add_nodes_from(range(5))
    filtration = str([([0],15),([1],16),([5],16),([2],17),([4],17),([3],18)])
    G.add_edges_from([[0,1],[1,2],[2,3],[3,4],[4,5],[5,0]])
    space = str([[0,1],[1,2],[2,3],[3,4],[4,5],[5,0]])
    
    return (space, filtration, G)


def complete():
    
    G = nx.complete_graph(8)
    filtration = str([([n],n) for n in G.nodes()])
    
    space = str([list(edge) for edge in list(G.edges())])
    
    return (space, filtration, G)


def plot_extended_diagram_plotly(fig, dgms, filt):
    
    a = min(filt)
    b = max(filt)
    
    for (dim,I) in dgms[0]:
        
        fig.add_trace(go.Scatter(x=[a,b], y=[a,b],
                fill=None,
                mode='lines',
                line_color='LightSkyBlue',
                showlegend=False
                ), row=1, col=1)
        
        fig.add_trace(go.Scatter(x=[I[0]], y=[I[1]],
                fill=None,
                mode='markers',
                name = 'dim ' + str(dim),
                marker=dict(
                    color='LightSkyBlue',
                    size=6,
                    line=dict(
                        color='LightSkyBlue',
                        width=0.5
                    )
                ),
                showlegend=False
                ), row=1, col=1)
        
    for (dim,I) in dgms[1]:
        
        fig.add_trace(go.Scatter(x=[a,b], y=[a,b],
                fill=None,
                mode='lines',
                line_color='LightSkyBlue',
                showlegend=False
                ), row=1, col=2)
        
        fig.add_trace(go.Scatter(x=[I[0]], y=[I[1]],
                fill=None,
                mode='markers',
                name = 'dim ' + str(dim),
                marker=dict(
                    color='LightSkyBlue',
                    size=6,
                    line=dict(
                        color='LightSkyBlue',
                        width=0.5
                    )
                ),
                showlegend=False
                ), row=1, col=2)
        
    for (dim,I) in dgms[2]:
        
        fig.add_trace(go.Scatter(x=[a,b], y=[a,b],
                fill=None,
                mode='lines',
                line_color='LightSkyBlue',
                showlegend=False
                ), row=2, col=1)
        
        fig.add_trace(go.Scatter(x=[I[0]], y=[I[1]],
                fill=None,
                mode='markers',
                name = 'dim ' + str(dim),
                marker=dict(
                    color='LightSkyBlue',
                    size=6,
                    line=dict(
                        color='LightSkyBlue',
                        width=0.5
                    )
                ),
                showlegend=False
                ), row=2, col=1)
        
    for (dim,I) in dgms[3]:
        
        fig.add_trace(go.Scatter(x=[a,b], y=[a,b],
                fill=None,
                mode='lines',
                line_color='LightSkyBlue',
                showlegend=False
                ), row=2, col=2)
        
        fig.add_trace(go.Scatter(x=[I[0]], y=[I[1]],
                fill=None,
                mode='markers',
                name = 'dim ' + str(dim),
                marker=dict(
                    color='LightSkyBlue',
                    size=6,
                    line=dict(
                        color='LightSkyBlue',
                        width=0.5
                    )
                ),
                showlegend=False
                ), row=2, col=2)
        
        
        
def plot_levelset_diagram_plotly(fig, dgms, filt):
    
    a = min(filt)
    b = max(filt)
    
    for (dim,I) in dgms[0]:
        
        fig.add_trace(go.Scatter(x=[a,b], y=[a,b],
                fill=None,
                mode='lines',
                line_color='LightSkyBlue',
                showlegend=False
                ), row=1, col=3)
        
        fig.add_trace(go.Scatter(x=[I[0]], y=[I[1]],
                fill=None,
                mode='markers',
                name = 'dim ' + str(dim),
                marker=dict(
                    color='LightSkyBlue',
                    size=6,
                    line=dict(
                        color='LightSkyBlue',
                        width=0.5
                    )
                ),
                showlegend=False
                ), row=1, col=3)
        
    for (dim,I) in dgms[1]:
        
        fig.add_trace(go.Scatter(x=[a,b], y=[a,b],
                fill=None,
                mode='lines',
                line_color='LightSkyBlue',
                showlegend=False
                ), row=1, col=4)
        
        fig.add_trace(go.Scatter(x=[I[0]], y=[I[1]],
                fill=None,
                mode='markers',
                name = 'dim ' + str(dim),
                marker=dict(
                    color='LightSkyBlue',
                    size=6,
                    line=dict(
                        color='LightSkyBlue',
                        width=0.5
                    )
                ),
                showlegend=False
                ), row=1, col=4)
        
    for (dim,I) in dgms[2]:
        
        fig.add_trace(go.Scatter(x=[a,b], y=[a,b],
                fill=None,
                mode='lines',
                line_color='LightSkyBlue',
                showlegend=False
                ), row=2, col=3)
        
        fig.add_trace(go.Scatter(x=[I[0]], y=[I[1]],
                fill=None,
                mode='markers',
                name = 'dim ' + str(dim),
                marker=dict(
                    color='LightSkyBlue',
                    size=6,
                    line=dict(
                        color='LightSkyBlue',
                        width=0.5
                    )
                ),
                showlegend=False
                ), row=2, col=3)
        
    for (dim,I) in dgms[3]:
        
        fig.add_trace(go.Scatter(x=[a,b], y=[a,b],
                fill=None,
                mode='lines',
                line_color='LightSkyBlue',
                showlegend=False
                ), row=2, col=4)
        
        fig.add_trace(go.Scatter(x=[I[0]], y=[I[1]],
                fill=None,
                mode='markers',
                name = 'dim ' + str(dim),
                marker=dict(
                    color='LightSkyBlue',
                    size=6,
                    line=dict(
                        color='LightSkyBlue',
                        width=0.5
                    )
                ),
                showlegend=False
                ), row=2, col=4)
    
    

def to_barcode_ext(dgms):
    
    """Receives extended dgms and outputs an extended barcode."""
    
    ORD = dgms[0]
    REL = dgms[1]
    EP = dgms[2]
    EP_ = dgms[3]
    
    barcode = [] # to be a list of dict
    
    for point in ORD:
        
        interval = [point[1][0], point[1][1]]
        barcode.append({
            "dimension":point[0],
            "interval":interval,
            "type":'ORD'
            })
        
    for point in REL:
        
        interval = [point[1][0], point[1][1]]
        barcode.append({
            "dimension":point[0],
            "interval":interval,
            "type":'REL'
            })   
        
    for point in EP:
        
        interval = [point[1][0], point[1][1]]
        barcode.append({
            "dimension":point[0],
            "interval":interval,
            "type":'EP+'
            })  
    for point in EP_:
        
        interval = [point[1][0], point[1][1]]
        barcode.append({
            "dimension":point[0],
            "interval":interval,
            "type":'EP-'
            })   
        
        
    return barcode
        



def threshold(G,t):
    
    H = G.copy()
    
    print("copy of graph done")
    
    for e in G.edges.data():
        
        if e[2]['weight'] > t:
            
            print("into threshold condition")
        
            H.remove_edge(*e[:2])
            
            print("edge successfully removed")
            
    nt = Network("340px", "860px",notebook=True)
    nt.from_nx(H)
    
    return nt
        
        
        
def graph_time_series(space, filtration):
    
    st.markdown("Use the slider below to observe how the complex evolves with its filtration.")
    
    
    f = eval(filtration)
    f_vertices = [v[0] for v in f]
    f_values = [v[1] for v in f]
        
    G = nx.Graph()

    for edge in eval(space):
        
        i1 = f_vertices.index([edge[0]])
        i2 = f_vertices.index([edge[1]])
        w1 = f_values[i1]
        w2 = f_values[i2]
        w = max(w1,w2)
            
        G.add_edge(*edge, weight=w)
        
    time_series = [(threshold(G,t),t) for t in f_values]

    return time_series



        
    
    
    
    