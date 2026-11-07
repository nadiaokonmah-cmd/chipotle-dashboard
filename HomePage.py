# This creates the main landing page for the Streamlit application.
# Contains an introduction to the project and guide users to other pages.

# Import Streamlit
import streamlit as st

# st.set_page_config() is used to configure the page's appearance in the browser tab.
# It's good practice to set this as the first Streamlit command in your script.
st.set_page_config(
    page_title="Chipotle Data Dashboard",  # The title that appears in the browser tab
    page_icon="🌯",         # An emoji that appears as the icon in the browser tab
)

# WELCOME PAGE TITLE
st.title("Welcome to the Chipotle Bowl Dashboard! 🌯")

# INTRODUCTORY TEXT
st.write("""
Ever wondered which ingredients make the ultimate Chipotle bowl?

This website explores Chipotle bowl ingredients using data visualizations and
customer preference surveys.

### How to Use This Website

🌯 Home Page:
Learn about the Chipotle Bowl Dashboard.

📝 Survey Page:
Tell us your favorite Chipotle protein and rate it!

📊 Visuals Page:
Explore ingredient preference scores and survey results
through interactive data visualizations.


Note: The preference scores are illustrative sample data,
not official Chipotle statistics.
""")

# OPTIONAL: ADD AN IMAGE
# 1. Navigate to the 'images' folder in your Lab02 directory.
# 2. Place your image file (e.g., 'welcome_image.png') inside that folder.
# 3. Uncomment the line below and change the filename to match yours.
#
st.image("images/imsohungryrn.jpeg")
