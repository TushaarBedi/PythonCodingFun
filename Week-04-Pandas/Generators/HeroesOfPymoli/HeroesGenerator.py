# Environment Setup
# ----------------------------------------------------------------
# Dependencies
import csv
import pandas as pd
import random
import numpy as np

# Output File Name
file_output_players = "generated_data/players_complete.csv"
file_output_items = "generated_data/items_complete.csv"
file_output_purchases_json = "generated_data/purchase_data_3.json"
file_output_purchases_csv = "generated_data/purchase_data_3.csv"

# Convert the Players List to a Data Frame
players = pd.read_csv("raw_data/players.csv", dtype="str", header=0)
total_players = len(players)

items = pd.read_table("raw_data/items.txt", delimiter="\t", dtype="str")
total_items = len(items)

# Generator Conditions (Change as Needed)
# ----------------------------------------------------------------

# Population Counts
total_purchase_count = 78
player_count = len(players) - 27
item_count = len(items) - 6

# Player Weight
genders = ["Male", "Female", "Other / Non-Disclosed"]
gender_weights = [0.82, 0.16, 0.02]

age_ranges = [7, 15, 20, 25, 30, 35, 40, 45]
age_weights = [0.01, 0.09, 0.20, 0.46, 0.10, 0.08, 0.05, 0.01]

# Item Prices
low_price = 1
high_price = 5

# Generate Players
# ----------------------------------------------------------------

# Generate all gender probabilities
gender_probabilities = zip(genders, gender_weights)
gender_profiles = []

# Generate a sufficient number of genders
for gender in gender_probabilities:
    gender_profiles = gender_profiles + \
        [gender[0]] * int(gender[1] * total_players)

# Generate random ages
age_probabilities = zip(age_ranges, age_weights)
age_counts = []
age_profiles = []

for age in age_probabilities:
    age_counts = age_counts + [int(age[1] * total_players)]

age_probabilities = zip(age_counts, age_ranges)

# Generate right number of random numbers
prev_age = age_ranges[0]

for age in age_probabilities:
    for x in range(age[0]):
        age_profiles = age_profiles + [random.randint(prev_age, age[1])]
    prev_age = age[1]

random.shuffle(gender_profiles)
random.shuffle(age_profiles)

# Convert lists into pandas data frames
gender_profiles_pd = pd.Series(gender_profiles)
age_profiles_pd = pd.Series(age_profiles)

# Combine the data frames to match the number of players
players = players[0:player_count]
gender_profiles_pd = gender_profiles_pd[0:player_count]
age_profiles_pd = age_profiles_pd[0:player_count]

# Combine all datasets
players["Age"] = age_profiles_pd.values
players["Gender"] = gender_profiles_pd.values

# Export as JSON
# players.to_json(file_output_players, orient="records")
players.to_csv(file_output_players, index_label="Player ID")

# Generate the Item Data
# ----------------------------------------------------------------
items["Price"] = np.random.uniform(low_price, high_price, items.shape[0])
items = items.round({"Price": 2})

# Export the Items to a CSV
items.to_csv(file_output_items, index_label="Item ID")

# Generate the Purchases
# ----------------------------------------------------------------
# Setup the purchases data frame
index = ["Purchase ID"]
columns = ["SN", "Item ID", "Item Name", "Item Price"]
purchases = pd.DataFrame(index=index, columns=columns)

purchased_items = []
for x in range(total_purchase_count):

    print("Now Rendering: %s of %s records..." % (x, total_purchase_count))

    rand_player = np.random.randint(0, player_count)
    rand_item = np.random.randint(0, item_count)

    selected_user = players.iloc[rand_player]["SN"]
    selected_user_age = players.iloc[rand_player]["Age"]
    selected_user_gender = players.iloc[rand_player]["Gender"]
    selected_item_id = rand_item
    selected_item_name = items.iloc[rand_item]["Item Name"]
    selected_item_price = items.iloc[rand_item]["Price"]

    purchased_items = purchased_items + list(zip([selected_user],
                                                 [selected_user_age],
                                                 [selected_user_gender],
                                                 [selected_item_id],
                                                 [selected_item_name],
                                                 [selected_item_price]))


purchased_items_pd = pd.DataFrame(purchased_items, columns=["SN",
                                                            "Age",
                                                            "Gender",
                                                            "Item ID",
                                                            "Item Name",
                                                            "Price"])

# Export the Purchase List as CSVs and JSONs
purchased_items_pd.to_csv(file_output_purchases_csv, index_label="Purchase ID")
purchased_items_pd.to_json(file_output_purchases_json, orient="records")
