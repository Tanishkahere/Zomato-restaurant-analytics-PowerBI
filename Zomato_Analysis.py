# %% [markdown]
# # 🍽️ Zomato Restaurant Data Analysis
# 
# ## 📌 Project Overview
# 
# This project analyzes Zomato restaurant data from across India to identify trends in restaurant distribution, cuisines, pricing, ratings, and customer preferences. The objective is to derive meaningful business insights using Python, Pandas, Matplotlib, and Power BI.
# 
# ## 🎯 Objectives
# 
# - Analyze restaurant distribution across cities
# - Identify the most popular cuisines
# - Study restaurant ratings
# - Analyze pricing trends
# - Compare ratings with pricing
# - Evaluate delivery services
# - Generate business recommendations
# 
# ## 🛠️ Tools & Technologies
# 
# - Python
# - Pandas
# - NumPy
# - Matplotlib
# - Jupyter Notebook
# - Power BI
# - Git & GitHub
# 
# ## 📂 Dataset
# 
# Source: Kaggle - Zomato Restaurants in India Dataset

# %%
import pandas as pd
import numpy as np

# %%
import os

os.listdir("../data")

# %%
import os
print(os.getcwd())



# %%
import os

print(os.listdir())

# %%
print(os.listdir("../"))

# %%
import os

print(os.listdir("../data"))

# %%
import os
print(os.listdir("../data"))

# %%
df = pd.read_csv("../data/zomato_raw.csv")

# %%
df.head()

# %%
df.shape

# %%
df.columns

# %%
df.info()

# %%
df.isnull().sum()

# %%
df.duplicated().sum()

# %%
df[df.duplicated()].head()

# %%
print("Total rows:", len(df))
print("Duplicate rows:", df.duplicated().sum())

# %%
df[df.duplicated()].head(10)

# %%
df.nunique()

# %%
df["res_id"].value_counts().head(10)

# %%
df["res_id"].value_counts().head(10)

# %%
df_unique = df.drop_duplicates(subset="res_id", keep="first")

print("Original rows:", len(df))
print("Rows after removing duplicate restaurant IDs:", len(df_unique))
print("Unique restaurant IDs:", df["res_id"].nunique())

# %%
df[df["res_id"] == 18631911]

# %%
df = df.drop_duplicates(subset="res_id", keep="first")

# %%
print(df.shape)

# %%
df.to_csv("../data/zomato_cleaned.csv", index=False)

# %%
city_counts = df["city"].value_counts()

city_counts.head(10)

# %%
import matplotlib.pyplot as plt

top10_cities = df["city"].value_counts().head(10)

plt.figure(figsize=(10,6))
plt.bar(top10_cities.index, top10_cities.values)

plt.title("Top 10 Cities by Number of Restaurants")
plt.xlabel("City")
plt.ylabel("Number of Restaurants")

plt.xticks(rotation=45)

plt.show()

# %% [markdown]
# ## Analysis 1: Top 10 Cities by Number of Restaurants
# 
# ### Business Question
# Which cities have the highest number of restaurants listed on Zomato?
# 
# ### Observation
# - Bangalore has the highest number of restaurants.
# - Mumbai ranks second.
# - Pune and Chennai also have a strong restaurant presence.
# - New Delhi is among the top five cities.
# 
# ### Business Insight
# The restaurant market is highly concentrated in metropolitan cities. Businesses planning to expand through Zomato can prioritize these cities due to their large customer base and high restaurant density.

# %%
df["cuisines"].head()

# %%
all_cuisines = (
    df["cuisines"]
    .dropna()
    .str.split(", ")
    .explode()
)

all_cuisines.head(10)

# %%
top_cuisines = all_cuisines.value_counts().head(15)

top_cuisines

# %%
all_cuisines.value_counts()

# %%
import matplotlib.pyplot as plt

plt.figure(figsize=(12,6))

