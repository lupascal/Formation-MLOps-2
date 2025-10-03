import requests
import streamlit as st

from config import INFERENCE_HOST

st.title('My Wind Turbine App')
st.header('Requesting predictions to a service exposing a model')

default_wind_speed_avg = 0
received_wind_speed_avg = st.text_input(
    "Wind speed average (Ws1_avg)", default_wind_speed_avg)

default_wind_speed_avg2 = 0
received_wind_speed_avg2 = st.text_input(
    "Wind speed average (Ws2_avg)", default_wind_speed_avg2)

if st.button('Predict with an embedded model !'):
    prediction = requests.get(
        f'http://{INFERENCE_HOST}:5000/predict?Ws1_avg={received_wind_speed_avg}&Ws2_avg={received_wind_speed_avg2}').json()
    st.write('👇 Prediction with wind speed average at 👇' +
             received_wind_speed_avg)
    st.write(prediction)

st.image('https://media.giphy.com/media/rQdPpBsXTy7GU/giphy.gif',
         use_column_width=True)
