import pandas as pd
from datetime import datetime, timedelta
import random

def generate_phone():
  return f"{random.randint(100, 999)}{random.randint(1000000, 9999999)}"

def generate_email(name, domain="gmail.com"):
  return f"{name.lower().replace(' ', '')}{random.randint(100, 999)}@{domain}"

def generate_indian_address():
  states = ["Maharashtra", "Tamil Nadu", "Karnataka", "Gujarat", "Uttar Pradesh", "West Bengal", "Andhra Pradesh", "Telangana", "Bihar", "Madhya Pradesh"]
  cities = ["Mumbai", "Delhi", "Bangalore", "Hyderabad", "Chennai", "Kolkata", "Pune", "Ahmedabad", "Surat", "Jaipur"]
  state = random.choice(states)
  city = random.choice(cities)
  street_num = random.randint(1, 100)
  street_name = random.choice(["Main Road", "MG Road", "Park Street", "Sarat Bose Road", "Tilak Road"])
  area = random.choice(["Andheri", "Bandra", "Koramangala", "HSR Layout", "Indiranagar"])
  return f"{street_num} {street_name}, {area}, {city}, {state}"

def generate_company_name():
  company_prefixes = ["Tech", "Corp", "Inc", "Solutions", "Systems", "Global", "International", "Limited", "Group", "Enterprise", "Digital", "Innovative", "Creative", "Smart", "Future"]
  company_suffixes = ["Solutions", "Technologies", "Services", "Consulting", "Industries", "Group", "Corporation", "Limited", "Enterprise", "Partners"]
  prefix = random.choice(company_prefixes)
  suffix = random.choice(company_suffixes)
  return f"{prefix} {suffix}"

today = datetime.today()
three_years_ago = today - timedelta(days=365 * 3)

df = pd.DataFrame(columns=["Name", "Company", "Phone", "Email", "Address", "Start Date", "Renewal Date"])

for i in range(500):
  first_name = random.choice(["Raj", "Veer", "Arjun", "Aditya", "Krishna", "Vikram"])
  last_name = random.choice(["Kumar", "Verma", "Kapoor", "Sharma", "Singh", "Mishra", "Pichai", "Nadar"])
  name = f"{first_name} {last_name}"
  company = generate_company_name()
  phone = generate_phone()
  email = generate_email(name)
  address = generate_indian_address()
  start_date = random.choice(pd.date_range(three_years_ago, today))
  renewal_date = start_date + timedelta(days=330)

  data = {
      "Name": name,
      "Company": company,
      "Phone": phone,
      "Email": email,
      "Address": address,
      "Start Date": start_date.strftime("%d-%m-%Y"),
      "Renewal Date": renewal_date.strftime("%d-%m-%Y")
  }

  df = pd.concat([df, pd.DataFrame([data])], ignore_index=True)

df.to_csv('generated_data.csv', index=False)