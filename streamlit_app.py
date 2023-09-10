# -*- coding: utf-8 -*-
"""
Created on Thu Sep  7 16:11:01 2023

@author: sebastien.liandrat
"""

import streamlit as st
import pandas as pd
import numpy as np


st.set_page_config(page_title="Accueil")



st.title("Récapitulatif des notes renseignées")
    
df = pd.read_csv("Tableau_notes.csv", index_col = 0)

df = df.replace({0 : np.nan})

st.write(~df.isna())



somme_points = 42

if st.checkbox('Afficher les résultats'):
    df = pd.read_csv("Tableau_notes.csv", index_col = 0)
    
    somme_Clem = sum([df.loc["Clem"]["TL_repas"],
                     df.loc["Clem"]["TL_anim"],
                     df.loc["Clem"]["TL_deco"],
                     df.loc["Clem"]["LS_repas"],
                     df.loc["Clem"]["LS_anim"],
                     df.loc["Clem"]["LS_deco"]])
    
    note_Clem_TL_repas_ajustee = df.loc["Clem"]["TL_repas"] * somme_points/somme_Clem
    note_Clem_TL_anim_ajustee = df.loc["Clem"]["TL_anim"] * somme_points/somme_Clem
    note_Clem_TL_déco_ajustee = df.loc["Clem"]["TL_deco"] * somme_points/somme_Clem

    note_Clem_LS_repas_ajustee = df.loc["Clem"]["LS_repas"]* somme_points/somme_Clem
    note_Clem_LS_anim_ajustee = df.loc["Clem"]["LS_anim"]* somme_points/somme_Clem
    note_Clem_LS_déco_ajustee = df.loc["Clem"]["LS_deco"]* somme_points/somme_Clem
    
    somme_Clem_ajustee = sum([note_Clem_TL_repas_ajustee,note_Clem_TL_anim_ajustee,note_Clem_TL_déco_ajustee,
                              note_Clem_LS_repas_ajustee,note_Clem_LS_anim_ajustee,note_Clem_LS_déco_ajustee
                              ])
    
    st.write("Clem" ,somme_Clem, somme_Clem_ajustee)
    
    somme_Sonny = sum([df.loc["Sonny"]["TL_repas"],
                     df.loc["Sonny"]["TL_anim"],
                     df.loc["Sonny"]["TL_deco"],
                     df.loc["Sonny"]["LS_repas"],
                     df.loc["Sonny"]["LS_anim"],
                     df.loc["Sonny"]["LS_deco"]])
    
    note_Sonny_TL_repas_ajustee = df.loc["Sonny"]["TL_repas"] * somme_points/somme_Sonny
    note_Sonny_TL_anim_ajustee = df.loc["Sonny"]["TL_anim"] * somme_points/somme_Sonny
    note_Sonny_TL_déco_ajustee = df.loc["Sonny"]["TL_deco"] * somme_points/somme_Sonny

    note_Sonny_LS_repas_ajustee = df.loc["Sonny"]["LS_repas"]* somme_points/somme_Sonny
    note_Sonny_LS_anim_ajustee = df.loc["Sonny"]["LS_anim"]* somme_points/somme_Sonny
    note_Sonny_LS_déco_ajustee = df.loc["Sonny"]["LS_deco"]* somme_points/somme_Sonny
    
    somme_Sonny_ajustee = sum([note_Sonny_TL_repas_ajustee,note_Sonny_TL_anim_ajustee,note_Sonny_TL_déco_ajustee,
                              note_Sonny_LS_repas_ajustee,note_Sonny_LS_anim_ajustee,note_Sonny_LS_déco_ajustee
                              ])
    
    st.write("Sonny" ,somme_Sonny, somme_Sonny_ajustee)
    
    
    somme_Luciano = sum([df.loc["Luciano"]["CS_repas"],
                     df.loc["Luciano"]["CS_anim"],
                     df.loc["Luciano"]["CS_deco"],
                     df.loc["Luciano"]["LS_repas"],
                     df.loc["Luciano"]["LS_anim"],
                     df.loc["Luciano"]["LS_deco"]])
    
    note_Luciano_CS_repas_ajustee = df.loc["Luciano"]["CS_repas"] * somme_points/somme_Luciano
    note_Luciano_CS_anim_ajustee = df.loc["Luciano"]["CS_anim"] * somme_points/somme_Luciano
    note_Luciano_CS_déco_ajustee = df.loc["Luciano"]["CS_deco"] * somme_points/somme_Luciano

    note_Luciano_LS_repas_ajustee = df.loc["Luciano"]["LS_repas"]* somme_points/somme_Luciano
    note_Luciano_LS_anim_ajustee = df.loc["Luciano"]["LS_anim"]* somme_points/somme_Luciano
    note_Luciano_LS_déco_ajustee = df.loc["Luciano"]["LS_deco"]* somme_points/somme_Luciano
    
    somme_Luciano_ajustee = sum([note_Luciano_CS_repas_ajustee,
                                 note_Luciano_CS_anim_ajustee,
                                 note_Luciano_CS_déco_ajustee,
                              note_Luciano_LS_repas_ajustee,
                              note_Luciano_LS_anim_ajustee,
                              note_Luciano_LS_déco_ajustee
                              ])
    
    st.write("Luciano" ,somme_Luciano, somme_Luciano_ajustee)
    
    
    
    somme_Tom = sum([df.loc["Tom"]["CS_repas"],
                     df.loc["Tom"]["CS_anim"],
                     df.loc["Tom"]["CS_deco"],
                     df.loc["Tom"]["LS_repas"],
                     df.loc["Tom"]["LS_anim"],
                     df.loc["Tom"]["LS_deco"]])
   
    note_Tom_CS_repas_ajustee = df.loc["Tom"]["CS_repas"] * somme_points/somme_Tom
    note_Tom_CS_anim_ajustee = df.loc["Tom"]["CS_anim"] * somme_points/somme_Tom
    note_Tom_CS_déco_ajustee = df.loc["Tom"]["CS_deco"] * somme_points/somme_Tom

    note_Tom_LS_repas_ajustee = df.loc["Tom"]["LS_repas"]* somme_points/somme_Tom
    note_Tom_LS_anim_ajustee = df.loc["Tom"]["LS_anim"]* somme_points/somme_Tom
    note_Tom_LS_déco_ajustee = df.loc["Tom"]["LS_deco"]* somme_points/somme_Tom
    
    somme_Tom_ajustee = sum([note_Tom_CS_repas_ajustee,
                                 note_Tom_CS_anim_ajustee,
                                 note_Tom_CS_déco_ajustee,
                              note_Tom_LS_repas_ajustee,
                              note_Tom_LS_anim_ajustee,
                              note_Tom_LS_déco_ajustee
                              ])
    
    st.write("Tom" ,somme_Tom, somme_Tom_ajustee)
    

    somme_Lucile = sum([df.loc["Lucile"]["CS_repas"],
                     df.loc["Lucile"]["CS_anim"],
                     df.loc["Lucile"]["CS_deco"],
                     df.loc["Lucile"]["TL_repas"],
                     df.loc["Lucile"]["TL_anim"],
                     df.loc["Lucile"]["TL_deco"]])
   
    note_Lucile_CS_repas_ajustee = df.loc["Lucile"]["CS_repas"] * somme_points/somme_Lucile
    note_Lucile_CS_anim_ajustee = df.loc["Lucile"]["CS_anim"] * somme_points/somme_Lucile
    note_Lucile_CS_déco_ajustee = df.loc["Lucile"]["CS_deco"] * somme_points/somme_Lucile

    note_Lucile_TL_repas_ajustee = df.loc["Lucile"]["TL_repas"]* somme_points/somme_Lucile
    note_Lucile_TL_anim_ajustee = df.loc["Lucile"]["TL_anim"]* somme_points/somme_Lucile
    note_Lucile_TL_déco_ajustee = df.loc["Lucile"]["TL_deco"]* somme_points/somme_Lucile
    
    somme_Lucile_ajustee = sum([note_Lucile_CS_repas_ajustee,
                                 note_Lucile_CS_anim_ajustee,
                                 note_Lucile_CS_déco_ajustee,
                              note_Lucile_TL_repas_ajustee,
                              note_Lucile_TL_anim_ajustee,
                              note_Lucile_TL_déco_ajustee
                              ])
    
    st.write("Lucile" ,somme_Lucile, somme_Lucile_ajustee)
    
    somme_Seb = sum([df.loc["Seb"]["CS_repas"],
                     df.loc["Seb"]["CS_anim"],
                     df.loc["Seb"]["CS_deco"],
                     df.loc["Seb"]["TL_repas"],
                     df.loc["Seb"]["TL_anim"],
                     df.loc["Seb"]["TL_deco"]])
    
    note_Seb_CS_repas_ajustee = df.loc["Seb"]["CS_repas"] * somme_points/somme_Seb
    note_Seb_CS_anim_ajustee = df.loc["Seb"]["CS_anim"] * somme_points/somme_Seb
    note_Seb_CS_déco_ajustee = df.loc["Seb"]["CS_deco"] * somme_points/somme_Seb

    note_Seb_TL_repas_ajustee = df.loc["Seb"]["TL_repas"]* somme_points/somme_Seb
    note_Seb_TL_anim_ajustee = df.loc["Seb"]["TL_anim"]* somme_points/somme_Seb
    note_Seb_TL_déco_ajustee = df.loc["Seb"]["TL_deco"]* somme_points/somme_Seb
    
    somme_Seb_ajustee = sum([note_Seb_CS_repas_ajustee,
                                 note_Seb_CS_anim_ajustee,
                                 note_Seb_CS_déco_ajustee,
                              note_Seb_TL_repas_ajustee,
                              note_Seb_TL_anim_ajustee,
                              note_Seb_TL_déco_ajustee
                              ])
    
    st.write("Seb" ,somme_Seb, somme_Seb_ajustee)
    
    if st.checkbox('Résultats :'):
        
        total_TL_ajustee = sum([note_Clem_TL_repas_ajustee,
                        note_Clem_TL_anim_ajustee,
                        note_Clem_TL_déco_ajustee,
                        note_Sonny_TL_repas_ajustee,
                        note_Sonny_TL_anim_ajustee,
                        note_Sonny_TL_déco_ajustee,
                        note_Lucile_TL_repas_ajustee,
                        note_Lucile_TL_anim_ajustee,
                        note_Lucile_TL_déco_ajustee,
                        note_Seb_TL_repas_ajustee,
                        note_Seb_TL_anim_ajustee,
                        note_Seb_TL_déco_ajustee])
        
        total_CS_ajustee = sum([note_Tom_CS_repas_ajustee,
                        note_Tom_CS_anim_ajustee,
                        note_Tom_CS_déco_ajustee,
                        note_Luciano_CS_repas_ajustee,
                        note_Luciano_CS_anim_ajustee,
                        note_Luciano_CS_déco_ajustee,
                        note_Lucile_CS_repas_ajustee,
                        note_Lucile_CS_anim_ajustee,
                        note_Lucile_CS_déco_ajustee,
                        note_Seb_CS_repas_ajustee,
                        note_Seb_CS_anim_ajustee,
                        note_Seb_CS_déco_ajustee])
        
        total_LS_ajustee = sum([note_Clem_LS_repas_ajustee,
                        note_Clem_LS_anim_ajustee,
                        note_Clem_LS_déco_ajustee,
                        note_Sonny_LS_repas_ajustee,
                        note_Sonny_LS_anim_ajustee,
                        note_Sonny_LS_déco_ajustee,
                        note_Sonny_LS_repas_ajustee,
                        note_Sonny_LS_anim_ajustee,
                        note_Sonny_LS_déco_ajustee,
                        note_Luciano_LS_repas_ajustee,
                        note_Luciano_LS_anim_ajustee,
                        note_Luciano_LS_déco_ajustee])
                        
        st.write("Somme ajustée Tom Luciano : ", total_TL_ajustee)
        st.write("Somme ajustée Clem Sonny : ", total_CS_ajustee)
        st.write("Somme ajustée Lucile Seb : ", total_LS_ajustee)
        
        
        note_Clem_TL_repas = df.loc["Clem"]["TL_repas"]
        note_Clem_TL_anim = df.loc["Clem"]["TL_anim"]
        note_Clem_TL_déco = df.loc["Clem"]["TL_deco"]

        note_Clem_LS_repas = df.loc["Clem"]["LS_repas"]
        note_Clem_LS_anim = df.loc["Clem"]["LS_anim"]
        note_Clem_LS_déco = df.loc["Clem"]["LS_deco"]
        
        note_Luciano_CS_repas = df.loc["Luciano"]["CS_repas"]
        note_Luciano_CS_anim = df.loc["Luciano"]["CS_anim"]
        note_Luciano_CS_déco = df.loc["Luciano"]["CS_deco"]

        note_Luciano_LS_repas = df.loc["Luciano"]["LS_repas"]
        note_Luciano_LS_anim = df.loc["Luciano"]["LS_anim"]
        note_Luciano_LS_déco = df.loc["Luciano"]["LS_deco"]
        
        note_Tom_CS_repas = df.loc["Tom"]["CS_repas"]
        note_Tom_CS_anim = df.loc["Tom"]["CS_anim"]
        note_Tom_CS_déco = df.loc["Tom"]["CS_deco"]

        note_Tom_LS_repas = df.loc["Tom"]["LS_repas"]
        note_Tom_LS_anim = df.loc["Tom"]["LS_anim"]
        note_Tom_LS_déco = df.loc["Tom"]["LS_deco"]
        
        note_Lucile_TL_repas = df.loc["Lucile"]["TL_repas"]
        note_Lucile_TL_anim = df.loc["Lucile"]["TL_anim"]
        note_Lucile_TL_déco = df.loc["Lucile"]["TL_deco"]

        note_Lucile_CS_repas = df.loc["Lucile"]["CS_repas"]
        note_Lucile_CS_anim = df.loc["Lucile"]["CS_anim"]
        note_Lucile_CS_déco = df.loc["Lucile"]["CS_deco"]
        
        note_Seb_TL_repas = df.loc["Seb"]["TL_repas"]
        note_Seb_TL_anim = df.loc["Seb"]["TL_anim"]
        note_Seb_TL_déco = df.loc["Seb"]["TL_deco"]

        note_Seb_CS_repas = df.loc["Seb"]["CS_repas"]
        note_Seb_CS_anim = df.loc["Seb"]["CS_anim"]
        note_Seb_CS_déco = df.loc["Seb"]["CS_deco"]
        
        note_Sonny_TL_repas = df.loc["Sonny"]["TL_repas"]
        note_Sonny_TL_anim = df.loc["Sonny"]["TL_anim"]
        note_Sonny_TL_déco = df.loc["Sonny"]["TL_deco"]

        note_Sonny_LS_repas = df.loc["Sonny"]["LS_repas"]
        note_Sonny_LS_anim = df.loc["Sonny"]["LS_anim"]
        note_Sonny_LS_déco = df.loc["Sonny"]["LS_deco"]
        
        
        total_TL = sum([note_Clem_TL_repas,
                        note_Clem_TL_anim,
                        note_Clem_TL_déco,
                        note_Sonny_TL_repas,
                        note_Sonny_TL_anim,
                        note_Sonny_TL_déco,
                        note_Lucile_TL_repas,
                        note_Lucile_TL_anim,
                        note_Lucile_TL_déco,
                        note_Seb_TL_repas,
                        note_Seb_TL_anim,
                        note_Seb_TL_déco])
        
        total_CS = sum([note_Tom_CS_repas,
                        note_Tom_CS_anim,
                        note_Tom_CS_déco,
                        note_Luciano_CS_repas,
                        note_Luciano_CS_anim,
                        note_Luciano_CS_déco,
                        note_Lucile_CS_repas,
                        note_Lucile_CS_anim,
                        note_Lucile_CS_déco,
                        note_Seb_CS_repas,
                        note_Seb_CS_anim,
                        note_Seb_CS_déco])
        
        total_LS = sum([note_Clem_LS_repas,
                        note_Clem_LS_anim,
                        note_Clem_LS_déco,
                        note_Sonny_LS_repas,
                        note_Sonny_LS_anim,
                        note_Sonny_LS_déco,
                        note_Sonny_LS_repas,
                        note_Sonny_LS_anim,
                        note_Sonny_LS_déco,
                        note_Luciano_LS_repas,
                        note_Luciano_LS_anim,
                        note_Luciano_LS_déco])
        
        
        
        
        st.write("Somme non ajustée Tom Luciano : ", total_TL/12)
        st.write("Somme non ajustée Clem Sonny : ", total_CS/12)
        st.write("Somme non ajustée Lucile Seb : ", total_LS/12)
        
       
    