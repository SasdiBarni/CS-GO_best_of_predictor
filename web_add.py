# -*- coding: utf-8 -*-
"""
Created on Fri Dec  2 21:23:37 2022

@author: sasdi
"""

import numpy as np
import pickle
import streamlit as st

loaded_model = pickle.load(open('C:/Users/sasdi/Documents/Python Scripts/dtree_model.svl', 'rb'))

#input_data = (57,	14,	61,	29,
#              0.0,	71.1,	-4.0,	79.9,	0.0,
#            1.04,	11.0,	3.0,	18.0,	5.0,
#              0.0,	65.2,	-7.0,	60.8,	-1.0,
#              0.70,	34.0,	30.0,	4.0,	81.6,
#              79.2,	1.10,	23.0,	31.0,	-8.0,
#              77.5,	60.0,	0.97,	8.0,	10.0,
#              -2.0,	76.3,	73.3,	0.90,	3.0,
#              8.0,	-5.0,	31.9,	50.0,	0.34)




def predicting(input_data):
    #input to numpy array
    input_array = np.asarray(input_data)

    #reshape numpy array
    input_array_reshaped = input_array.reshape(1, -1)

    prediction = loaded_model.predict(input_array_reshaped)
    
    return prediction
    




def main():
    
    st.title('Counter-Strike "Best of" Prediction Web APP')
    
    kills = st.text_input('kills')
    assits = st.text_input('assits')
    deaths = st.text_input('deaths')
    hs = st.text_input('hs')
    
    flash_assists = st.text_input('flash_assists')
    kast = st.text_input('kast')
    kddiff = st.text_input('kddiff')
    adr = st.text_input('adr')
    fkdiff = st.text_input('fkdiff')
    
    rating = st.text_input('rating')    
    m1_kills = st.text_input('m1_kills')
    m1_assists = st.text_input('m1_assists')
    m1_deaths = st.text_input('m1_deaths')
    m1_hs = st.text_input('m1_hs')
    
    m1_flash_assists = st.text_input('m1_flash_assists')
    m1_kast = st.text_input('Kast of map 1')
    m1_kddiff = st.text_input('m1_kddiff')
    m1_adr = st.text_input('m1_adr')
    m1_fkdiff = st.text_input('m1_fkdiff')
    
    m1_rating = st.text_input('m1_rating')
    kills_ct = st.text_input('kills_ct')
    deaths_ct = st.text_input('deaths_ct')
    kddiff_ct = st.text_input('kddiff_ct')
    adr_ct = st.text_input('adr_ct')
    
    kast_ct = st.text_input('kast_ct')
    rating_ct = st.text_input('rating_ct')
    kills_t = st.text_input('kills_t')
    deaths_t = st.text_input('deaths_t')
    kddiff_t = st.text_input('kddiff_t')
    
    adr_t = st.text_input('adr_t')
    kast_t = st.text_input('kast_t')
    rating_t = st.text_input('rating_t')
    m1_kills_ct = st.text_input('m1_kills_ct')
    m1_deaths_ct = st.text_input('m1_deaths_ct')
    
    m1_kddiff_ct = st.text_input('m1_kddiff_ct')
    m1_adr_ct = st.text_input('m1_adr_ct')
    m1_kast_ct = st.text_input('m1_kast_ct')
    m1_rating_ct = st.text_input('m1_rating_ct')
    m1_kills_t = st.text_input('m1_kills_t')
    
    m1_deaths_t = st.text_input('m1_deaths_t')
    m1_kddiff_t = st.text_input('m1_kddiff_t')
    m1_adr_t = st.text_input('m1_adr_t')
    m1_kast_t = st.text_input('m1_kast_t')
    m1_rating_t = st.text_input('m1_rating_t')

    best_of = ''
    
    if st.button('Predict'):
        best_of = predicting([kills, assits, deaths, hs,
                              flash_assists, kast, kddiff, adr, fkdiff,
                              rating, m1_kills, m1_assists, m1_deaths, m1_hs,
                              m1_flash_assists, m1_kast, m1_kddiff, m1_adr, m1_fkdiff,
                              m1_rating, kills_ct, deaths_ct, kddiff_ct, adr_ct,
                              kast_ct, rating_ct, kills_t, deaths_t, kddiff_t,
                              adr_t, kast_t, rating_t, m1_kills_ct, m1_deaths_ct,
                              m1_kddiff_ct, m1_adr_ct, m1_kast_ct, m1_rating_ct, m1_kills_t, 
                              m1_deaths_t, m1_kddiff_t, m1_adr_t, m1_kast_t, m1_rating_t])
        
    st.success("Best of: " + str(best_of))
    

if __name__=='__main__':
    main()
        
        
        