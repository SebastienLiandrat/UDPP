# -*- coding: utf-8 -*-
"""
Created on Thu Sep  7 16:11:01 2023

@author: sebastien.liandrat
"""

import streamlit as st


st.set_page_config(page_title="Accueil")

#st.write("Hello")

if st.checkbox('Afficher les notes du repas de Luciano & Tom'):
    with st.form('addition'):
        st.session_state.note_Clem_L_T_repas = st.number_input('Repas',value=  st.session_state.note_Clem_L_T_repas , min_value=0.0, max_value=10.0, step=0.5)
        st.session_state.note_Clem_L_T_anim = st.number_input('Animation',min_value=0.0, max_value=10.0, step=0.5)
        st.session_state.note_Clem_L_T_déco = st.number_input('Décoration',min_value=0.0, max_value=10.0, step=0.5)
        submit = st.form_submit_button('Actualiser')

    if submit:
        st.write("Repas : ",st.session_state.note_Clem_L_T_repas)
        st.write("Animation : ", st.session_state.note_Clem_L_T_anim)
        st.write("Décoration : ", st.session_state.note_Clem_L_T_déco)



if 'note_Clem' not in st.session_state:
    st.session_state.note_Clem = 10