# Imports the Google Cloud client library
from google.cloud import ndb
import os


class Contact(ndb.Model):
    name = ndb.StringProperty()
    phone = ndb.StringProperty()
    email = ndb.StringProperty()


if __name__ == '__main__':
    os.environ["GOOGLE_APPLICATION_CREDENTIALS"] = "../keys/simonetestingproject.json"
    client = ndb.Client()

    with client.context():
        contact1 = Contact(id="1",
                           name="John Smith",
                           phone="555 617 8993",
                           email="john.smith@gmail.com")
        contact1.put()
        contact2 = Contact(id="2",
                           name="Jane Doe",
                           phone="555 445 1937",
                           email="jane.doe@gmail.com")
        contact2.put()

        query = Contact.query()
        all_names = [c.name for c in query]

        print(all_names)

        query = Contact.query().filter(Contact.name == "John Smith")
        filtered_names = [c.name for c in query]

        print(filtered_names)

        query = Contact.query().order(Contact.name, Contact.email)
        ordered_names = [c.name for c in query]

        print(ordered_names)
