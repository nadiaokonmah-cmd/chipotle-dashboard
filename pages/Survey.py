# This creates the page for users to input data.
# The collected data should be appended to the 'data.csv' file.

import streamlit as st
import pandas as pd
import os # The 'os' module is used for file system operations (e.g. checking if a file exists).
import csv

# PAGE CONFIGURATION
st.set_page_config(
    page_title="Chipotle Survey",
    page_icon="📝",
)

# PAGE TITLE AND USER DIRECTIONS
st.title("Chipotle Preference Survey 🌯")
st.write("""
What's your favorite Chipotle protein?

Fill out the survey below to share your preferences!
""")

# DATA INPUT FORM
# 'st.form' creates a container that groups input widgets.
# The form is submitted only when the user clicks the 'st.form_submit_button'.
# This is useful for preventing the app from re-running every time a widget is changed.
with st.form("survey_form"):
    # Create text input widgets for the user to enter data.
    # The first argument is the label that appears above the input box.
    category_input = st.text_input("What's your favorite Chipotle protein?")
    value_input = st.text_input("How would you rate it from 1 to 10?")

    # The submit button for the form.
    submitted = st.form_submit_button("Submit Data")

    # This block of code runs ONLY when the submit button is clicked.
    if submitted:
        if category_input.strip() == "" or value_input.strip() == "":
            st.error("Please answer both questions.")
        else:
            try:
                rating = float(value_input)
                if 1 <= rating <= 10:
                    with open("data.csv", "a", newline="") as file:
                        writer = csv.writer(file)
                        writer.writerow([category_input, rating])

                    st.success("Your data has been submitted!")
                    st.write(
                        f"You chose {category_input} and rated it {rating}/10!"
                    )
                else:
                    st.error("Please enter a rating from 1 to 10.")
            except ValueError:
                st.error("Please enter a valid number.")



# DATA DISPLAY
# This section shows the current contents of the CSV file, which helps in debugging.
st.divider() # Adds a horizontal line for visual separation.
st.header("Current Survey Responses")

# Check if the CSV file exists and is not empty before trying to read it.
if os.path.exists('data.csv') and os.path.getsize('data.csv') > 0:
    # Read the CSV file into a pandas DataFrame.
    current_data_df = pd.read_csv('data.csv')
    # Display the DataFrame as a table.
    st.dataframe(current_data_df)
else:
    st.warning("No survey data available yet.")
