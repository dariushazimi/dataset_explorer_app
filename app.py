# Author: Dariush Azimi
# Created: April 22, 2020

import os
import streamlit as st
import pandas as pd

import matplotlib.pyplot as plt
import matplotlib
matplotlib.use('Agg')
import seaborn as sns


def main():
    """ Common ML Dataset Explorer App """
    st.title("Common ML Dataset Explorer App")
    st.subheader("Simple Data Exploration")

    html_temp = """
    <div style = "background-color:tomato;"> <p style="color:white; font-size:10px";> This is great</p.
    """

    st.markdown(html_temp, unsafe_allow_html=True)

    def file_selector(folder_path = './datasets'):
        filenames = os.listdir(folder_path)
        selected_filename = st.selectbox("Select a file", filenames)
        return os.path.join(folder_path, selected_filename)
    
    filename = file_selector()

    # show the user that they have actually selected the file

    # st.write("You selected {}".format(filename))
    #lets make it more beutiful with some colors
    st.info("You selected {}".format(filename))

    # read data
    df = pd.read_csv(filename)
    # show dataset
    if st.checkbox("show Dataset"):
        # you can limite the number of rows if you want
        #number = st.number_input("number of rows to view", 5, 10)
        number = st.number_input("Number of rows to view",min_value=0,value=5,step=1)
        st.dataframe(df.head(number))
    
    # show columns
    if st.button("column names"):
        st.write(df.columns)
    #    st.map()
    # show shape
    if st.checkbox("Show datata shad"):
        #Removed the line below as we now have a condition to show either rows or columns
        #st.write(df.shape)
        data_dim = st.radio("show dimention by ", ("Rows", "Columns"))
        if data_dim == 'Rows':
            st.text("Number of Rows")
            st.write(df.shape[0])
        elif data_dim == 'Columns':
            st.text("Number of Columns")
            st.write(df.shape[1])
        else:
             st.write(df.shap)
    
    # select columns
    if st.checkbox("Selected columns to show"):
        all_columns =  df.columns.tolist()
        selected_columns = st.multiselect("Select", all_columns)
        new_df = df[selected_columns]
        st.dataframe(new_df)

   
   
    # select rows
    if st.checkbox("Selected rows to show"):
        selected_indices = st.multiselect('Select rows:', df.index)
        selected_rows = df.loc[selected_indices]
        st.write('# Selected Rows', selected_rows)

    
    # show values

    if st.button("value counts"):
        st.text("value counts by target/class")
        # we are slecting the last column
        st.write(df.iloc[:,-1].value_counts())
   
    # show datatypes

    if st.button("Data types"):
        st.text("value counts by target/class")
        st.write(df.dtypes)
    
   
    # select columns
    # show summary


if __name__ == '__main__':
    main()