import abc
from datetime import datetime
from uuid import uuid4


class DomainEvent(abc.ABC):
    _id: str = str(uuid4())
    _emitted_at: datetime = datetime.today()
