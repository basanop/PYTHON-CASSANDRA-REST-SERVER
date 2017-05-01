import uuid
from cassandra.cqlengine import columns
from models.base import Base

__author__ = 'puneet'

class ActivityByUser(Base):
    """
        Model activity by user
    """
    date = columns.Text(primary_key=True)
    event = columns.Text(primary_key=True)
    domain = columns.Text(primary_key=True)
    id = columns.UUID(primary_key=True, default=uuid.uuid1())
    url = columns.Text()
    user_id = columns.Integer()
    datetime = columns.DateTime()

    def get_data(self):
        return {
            'id': str(self.id),
            'date': self.date,
            'user_id': self.user_id,
            'timestamp': self.timestamp
        }
