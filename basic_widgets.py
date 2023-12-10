import streamlit as st
import datetime
import pandas as pd

name = st.text_input(label="Nama Lengkap", value="")
st.write("Nama: ", name)

text = st.text_area("Feedback")
st.write("Feedback: ", text)

number = st.number_input(label="Umur")
st.write("Umur: ", int(number), "tahun")

date = st.date_input(label="Tanggal lahir", min_value=datetime.date(1900, 1, 1))
st.write("Tanggal lahir: ", date)

uploaded_file = st.file_uploader("Choose a CSV file")
if uploaded_file:
    df = pd.read_csv(uploaded_file)
    st.dataframe(df)

picture = st.camera_input("Take a picture")
if picture:
    st.image(picture)

if st.button("Say hello"):
    st.write("Hello there")

agree = st.checkbox("I agree")
if agree:
    st.write("Welcome to MyApp")

genre = st.radio(
    label="What's your favorite movie genre?",
    options=(
        "Comedy",
        "Drama",
        "Documentary",
    ),
    horizontal=False,
)

sports = st.selectbox(
    label="What's your favorite sport?",
    options=(
        "Futsal",
        "Badminton",
        "Volley",
    ),
)

foods = st.multiselect(
    label="What's your favorite food?",
    options=(
        "Indomie",
        "Rendang",
        "Rawon",
    ),
)

values = st.slider(
    label="Select a range of values",
    min_value=0,
    max_value=100,
    value=(0, 100),
)
st.write("Values:", values)
