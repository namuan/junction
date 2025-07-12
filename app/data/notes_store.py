import logging

import attr

from app.core.uuid_utils import gen_uuid
from app.data import BaseEntity, BaseStore

NOTES_RECORD_TYPE = "notes"


@attr.s(auto_attribs=True)
class NotesEntity(BaseEntity):
    id: str
    content: str


class NotesStore(BaseStore):
    def __init__(self, data_store):
        super().__init__(data_store)

    def get_scratch_note(self):
        logging.info("Get Notes")
        table = self.ds.table_for(NOTES_RECORD_TYPE)
        notes_row = table.find_one(name=NOTES_RECORD_TYPE)
        if not notes_row:
            return None
        return NotesEntity.from_json_str(notes_row["object"])

    def update_scratch_note(self, plain_text_note):
        note_entity = NotesEntity(
            content=plain_text_note,
            id=gen_uuid()
        )
        table = self.ds.table_for(NOTES_RECORD_TYPE)
        table.upsert(
            dict(
                name=NOTES_RECORD_TYPE,
                note_id=note_entity.id,
                object=note_entity.to_json_str(),
            ),
            ["note_id"],
        )
        logging.info("Update note: {}".format(note_entity.id))
