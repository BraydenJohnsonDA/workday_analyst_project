from faker import Faker
import pandas as pd
import random
from datetime import date

fake = Faker()

job_titles = [
    "HR Assistant", "Financial Analyst", "IT Support", 
    "Supply Chain Clerk", "Registered Nurse", "Billing Specialist"
]

departments = ["HR", "Finance", "IT", "Supply Chain", "Nursing"]

data = []

for _ in range(15):
    first = fake.first_name()
    last = fake.last_name()
    worker_id = fake.unique.random_int(min=2000, max=9999)
    job_title = random.choice(job_titles)
    department = random.choice(departments)
    manager_name = fake.name()
    start_date = fake.date_between(start_date=date(2023, 1, 1), end_date=date(2024, 12, 31))
    
    data.append({
        "Worker ID": worker_id,
        "First Name": first,
        "Last Name": last,
        "Job Title": job_title,
        "Department": department,
        "Manager Name": manager_name,
        "Effective Start Date": start_date
    })

df = pd.DataFrame(data)
df.to_excel("mass_worker_data_load_template.xlsx", index=False)
print(" File created: mass_worker_data_load_template.xlsx")
