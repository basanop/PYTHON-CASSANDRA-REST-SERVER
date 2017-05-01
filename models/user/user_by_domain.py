import uuid
from cassandra.cqlengine import columns
from models.base import Base

__author__ = 'puneet'

class UserByDomain(Base):
    """
        Model Person object by company & city in the database
    """
    domain = columns.Text(primary_key=True)
    city = columns.Text(primary_key=True)
    counter = columns.Counter()

    def get_data(self):
        """ convert model to String """
        return {
            'domain' : self.domain,
            'city'   : self.city,
            'counter': self.counter
        }
