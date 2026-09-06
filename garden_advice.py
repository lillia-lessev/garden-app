# Hardcoded values for the season and plant type
season = input(str("Input season: "))
plant_type = input(str("Input flower: "))

# Variable to hold gardening advice
advice = {
    "summer": "Water your plants regularly and provide some shade.\n",
    "winter": "Protect your plants from frost with covers.\n",
    "other_season": "No advice for this season.\n",
    "flower": "Use fertiliser to encourage blooms.\n",
    "vegetable": "Keep an eye out for pests!\n",
    "other_season": "No advice for this type of plant."
}

advice_str = ""

# Determine advice based on the season
if season == "summer" or season == "winter":
    advice_str += advice[season]
else:
    advice_str += advice["other_season"]

# Determine advice based on the plant type
if plant_type == "flower" or plant_type == "vegetable":
    advice_str += advice[plant_type]
else:
    advice_str += advice["other_season"]


# Print the generated advice
print(advice_str)

# TODO: Examples of possible features to add:
# - Add detailed comments explaining each block of code.
# - Refactor the code into functions for better readability and modularity.
# - Store advice in a dictionary for multiple plants and seasons.
# - Recommend plants based on the entered season.
