import uuid
from cassandra.cqlengine import columns
from models.base import Base

__author__ = 'puneet'

class ActivityByCompany(Base):
    """
        Model activity by Activity
    """
    company = columns.Text(primary_key=True)
    date = columns.Text(primary_key=True)
    clicks = columns.Counter()
    views  = columns.Counter()
    subscribes = columns.Counter()
    orders = columns.Counter()


    def get_data(self):
        return {
            'id': str(self.id),
            'date': self.date,
            'company': self.company,
            'clicks' : self.clicks,
            'views'  : self.views,
            'subscribes' : self.subscribes
        }
