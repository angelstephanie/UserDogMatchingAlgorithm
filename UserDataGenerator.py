import pandas as pd
import random
from faker import Faker

# Initialize Faker to generate fake data
fake = Faker()

# Define options for user to pick from
locations = ['Islands','Kwai Tsing','North', 'Sai Kung','Sha Tin','Tai Po', 'Tsuen Wan',
             'Tuen Mun','Yuen Long', 'Kowloon City','Kwun Tong','Sham Shui Po','Wong Tai Sin', 
             'Yau Tsim Mong','Central and Western', 'Eastern','Southern','Wan Chai' ]
dog_characteristics = ['Calm', 'Gentle','Friendly','Loyal','Well-trained','Energetic','Affectionate','Independent','Playful']
dog_breed = ["Mixed Breed", "Labrador Retriever", "Shih Tzu", "Poodle", "Chihuahua", "French Bulldog", "Golden Retriever", 
             "Pug", "Beagle", "Siberian Husky", "Maltese", "Border Collie", "Cavalier King Charles Spaniel", "Shetland Sheepdog", 
             "Corgi", "Akita", "Dalmatian", "Bichon Frise", "Shiba Inu"]

# Generate 20 random individuals with age, gender, and emotional issues
data = []
for _ in range(1,21):
    id = _
    name = fake.name()
    age = random.randint(18, 50)
    gender = fake.random_element(elements=('Male', 'Female'))
    location = fake.random_element(elements=locations)
    preferred_characteristic = fake.random_elements(elements=dog_characteristics, length=random.randint(0,4), unique=True)
    preferred_breed = fake.random_elements(elements=dog_breed, length=random.randint(0,4), unique=True)
    data.append({'user_id': id, 'user_name': name,'user_age': age, 'user_gender': gender, 'user_location':location, 
                 'user_preferred_dog_breed': preferred_breed, 'user_preferred_dog_characteristics': preferred_characteristic})

# Create a DataFrame using pandas
df = pd.DataFrame(data)

# Write the DataFrame to a CSV file
df.to_csv('UserData.csv', index=False)

print("CSV file with random individuals created using pandas successfully.")