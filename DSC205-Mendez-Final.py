import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import streamlit as st

url = "https://raw.githubusercontent.com/iantonios/dsc205/refs/heads/main/bike_sharing.csv"
#read Url
data = pd.read_csv(url)

# Ensure the 'dteday' column is a datetime type
data['dteday'] = pd.to_datetime(data['dteday'])

# Line plot of total ridership over time
st.header("Total Ridership Over Time")
plt.figure(figsize=(10, 5))
plt.plot(data['dteday'], data['cnt'], label='Total Ridership', color='red')
plt.xlabel("Date")
plt.ylabel("Total Ridership")
plt.title("Total Ridership Over Time")
plt.legend()
st.pyplot(plt)
#END OF PART 1
st.markdown("---")

# Bar plot of total ridership by season
st.header("Total Ridership by Season")
season_labels = {1: 'Winter', 2: 'Spring', 3: 'Summer', 4: 'Fall'} #differnt seasons bars
data['season_label'] = data['season'].map(season_labels)
season_totals = data.groupby('season_label')['cnt'].sum().reset_index()

plt.figure(figsize=(8, 5))
sns.barplot(x='season_label', y='cnt', data=season_totals, palette='plasma')
plt.xlabel("Season")
plt.ylabel("Total Ridership")
plt.title("Total Ridership by Season")
st.pyplot(plt)
#END OF PART 2
st.markdown("---")

st.header("Total Ridership with Rolling Average")

# Use radio button to select rolling average window
rolling_option = st.radio("Select Rolling Average:", ["7-day Average", "14-day Average"])

# Determine the rolling window based on user selection
if rolling_option == "7-day Average":
    rolling_window = 7
elif rolling_option == "14-day Average":
    rolling_window = 14


# Calculate the rolling average
data['rolling_avg'] = data['cnt'].rolling(window=rolling_window).mean()

# Plot the total ridership and rolling average
plt.figure(figsize=(12, 6))
plt.plot(data['dteday'], data['cnt'], label='Total Ridership', color='blue', alpha=0.5)
plt.plot(data['dteday'], data['rolling_avg'], label=f'{rolling_window}-day Rolling Average', color='red')
plt.xlabel("Date")
plt.ylabel("Total Ridership")
plt.title(f"Total Ridership with {rolling_window}-day Rolling Average")
plt.legend()
st.pyplot(plt)






