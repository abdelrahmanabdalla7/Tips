import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import streamlit as st

uploaded_file="tips.csv"
data=pd.read_csv(uploaded_file)
print (data)

st.title("Tips Data Dashboard")
st.header("Data Overview")
st.write("First few rows of the dataset:")
st.dataframe(data.head())

#Data summary
st.header("Summary statistics")
st.write(data.describe())

#Select columns for visualization
st.header("Data Visualization")
st.write ("Select columns to visualize:")

x_axis=st.selectbox("X-axis",data.columns)
y_axis=st.selectbox("Y-axis",data.columns)

plot_type=st.radio("Select plot type:",["Scatter plot","line plot","Histogram plot"])

if plot_type == "Scatter plot":
    st.subheader("scatter plot")
    fig=plt.figure()
    sns.scatterplot(data=data,x=x_axis,y=y_axis)
    plt.xlabel(x_axis)
    plt.ylabel(y_axis)
    st.pyplot(fig)
elif plot_type == "line plot":
    st.subheader("line plot")
    fig=plt.figure()
    sns.lineplot(data=data,x=x_axis,y=y_axis)
    plt.xlabel(x_axis)
    plt.ylabel(y_axis)
    st.pyplot(fig)
else:
    plot_type == "Histogram plot"
    st.subheader("Hist plot")
    fig=plt.figure()
    sns.histplot(data=data,x=x_axis)
    plt.xlabel(x_axis)
    plt.ylabel(y_axis)
    st.pyplot(fig)

st.header("Correlation Heatmap")
if st.button("Generate heatmap"):
    fig=plt.figure()
    sns.heatmap(data.corr(numeric_only=True),annot=True,cmap="Blues")
    st.pyplot(fig)
st.write("Explore and analysis your data ")