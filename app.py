import streamlit as st
import pandas as pd
import numpy as np
import pickle
import time
import sklearn

pipe = pickle.load(open('LinearRegressionModel.pkl', 'rb'))
df = pd.read_csv('FinalData.csv')

def find_names(company):
    return(sorted(df[df['company'] == company]['model'].unique()))


col1, col2 = st.columns(2)
col1.image('car.jpg')
col2.markdown("<br><h1>CAR<br>PRICE<br>PREDICTOR<h1><br>",True)
time.sleep(2)

col1, col2 = st.columns(2)
company = col1.selectbox('SELECT COMPANY OF CAR', sorted(df['company'].unique()))
model = col2.selectbox('SELECT COMPANY OF CAR', find_names(company))

year = st.slider("SELECT PURCHASE YEAR OF CAR",min_value=1995, max_value=2020, step=1)
km_driven = st.number_input("ENTER TOTAL KILOMETERS CAR DRIVED", step=1)

col1, col2, col3, col4 = st.columns(4)
fuel = col1.selectbox("FUEL TYPE",df['fuel'].unique())
seller_type = col2.selectbox("TYPE OF SELLER",df['seller_type'].unique())
transmission = col3.selectbox("TRANSMISSION MODE",df['transmission'].unique())
owner = col4.selectbox("TYPE OF OWNER ",df['owner'].unique())

seats = st.selectbox("ENTER TOTAL SEATS IN CAR", sorted(df['seats'].unique()))
mileage = st.number_input("ENTER MILEAGE OF CAR IN kmpl", step=.1)
engine = st.number_input("ENTER ENGINE CAPACITY OF CAR IN cc", step=1)

col1,col2,col3 = st.columns([3,1,5])
if col3.button("SUBMIT"):
    price = pipe.predict(pd.DataFrame([[year,km_driven,fuel,seller_type,transmission,owner,mileage,engine,seats,company,model]],
                        columns=['year','km_driven', 'fuel', 'seller_type',
                                 'transmission', 'owner', 'mileage', 'engine', 'seats', 'company','model']))[0]

    st.markdown(f"<h3>APPROXIMATE PRICE OF THE CAR COULD BE {round(np.exp(price))}<h3>",True)
