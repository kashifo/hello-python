import pandas as pd
from datetime import datetime, timedelta
import random
import string

df = pd.DataFrame(columns=["din", "name", "phone", "email", "address", "aadhar", "pan"])

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

used_dins = set()

for i in range(10):
  din = random.randint(10000000, 99999999)
  first_name = random.choice(["Raj", "Veer", "Arjun", "Aditya", "Krishna", "Vikram"])
  last_name = random.choice(["Kumar", "Verma", "Kapoor", "Sharma", "Singh", "Mishra", "Pichai", "Nadar"])
  name = f"{first_name} {last_name}"
  phone = generate_phone()
  email = generate_email(name)
  address = generate_indian_address()
  aadharID = f"{random.randint(1000, 9999)}-{random.randint(1000, 9999)}-{random.randint(1000, 9999)}"
  pan = ''.join(random.choice(string.ascii_uppercase) for _ in range(5)) + str(random.randint(100, 999)) + f"{random.choice(string.ascii_uppercase)}"

  while True:
        din = random.randint(10000000, 99999999)
        if din not in used_dins:
            used_dins.add(din)
            break

  data = {
      "name": name,
      "phone": phone,
      "email": email,
      "address": address,

      "aadhar": aadharID,
      "pan": pan,
      "din": din
  }

  df = pd.concat([df, pd.DataFrame([data])], ignore_index=True)

df.to_csv('director_list.csv', index=False)