bars = plt.bar(top_cuisines.index, top_cuisines.values)

plt.title("Top 15 Most Popular Cuisines", fontsize=18, fontweight='bold')
plt.xlabel("Cuisine", fontsize=13)
plt.ylabel("Number of Restaurants", fontsize=13)

plt.xticks(rotation=45)

plt.grid(axis="y", linestyle="--", alpha=0.5)

for bar in bars:
    plt.text(
        bar.get_x() + bar.get_width()/2,
        bar.get_height() + 50,
        int(bar.get_height()),
        ha="center",
        fontsize=9
    )

plt.tight_layout()
plt.show()

# %% [markdown]
# ## Analysis 2: Most Popular Cuisines
# 
# ### Business Question
# Which cuisines are served by the highest number of restaurants on Zomato?
# 
# ### Observation
# - North Indian cuisine is served by the largest number of restaurants.
# - Chinese cuisine is also highly popular across cities.
# - Fast Food, Cafe, South Indian, and Continental are among the most common cuisines.
# 
# ### Business Insight
# Restaurants serving popular cuisines have a larger market presence. Businesses planning to open new restaurants should consider offering high-demand cuisines or combining popular cuisine categories to attract more customers.

# %%
import matplotlib.pyplot as plt

plt.figure(figsize=(10,6))

plt.hist(df["aggregate_rating"], bins=20)

plt.title("Distribution of Restaurant Ratings", fontsize=18, fontweight="bold")
plt.xlabel("Rating", fontsize=13)
plt.ylabel("Number of Restaurants", fontsize=13)

plt.grid(axis="y", linestyle="--", alpha=0.5)

plt.show()

# %% [markdown]
# import matplotlib.pyplot as plt
# 
# plt.figure(figsize=(10,6))
# 
# plt.hist(df["aggregate_rating"], bins=20)
# 
# plt.title("Distribution of Restaurant Ratings", fontsize=18, fontweight="bold")
# plt.xlabel("Rating", fontsize=13)
# plt.ylabel("Number of Restaurants", fontsize=13)
# 
# plt.grid(axis="y", linestyle="--", alpha=0.5)
# 
# plt.show()

# %%
plt.figure(figsize=(10,6))

plt.hist(df["average_cost_for_two"], bins=30)

plt.title("Distribution of Average Cost for Two", fontsize=18, fontweight="bold")
plt.xlabel("Average Cost for Two (₹)", fontsize=13)
plt.ylabel("Number of Restaurants", fontsize=13)

plt.grid(axis="y", linestyle="--", alpha=0.5)

plt.show()

# %%
plt.figure(figsize=(10,6))

plt.scatter(
    df["average_cost_for_two"],
    df["aggregate_rating"],
    alpha=0.3
)

plt.title("Average Cost for Two vs Aggregate Rating", fontsize=18, fontweight="bold")
plt.xlabel("Average Cost for Two (₹)", fontsize=13)
plt.ylabel("Aggregate Rating", fontsize=13)

plt.grid(alpha=0.4)

plt.show()

# %% [markdown]
# ## Analysis 5: Rating vs Average Cost
# 
# ### Business Question
# Is there a relationship between restaurant pricing and customer ratings?
# 
# ### Observation
# - Each point represents one restaurant.
# - Most restaurants are concentrated in the lower to mid-price range.
# - Higher-priced restaurants do not always receive higher ratings.
# 
# ### Business Insight
# Restaurant quality, as reflected by customer ratings, is not solely determined by pricing. Budget-friendly restaurants can achieve ratings comparable to premium restaurants by focusing on food quality and customer experience.

# %%
df["delivery"].value_counts()

# %%
delivery_df = df[df["delivery"] != 0]

# %%
delivery_rating = delivery_df.groupby("delivery")["aggregate_rating"].mean()

delivery_rating

# %%
plt.figure(figsize=(6,5))

delivery_rating.plot(kind="bar")

