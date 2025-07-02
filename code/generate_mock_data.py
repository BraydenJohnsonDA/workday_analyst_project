from faker import Faker
import pandas as pd
import random

fake = Faker()

data = []

for _ in range(30):
    first = fake.first_name()
    last = fake.last_name()
    email = f"{first.lower()}.{last.lower()}@company.com" if random.random() > 0.1 else ""
    emp_id = fake.unique.random_int(min=1000, max=9999)
    department = random.choice(["HR", "Finance", "IT"])
    status = random.choice(["Active", "Terminated"])

    data.append({
        "Employee ID": emp_id,
        "First Name": first,
        "Last Name": last,
        "Email": email,
        "Department": department,
        "Status": status
    })

df = pd.DataFrame(data)
df.to_excel("mock_employee_data.xlsx", index=False)
print(" File created: mock_employee_data.xlsx")
