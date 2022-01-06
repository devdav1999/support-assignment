import streamlit as st
import wget


cat_101 = wget.download('https://http.cat/101.jpg') 
cat_102 = wget.download('https://http.cat/102.jpg') 


st.title("My Streamlit App!")

with st.form("app_form"):
  status_code = st.radio("Pick a status code", ('101','102','405','406','407','416','417','500','502','521'))
  
  submitted = st.form_submit_button("Submit")
  if submitted:
    if status_code == '101':
      st.image('101.jpg')
    elif status_code == '102':
      st.image('102.jpg')

