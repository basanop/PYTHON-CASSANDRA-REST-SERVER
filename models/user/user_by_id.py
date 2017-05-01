import uuid
from cassandra.cqlengine import columns
from models.base import Base

__author__ = 'puneet'

class UserById(Base):
    """
        Model Person object in database
    """

    id = columns.Integer(primary_key=True)
    first_name = columns.Text()
    last_name = columns.Text()
    email = columns.Text()
    company = columns.Text()
    city = columns.Text()

    def get_data(self):
        return {
            'id': str(self.id),
            'first_name': self.first_name,
            'last_name' : self.last_name,
            'email'     : self.email,
            'company'   : self.company,
            'city'      : self.city
        }
