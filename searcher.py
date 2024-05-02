import json
from api import GOOGLE_API_KEY
import google.generativeai as gen_ai
import streamlit as st
from _base_prompt import get_prompt
from extract import extract_json

st.set_page_config(
    page_title="History Searcher",  # Page title
    page_icon=":brain:",  # Favicon emoji
    layout="centered",  # Page layout option
)

GOOGLE_API_KEY = GOOGLE_API_KEY

# Set up Google Gemini-Pro AI model
gen_ai.configure(api_key=GOOGLE_API_KEY)
model = gen_ai.GenerativeModel('gemini-pro')

def beautify_events(events):
    for event in events:
        st.subheader(event['title'])
        st.markdown(f"**Date:** {event['date']}")
        st.markdown(f"**Description:** {event['description']}")
        st.markdown(f"**Location:** {event['location']}")
        st.markdown(f"[Wikipedia Link]({event['wiki_link']})")
        st.write('\n')

date = st.text_input("Ask Gemini-Pro...")
if date:
    # Display user's prompt
    st.write("User Prompt:")
    st.write(date)

    # Get prompt based on the selected date
    prompt = get_prompt(date)

    # Send user's message to Gemini-Pro and get the response
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
