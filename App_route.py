# -*- coding: utf-8 -*-

import streamlit as st
import numpy as np
import pandas as pd
import community
import networkx as nx 
import networkx.algorithms.community as nx_eval
import matplotlib.pyplot as plt

st.set_page_config(page_title='Route Prediction')

st.title('Optimal Route Prediction')

#add a sidebar
st.sidebar.subheader("Import Files")
test_case = st.sidebar.file_uploader(label = "Upload your xlsx file",
                         type = ['xlsx'])

global df
if test_case is not None:

    df = pd.read_excel(test_case)
    try:
        st.subheader('File uploaded')
        st.write(df)
    except Exception as e:
        print(e)
        st.write("Please upload file")
       
    N_G = nx.from_pandas_edgelist(df, source = 'Origin_code', target = 'Dest_code')
    greedy = nx.community.greedy_modularity_communities(N_G)
        
    if st.button("Click to show partition: "):
            st.write(greedy, len(greedy))
        
    node_groups_grd = []
    
    for i in greedy:
        node_groups_grd.append(list(i))
          
        node_groups_grd
    
        # plot the communities
    color_map_grd = []
    for node in N_G:
        if node in node_groups_grd[0]:
            color_map_grd.append('green')
        elif node in node_groups_grd[1]:
            color_map_grd.append('blue')
        elif node in node_groups_grd[2]:
            color_map_grd.append('gray')
        elif node in node_groups_grd[3]:
            color_map_grd.append('orange')
        elif node in node_groups_grd[4]:
            color_map_grd.append('pink')
        elif node in node_groups_grd[5]:
            color_map_grd.append('cyan')
        elif node in node_groups_grd[6]:
            color_map_grd.append('magenta')
        elif node in node_groups_grd[7]:
            color_map_grd.append('teal')
        else: 
            color_map_grd.append('red')  
    fig, ax = plt.subplots(figsize = (30,15))
    pos1 = nx.spring_layout(N_G, k = 0.2) # nodes name
    nx.draw_networkx(N_G, pos1 ,node_size = 58, node_color = 'green')
    nx.draw(N_G,node_size = 58, node_color=color_map_grd, with_labels=True)
    st.pyplot(fig)


    st.info("Partition Graph")
    
    
    
    st.subheader("For Greedy Modularity")
    
    st.write("Modularity:", nx.community.modularity(N_G, eval('greedy')))
    st.write("Coverage:",nx.community.coverage(N_G, eval('greedy')))
    st.write("Performance:",nx.community.performance(N_G, eval('greedy')))
    
    
    
    if st.button("Click to show edge betweeness centrality of graph"):
        edge_BC = nx.edge_betweenness_centrality(N_G)
        st.info(sorted(edge_BC.items(), key=lambda edge_BC : (edge_BC[1], edge_BC[0]), reverse = True))
    
    st.subheader("Thanks for visit.")
   
