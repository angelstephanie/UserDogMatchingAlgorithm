import pandas as pd
import json
import ast
from itertools import product

# Convert to DataFrames
user_df = pd.read_csv("UserData.csv")
dog_df = pd.read_csv("DogData.csv")

# Define weight factors
WEIGHT_BREED = 0.2
WEIGHT_CHARACTERISTICS = 0.3
WEIGHT_LOCATION = 0.5

# Compute matches
matches = []

for user, dog in product(user_df.itertuples(index=False), dog_df.itertuples(index=False)):
    # Calculate Match Breed
    breed_match = 100 if dog.dog_breed in ast.literal_eval(user.user_preferred_dog_breed) else 0

    # Calculate characteristics match percentage
    common_characteristics = set(ast.literal_eval(user.user_preferred_dog_characteristics)) & set(ast.literal_eval(dog.dog_characteristics))
    char_match = (len(common_characteristics) / len(user.user_preferred_dog_characteristics)) * 100 if user.user_preferred_dog_characteristics else 0

    # Location match
    location_match = 100 if dog.dog_location in user.user_location else 0

    # Weighted score
    final_score = (breed_match * WEIGHT_BREED) + (char_match * WEIGHT_CHARACTERISTICS) + (location_match * WEIGHT_LOCATION)
    
    matches.append([user.user_id, dog.dog_id, final_score])

print(matches[0])
# Convert matches to DataFrame and sort
matches_df = pd.DataFrame(matches, columns=['user_id', 'dog_id', 'match_percentage'])
matches_df = matches_df.sort_values(by=['user_id', 'match_percentage', 'dog_id'], ascending=[True, False, False])

# Display results
print(matches_df)

# Save to CSV
matches_df.to_csv('MatchUserWithDog.csv', index=False)



