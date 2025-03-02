import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

# Load the matches DataFrame (assuming it's already saved as a CSV)
matches_df = pd.read_csv('MatchUserWithDog.csv')

# Pivot the DataFrame to create a matrix for the heatmap
heatmap_data = matches_df.pivot(index='user_id', columns='dog_id', values='match_percentage')

# Set the size of the heatmap
plt.figure(figsize=(12, 8))

# Create the heatmap
sns.heatmap(heatmap_data, annot=False, fmt=".1f", cmap='viridis', cbar_kws={'label': 'Match Percentage'})

# Add title and labels
plt.title('Heatmap of Match Percentages for Users and Dogs', fontsize=16, pad= 20)
plt.xlabel('Dog ID', fontsize=12, labelpad=15)
plt.ylabel('User ID', fontsize=12, labelpad=15)

# Show the plot
plt.tight_layout()
plt.show()

