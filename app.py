import streamlit as st
import pickle
import pandas as pd
import numpy as np

# Load data
df = pickle.load(open('df.pkl','rb'))
pipe = pickle.load(open('pipe.pkl','rb'))

st.title("💻 Laptop Price Predictor")

# Company
company = st.selectbox('Brand',df['Company'].unique())

# Type
type = st.selectbox('Type',df['TypeName'].unique())

# RAM
ram = st.selectbox('RAM (GB)',[2,4,6,8,12,16,24,32,64])

# Weight
weight = st.number_input('Weight of the Laptop')

# Touchscreen
touchscreen = st.selectbox('Touchscreen',['No','Yes'])

if touchscreen == 'Yes':
    touchscreen = 1
else:
    touchscreen = 0

# IPS
ips = st.selectbox('IPS',['No','Yes'])

if ips == 'Yes':
    ips = 1
else:
    ips = 0

# Screen size
screen_size = st.number_input('Screen Size')

# Resolution
resolution = st.selectbox(
    'Screen Resolution',
    ['1920x1080','1366x768','1600x900','3840x2160','3200x1800','2880x1800','2560x1600','2560x1440','2304x1440']
)

# PPI calculation
X_res = int(resolution.split('x')[0])
Y_res = int(resolution.split('x')[1])

try:
    ppi = ((X_res**2 + Y_res**2)**0.5) / screen_size
except:
    ppi = 0

# CPU
cpu = st.selectbox('CPU',df['Cpu brand'].unique())

# HDD
hdd = st.selectbox('HDD (GB)',[0,128,256,512,1024,2048])

# SSD
ssd = st.selectbox('SSD (GB)',[0,8,128,256,512,1024])

# GPU
gpu = st.selectbox('GPU',df['Gpu brand'].unique())

# OS
os = st.selectbox('Operating System',df['os'].unique())

if st.button('Predict Price'):

    query = pd.DataFrame([[company,type,ram,weight,touchscreen,
                           ips,ppi,cpu,hdd,ssd,gpu,os]],
                         columns=['Company','TypeName','Ram','Weight','Touchscreen',
                                  'Ips','ppi','Cpu brand','HDD','SSD','Gpu brand','os'])

    prediction = pipe.predict(query)

    st.title("💰 Predicted Price: ₹ " + str(int(np.exp(prediction[0]))))
