import streamlit as st

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