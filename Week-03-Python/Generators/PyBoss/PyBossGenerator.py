# -*- coding: UTF-8 -*-
"""Generate Data for PyBoss.

This module generates an employee dataset for the PyBoss Homework.
"""
# Dependencies
import csv
import random
from faker import Factory

# Fake data generator
fake = Factory.create("en_US")

# Create output file name
file_output_name = "employee_data1.csv"

# Set employee counts
emp_count = 650

# Create emp_ids
emp_ids = random.sample(range(1, 655), emp_count)


# Create variety of fake employee data
def get_dob():
    """Generate a fake date-of-birth."""
    return (
        fake.date_time_between(
            start_date="-45y",
            end_date="-22y",
            tzinfo=None)).strftime("%Y-%m-%d")

emp_names = ["{} {}".format(fake.first_name(), fake.last_name()) for _ in range(emp_count)]
emp_dobs = [get_dob() for _ in range(emp_count)]
emp_ssns = [fake.ssn() for _ in range(emp_count)]
emp_states = [fake.state() for _ in range(emp_count)]

# Combine all data into a single list
emp_db = zip(emp_ids, emp_names, emp_dobs, emp_ssns, emp_states)

# Print the employee list to terminal
print(emp_db)

# Output the employee list to a csv
# Write all of the election data to csv
with open(file_output_name, "w", newline="") as datafile:
    writer = csv.writer(datafile)
    writer.writerow(["Emp ID", "Name", "DOB", "SSN", "State"])
    writer.writerows(emp_db)
