import pandas as pd
from datetime import datetime, timedelta

# Define starting and ending dates for random start date generation
today = datetime.today()
three_years_ago = today - timedelta(days=365 * 3)

# Define function to generate random phone number (10 digits)
def generate_phone():
  return f"{random.randint(100, 999)}{random.randint(1000000, 9999999)}"

# Define function to generate random email
def generate_email(name, domain="example.com"):
  return f"{name.lower()}.{random.randint(100, 999)}@{domain}"

# Define function to generate random address
def generate_address():
  street_num = random.randint(1, 1000)
  street_name = f"{random.choice(['Main', 'Elm', 'Maple', 'Oak'])} St"
  city = f"City-{random.randint(100, 999)}"
  return f"{street_num} {street_name}, {city}"

# Import libraries for random data generation (optional)
import random

# Create empty DataFrame
df = pd.DataFrame(columns=["Name", "Company", "Phone", "Email", "Address", "Start Date", "Renewal Date"])

# Loop to generate 500 rows
for i in range(10):
  # Generate random names
  first_name = f"Name-{i+1}"
  last_name = random.choice(["Smith", "Johnson", "Williams", "Brown", "Jones"])
  name = f"{first_name} {last_name}"
  
  # Generate random company name
  company = f"Company-{random.randint(1000, 9999)}"

  # Generate random phone number
  phone = generate_phone()

  # Generate random email
  email = generate_email(name)

  # Generate random address
  address = generate_address()

  # Generate random start date within the specified range
  start_date = random.choice(pd.date_range(three_years_ago, today))

  # Calculate renewal date (11 months from start date)
  renewal_date = start_date + timedelta(days=330)  # 11 months

  # Create a Series with the generated data
  data = pd.Series({
      "Name": name,
      "Company": company,
      "Phone": phone,
      "Email": email,
      "Address": address,
      "Start Date": start_date.strftime("%d-%m-%Y"),
      "Renewal Date": renewal_date.strftime("%d-%m-%Y")
  })

  # Append the Series to the DataFrame
  # df = df.append(data, ignore_index=True)
  df = pd.concat([df, data], ignore_index=True)

df.to_csv('generated_data.csv', index=False)

# Print the DataFrame (optional)
print(df.head())