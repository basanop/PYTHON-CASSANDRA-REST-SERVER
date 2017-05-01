import uuid
from cassandra.cqlengine import columns
from models.base import Base

__author__ = 'puneet'

class UserByCompanyCity(Base):
    """
        Model Person object by company & city in the database
    """
    company = columns.Text(primary_key=True)
    city = columns.Text(primary_key=True)
    id = columns.Integer(primary_key=True)
    first_name = columns.Text()
    last_name = columns.Text()
    email = columns.Text()
    
    def get_data(self):
        return {
            'id': str(self.id),
            'first_name': self.first_name,
            'last_name' : self.last_name,
            'email'     : self.email,
            'company'   : self.company,
            'city'      : self.city
        }
