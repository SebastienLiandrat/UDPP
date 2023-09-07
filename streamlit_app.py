# -*- coding: utf-8 -*-
"""
Created on Thu Sep  7 16:11:01 2023

@author: sebastien.liandrat
"""

import streamlit as st
import pandas as pd


st.set_page_config(page_title="Accueil")

st.write("Hello")

if 'note_Clem' in st.session_state:
    st.write(st.session_state.note_Clem)
    
df = pd.read_csv("Tableau_notes.csv", index_col = 0)

st.write(df)