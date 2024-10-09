import streamlit as st
from streamlit_lottie import st_lottie
import requests
import psycopg2 as pg
import pandas as pd
sidebar_bg="""<style>[data-testid="stSidebar"]{background-color:#e5e5f7;opacity:2;background-image:url('https://img.freepik.com/free-photo/green-paint-brush-textured-background_53876-104801.jpg?ga=GA1.1.1820696419.1725225547&semt=ais_hybrid');}</style>"""
st.markdown(sidebar_bg,unsafe_allow_html=True)
st.columns(3)[1].html('''<h1>Filters 🗃️</h1>''')
st.divider()
choice=st.selectbox(':red[States list :]',['Andhra','Kerala','Assam','Himachal','Punjab','Rajasthan','South bengal','Telengana','Uttar Pradesh','West bengal'], placeholder='Select to filter')
if choice=='Andhra':
        an=pd.read_csv('C:/Users/ukesh/OneDrive/Desktop/Python/bus_details/Andhra_buses.csv')
        route_name=st.selectbox(f'{choice} routes :',an['Route_name'])
        if route_name:
                type=st.radio(' Select Bus type :',options=['Sleeper','Seater','A/C','Non A/C'])
                a,b=st.slider('Select price range :',min_value=100,max_value=7000,step=50,value=(100,7000))
                st.write('Selected range :',a, "-",b)
                time=st.time_input('Select time :',value=None)
                st.write(time)
                btn =st.columns(3)[1].button('Apply')
        if btn:
                con=pg.connect(
                host='localhost',
                port='5432',
                database='jack',
                user='postgres',
                password='137700')
                cur=con.cursor()
                if type == 'Sleeper':
                       bus_ty = 'bus_type LIKE %s'
                       bus_ty_value = '%Sleeper%'
                elif type == 'Seater':
                        bus_ty = 'bus_type LIKE %s'
                        bus_ty_value = '%Seater%'
                elif type == 'A/C':
                        bus_ty = 'bus_type LIKE %s'
                        bus_ty_value = '%A/C%'
                elif type == 'Non A/C':
                        bus_ty = 'bus_type LIKE %s'
                        bus_ty_value = '%Non A/C%'
                q = f'''
                SELECT * FROM redbus 
                WHERE price BETWEEN %s AND %s 
                AND route_name = %s 
                AND {bus_ty}  
                AND departing_time>='{time}'
                ORDER BY price,departing_time ASC;
                '''
                p = [a, b, route_name]
                p.append(bus_ty_value)
                cur.execute(q, p)
                data = cur.fetchall()
                result = pd.DataFrame(data, columns=["id", "bus_name", "bus_type", "price", "departing_time", "reaching_time", "duration", "star_rating", "seats_available", "route_link", "route_name"])
                if result.empty:
                        st.error(':red[ No buses found, try again...]', icon="⌛")
                else:
                        st.write(result)
                
        
if choice=='Kerala':
        an=pd.read_csv('C:/Users/ukesh/OneDrive/Desktop/Python/bus_details/Kerala_buses.csv')
        route_name=st.selectbox(f'{choice} routes',an['Route_name'])
        if route_name:
                type=st.radio(' Select Bus type :',options=['Sleeper','Seater','A/C','Non A/C'])
                a,b=st.slider('Select price range :',min_value=100,max_value=7000,step=50,value=(100,7000))
                st.write('Selected range :',a, "-",b)
                time=st.time_input('Select time :',value=None)
                st.write(time)
                btn =st.columns(3)[1].button('Apply')
        if btn:
                con=pg.connect(
                host='localhost',
                port='5432',
                database='jack',
                user='postgres',
                password='137700')
                cur=con.cursor()
                if type == 'Sleeper':
                       bus_ty = 'bus_type LIKE %s'
                       bus_ty_value = '%Sleeper%'
                elif type == 'Seater':
                        bus_ty = 'bus_type LIKE %s'
                        bus_ty_value = '%Seater%'
                elif type == 'A/C':
                        bus_ty = 'bus_type LIKE %s'
                        bus_ty_value = '%A/C%'
                elif type == 'Non A/C':
                        bus_ty = 'bus_type LIKE %s'
                        bus_ty_value = '%Non A/C%'
                q = f'''
                SELECT * FROM redbus 
                WHERE price BETWEEN %s AND %s 
                AND route_name = %s 
                AND {bus_ty}  
                AND departing_time>='{time}'
                ORDER BY price,departing_time ASC;
                '''
                p = [a, b, route_name]
                p.append(bus_ty_value)
                cur.execute(q, p)
                data = cur.fetchall()
                result = pd.DataFrame(data, columns=["id", "bus_name", "bus_type", "price", "departing_time", "reaching_time", "duration", "star_rating", "seats_available", "route_link", "route_name"])
                if result.empty:
                        st.error(':red[ No buses found, try again...]', icon="⌛")
                else:
                        st.write(result)
