import streamlit as st
import pandas as pd

# Simulated data using pandas (make sure you have enough universities for each major)
data = {
    'Major': ['Computer Science', 'Electrical Engineering', 'Mechanical Engineering', 
              'Civil Engineering', 'Chemical Engineering', 'Physics', 'Mathematics',
              'Biology', 'Chemistry', 'Economics', 'Psychology', 'Sociology',
              'Political Science', 'Philosophy', 'History', 'English', 'Art',
              'Music', 'Business', 'Finance'],
    'University': ['MIT', 'Stanford', 'Harvard', 'UC Berkeley', 'Caltech', 'Princeton', 
                   'Yale', 'Columbia', 'Cornell', 'University of Chicago', 
                   'UCLA', 'University of Michigan', 'Duke', 'UPenn', 'Brown',
                   'Dartmouth', 'University of Toronto', 'Johns Hopkins', 'Northwestern', 'NYU'],
    'Rank': [1, 2, 3, 4, 5, 6, 7, 8, 9, 10] * 2  # Make sure the ranking pattern fits
}

# Load the simulated data into a Pandas DataFrame
df = pd.DataFrame(data)

# Streamlit app setup
st.title("University Rankings App")
st.write("Select your major to see the top universities!")

# Step 1: Input user's name
name = st.text_input("Enter your name", "")

# Step 2: Display the available majors in a dropdown
majors = df['Major'].unique()  # Get a unique list of all majors in the dataset
selected_major = st.selectbox("Select your major", majors)

# Step 3: Check if the user entered their name and selected a major
if name and selected_major:
    # Filter the data for the selected major
    major_data = df[df['Major'] == selected_major].sort_values(by='Rank').head(10)

    # Step 4: Display a greeting message
    st.write(f"Hello {name}, here is the top university for {selected_major}:")

    # Step 5: Display the results in a table format
    st.table(major_data[['Rank', 'University']])

# Optional: If the user hasn't entered their name yet
else:
    st.write("Please enter your name and select a major to see the rankings.")
