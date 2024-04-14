#Commands for VM
#pip install virtualenv --> virtualenv env --> env\scripts\activate --> pip install streamlit openai

# Cell 1: Setup
import streamlit as st
from openai import OpenAI
import os
import pandas as pd
import numpy as np

st.title('Hello, Lonely Octopus!')

st.header('This is a header')
st.subheader('This is a subheader')
st.text('This is some black text.')



df = pd.DataFrame(np.random.randn(20, 3), columns=['a', 'b', 'c'])
st.line_chart(df)

# Generate a date range for a month
dates = pd.date_range(start="2024-01-01", end="2024-01-31")

# Weather data remains the same as the previous example
weather_data = {
    "Avg Temperature (°C)": np.round(np.random.normal(loc=18, scale=5, size=len(dates)), 1),
    "Humidity (%)": np.random.randint(40, 80, size=len(dates)),
    "Wind Speed (km/h)": np.round(np.random.uniform(5, 20, size=len(dates)), 1)
}
df_weather = pd.DataFrame(weather_data, index=dates)

# Generating monthly sales data for different services
services = ["Cruises", "Skydiving", "Water skiing"]
sales_data = {
    service: np.random.randint(200, 500, size=12) for service in services
}
months = pd.date_range(start="2024-01-01", end="2024-12-01", freq='MS')
df_sales = pd.DataFrame(sales_data, index=months.strftime('%B'))

chart_type = st.selectbox('Choose a chart type:', ['Line', 'Bar'])

if chart_type == 'Line':
    st.write("Weather Data Overview")
    st.line_chart(df_weather)
elif chart_type == 'Bar':
    st.write("Monthly Sales Data")
    st.bar_chart(df_sales)

people_info = {
    "Tina": {"country": "Canada", "fav_color": "yellow"},
    "Rex": {"country": "the Phillipines", "fav_color": "purple"},
    "Harshit": {"country": "India", "fav_color": "orange"},
    "Julian": {"country": "Australia", "fav_color": "black"},
    "Ibraheem": {"country": "Morocco", "fav_color": "light blue"},
}

# Use a sidebar selectbox for the user to choose a name
selected_name = st.sidebar.selectbox('Which Lonely Octopus are you interested in?', list(people_info.keys()))

# Retrieve the country and favorite color for the selected name
selected_info = people_info[selected_name]

# Display the customized sentence with HTML for styling
st.markdown(f"<b>{selected_name}</b> is from <b>{selected_info['country']}</b>. Favorite color: <b>{selected_info['fav_color']}</b>.", unsafe_allow_html=True)

col1, col2 = st.columns(2)
with col1:
    st.line_chart(df['a'])
with col2:
    st.line_chart(df['b'])

with st.expander("See explanation"):
    st.text("Here you can put in detailed explanations.")

if st.button('What is Streamlit?'):
    st.write('A faster way to build and share data apps. Streamlit turns data scripts into shareable web apps in minutes.')
else:
    st.write('Click me to define streamlit.')


# Get your OpenAI API key from environment variables 
api_key = os.getenv("OPENAI_API_KEY2")  # Used in production
client = OpenAI(api_key=api_key)

# Cell 2: Title & Description
st.title('🤖 AI Content Assistant')
st.markdown('I was made to help you craft interesting Social media posts.')

# Cell 3: Function to generate text using OpenAI
def analyze_text(text):
    if not api_key:
        st.error("OpenAI API key is not set. Please set it in your environment variables.")
        return
    
    client = OpenAI(api_key=api_key)
    model = "gpt-3.5-turbo"  # Using the GPT-3.5 model

    # Instructions for the AI (adjust if needed)
    messages = [
        {"role": "system", "content": "You are an assistant who helps craft social media posts."},
        {"role": "user", "content": f"Please help me write a social media post based on the following, make sure you detail with bullet points and steps:\n{text}"}
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
user_input = st.text_area("Enter a brief for your post:", "How should you maintain a deployed model?")

if st.button('Generate Post Content'):
    with st.spinner('Generating Text...'):
        post_text = analyze_text(user_input)
        st.write(post_text)

    with st.spinner('Generating Thumbnail...'):
        thumbnail_url = generate_image(user_input)  # Consider adjusting the prompt for image generation if needed
        st.image(thumbnail_url, caption='Generated Thumbnail')
