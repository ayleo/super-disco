import streamlit as st
import plotly.express as px
from backend import get_data

# Add title, text input, slider, and selectbox widgets
st.title('Weather Forecast for the next days')
cityname = st.text_input("City", "", placeholder="Insert the city name")
days = st.slider("Forecast Days", 1, 5, help="Select the number of days you want to forecast")
data_source = st.selectbox("Data Source", ["Temperature", "Sky Condition"])

# Add a subheader using the correct phrasing
if days <= 1:
    st.subheader(f"{data_source} for the next {days} day in {cityname}")
else:
    st.subheader(f"{data_source} for the next {days} days in {cityname}")


if cityname:
    try:
        filtered_content = get_data(cityname, days)

        if data_source == "Temperature":
            temperatures = [x["main"]["temp"] / 10 for x in filtered_content]
            dates = [x["dt_txt"] for x in filtered_content]
            figure = px.line(x=dates, y=temperatures, labels={"x": "Date", "y": "Temperature"})
            st.plotly_chart(figure)


        if data_source == "Sky Condition":
            images = {"Clear": "imgs/clear.png", "Clouds": "imgs/cloud.png", "Rain": "imgs/rain.png",
                      "Snow": "imgs/snow.png"}
            sky_conditions = [x["weather"][0]["main"] for x in filtered_content]
            print(sky_conditions)
            image_paths = [images[condition] for condition in sky_conditions]

            st.image(image_paths, width=115)
    except KeyError:
        st.error("City not found, please try again. (e.g. London, Paris, Berlin)")