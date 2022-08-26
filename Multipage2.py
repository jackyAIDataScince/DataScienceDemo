import streamlit as st
import pandas as pd
import numpy as np
import pickle  #to load a saved model
import base64  #to open .gif files in streamlit app

import time    #Time for processing 


@st.cache(suppress_st_warning=True)
def get_fvalue(val):
    feature_dict = {"No":1,"Yes":2}
    for key,value in feature_dict.items():
        if val == key:
            return value

def get_value(val,my_dict):
    for key,value in my_dict.items():
        if val == key:
            return value

#st.markdown("# Main page 🎈")
#st.sidebar.markdown("# Main page 🎈")
st.title("Data Science Demo") 
st.sidebar.subheader("Application Menu")
app_mode = st.sidebar.selectbox('Select Page',['Home','Prediction','Upload']) #two pages

'Starting a long computation...'

df = pd.read_csv("sales.csv")
st.table(df)
#st.write(df.head())


# Add a placeholder
latest_iteration = st.empty()
bar = st.progress(0)

for i in range(100):
  # Update the progress bar with each iteration.
  latest_iteration.text(f'Iteration {i+1}')
  bar.progress(i + 1)
  time.sleep(0.1)

'...and now we\'re done!'
