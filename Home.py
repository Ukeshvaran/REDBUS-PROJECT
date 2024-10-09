import streamlit as st # To import streamlit
import webbrowser # To create a connection with web_browser
import firebase_admin # To push data to cloud database
from firebase_admin import auth # used to authenticate credentials
from firebase_admin import credentials  # used to verify input credentials
import time
# To add logo
st.logo(image='https://cdn-icons-png.freepik.com/256/3066/3066259.png?ga=GA1.1.1820696419.1725225547&semt=ais_hybrid',link="https://www.redbus.in")
# To verify credentials
cred=credentials.Certificate('ticketbooking-63632-b649ea976ab1.json')
if not firebase_admin._apps:
    firebase_admin.initialize_app(cred)
# To add page_background
page_bg="""<style>[data-testid="stAppViewContainer"]{background-color: #e5e5f7;opacity:100;background-image:url("https://img.freepik.com/free-vector/gray-background-with-earth-map_1017-18759.jpg?w=1380&t=st=1727283293~exp=1727283893~hmac=a8ac83e65b91654789001eb7f884d0079ce410a0c0254d5728c8162a2aea49ba");}</style>"""
st.markdown(page_bg,unsafe_allow_html=True)
# To add sidebar_background
sidebar_bg="""<style>[data-testid="stSidebar"]{background-color:#e5e5f7;opacity:2;background-image:url('https://img.freepik.com/free-photo/green-paint-brush-textured-background_53876-104801.jpg?ga=GA1.1.1820696419.1725225547&semt=ais_hybrid');}</style>"""
st.markdown(sidebar_bg,unsafe_allow_html=True)
#To add page_title
st.title("Online Bus Ticket Booking Site 🚇")
st.divider()
# Actual code for the webpage
def app():
    choice=st.selectbox('Login/Signup',['Login','Signup'])
    def run(email):
        try: # To authenticate user by email from the database
            auth.get_user_by_email(email)
            st.columns(5)[2].markdown(''':green[Success]''',unsafe_allow_html=True)
            st.balloons()
            time.sleep(1)
            webbrowser.open('http://localhost:8501/profile')
        except: # To throw exceptional error
            st.warning("Login failed")
    if choice=='Login': #login
        email=st.text_input('Email or phone number',placeholder='Email or phone number')
        password =st.text_input('password',type='password',placeholder='password')
        if st.columns(5)[2].button("Login",type="primary"):
            run(email)
    else: #signup
        user_id=st.text_input('Username',placeholder='user name')
        email_id=st.text_input('Email ID',placeholder='Email')
        user_pass=st.text_input('Password',type='password',placeholder='password')
        check_box=st.checkbox('Click here',value=False)
        if check_box and email_id and user_pass and user_id:
            if st.columns(5)[2].button("Signup",type="primary"):
                try: # To create an account in the database
                    auth.create_user(email=email_id,password=user_pass,uid=user_id)
                    st.columns(5)[2].markdown("Account created successfully")
                    st.balloons()
                except: # To throw an exceptional error if the user already exists
                    st.columns(3)[1].warning("Account already exists")
                    st.snow()
                    st.columns(5)[2].markdown(''':red[Login to continue]''')
app()
st.divider()





