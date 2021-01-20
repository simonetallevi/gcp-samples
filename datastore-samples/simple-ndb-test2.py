# Imports the Google Cloud client library
from google.cloud import ndb
import uuid
import os


class Contact(ndb.Model):
    name = ndb.StringProperty()
    phone = ndb.StringProperty()
    email = ndb.StringProperty()


if __name__ == '__main__':
    os.environ["GOOGLE_APPLICATION_CREDENTIALS"] = "../keys/simonetestingproject.json"
    client = ndb.Client()

    with client.context():
        for i in range(0, 100):
            contact1 = Contact(id=str(uuid.uuid4()),
                               name=f"contact {i}",
                               phone=f"555 617 899{i}",
                               email=f"john.smith{i}@gmail.com")
            contact1.put()

        query = Contact.query().filter(Contact.name == "contact 99")

        for e in query:
            print(e)
