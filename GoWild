#Commands for VM
#pip install virtualenv --> virtualenv env --> env\scripts\activate --> pip install streamlit openai

import streamlit as st

st.title('Hello, Lonely Octopus!')

st.header('This is a header')
st.subheader('This is a subheader')
st.text('This is some black text.')

import pandas as pd
import numpy as np

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
