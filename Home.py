import streamlit as st
import csv

st.set_page_config(page_title="Home", page_icon="🥸")

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

col3, empty_col, col4 = st.columns([1.5, 0.7, 1.5])

with open("data.csv", "r") as file:
    reader = list(csv.DictReader(file, delimiter=";"))

with col3:
    for row in reader[:10]:
        st.header(row["title"])
        st.write(row["description"])
        st.image("images/" + row["image"])
        st.write(f"[Source Code]({row['url']})") # Don't even need markdown here

with col4:
    for row in reader[10:]:
        st.header(row["title"])
        st.write(row["description"])
        st.image("images/" + row["image"]) # Much better and simple
        st.write(f"[Source Code]({row['url']})")