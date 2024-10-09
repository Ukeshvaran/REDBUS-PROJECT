import streamlit as st
import requests
from streamlit_lottie import st_lottie
sidebar_bg="""<style>[data-testid="stSidebar"]{background-color:#e5e5f7;opacity:2;background-image:url('https://img.freepik.com/free-photo/green-paint-brush-textured-background_53876-104801.jpg?ga=GA1.1.1820696419.1725225547&semt=ais_hybrid');}</style>"""
st.markdown(sidebar_bg,unsafe_allow_html=True)
st.columns(3)[1].markdown(""" # **About** 📄""")
st.divider()
def load(url):
    r=requests.get(url)
    if r.status_code!=200:
        return None
    return r.json()
url='https://lottie.host/a85a29f2-4a4b-46eb-a32a-a5bbdf9ffcd7/AJGlbMi1go.json'
data=load(url)
st_lottie(data,key="Click",loop=True,width=670,height=400)
st.divider()
st.image('C:/Users/ukesh/OneDrive/Desktop/Python/icon_fin.jpg',width=100)
st.markdown(":violet[Welcome to this interactive website...! Hi user  i'm ukesh currently mastering the art of data-science from Guvi crafted this as my very first website which is created to help user filter out the buses which suits them based on routes , rating , seats , fare and on various other options available. The main goal of this website is to make user feel comfortable with smooth filtering options and to get their desired bus.]")
st.markdown(":red[Quote of the day] : :green[Every expert was once a beginner 🎯]")
senti=st.feedback("faces")
selected=['Sad','Not satisfied','Satisfied','Happy','Extremly happy']
if senti:
    st.write(selected[senti])
if st.columns(5)[2].button("Know more",type="primary"):
    with st.chat_message("user"):
        def fd_btn():
            st.columns(3)[1].markdown(":green[Thanks for your feedback...!]")
            st.balloons()
        st.write(":green[This Website is not fully created and fully functional yet ,  if you do have any suggestions feel free to share it with me]:wave:")
        txt=st.text_area(label="Enter your Suggetions/feedback: ",max_chars=1000,placeholder="Feedback or suggestions ")
        btn=st.columns(5)[2].button("Submit",type="primary",on_click=fd_btn)
st.video('https://youtu.be/eyAAUGhvZu8?si=FnVAwodWGhEcJWEo',loop=True,autoplay=True,subtitles=None,muted=True)
st.columns(3)[0].write(':copyright: App Deployed by :blue[ukesh]')


