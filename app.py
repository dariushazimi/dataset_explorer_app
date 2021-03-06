# Author: Dariush Azimi
# Created: April 22, 2020

import matplotlib.pyplot as plt
import matplotlib
import os
import pandas as pd
import streamlit as st
import seaborn as sns
matplotlib.use('Agg')


def main():
    """ Machine Learning Dataset Explorer App """
    st.title("Machine Learning Dataset Explorer App")
    st.subheader("Simple Data Exploration")

    # html_temp = """
    # <div style = "background-color:tomato;"> <p style="color:white; font-size:10px";> This is great</p.
    # """

    # st.markdown(html_temp, unsafe_allow_html=True)

    def file_selector(folder_path='./datasets'):
        filenames = os.listdir(folder_path)
        selected_filename = st.selectbox("Select a file", filenames)
        return os.path.join(folder_path, selected_filename)

    filename = file_selector()

    # show the user that they have actually selected the file
    # st.write("You selected {}".format(filename))
    # lets make it more beutiful with some colors
    st.info("You selected {}".format(filename))

    # read data
    df = pd.read_csv(filename)
    # show dataset
    if st.checkbox("show Dataset"):
        # you can limite the number of rows if you want
        # number = st.number_input("number of rows to view", 5, 10)
        number = st.number_input("Number of rows", min_value=0, value=5, step=1)
        st.dataframe(df.head(number))
    # show columns
    if st.button("column names"):
        st.write(df.columns)
    # st.map()
    # show shape
    if st.checkbox("Show datata shad"):
        # Removed the line below as we now have a condition to show either rows or columns
        # st.write(df.shape)
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
        st.write('# Selected Columns')
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
        st.write(df.iloc[:, -1].value_counts())
    # show datatypes

    if st.button("Data types"):
        st.text("value counts by target/class")
        st.write(df.dtypes)
    # show summary
    if st.checkbox("Summary"):
        st.write(df.describe())
    # Transpose summary
    if st.checkbox("Transpose"):
        st.write(df.describe().T)

    # Plot and visualization

    st.subheader("Data Visualization")

    # Correlation
    # Seaborn Plot
    if st.checkbox("Correlation plot[seaborn]"):
        st.write(sns.heatmap(df.corr(), annot=True))
        st.pyplot()

    # Pie Chart
    if st.checkbox("Pie Plot"):
        all_columns_names = df.columns.tolist()
        if st.button('Generating Pie Plot'):
            st.success('Generating a Pie Plot')
            st.write(df.iloc[:, -1].value_counts().plot.pie(autopct="%1.1f%%"))
            st.pyplot()

    # Count plot
    if st.checkbox("plot of value count"):
        st.text("Value counts by Traget/Class")
        all_columns_names = df.columns.tolist()
        primary_col = st.selectbox("Primary column to groupby", all_columns_names)
        selected_columns_names = st.multiselect("select columns ", all_columns_names)
        if st.button("Plot"):
            st.text("Generate Plot")
            if selected_columns_names:
                vc_plot = df.groupby(primary_col)[selected_columns_names].count()
            else:
                vc_plot = df.iloc[:, -1].value_counts
            st.write(vc_plot.plot(kind='bar'))
            st.pyplot()

    # Customizable Plot
    st.subheader("Customizable Plot")
    all_columns_names = df.columns.tolist()
    type_of_plot = st.selectbox("Slect type of plot", ['area', 'bar', 'line', 'hist', 'box', 'kde'])
    
    # we need to be able to slect the columns

    selected_columns_names = st.multiselect('Select columns to plot', all_columns_names)

    if st.button("Generate Plot"):
        st.success("Genrating Customizable Plot of {} for {}".format(type_of_plot, selected_columns_names))

        # Plot by Streamlit
        if type_of_plot == 'area':
            # create a custom data
            cust_data = df[selected_columns_names]
            # and now plot it by passing in our custom dataset
            st.area_chart(cust_data)
        elif type_of_plot == 'bar':
            # create a custom data
            cust_data = df[selected_columns_names]
            # and now plot it by passing in our custom dataset
            st.bar_chart(cust_data)
        elif type_of_plot == 'line':
            # create a custom data
            cust_data = df[selected_columns_names]
            # and now plot it by passing in our custom dataset
            st.line_chart(cust_data)
        # Custome plot
        elif type_of_plot:
            # create a custom data
            cust_plot = df[selected_columns_names].plot(kind=type_of_plot)
            # and now plot it by passing in our custom dataset
            st.write(cust_plot)
            st.pyplot()

    if st.button("Life is great :) "):
        st.balloons()


if __name__ == '__main__':
    main()
