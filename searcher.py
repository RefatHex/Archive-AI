import json
import random
from api import GOOGLE_API_KEY
import google.generativeai as gen_ai
import streamlit as st
from _base_prompt import get_prompt
from world_map import render_map

st.set_page_config(
    page_title="History Searcher",  
    page_icon=":brain:", 
    layout="centered", 
)

GOOGLE_API_KEY = GOOGLE_API_KEY


gen_ai.configure(api_key=GOOGLE_API_KEY)
model = gen_ai.GenerativeModel('gemini-pro')

def beautify_events(events):
    country_colors = []
    for event in events:
        st.subheader(event['title'])
        st.markdown(f"**Date:** {event['date']}")
        st.markdown(f"**Description:** {event['description']}")
        st.markdown(f"**Location:** {event['location']}")
        st.markdown(f"[Wikipedia Link]({event['wiki_link']})")
        st.write('\n')
        country_colors.append({
            'countryCode': event['location'],
            'color': "#{:06x}".format(random.randint(0, 0xFFFFFF))  
        })
    

    render_map(country_colors)


date = st.text_input("Ask Gemini-Pro...")
if date:

    st.write("User Prompt:")
    st.write(date)

   
    prompt = get_prompt(date)

    gemini_response = model.generate_content(prompt)
    content=gemini_response.text
    try:
        content_json = json.loads(content)
        if 'events' in content_json:
            beautify_events(content_json['events'])
        
            
        else:
            st.markdown(content)
            st.error("No valid events found in Gemini-Pro's response.")
    except json.JSONDecodeError:
        st.error("Invalid JSON response from Gemini-Pro.")
        print(content)
  

   
    
      
        
if __name__ == "__beautify_events__":
    beautify_events()