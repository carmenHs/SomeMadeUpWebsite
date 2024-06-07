#Commands for VM
#pip install virtualenv --> virtualenv env --> env\scripts\activate --> pip install streamlit openai

# Cell 1: Setup
import streamlit as st
from openai import OpenAI
import os
import pandas as pd
import numpy as np

st.title('Hello!')

st.header('Princess Zelda & Princess Daisy')
st.text('A page dedicated to the cutest most well-behaved cats in the quantumverse XD')



df = pd.DataFrame(np.random.randn(20, 3), columns=['Zelas Cuteness', 'Daisys Cuteness', 'Overall Cat Graciouseness'])
st.line_chart(df)

# Generate a date range for a month
dates = pd.date_range(start="2024-01-01", end="2024-01-31")

# Weather data remains the same as the previous example
kitty_data = {
    "Zela's Cuteness": np.round(np.random.normal(loc=18, scale=5, size=len(dates)), 1),
    "Daisy's Cuteness": np.random.randint(40, 80, size=len(dates)),
    "Overall Cat Graciouseness": np.round(np.random.uniform(5, 20, size=len(dates)), 1)
}
df_cats = pd.DataFrame(kitty_data, index=dates)

people_info = {
    "Hunter": {"Info": "luvs BOTH Daisy and Zelda!", "type": "Afro"},
    "Carmen": {"Info": "luvs BOTH Daisy and Zelda!", "type": "kinda short in height"},
    "Daisy": {"Info": "is 1 yr (almost)", "type": "medium hair Snuggle Bug!"},
    "Zelda": {"Info": "is 1 and a few months", "type": "long hair Cutey!"},
}

# Use a sidebar selectbox for the user to choose a name
selected_name = st.sidebar.selectbox('Harmon Family Tree. See more info about...', list(people_info.keys()))

# Retrieve the country and favorite color for the selected name
selected_info = people_info[selected_name]

# Display the customized sentence with HTML for styling
st.markdown(f"<b>{selected_name}</b> <b>{selected_info['Info']}</b>. Personal trait : <b>{selected_info['type']}</b>.", unsafe_allow_html=True)

# Get your OpenAI API key from environment variables 
api_key = os.getenv("OPENAI_API_KEY")  # Used in production
client = OpenAI(api_key=api_key)

# Cell 2: Title & Description
st.title('🤖 AI Content Assistant')
st.markdown('What do you need to know about what makes Zelda and Daisy so amazing?.')

# Cell 3: Function to generate text using OpenAI
def analyze_text(text):
    if not api_key:
        st.error("OpenAI API key is not set. Please set it in your environment variables.")
        return
    
    client = OpenAI(api_key=api_key)
    model = "gpt-3.5-turbo"  # Using the GPT-3.5 model

    # Instructions for the AI (adjust if needed)
    messages = [
        {"role": "system", "content": "You are a researcher who studies the behavior and personality traits of the cats Zelda, a long haired brown cat, and Daisy, a short haired white, grey, and black cat, given their loving home and environemnt. They have some days packed with adventure where they go on outside walks, etc. And your goal is to spread awareness and interesting facts on these two amazing feline princesses."},
        {"role": "user", "content": f"Please help me understand more about the greatest cats, Zelda and Daisy, given the following point of curiosity, make sure you detail with bullet points and real life examples:\n{text}"}
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
user_input = st.text_area("Curiosity is not just for cats! What are the mysteries of Zelda and Daisy you would like to uncover?")

if st.button('Generate Post Content'):
    with st.spinner('Generating Text...'):
        post_text = analyze_text(user_input)
        st.write(post_text)

    with st.spinner('Generating Cat Image...'):
        catimage_url = generate_image(user_input)  # Consider adjusting the prompt for image generation if needed
        st.image(thumbnail_url, caption='Generated Thumbnail')
