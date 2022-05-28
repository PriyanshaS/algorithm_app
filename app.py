import streamlit as st
import pickle
import numpy as np

import pandas as pd
NMF_applied=pickle.load(open('model_final_NMF.pkl','rb'))
SVD_applied=pickle.load(open('model_final_SVD.pkl','rb'))
SVDpp_applied=pickle.load(open('model_final_SVDpp.pkl','rb'))
KNNWithZScore_applied=pickle.load(open('model_final_KNN.pkl','rb'))
CoClustering_applied=pickle.load(open('model_final_CoC.pkl','rb'))
cv=pickle.load(open('model_final_cv.pkl','rb'))
csv=pickle.load(open('model_final_csv.pkl','rb'))
def recommend(movie,dataSet):
     l=[]
     for i in range(len(dataSet)):
             if dataSet['iid'][i]==movie:
                 if i<3:
                    for j in range(i+1,i+6):
                        l.append(dataSet['iid'][j])
                    break
                 elif i>(len(dataSet)-4):
                    for j in range(i-5,i):
                        l.append(dataSet['iid'][j])
                    break
                 else:
                    for j in range(i-3,i+3):
                        if i==j:
                           continue
                        l.append(dataSet['iid'][j])
                    return l
movies_list=pickle.load(open('model_final.pkl','rb'))
list_of_algo=['NMF','SVD','SVDpp','KNN','Co-Clustering']
def display_algo(name):
    if name=='NMF':
        recommendations =recommend(selected_movie,KNNWithZScore_applied)
        st.write('RECOMMENDED MOVIES')
        for i in recommendations:
         st.write(i)
    elif name=='SVD':
        recommendations =recommend(selected_movie,SVD_applied)
        for i in recommendations:
         st.write(i)
    elif name=='SVDpp':
        recommendations =recommend(selected_movie,SVDpp_applied)
        for i in recommendations:
         st.write(i)
    elif name=='KNN':
        recommendations =recommend(selected_movie,KNNWithZScore_applied)
        for i in recommendations:
         st.write(i)
    elif name=='Co-Clustering':
        recommendations =recommend(selected_movie,CoClustering_applied)
        for i in recommendations:
         st.write(i)
         
def display_page(name):
        chart_data=[]
        cvf= cv['test_rmse'][i]
        arr= np.array(cvf)
        chart_data = pd.DataFrame(
        arr,
        columns=["RMSE"])
        st.bar_chart(chart_data)
        st.write('The graph above represents the RMSE values for the '+ list_of_algo[i]+' algorithm vs Folds ')
    
        chart_data=[]
        cvf= cv['test_mae'][i]
        arr= np.array(cvf)
        chart_data = pd.DataFrame(
        arr,
        columns=["MAE"])
        st.bar_chart(chart_data)
        
        st.write('The graph above represents the MAE values for the '+ list_of_algo[i]+' algorithm vs Folds ')
       
def compare():
        chart_data=[]
        cvf= cv['RMSE']
        arr= np.array(cvf)
        chart_data = pd.DataFrame(
        arr,
        columns=["RMSE"])
        st.bar_chart(chart_data)
        st.write('The graph above represents the mean RMSE values for NMF , SVD , SVDpp , KNN and Co-Clustering algorithms ')
        
        chart_data=[]
        cvf= cv['MAE']
        arr= np.array(cvf)
        chart_data = pd.DataFrame(
        arr,
        columns=["MAE"])
        st.bar_chart(chart_data)
        st.write('The graph above represents the mean MAE values for NMF , SVD , SVDpp , KNN and Co-Clustering algorithms ')
        
        
        
        
if st.sidebar.button('Home'):
     st.markdown("<h1 style='text-align: center; color: white;'>Recommendation System Analyser</h1>", unsafe_allow_html=True)
     st.markdown("<h4 style='text-align: center; color: grey;'>An app that compares different kinds of algorithms that a web-streaming app (like Netflix) may use for their Recommendation Engine.</h2>", unsafe_allow_html=True) 
     selected_movie =st.sidebar.selectbox('Choose your favourite movie',movies_list)
     sidebar_select=st.sidebar.selectbox('Select algorithm',list_of_algo)
else:
    selected_movie =st.sidebar.selectbox('Choose your favourite movie',movies_list)
    sidebar_select=st.sidebar.selectbox('Select algorithm',list_of_algo)
    if st.sidebar.button('Compare'):
      st.title('Recommendation System Analyser')
      compare()
      
    else:
     st.title('Recommendation System Analyser')
     display_algo(sidebar_select)
     for i in range(len(list_of_algo)):
        if sidebar_select==list_of_algo[i]:
           display_page(i)
 
         


