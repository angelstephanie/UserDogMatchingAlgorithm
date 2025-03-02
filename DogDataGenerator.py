import pandas as pd
import random
from faker import Faker

# Initialize Faker to generate fake data
fake = Faker()

# Define options for user to pick from
locations = ['Islands','Kwai Tsing','North', 'Sai Kung','Sha Tin','Tai Po', 'Tsuen Wan',
             'Tuen Mun','Yuen Long', 'Kowloon City','Kwun Tong','Sham Shui Po','Wong Tai Sin', 
             'Yau Tsim Mong','Central and Western', 'Eastern','Southern','Wan Chai' ]
dog_characteristics =['Calm', 'Gentle','Friendly','Loyal','Well-trained','Energetic','Affectionate','Independent','Playful']
dog_names = ["Buddy", "Max", "Charlie", "Bella", "Lucy", "Daisy", "Rocky", "Molly", "Bailey", "Sadie", "Cooper", 
             "Toby", "Roxy", "Duke", "Zoe", "Chester", "Lola", "Oscar", "Winston", "Coco"]
dog_breed = ["Mixed Breed", "Labrador Retriever", "Shih Tzu", "Poodle", "Chihuahua", "French Bulldog", "Golden Retriever", 
             "Pug", "Beagle", "Siberian Husky", "Maltese", "Border Collie", "Cavalier King Charles Spaniel", "Shetland Sheepdog", 
             "Corgi", "Akita", "Dalmatian", "Bichon Frise", "Shiba Inu"]

# Generate 20 random individuals with age, gender, and emotional issues
data = []
for _ in range(1,41):
    id = _
    name = fake.random_element(elements=dog_names)
    age = random.randint(0, 18)
    gender = fake.random_element(elements=('Male', 'Female'))
    location = fake.random_element(elements=locations)
    characteristic = fake.random_elements(elements=dog_characteristics, length=random.randint(0,4), unique=True)
    breed = fake.random_element(elements=dog_breed)
    data.append({'dog_id': id, 'dog_name': name, 'dog_age': age, 'dog_gender': gender, 'dog_location': location, 'dog_breed': breed, 'dog_characteristics': characteristic})

# Create a DataFrame using pandas
df = pd.DataFrame(data)

# Write the DataFrame to a CSV file
df.to_csv('DogData.csv', index=False)

print("CSV file with random dogs created using pandas successfully.")