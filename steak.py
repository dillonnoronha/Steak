# Define a dictionary of steak cuts and their corresponding protein content
steak_cuts = {
    "tenderloin": 12,
    "ribeye": 17,
    "sirloin": 21,
    "porterhouse": 29,
    "t-bone": 26
}

# Define a dictionary of steak cuts and their recommended cooking methods
cooking_methods = {
    "tenderloin": "pan-seared",
    "ribeye": "grilled",
    "sirloin": "pan-seared",
    "porterhouse": "grilled",
    "t-bone": "grilled"
}

# Define a variable to keep track of the total protein intake
total_protein = 0

# Iterate over the steak cuts and print their information
for cut, protein in steak_cuts.items():
    print(f"The {cut} steak has {protein} grams of protein.")
    print(f"It is recommended to cook the {cut} steak using the {cooking_methods[cut]} method.")
    # Prompt the user for their preferred cooking method for the current steak cut
    user_method = input(f"How would you like your {cut} steak cooked? ")
    # Update the total protein intake based on the user's selection
    if user_method == cooking_methods[cut]:
        total_protein += protein

# Print the total protein intake
print(f"Based on your selections, you will consume a total of {total_protein} grams of protein.")
