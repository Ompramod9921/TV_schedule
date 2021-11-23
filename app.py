import streamlit as st
import requests
import pandas as pd
import json

st.set_page_config(page_title='TV Schedule',page_icon='👽')
hide_streamlit_style = """
            <style>
            #MainMenu {visibility: hidden;}
            footer {visibility: hidden;}
            </style>
            """
st.markdown(hide_streamlit_style, unsafe_allow_html=True)

st.title("Television Schedule")
st.write("Made with ❤️ by om pramod")
st.markdown("*****")

url = "https://indian-tv-schedule.p.rapidapi.com/searchChannel"

language = st.selectbox("Select a language", ["Hindi", "Marathi","Punjabi" ,"Urdu", "Bengali" ,"English" ,"Malayalam" ,"Tamil", "Gujarati", "Odia" ,"Telugu" ,"Bhojpuri", "Kannada" ,"Assamese" ,"Nepali" ,"French"])

if language == "Hindi" :
    querystring = {"lang":"Hindi"}
elif language == "Marathi":
    querystring = {"lang":"Marathi"}
elif language == "Punjabi":
    querystring = {"lang":"Marathi"}
elif language == "Urdu":
    querystring = {"lang":"Urdu"}
elif language == "Bengali":
    querystring = {"lang":"Bengali"}
elif language == "English":
    querystring = {"lang":"English"}
elif language == "Malayalam":
    querystring = {"lang":"Malayalam"}
elif language == "Tamil":
    querystring = {"lang":"Tamil"}
elif language == "Gujarati":
    querystring = {"lang":"Gujarati"}
elif language == "Odia":
    querystring = {"lang":"Odia"}
elif language == "Telugu":
    querystring = {"lang":"Telugu"}
elif language == "Bhojpuri":
    querystring = {"lang":"Bhojpuri"}
elif language == "Kannada":
    querystring = {"lang":"Kannada"}
elif language == "Assamese":
    querystring = {"lang":"Assamese"}
elif language == "Nepali":
    querystring = {"lang":"Nepali"}
elif language == "French":
    querystring = {"lang":"French"}

headers = {
    'x-rapidapi-host': "indian-tv-schedule.p.rapidapi.com",
    'x-rapidapi-key': "e4998fab02mshd659411da63b59ap18d367jsn43b1841d6872"
    }

response = requests.request("GET", url, headers=headers, params=querystring)

channel = response.text
channel = channel.replace('"','')
channel = channel.replace("[","")
channel = channel.replace("]",'')

fav_channel = st.selectbox("Select a channel",options=[opt.strip() for opt in channel.split(",")])


url = "https://indian-tv-schedule.p.rapidapi.com/TodaySchedule"

querystring = {"channel":fav_channel}

headers = {
    'x-rapidapi-host': "indian-tv-schedule.p.rapidapi.com",
    'x-rapidapi-key': "e4998fab02mshd659411da63b59ap18d367jsn43b1841d6872"
    }

response = requests.request("GET", url, headers=headers, params=querystring)

#converting to dictionary
response = response.json()

response= pd.DataFrame.from_dict(response,orient ='index').drop(['other-details'], axis = 1)

if st.button("Get Todays Schedule") :
    try :
        st.table(response)
    except:
        st.error("some error occured")



