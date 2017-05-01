import uuid
from cassandra.cqlengine import columns
from models.base import Base

__author__ = 'puneet'

class CountActivityByUser(Base):
    """
        Model activity by user
    """
    date = columns.Text(primary_key=True)
    company =columns.Text(primary_key=True)
    counter = columns.Counter()

    def get_data(self):
        return {
            'id': str(self.id),
            'date': self.date,
            'user_id': self.user_id,
            'timestamp': self.timestamp
        }
