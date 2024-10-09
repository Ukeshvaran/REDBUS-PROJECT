import streamlit as st
import requests
from streamlit_lottie import st_lottie
sidebar_bg="""<style>[data-testid="stSidebar"]{background-color:#e5e5f7;opacity:2;background-image:url('https://img.freepik.com/free-photo/green-paint-brush-textured-background_53876-104801.jpg?ga=GA1.1.1820696419.1725225547&semt=ais_hybrid');}</style>"""
st.markdown(sidebar_bg,unsafe_allow_html=True)
st.columns(3)[1].markdown(""" # **Settings** ⚙️""")
st.divider()
def load(url):
    r=requests.get(url)
    if r.status_code!=200:
        return None
    return r.json()
url='https://lottie.host/d41f3b60-e29d-4242-b045-220fe0fe9dac/YyjjfhboHe.json'
data=load(url)
st_lottie(data,key="Click",loop=True,width=750,height=130)
choice=st.selectbox(":grey[Settings] :",options=['Profile','Notifications','Language','about'],index=None)