if choice=='Assam':
        an=pd.read_csv('C:/Users/ukesh/OneDrive/Desktop/Python/bus_details/assam_buses.csv')
        route_name=st.selectbox(f'{choice} routes',an['Route_name'])
        if route_name:
                type=st.radio(' Select Bus type :',options=['Sleeper','Seater','A/C','Non A/C'])
                a,b=st.slider('Select price range :',min_value=100,max_value=7000,step=50,value=(100,7000))
                st.write('Selected range :',a, "-",b)
                time=st.time_input('Select time :',value=None)
                st.write(time)
                btn =st.columns(3)[1].button('Apply')
        if btn:
                con=pg.connect(
                host='localhost',
                port='5432',
                database='jack',
                user='postgres',
                password='137700')
                cur=con.cursor()
                if type == 'Sleeper':
                       bus_ty = 'bus_type LIKE %s'
                       bus_ty_value = '%Sleeper%'
                elif type == 'Seater':
                        bus_ty = 'bus_type LIKE %s'
                        bus_ty_value = '%Seater%'
                elif type == 'A/C':
                        bus_ty = 'bus_type LIKE %s'
                        bus_ty_value = '%A/C%'
                elif type == 'Non A/C':
                        bus_ty = 'bus_type LIKE %s'
                        bus_ty_value = '%Non A/C%'
                q = f'''
                SELECT * FROM redbus 
                WHERE price BETWEEN %s AND %s 
                AND route_name = %s 
                AND {bus_ty}  
                AND departing_time>='{time}'
                ORDER BY price,departing_time ASC;
                '''
                p = [a, b, route_name]
                p.append(bus_ty_value)
                cur.execute(q, p)
                data = cur.fetchall()
                result = pd.DataFrame(data, columns=["id", "bus_name", "bus_type", "price", "departing_time", "reaching_time", "duration", "star_rating", "seats_available", "route_link", "route_name"])
                if result.empty:
                        st.error(':red[ No buses found, try again...]', icon="⌛")
                else:
                        st.write(result)
if choice=='Himachal':
        an=pd.read_csv('C:/Users/ukesh/OneDrive/Desktop/Python/bus_details/himachal_buses.csv')
        route_name=st.selectbox(f'{choice} routes',an['Route_name'])
        if route_name:
                type=st.radio(' Select Bus type :',options=['Sleeper','Seater','A/C','Non A/C'])
                a,b=st.slider('Select price range :',min_value=100,max_value=7000,step=50,value=(100,7000))
                st.write('Selected range :',a, "-",b)
                time=st.time_input('Select time :',value=None)
                st.write(time)
                btn =st.columns(3)[1].button('Apply')
        if btn:
                con=pg.connect(
                host='localhost',
                port='5432',
                database='jack',
                user='postgres',
                password='137700')
                cur=con.cursor()
                if type == 'Sleeper':
                       bus_ty = 'bus_type LIKE %s'
                       bus_ty_value = '%Sleeper%'
                elif type == 'Seater':
                        bus_ty = 'bus_type LIKE %s'
                        bus_ty_value = '%Seater%'
                elif type == 'A/C':
                        bus_ty = 'bus_type LIKE %s'
                        bus_ty_value = '%A/C%'
                elif type == 'Non A/C':
                        bus_ty = 'bus_type LIKE %s'
                        bus_ty_value = '%Non A/C%'
                q = f'''
                SELECT * FROM redbus 
                WHERE price BETWEEN %s AND %s 
                AND route_name = %s 
                AND {bus_ty}  
                AND departing_time>='{time}'
                ORDER BY price,departing_time ASC;
                '''
                p = [a, b, route_name]
                p.append(bus_ty_value)
                cur.execute(q, p)
                data = cur.fetchall()
                result = pd.DataFrame(data, columns=["id", "bus_name", "bus_type", "price", "departing_time", "reaching_time", "duration", "star_rating", "seats_available", "route_link", "route_name"])
                if result.empty:
                        st.error(':red[ No buses found, try again...]', icon="⌛")
                else:
                        st.write(result)
