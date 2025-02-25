import os
from itertools import islice

import streamlit as st
import csv

st.set_page_config("wide")

co1, col2 = st.columns(2)

with co1:
    st.image("images/my_image.jpg", width=450)

with col2:
    st.title("Elara Mendes")
    text = """
    I'm Elara, a trans woman who loves creating useful and cool things. I'm also passionate about forensics and data analysis.
    \n
    I'm a cybersecurity student which is exploring the Python world. 💕
    """
    st.info(text)

st.write("Below you can find the projects that I'm working on, feel free to contact me.")

images_folder = "images"

col3, col4 = st.columns(2)

with col3:
    with open("data.csv", "r") as file:
        reader = list(csv.DictReader(file, delimiter=";"))
        for row in reader[:10]:
            st.subheader(row["title"])
            st.write(row["description"])
            folder_path = os.path.join(images_folder, row["image"])
            st.image(folder_path)
            st.markdown(f"[Source Code]({row['url']})")

with col4:
    with open("data.csv", "r") as file:
        reader = list(csv.DictReader(file, delimiter=";"))
        for row in reader[10:]:
            st.subheader(row["title"])
            st.write(row["description"])
            folder_path = os.path.join(images_folder, row["image"])
            st.image(folder_path)
            st.markdown(f"[Source Code]({row['url']})")