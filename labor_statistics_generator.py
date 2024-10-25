import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
import os  # Import os module for file operations

# 1. Create output directory if it doesn't exist
output_dir = 'output'
os.makedirs(output_dir, exist_ok=True)  # Create the directory if it doesn't exist

# 2. Create manual data using pandas
names = ['Ahmed', 'Maryam', 'Saeed', 'Khalid', 'Mona']
cities = ['Cairo', 'Dubai', 'Riyadh', 'Beirut', 'Amman']
ages = [25, 30, 22, 35, 28]

# Create DataFrame using pandas
df_manual = pd.DataFrame({
    'Name': names,
    'Age': ages,
    'City': cities
})

# 3. Generate random salary data using numpy
salaries = np.random.randint(3000, 10000, size=5)
df_manual['Salary'] = salaries

# 4. Generate random work hours data using numpy
work_hours = np.random.randint(160, 200, size=5)
df_manual['Work Hours'] = work_hours

# 5. Save the data to CSV and Excel files
csv_file_path = os.path.join(output_dir, 'generated_data.csv')
excel_file_path = os.path.join(output_dir, 'generated_data.xlsx')

df_manual.to_csv(csv_file_path, index=False)
df_manual.to_excel(excel_file_path, index=False)

print(f"\nData saved to '{csv_file_path}' and '{excel_file_path}'.")

# 6. Display basic statistics for the data
stats = df_manual.describe()

# 7. Save statistics to a text file
stats_file_path = os.path.join(output_dir, 'data_statistics.txt')
with open(stats_file_path, 'w') as f:
    f.write("General statistics of the data:\n")
    f.write(str(stats))

print(f"\nStatistics saved to '{stats_file_path}'.")

# 8. Detailed plot for each worker with their details

# Using a color palette for better aesthetics
colors = sns.color_palette("husl", len(df_manual))  # Generate a color palette

plt.figure(figsize=(10, 6))  # Setting figure size

# Bar chart for work hours with improved aesthetics
bars = plt.bar(df_manual['Name'], df_manual['Work Hours'], color=colors, alpha=0.9, edgecolor='black')

# Adding work hours above each bar
for i, bar in enumerate(bars):
    yval = bar.get_height()
    plt.text(bar.get_x() + bar.get_width()/2, yval, f"{df_manual['Work Hours'][i]}", 
             ha='center', va='bottom', fontsize=10)

plt.title('Work Hours for Each Worker', fontsize=18, fontweight='bold')
plt.xlabel('Name', fontsize=14)
plt.ylabel('Work Hours', fontsize=14)
plt.xticks(fontsize=12)
plt.yticks(fontsize=12)
plt.grid(axis='y', linestyle='--', alpha=0.7)  # Add grid lines only for the y-axis
plt.tight_layout()  # Adjust layout for better spacing

# Save the figure to the output directory
plt.savefig(os.path.join(output_dir, 'detailed_work_hours_and_salary.png'))
plt.close()  # Close the figure
print("Saved: detailed_work_hours_and_salary.png in output/")

# Work Hours per Person with values
plt.figure(figsize=(10, 6))  # Setting figure size

# Use the actual work hours as the values
plt.plot(df_manual['Name'], df_manual['Work Hours'], marker='o', linestyle='--', color='blue', markersize=8)
plt.title('Work Hours per Person', fontsize=18)
plt.xlabel('Name', fontsize=14)
plt.ylabel('Work Hours', fontsize=14)

# Adding work hours on top of the points
for i, value in enumerate(df_manual['Work Hours']):
    plt.text(i, value + 1, str(value), ha='center', fontsize=10)  # Display the work hours above the point

plt.xticks(fontsize=12)
plt.grid(True)
plt.tight_layout()  # Adjust layout for better spacing
plt.savefig(os.path.join(output_dir, 'work_hours_per_person.png'))  # Save the figure to output
plt.close()  # Close the figure
print("Saved: work_hours_per_person.png in output/")
