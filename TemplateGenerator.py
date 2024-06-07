#Commands for VM
#pip install virtualenv --> virtualenv env --> env\scripts\activate --> pip install streamlit openai

# Cell 1: Setup
import streamlit as st
from openai import OpenAI
import os
import pandas as pd
import numpy as np

st.title('Template Generator!')

st.header('Generate a template for your your customers.')
st.text('A page for generating helpful templates by Wize Solutions.')



df = pd.DataFrame(np.random.randn(20, 3), columns=['DataPoint1', 'DataPoint2', 'DataPoint3'])
st.line_chart(df)

# Generate a date range for a month
dates = pd.date_range(start="2024-01-01", end="2024-01-31")

# Weather data remains the same as the previous example
kitty_data = {
    "Value1": np.round(np.random.normal(loc=18, scale=5, size=len(dates)), 1),
    "Value2": np.random.randint(40, 80, size=len(dates)),
    "Value3": np.round(np.random.uniform(5, 20, size=len(dates)), 1)
}
df_cats = pd.DataFrame(kitty_data, index=dates)

people_info = {
    "Value1": {"Info": "these are more details on value1", "type": "Value1"},
    "Value2": {"Info": "these are more details on value2", "type": "Value2"},
    "Value3": {"Info": "these are more details on value3", "type": "Value3"}
}

# Use a sidebar selectbox for the user to choose a name
selected_name = st.sidebar.selectbox('See more info about...', list(people_info.keys()))

# Retrieve the country and favorite color for the selected name
selected_info = people_info[selected_name]

# Display the customized sentence with HTML for styling
st.markdown(f"<b>{selected_name}</b> <b>{selected_info['Info']}</b>. Personal trait : <b>{selected_info['type']}</b>.", unsafe_allow_html=True)

# Get your OpenAI API key from environment variables 
api_key = os.getenv("OPENAI_API_KEY")  # Used in production
client = OpenAI(api_key=api_key)

# Cell 2: Title & Description
st.title('🤖 AI Template Generation Assistant')
st.markdown('What Template do you need?.')

# Cell 3: Function to generate text using OpenAI
def analyze_text(text):
    if not api_key:
        st.error("OpenAI API key is not set. Please set it in your environment variables.")
        return
    
    client = OpenAI(api_key=api_key)
    model = "gpt-3.5-turbo"  # Using the GPT-3.5 model

    # Instructions for the AI (adjust if needed)
    messages = [
        {"role": "system", "content": "You are a liecensing office that needs to generate various templates to help organize documentation and other business uses."},
        {"role": "user", "content": f"Please help me build a template for the given topic, scenario or occasion, make sure you provide a framework that is professional, detailed and concise that I can easily incorporate and adapt to my situation,:\n{text}"}
    ]

    response = client.chat.completions.create(
        model=model,
        messages=messages,
        temperature=0  # Lower temperature for less random responses
    )
    return response.choices[0].message.content


# Cell 4: Function to generate the image
def generate_image(text):
    if not api_key:
        st.error("OpenAI API key is not set. Please set it in your environment variables.")
        return

    response = client.images.generate(
        model="dall-e-3",
        prompt=text,
        size="1024x1024",
        quality="standard",
        n=1,
    )

    # Assuming the API returns an image URL; adjust based on actual response structure
    return response.data[0].url

# Cell 4: Streamlit UI 
user_input = st.text_area("What type of template can I help you generate?")

if st.button('Generate Template'):
    with st.spinner('Generating...'):
        post_text = analyze_text(user_input)
        st.write(post_text)

    with st.spinner('Generating Image...'):
        catimage_url = generate_image(user_input)  # Consider adjusting the prompt for image generation if needed
        st.image(thumbnail_url, caption='Generated Template Image')
