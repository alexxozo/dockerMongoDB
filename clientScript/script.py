from pymongo import MongoClient
from faker import Factory
import time

client = MongoClient('db', 27017)
db = client["fake-data"]

def create_names(fake):
    for x in range(10):
        genName = fake.first_name()
        genSurname = fake.last_name()
        genJob = fake.job()
        genCountry = fake.country()

        result = db.fake.insert_one(
            {
                'name': genName,
                'surname': genSurname,
                'job': genJob,
                'country': genCountry
            }
        )

        print ("id: {}".format(str(result.inserted_id)))
        time.sleep(1)

if __name__ == '__main__':
    print('Hello from Client Container')
    fake = Factory.create()
    create_names(fake)