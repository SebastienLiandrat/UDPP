# -*- coding: utf-8 -*-
"""
Created on Thu Sep  7 16:11:01 2023

@author: sebastien.liandrat
"""

import streamlit as st
import pandas as pd


st.set_page_config(page_title="Accueil")


df = pd.read_csv("Tableau_notes.csv", index_col = 0)
note_Tom_CS_repas = df.loc["Tom"]["CS_repas"]
note_Tom_CS_anim = df.loc["Tom"]["CS_anim"]
note_Tom_CS_déco = df.loc["Tom"]["CS_deco"]

note_Tom_LS_repas = df.loc["Tom"]["LS_repas"]
note_Tom_LS_anim = df.loc["Tom"]["LS_anim"]
note_Tom_LS_déco = df.loc["Tom"]["LS_deco"]


if st.checkbox('Afficher les notes'):
    st.write(df.loc["Tom"])
    
    with st.form('addition'):
        st.write("Notes pour Clem et Sonny")
        note_Tom_CS_repas = st.number_input('Repas',value=  note_Tom_CS_repas , min_value=0.0, max_value=10.0, step=0.5)
        note_Tom_CS_anim = st.number_input('Animation', value = note_Tom_CS_anim, min_value=0.0, max_value=10.0, step=0.5)
        note_Tom_CS_déco = st.number_input('Décoration',value = note_Tom_CS_déco, min_value=0.0, max_value=10.0, step=0.5)
        submit = st.form_submit_button('Actualiser')

    if submit:
        df.loc["Tom"]["CS_repas"] = note_Tom_CS_repas
        df.loc["Tom"]["CS_anim"] = note_Tom_CS_anim
        df.loc["Tom"]["CS_deco"] = note_Tom_CS_déco
        df.to_csv("Tableau_notes.csv")
        #st.write(df)
        
        
    
    with st.form('addition 2'):
        st.write("Notes pour Lucile et Séb")
        note_Tom_LS_repas = st.number_input('Repas',value=  note_Tom_LS_repas , min_value=0.0, max_value=10.0, step=0.5)
        note_Tom_LS_anim = st.number_input('Animation', value = note_Tom_LS_anim, min_value=0.0, max_value=10.0, step=0.5)
        note_Tom_LS_déco = st.number_input('Décoration',value = note_Tom_LS_déco, min_value=0.0, max_value=10.0, step=0.5)
        submit = st.form_submit_button('Actualiser2')

    if submit:
        df.loc["Tom"]["LS_repas"] = note_Tom_LS_repas
        df.loc["Tom"]["LS_anim"] = note_Tom_LS_anim
        df.loc["Tom"]["LS_deco"] = note_Tom_LS_déco
        df.to_csv("Tableau_notes.csv")
        #st.write(df)
    


    
