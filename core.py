import streamlit as st
import pandas as pd
import base64
import matplotlib.pyplot as plt
import seaborn as sns
import numpy as np
import plotly.express as px
from PIL import Image

st.title('Core Curriculum 5 Year Data Analysis')

st.markdown("""
This app analyzes data pertaining to Core class types, theme of core class, number of core class and other parameters to visualize evolution of the Core curriculum over the years.
""")

excel_file = 'Core Curriculum Data Analysis.xlsx'
sheet_name = 'CORE'

df = pd.read_excel(excel_file,
                   sheet_name=sheet_name,
                   usecols="A,C,D,E,J,L",
                   header=0)

df2 = pd.read_excel(excel_file,
                   sheet_name=sheet_name,
                   usecols="Q:W",
                   header=0)

st.dataframe(df)

semester = df[df.columns[1]].unique().tolist()
semester_selection = st.sidebar.multiselect('Please select a semester:',
                                    semester,
                                    default=semester[-1]
                                    )

category = df[df.columns[3]].unique().tolist()
category_selection = st.sidebar.multiselect('Please select a Core Category:',
                                    category,
                                    default=category[-1]
                                    )

division = df[df.columns[5]].unique().tolist()
division_selection = st.sidebar.multiselect('Academic Division:',
                                    division,
                                    default=division[-1]
                                    )

mask = (df[df.columns[1]].isin(semester_selection)) & (df[df.columns[5]].isin(division_selection)) & (df[df.columns[3]].isin(category_selection))
number_of_result = df[mask].shape[0]
st.markdown(f'*Available Results: {number_of_result}*')

df[mask]

semester2=df[mask][df[mask].columns[1]].unique().tolist()
category2=df[mask][df[mask].columns[3]].unique().tolist()
cat4=[]

st.markdown(semester2)
st.markdown(category2)

# checker=True
# while checker:
#     if len(semester2)<len(category2):
#         for num in range(len(category2)-len(semester2)):
#             semester2.append(0)
#             checker=False
#     elif len(semester2)>len(category2):
#         for num in range(len(semester2)-len(category2)):
#             category2.append(0)
#             checker=False
#     else:
#         pass
#         checker=False

pie_chart = px.pie(df2,title="Aggregated Core Curriculum Category Distribution from AY17/18 to AY21/22",values=df2[df2.columns[1]],names=df2[df2.columns[0]])
st.plotly_chart(pie_chart)
