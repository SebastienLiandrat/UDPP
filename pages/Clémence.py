# -*- coding: utf-8 -*-
"""
Created on Thu Sep  7 16:11:01 2023

@author: sebastien.liandrat
"""

import streamlit as st
import pandas as pd


st.set_page_config(page_title="Accueil")


df = pd.read_csv("Tableau_notes.csv", index_col = 0)
note_Clem_TL_repas = df.loc["Clem"]["TL_repas"]
note_Clem_TL_anim = df.loc["Clem"]["TL_anim"]
note_Clem_TL_déco = df.loc["Clem"]["TL_deco"]

note_Clem_LS_repas = df.loc["Clem"]["LS_repas"]
note_Clem_LS_anim = df.loc["Clem"]["LS_anim"]
note_Clem_LS_déco = df.loc["Clem"]["LS_deco"]


if st.checkbox('Afficher les notes'):
    st.dataframe(pd.DataFrame(df.loc["Clem"]))
    with st.form('addition'):
        st.write("Notes pour Tom et Luciano")
        note_Clem_TL_repas = st.number_input('Repas',value=  note_Clem_TL_repas , min_value=0.0, max_value=10.0, step=0.5)
        note_Clem_TL_anim = st.number_input('Animation', value = note_Clem_TL_anim, min_value=0.0, max_value=10.0, step=0.5)
        note_Clem_TL_déco = st.number_input('Décoration',value = note_Clem_TL_déco, min_value=0.0, max_value=10.0, step=0.5)
        submit = st.form_submit_button('Actualiser')

    if submit:
        df.loc["Clem"]["TL_repas"] = note_Clem_TL_repas
        df.loc["Clem"]["TL_anim"] = note_Clem_TL_anim
        df.loc["Clem"]["TL_deco"] = note_Clem_TL_déco
        df.to_csv("Tableau_notes.csv")
        #st.write(df)
        
        
    
    with st.form('addition 2'):
        st.write("Notes pour Lucile et Séb")
        note_Clem_LS_repas = st.number_input('Repas',value=  note_Clem_LS_repas , min_value=0.0, max_value=10.0, step=0.5)
        note_Clem_LS_anim = st.number_input('Animation', value = note_Clem_LS_anim, min_value=0.0, max_value=10.0, step=0.5)
        note_Clem_LS_déco = st.number_input('Décoration',value = note_Clem_LS_déco, min_value=0.0, max_value=10.0, step=0.5)
        submit = st.form_submit_button('Actualiser2')

    if submit:
        df.loc["Clem"]["LS_repas"] = note_Clem_LS_repas
        df.loc["Clem"]["LS_anim"] = note_Clem_LS_anim
        df.loc["Clem"]["LS_deco"] = note_Clem_LS_déco
        df.to_csv("Tableau_notes.csv")
        #st.write(df)
    


