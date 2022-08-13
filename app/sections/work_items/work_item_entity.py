import attr as attr

from app.data import BaseEntity


@attr.s(auto_attribs=True)
class WorkItemEntity(BaseEntity):
    number: int
    title: str
    status: str
    url: str = "http://example.com"