if choice=='Punjab':
        an=pd.read_csv('C:/Users/ukesh/OneDrive/Desktop/Python/bus_details/punjab_buses.csv')
        route_name=st.selectbox(f'{choice} routes',an['Route_name'])
        if route_name:
                type=st.radio(' Select Bus type :',options=['Sleeper','Seater','A/C','Non A/C'])
                a,b=st.slider('Select price range :',min_value=100,max_value=7000,step=50,value=(100,7000))
                st.write('Selected range :',a, "-",b)
                time=st.time_input('Select time :',value=None)
                st.write(time)
                btn =st.columns(3)[1].button('Apply')
        if btn:
                con=pg.connect(
                host='localhost',
                port='5432',
                database='jack',
                user='postgres',
                password='137700')
                cur=con.cursor()
                if type == 'Sleeper':
                       bus_ty = 'bus_type LIKE %s'
                       bus_ty_value = '%Sleeper%'
                elif type == 'Seater':
                        bus_ty = 'bus_type LIKE %s'
                        bus_ty_value = '%Seater%'
                elif type == 'A/C':
                        bus_ty = 'bus_type LIKE %s'
                        bus_ty_value = '%A/C%'
                elif type == 'Non A/C':
                        bus_ty = 'bus_type LIKE %s'
                        bus_ty_value = '%Non A/C%'
                q = f'''
                SELECT * FROM redbus 
                WHERE price BETWEEN %s AND %s 
                AND route_name = %s 
                AND {bus_ty}  
                AND departing_time>='{time}'
                ORDER BY price,departing_time ASC;
                '''
                p = [a, b, route_name]
                p.append(bus_ty_value)
                cur.execute(q, p)
                data = cur.fetchall()
                result = pd.DataFrame(data, columns=["id", "bus_name", "bus_type", "price", "departing_time", "reaching_time", "duration", "star_rating", "seats_available", "route_link", "route_name"])
                if result.empty:
                        st.error(':red[ No buses found, try again...]', icon="⌛")
                else:
                        st.write(result)
if choice=='Rajasthan':
        an=pd.read_csv('C:/Users/ukesh/OneDrive/Desktop/Python/bus_details/Rajasthan_buses.csv')
        route_name=st.selectbox(f'{choice} routes',an['Route_name']) 
        if route_name:
                type=st.radio(' Select Bus type :',options=['Sleeper','Seater','A/C','Non A/C'])
                a,b=st.slider('Select price range :',min_value=100,max_value=7000,step=50,value=(100,7000))
                st.write('Selected range :',a, "-",b)
                time=st.time_input('Select time :',value=None)
                st.write(time)
                btn =st.columns(3)[1].button('Apply')
        if btn:
                con=pg.connect(
                host='localhost',
                port='5432',
                database='jack',
                user='postgres',
                password='137700')
                cur=con.cursor()
                if type == 'Sleeper':
                       bus_ty = 'bus_type LIKE %s'
                       bus_ty_value = '%Sleeper%'
                elif type == 'Seater':
                        bus_ty = 'bus_type LIKE %s'
                        bus_ty_value = '%Seater%'
                elif type == 'A/C':
                        bus_ty = 'bus_type LIKE %s'
                        bus_ty_value = '%A/C%'
                elif type == 'Non A/C':
                        bus_ty = 'bus_type LIKE %s'
                        bus_ty_value = '%Non A/C%'
                q = f'''
                SELECT * FROM redbus 
                WHERE price BETWEEN %s AND %s 
                AND route_name = %s 
                AND {bus_ty}  
                AND departing_time>='{time}'
                ORDER BY price,departing_time ASC;
                '''
                p = [a, b, route_name]
                p.append(bus_ty_value)
                cur.execute(q, p)
                data = cur.fetchall()
                result = pd.DataFrame(data, columns=["id", "bus_name", "bus_type", "price", "departing_time", "reaching_time", "duration", "star_rating", "seats_available", "route_link", "route_name"])
                if result.empty:
                        st.error(':red[ No buses found, try again...]', icon="⌛")
                else:
                        st.write(result)   
