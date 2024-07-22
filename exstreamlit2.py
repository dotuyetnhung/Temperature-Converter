import streamlit as st
import pandas as pd

with st.form('my form'): 
    st.header ("Registration Form")
    col1, col2, col3 = st.columns(3)
    with col1:
        col1_data = st.selectbox('',['Mr', 'Mrs', 'Miss'])
    with col2:
        col2_data = st.text_input('First name')
    with col3:
        col3_data = st.text_input('Last name')

    Designation = st.selectbox("Designation",
                            ["software", 
                             "Sr.software",
                             "Technical Lead",
                             "Manager",
                             "Sr. Manager",
                             "Proiject Manager"])
    
    date_input_data = st.date_input("Date of birth")

    sex = st.radio('Select Gender',
            ['Male', 'Female', 'Prefered Not to Say'])
    
    age = st.slider('Age',1, 100, 20)
    
    submit_button = st.form_submit_button()

    data = {
            "Name" : f'{col1_data} {col2_data} {col3_data}',
            "Age" : age,
            "Gender" : sex,
            "Data of Birth" : date_input_data.strftime('%Y-%m-%d'),
            "Designation" : Designation
        }

    if submit_button == True:
        st.success("Form Subimitted Sucessfully")
        st.write(data)

        df = pd.DataFrame(data, index=[0])
        df.to_excel('Info.xlsx')

    
    