plt.title("Average Rating by Delivery Availability", fontsize=16, fontweight="bold")
plt.xlabel("Delivery")
plt.ylabel("Average Rating")

plt.xticks([0, 1], ["No Delivery", "Delivery"], rotation=0)

plt.grid(axis="y", linestyle="--", alpha=0.5)

plt.show()

# %% [markdown]
# ## Analysis 6: Delivery vs Rating
# 
# ### Business Question
# Do restaurants offering delivery receive higher customer ratings?
# 
# ### Observation
# - The chart compares the average ratings of restaurants with and without delivery.
# - The difference in ratings indicates whether delivery service has an association with customer satisfaction.
# 
# ### Business Insight
# Offering delivery alone does not guarantee higher customer ratings. Restaurant quality, food consistency, and service remain the primary factors influencing customer satisfaction.

# %%
import seaborn as sns

# %%
city_cost = (
    df.groupby("city")["average_cost_for_two"]
    .mean()
    .sort_values(ascending=False)
    .head(10)
)

city_cost

# %%
plt.figure(figsize=(12,6))

sns.barplot(
    x=city_cost.index,
    y=city_cost.values
)

plt.title("Top 10 Cities by Average Cost for Two", fontsize=18, fontweight="bold")
plt.xlabel("City", fontsize=13)
plt.ylabel("Average Cost for Two (₹)", fontsize=13)

plt.xticks(rotation=45)

plt.tight_layout()
plt.show()

# %% [markdown]
# ## Analysis 7: City-wise Average Cost
# 
# ### Business Question
# Which cities have the highest average dining cost for two people?
# 
# ### Observation
# - The chart shows the top 10 cities with the highest average dining cost.
# - Some metropolitan and tourist cities have significantly higher restaurant prices than others.
# 
# ### Business Insight
# Restaurant pricing varies across cities due to differences in customer spending power, tourism, and local market conditions. Businesses should adopt city-specific pricing strategies instead of using a uniform pricing model nationwide.

# %%
df["establishment"].head()

# %%
df["establishment"].value_counts()

# %%
df["establishment"].iloc[0]

# %%
print(df["establishment"].iloc[0])

# %%
df[["name", "establishment"]].head(10)

# %%
df.loc[0]

# %%
df = pd.read_csv("../data/zomato_raw.csv")

# %%
df = df.drop_duplicates(subset="res_id", keep="first")

# %%
df["establishment"].head()

# %%
df["establishment"] = (
    df["establishment"]
    .str.strip("[]")
    .str.replace("'", "", regex=False)
)

# %%
df["establishment"].head()

# %%
df["establishment"].head()

# %%
top_establishments = df["establishment"].value_counts().head(10)

top_establishments

# %%
plt.figure(figsize=(12,6))

sns.barplot(
    x=top_establishments.values,
    y=top_establishments.index,
    hue=top_establishments.index,
    palette="viridis",
    legend=False
)

plt.title("Top 10 Restaurant Types on Zomato", fontsize=18, fontweight="bold")
plt.xlabel("Number of Restaurants", fontsize=13)
plt.ylabel("Restaurant Type", fontsize=13)

plt.tight_layout()
plt.show()

# %% [markdown]
# ## Analysis 8: Restaurant Type Analysis
# 
# ### Business Question
# Which restaurant types dominate the Zomato platform?
# 
# ### Why this analysis?
# Understanding the distribution of restaurant types helps identify the most common business models in the food industry.
# 
# ### Observation
# - Quick Bites and Casual Dining dominate the platform.
# - Cafés and Bakeries also have a significant presence.
# - Premium restaurant formats are comparatively fewer.
# 
# ### Business Insight
# Most restaurants listed on Zomato belong to affordable and high-volume categories. Entrepreneurs entering the market may find greater demand in these segments, while premium dining targets a more niche customer base.

# %%
df[["votes", "aggregate_rating"]].head()

