import requests
from _base_prompt import get_prompt
import streamlit as st
import streamlit.components.v1 as components
from world_map import render_map

@st.cache  # eita decorator use korsi cache the function's return values pawar lai
def query_gemini_ai(prompt):
    url = "https://api.gemini.ai/endpoint"  # real api endpoint add marr
    headers = { 
        'Authorization': 'Bearer YOUR_ACCESS_TOKEN',   # token add marr
        'Content-Type': 'application/json' 
    }
    response = requests.post(url, headers=headers, json={'prompt': prompt})
    return response.json()




def main():
    st.title('Gemini AI Historic Event Searcher')
    date = st.text_input("Enter a date (YYYY-MM-DD): ")
    if date:
        prompt = get_prompt(date)  
        response = query_gemini_ai(prompt)
        st.write(response)  
        
    render_map()
        

       


if __name__ == '__main__':
    main()