if choice=='South bengal':
        an=pd.read_csv('C:/Users/ukesh/OneDrive/Desktop/Python/bus_details/South_bengal_buses.csv')
        route_name=st.selectbox(f'{choice} routes',an['Route_name'])
        if route_name:
                type=st.radio(' Select Bus type :',options=['Sleeper','Seater','A/C','Non A/C'])
                a,b=st.slider('Select price range :',min_value=100,max_value=7000,step=50,value=(100,7000))
                st.write('Selected range :',a, "-",b)
                time=st.time_input('Select time :',value=None)
                st.write(time)
                btn =st.columns(3)[1].button('Apply')
        if btn:
                con=pg.connect(
                host='localhost',
                port='5432',
                database='jack',
                user='postgres',
                password='137700')
                cur=con.cursor()
                if type == 'Sleeper':
                       bus_ty = 'bus_type LIKE %s'
                       bus_ty_value = '%Sleeper%'
                elif type == 'Seater':
                        bus_ty = 'bus_type LIKE %s'
                        bus_ty_value = '%Seater%'
                elif type == 'A/C':
                        bus_ty = 'bus_type LIKE %s'
                        bus_ty_value = '%A/C%'
                elif type == 'Non A/C':
                        bus_ty = 'bus_type LIKE %s'
                        bus_ty_value = '%Non A/C%'
                q = f'''
                SELECT * FROM redbus 
                WHERE price BETWEEN %s AND %s 
                AND route_name = %s 
                AND {bus_ty}  
                AND departing_time>='{time}'
                ORDER BY price,departing_time ASC;
                '''
                p = [a, b, route_name]
                p.append(bus_ty_value)
                cur.execute(q, p)
                data = cur.fetchall()
                result = pd.DataFrame(data, columns=["id", "bus_name", "bus_type", "price", "departing_time", "reaching_time", "duration", "star_rating", "seats_available", "route_link", "route_name"])
                if result.empty:
                        st.error(':red[ No buses found, try again...]', icon="⌛")
                else:
                        st.write(result)
if choice=='Telengana':
        an=pd.read_csv('C:/Users/ukesh/OneDrive/Desktop/Python/bus_details/telengana_buses.csv')
        route_name=st.selectbox(f'{choice} routes',an['Route_name'])
        if route_name:
                type=st.radio(' Select Bus type :',options=['Sleeper','Seater','A/C','Non A/C'])
                a,b=st.slider('Select price range :',min_value=100,max_value=7000,step=50,value=(100,7000))
                st.write('Selected range :',a, "-",b)
                time=st.time_input('Select time :',value=None)
                st.write(time)
                btn =st.columns(3)[1].button('Apply')
        if btn:
                con=pg.connect(
                host='localhost',
                port='5432',
                database='jack',
                user='postgres',
                password='137700')
                cur=con.cursor()
                if type == 'Sleeper':
                       bus_ty = 'bus_type LIKE %s'
                       bus_ty_value = '%Sleeper%'
                elif type == 'Seater':
                        bus_ty = 'bus_type LIKE %s'
                        bus_ty_value = '%Seater%'
                elif type == 'A/C':
                        bus_ty = 'bus_type LIKE %s'
                        bus_ty_value = '%A/C%'
                elif type == 'Non A/C':
                        bus_ty = 'bus_type LIKE %s'
                        bus_ty_value = '%Non A/C%'
                q = f'''
                SELECT * FROM redbus 
                WHERE price BETWEEN %s AND %s 
                AND route_name = %s 
                AND {bus_ty}  
                AND departing_time>='{time}'
                ORDER BY price,departing_time ASC;
                '''
                p = [a, b, route_name]
                p.append(bus_ty_value)
                cur.execute(q, p)
                data = cur.fetchall()
                result = pd.DataFrame(data, columns=["id", "bus_name", "bus_type", "price", "departing_time", "reaching_time", "duration", "star_rating", "seats_available", "route_link", "route_name"])
                if result.empty:
                        st.error(':red[ No buses found, try again...]', icon="⌛")
                else:
                        st.write(result)
