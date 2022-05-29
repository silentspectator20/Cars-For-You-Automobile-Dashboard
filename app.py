
import pandas as pd
import numpy as np
import plotly.express as px
import matplotlib.pyplot as plt
import streamlit as st
from PIL import Image
import seaborn as sns



st.set_page_config(page_title="CarsForYou",
                   page_icon=":car:", layout="wide")

st.title("Cars For You - Analysis Dashboard")


image = Image.open('car.jpg')
st.image(image, '')

def get_dataset():
    auto = pd.read_csv(r"C:\Users\jains\OneDrive\Desktop\ENGAGE\2. Cars Data1.csv")
    return auto
auto = get_dataset()


auto['Invoice'] = auto['Invoice'].str.replace('$','',regex=False)
auto['Invoice'] = auto['Invoice'].str.replace(',','',regex=False)
auto['Invoice'] = auto['Invoice'].astype(int)


auto['MSRP'] = auto['MSRP'].str.replace('$','',regex=False)
auto['MSRP'] = auto['MSRP'].str.replace(',','',regex=False)
auto['MSRP'] = auto['MSRP'].astype(int)



   

numeric_auto = auto.select_dtypes(['float', 'int'])
numeric_cols = numeric_auto.columns
   

text_auto = auto.select_dtypes(['object'])
text_cols = text_auto.columns

make_cols = auto['Make']
unique_make = make_cols.unique()

# display dataset
check_box = st.sidebar.checkbox(label="Display Dataset")

if check_box:
    st.write(auto)

# sidebar
st.sidebar.title("Settings")
feature_selection = st.sidebar.multiselect(
    "Features to plot", options=numeric_cols)
make_dropdown = st.sidebar.selectbox(label="Car Company", options=unique_make)

# plotting line graph
automake = auto[auto['Make'] == make_dropdown]
auto_features = automake[feature_selection]
plotly_fig = px.line(data_frame=auto_features, x=auto_features.index,
                     y=feature_selection, title=(str(make_dropdown)) + ' ' + 'Analysis')
st.plotly_chart(plotly_fig, use_container_width=True)

image = Image.open('car-1.jpg')
st.image(image, '')

#row a
a1, a2 = st.columns(2)
with a1:
    basic_histogram = px.histogram(data_frame=auto, nbins=10,title= 'Histogram of cars MSRP Price', x = 'MSRP')
    st.plotly_chart(basic_histogram, use_container_width=True)



with a2:
    basic_histogram = px.histogram(data_frame=auto, nbins=10,title= 'Histogram of cars Invoice Price', x = 'Invoice')
    st.plotly_chart(basic_histogram, use_container_width=True)

image = Image.open('car-2.jpg')
st.image(image, '')

#row b
b1, b2 = st.columns(2)
with b1:
    fig = px.bar(auto, x="Type", title="CARS OF A PARTICULAR TYPE ")
    st.plotly_chart(fig, use_container_width=True)
    

with b2:
    fig = px.box(auto, x="Type", y="Invoice",title="BODY TYPE VS PRICE OF CARS" )
    st.plotly_chart(fig, use_container_width=True)

#row c
c1, c2 = st.columns(2)
with c1:
    auto_scatter = px.scatter(
            data_frame=automake, x='MPG_City', y='Invoice', color='Model',title="MILEAGE VS PRICE OF "+ (str(make_dropdown)))
    st.plotly_chart(auto_scatter, use_container_width=True)


with c2:
    auto_scatter = px.scatter(data_frame = automake,x = 'Horsepower', y = 'Invoice', color ='Type',title="HORSEPOWER VS PRICE OF "+ (str(make_dropdown)) )
    st.plotly_chart(auto_scatter, use_container_width=True)


d1, d2 = st.columns((7,3))

with d1:
    
    plt.figure(figsize=(22,8))
    sns.heatmap(auto.corr(), annot=True, fmt='.2%')
    plt.title('Correlation between different variable',fontsize=20)
    plt.xticks(fontsize=14, rotation=320)
    plt.yticks(fontsize=14);
    st.pyplot(plt)


with d2:
    pie_chart = px.pie(data_frame=automake, values = 'Cylinders', names= 'Cylinders')
    st.plotly_chart(pie_chart, use_container_width=True)

fig = px.scatter_3d(auto, x='Horsepower', z='Invoice', y='MPG_City',color='Make',width=800,height=750, title="MILEAGE VS PRICE VS HORSEPOWER OF DIFFERENT CARS")
fig.update_layout(showlegend=True)
st.plotly_chart(fig, use_container_width=True)

hide_st_style = """
                <style>
                #MainMenu {visibility: hidden;}
                footer {visibility: hidden;}
                header {visibility: hidden;} 
                </style>
                """
st.markdown(hide_st_style,unsafe_allow_html= True)

with open('index.html') as f:
    st.markdown(f'{f.read()}', unsafe_allow_html=True)








