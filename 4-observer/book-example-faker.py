from faker import Faker
import sys
fake = Faker()
args = sys.argv[1:]
if len(args) == 1:
    output_filename = args[0]
    person_list = []
    for _ in range(0, 20):
        p = {"firstname": fake.first_name(), "lastname": fake.last_name()}
        person_list.append(p)
    person_list = iter(person_list)
    data = [f"{p['firstname']} {p['lastname']}" for p in person_list]
    data = ", ".join(data) + ", "
    with open(output_filename, "a") as f:
        f.write(data)
else:
    print("You need to pass the output filepath!")