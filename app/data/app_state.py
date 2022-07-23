import attr

from app.data import BaseEntity, BaseStore
from app.data.data_store import DataStore

APP_STATE_RECORD_TYPE = "app_state"


@attr.s(auto_attribs=True)
class AppStateEntity(BaseEntity):
    record_type: str = APP_STATE_RECORD_TYPE


class AppStateStore(BaseStore):
    def __init__(self, data_store: DataStore):
        super().__init__(data_store)
        self._app_state = self.get_app_state()

    @property
    def app_state(self):
        return self._app_state

    def update_app_state_in_db(self):
        table = self.ds.table_for(self.app_state.record_type)
        table.upsert(
            dict(name=self.app_state.record_type, object=self.app_state.to_json_str()),
            ["name"],
        )

    def get_app_state(self):
        table = self.ds.table_for(APP_STATE_RECORD_TYPE)
        app_state_db = table.find_one(name=APP_STATE_RECORD_TYPE)
        if not app_state_db:
            return AppStateEntity()

        return AppStateEntity.from_json_str(app_state_db["object"])