if choice=='Uttar Pradesh':
        an=pd.read_csv('C:/Users/ukesh/OneDrive/Desktop/Python/bus_details/up_buses.csv')
        route_name=st.selectbox(f'{choice} routes',an['Route_name'])
        if route_name:
                type=st.radio(' Select Bus type :',options=['Sleeper','Seater','A/C','Non A/C'])
                a,b=st.slider('Select price range :',min_value=100,max_value=7000,step=50,value=(100,7000))
                st.write('Selected range :',a, "-",b)
                time=st.time_input('Select time :',value=None)
                st.write(time)
                btn =st.columns(3)[1].button('Apply')
        if btn:
                con=pg.connect(
                host='localhost',
                port='5432',
                database='jack',
                user='postgres',
                password='137700')
                cur=con.cursor()
                if type == 'Sleeper':
                       bus_ty = 'bus_type LIKE %s'
                       bus_ty_value = '%Sleeper%'
                elif type == 'Seater':
                        bus_ty = 'bus_type LIKE %s'
                        bus_ty_value = '%Seater%'
                elif type == 'A/C':
                        bus_ty = 'bus_type LIKE %s'
                        bus_ty_value = '%A/C%'
                elif type == 'Non A/C':
                        bus_ty = 'bus_type LIKE %s'
                        bus_ty_value = '%Non A/C%'
                q = f'''
                SELECT * FROM redbus 
                WHERE price BETWEEN %s AND %s 
                AND route_name = %s 
                AND {bus_ty}  
                AND departing_time>='{time}'
                ORDER BY price,departing_time ASC;
                '''
                p = [a, b, route_name]
                p.append(bus_ty_value)
                cur.execute(q, p)
                data = cur.fetchall()
                result = pd.DataFrame(data, columns=["id", "bus_name", "bus_type", "price", "departing_time", "reaching_time", "duration", "star_rating", "seats_available", "route_link", "route_name"])
                if result.empty:
                        st.error(':red[ No buses found, try again...]', icon="⌛")
                else:
                        st.write(result) 
if choice=='West bengal':
       an=pd.read_csv('C:/Users/ukesh/OneDrive/Desktop/Python/bus_details/west_bengal_buses.csv')
       route_name=st.selectbox(f'{choice} routes',an['Route_name'])
       if route_name:
                type=st.radio(' Select Bus type :',options=['Sleeper','Seater','A/C','Non A/C'])
                a,b=st.slider('Select price range :',min_value=100,max_value=7000,step=50,value=(100,7000))
                st.write('Selected range :',a, "-",b)
                time=st.time_input('Select time :',value=None)
                st.write(time)
                btn =st.columns(3)[1].button('Apply')
                if btn:

                        con=pg.connect(
                        host='localhost',
                        port='5432',
                        database='jack',
                        user='postgres',
                        password='137700')
                        cur=con.cursor()
                        if type == 'Sleeper':
                                bus_ty = 'bus_type LIKE %s'
                                bus_ty_value = '%Sleeper%'
                        elif type == 'Seater':
                                bus_ty = 'bus_type LIKE %s'
                                bus_ty_value = '%Seater%'
                        elif type == 'A/C':
                                bus_ty = 'bus_type LIKE %s'
                                bus_ty_value = '%A/C%'
                        elif type == 'Non A/C':
                                bus_ty = 'bus_type LIKE %s'
                                bus_ty_value = '%Non A/C%'
                        q = f'''
                        SELECT * FROM redbus 
                        WHERE price BETWEEN %s AND %s 
                        AND route_name = %s 
                        AND {bus_ty}  
                        AND departing_time>='{time}'
                        ORDER BY price,departing_time ASC;
                        '''
                        p = [a, b, route_name]
                        p.append(bus_ty_value)
                        cur.execute(q, p)
                        data = cur.fetchall()
                        result = pd.DataFrame(data, columns=["id", "bus_name", "bus_type", "price", "departing_time", "reaching_time", "duration", "star_rating", "seats_available", "route_link", "route_name"])
                        if result.empty:
                                st.error(':red[ No buses found, try again...]', icon="⌛")
                        else:
                                st.write(result)
       

        
def load(url):
    r=requests.get(url)
    if r.status_code!=200:
        return None
    return r.json()
url='https://lottie.host/fbaf7f9f-c084-470b-b920-1805df446ccb/kThl0kpGpM.json'
data=load(url)
logo=st_lottie(data,key="Click",loop=True,width=640,height=300,quality="high")