# %%
plt.figure(figsize=(10,6))

sns.scatterplot(
    data=df,
    x="votes",
    y="aggregate_rating",
    alpha=0.4
)

plt.title("Votes vs Aggregate Rating", fontsize=18, fontweight="bold")
plt.xlabel("Number of Votes", fontsize=13)
plt.ylabel("Aggregate Rating", fontsize=13)

plt.tight_layout()
plt.show()

# %%
correlation = df["votes"].corr(df["aggregate_rating"])

print("Correlation:", round(correlation, 2))

# %% [markdown]
# ## Analysis 9: Votes vs Rating
# 
# ### Business Question
# Do restaurants with more customer votes tend to have higher ratings?
# 
# ### Why this analysis?
# Customer votes represent popularity, while ratings represent satisfaction. Comparing them helps understand whether popular restaurants are also highly appreciated.
# 
# ### Observation
# - Restaurants with a large number of votes generally maintain good ratings.
# - Many restaurants with few votes have ratings spread across a wider range.
# - A few restaurants receive exceptionally high numbers of votes, acting as outliers.
# 
# ### Business Insight
# Popularity and customer satisfaction are positively related, but they are not the same. Restaurants can achieve high ratings with fewer votes, while highly popular restaurants often sustain good ratings through consistent service and quality.

# %%
numeric_df = df[
    [
        "average_cost_for_two",
        "price_range",
        "aggregate_rating",
        "votes",
        "photo_count"
    ]
]

# %%
corr_matrix = numeric_df.corr()

corr_matrix

# %%
plt.figure(figsize=(8,6))

sns.heatmap(
    corr_matrix,
    annot=True,
    cmap="coolwarm",
    fmt=".2f"
)

plt.title("Correlation Heatmap", fontsize=18, fontweight="bold")

plt.show()

# %% [markdown]
# ## Analysis 10: Correlation Heatmap
# 
# ### Business Question
# How are the important numerical variables related to one another?
# 
# ### Why this analysis?
# A correlation heatmap provides an overview of relationships between multiple numerical variables at the same time.
# 
# ### Observation
# - Price Range and Average Cost for Two show a strong positive correlation.
# - Votes and Photo Count are positively related, indicating that popular restaurants often have more customer photos.
# - Aggregate Rating has only a moderate relationship with other variables.
# 
# ### Business Insight
# Restaurant popularity depends on multiple factors. Pricing influences cost-related metrics, while customer engagement (votes and photos) tends to move together. Ratings alone do not fully explain a restaurant's popularity.

# %%
df_clean = df.copy()

# %%
df_clean.columns

# %%
columns_to_drop = [
    "url",
    "address",
    "latitude",
    "longitude",
    "zipcode",
    "city_id",
    "country_id",
    "locality_verbose",
    "timings",
    "highlights",
    "opentable_support"
]

df_clean.drop(columns=columns_to_drop, inplace=True)

# %%
df_clean.head()

# %%
df_clean.columns

# %%
df_clean.isnull().sum()

# %%
df_clean["cuisines"] = df_clean["cuisines"].fillna("Unknown")
df_clean["rating_text"] = df_clean["rating_text"].fillna("Not Rated")

# %%
df_clean.isnull().sum()

# %%
df_clean.info()

# %%
df_clean.to_csv("../data/zomato_cleaned.csv", index=False)

# %%
import os

os.listdir("../data")

# %% [markdown]
# # Final Cleaned Dataset
# 
# ## Cleaning Performed
# 
# - Removed duplicate restaurants using `res_id`
# - Handled missing values in important columns
# - Removed unnecessary columns such as URL, Address, Latitude, Longitude, Zipcode, etc.
# - Prepared a clean dataset for dashboard creation in Power BI
# 
# ## Final Dataset
# 
# The cleaned dataset is exported as **zomato_cleaned.csv** and will be used for interactive dashboard development.


