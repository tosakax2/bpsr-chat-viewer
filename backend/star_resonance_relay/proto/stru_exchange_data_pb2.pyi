from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Optional as _Optional

DESCRIPTOR: _descriptor.FileDescriptor

class ExchangeData(_message.Message):
    __slots__ = ("item_config_id", "unlock", "cur_exchange_count", "expire_time", "last_refresh_time")
    ITEM_CONFIG_ID_FIELD_NUMBER: _ClassVar[int]
    UNLOCK_FIELD_NUMBER: _ClassVar[int]
    CUR_EXCHANGE_COUNT_FIELD_NUMBER: _ClassVar[int]
    EXPIRE_TIME_FIELD_NUMBER: _ClassVar[int]
    LAST_REFRESH_TIME_FIELD_NUMBER: _ClassVar[int]
    item_config_id: int
    unlock: int
    cur_exchange_count: int
    expire_time: int
    last_refresh_time: int
    def __init__(self, item_config_id: _Optional[int] = ..., unlock: _Optional[int] = ..., cur_exchange_count: _Optional[int] = ..., expire_time: _Optional[int] = ..., last_refresh_time: _Optional[int] = ...) -> None: ...
