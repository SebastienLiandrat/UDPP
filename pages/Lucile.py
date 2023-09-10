# -*- coding: utf-8 -*-
"""
Created on Thu Sep  7 16:11:01 2023

@author: sebastien.liandrat
"""

import streamlit as st
import pandas as pd


st.set_page_config(page_title="Accueil")


df = pd.read_csv("Tableau_notes.csv", index_col = 0)
note_Lucile_TL_repas = df.loc["Lucile"]["TL_repas"]
note_Lucile_TL_anim = df.loc["Lucile"]["TL_anim"]
note_Lucile_TL_déco = df.loc["Lucile"]["TL_deco"]

note_Lucile_CS_repas = df.loc["Lucile"]["CS_repas"]
note_Lucile_CS_anim = df.loc["Lucile"]["CS_anim"]
note_Lucile_CS_déco = df.loc["Lucile"]["CS_deco"]


if st.checkbox('Afficher les notes'):
    st.write(df.loc["Lucile"])
    
    with st.form('addition'):
        st.write("Notes pour Tom et Luciano")
        note_Lucile_TL_repas = st.number_input('Repas',value=  note_Lucile_TL_repas , min_value=0.0, max_value=10.0, step=0.5)
        note_Lucile_TL_anim = st.number_input('Animation', value = note_Lucile_TL_anim, min_value=0.0, max_value=10.0, step=0.5)
        note_Lucile_TL_déco = st.number_input('Décoration',value = note_Lucile_TL_déco, min_value=0.0, max_value=10.0, step=0.5)
        submit = st.form_submit_button('Actualiser')

    if submit:
        df.loc["Lucile"]["TL_repas"] = note_Lucile_TL_repas
        df.loc["Lucile"]["TL_anim"] = note_Lucile_TL_anim
        df.loc["Lucile"]["TL_deco"] = note_Lucile_TL_déco
        df.to_csv("Tableau_notes.csv")
        #st.write(df)
        
        
    
    with st.form('addition 2'):
        st.write("Notes pour Clem et Sonny")
        note_Lucile_CS_repas = st.number_input('Repas',value=  note_Lucile_CS_repas , min_value=0.0, max_value=10.0, step=0.5)
        note_Lucile_CS_anim = st.number_input('Animation', value = note_Lucile_CS_anim, min_value=0.0, max_value=10.0, step=0.5)
        note_Lucile_CS_déco = st.number_input('Décoration',value = note_Lucile_CS_déco, min_value=0.0, max_value=10.0, step=0.5)
        submit = st.form_submit_button('Actualiser2')

    if submit:
        df.loc["Lucile"]["CS_repas"] = note_Lucile_CS_repas
        df.loc["Lucile"]["CS_anim"] = note_Lucile_CS_anim
        df.loc["Lucile"]["CS_deco"] = note_Lucile_CS_déco
        df.to_csv("Tableau_notes.csv")
        #st.write(df)
    

