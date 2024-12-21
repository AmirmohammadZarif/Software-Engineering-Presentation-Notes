import time
from random import randint
from concurrent.futures import ThreadPoolExecutor, as_completed


def send_email(email):
    time.sleep(randint(1, 3)) 
    return f"Email sent to {email}"

emails = [f"user{i}@example.com" for i in range(10)]

with ThreadPoolExecutor() as executor:
    futures = [executor.submit(send_email, email) for email in emails]
    for future in as_completed(futures):
        print(future.result())