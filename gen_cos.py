import pandas as pd
from datetime import datetime, timedelta
import random
import string

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

def generate_gstin():
    # Generate random alphanumeric string for GSTIN
    alphanum = string.ascii_uppercase + string.digits
    gstin = ''.join(random.choice(alphanum) for _ in range(15))
    return f"{gstin[:2]}DE{gstin[2:7]}{gstin[7:12]}{gstin[12:]}"

def generate_cin():
    # Generate random alphanumeric string for CIN
    alphanum = string.ascii_uppercase + string.digits
    cin = ''.join(random.choice(alphanum) for _ in range(21))
    return f"U{cin}"

def generate_category():
    categories = ["Advertising", "Media", "E-commerce", "IT services", "Finance", "Healthcare", "Manufacturing", "Education", "Retail", "Construction"]
    return random.choice(categories)

def generate_director_din():
    return random.randint(10000000, 99999999)

def generate_company_data():
    today = datetime.today()
    three_years_ago = today - timedelta(days=365 * 3)

    company_name = generate_company_name()
    cin = generate_cin()
    gstin = generate_gstin()
    phone = generate_phone()
    email = generate_email(company_name)  # Use company name for email
    address = generate_indian_address()
    start_date = random.choice(pd.date_range(three_years_ago, today))
    renewal_date = start_date + timedelta(days=330)
    category = generate_category()
    status = random.choice(["active", "inactive", "vacated"])
    description = "Involved in various business activities."

    # Generate a fixed number of random director DINs
    num_directors = 2
    directors = [str(generate_director_din()) for _ in range(num_directors)]
    directors_str = ", ".join(directors)

    return {
        "companyName": company_name,
        "CIN": cin,
        "GSTIN": gstin,
        "phone": phone,
        "email": email,
        "address": address,
        "startDate": start_date.strftime("%Y-%m-%d"),
        "renewalDate": renewal_date.strftime("%Y-%m-%d"),
        "category": category,
        "directors": directors_str,
        "description": description,
        "status": status
    }

if __name__ == "__main__":
    company_data = []

    for _ in range(500):
        company_info = generate_company_data()
        company_data.append(company_info)

    company_df = pd.DataFrame(company_data)
    company_df.to_csv('companies.csv', index=False)