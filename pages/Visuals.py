# This creates the page for displaying data visualizations.

import streamlit as st
import json
import pandas as pd
import matplotlib.pyplot as plt


# PAGE CONFIGURATION
st.set_page_config(
    page_title="Visuals",
    page_icon="📈",
)

# PAGE TITLE
st.title("Chipotle Ingredient Visualizations 🌯")
st.write("Explore example ingredient preference scores!")

# PART 1: GRAPHS FROM data.json
infile = open("data.json", "r")
data = json.load(infile)
infile.close()

ingredients = data["data_points"]

names = []
scores = []
for ingredient in ingredients:
    names.append(ingredient["label"])
    scores.append(ingredient["value"])

# GRAPH 1: Static Bar CHart
st.header("1. Ingredient Preference Scores")
chart_data = pd.DataFrame({
    "Ingredient": names,
    "Preference Score": scores
})
st.bar_chart(
    chart_data,
    x="Ingredient",
    y="Preference Score"
)
st.write("This chart compares the example preference scores for six Chipotle ingredients.")

# GRAPH 2: Dynamic Pie Chart
st.header("2. Interactive Ingredient Breakdown")

st.write("Use the slider to choose how many ingredients to compare.")

st.slider(
    "How many ingredients do you want to compare?",
    min_value=2,
    max_value=len(names),
    value=4,
    key="ingredient_count"
)
count = st.session_state.ingredient_count
selected_names = names[:count]
selected_scores = scores[:count]

fig, ax = plt.subplots()
ax.pie(
    selected_scores,
    labels=selected_names,
    autopct="%1.1f%%"
)

ax.set_title("Chipotle Ingredient Preference Breakdown")

st.pyplot(fig)
plt.close(fig)


## PART 2: GRAPHS FROM data.csv
# Graph 3
st.divider()
st.header("Part 2: Chipotle Survey Results 🌯")

survey_data = pd.read_csv("data.csv")

survey_data["Value"] = pd.to_numeric(
    survey_data["Value"],
    errors="coerce"
)

survey_data = survey_data.dropna(subset=["Value"])


if not survey_data.empty:
    # GRAPH 3: Static Bar Chart
    st.subheader("3. Average Protein Ratings")
    averages = survey_data.groupby("Category")["Value"].mean()
    st.bar_chart(averages)
    st.write("This chart shows the average rating for each Chipotle protein.")


    # GRAPH 4: Dynamic Pie Chart
    st.subheader("4. Interactive Favorite Protein Breakdown")
    st.write("Use the slider to choose how many proteins to compare.")

    
    protein_counts = survey_data["Category"].value_counts()

    st.slider(
        "How many proteins do you want to compare?",
        min_value=1,
        max_value=len(protein_counts),
        value=min(3, len(protein_counts)),
        key="protein_count"
    )

    count = st.session_state.protein_count

    selected_proteins = protein_counts.index[:count]
    selected_counts = protein_counts.values[:count]

    fig2, ax2 = plt.subplots()

    ax2.pie(
        selected_counts,
        labels=selected_proteins,
        autopct="%1.1f%%"
    )

    ax2.set_title("Favorite Chipotle Proteins")

    st.pyplot(fig2)
    plt.close(fig2)

else:
    st.warning("No valid survey responses to graph yet.")
