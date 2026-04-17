from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Optional as _Optional

DESCRIPTOR: _descriptor.FileDescriptor

class FightSourceInfo(_message.Message):
    __slots__ = ("fight_source_type", "source_config_id")
    FIGHT_SOURCE_TYPE_FIELD_NUMBER: _ClassVar[int]
    SOURCE_CONFIG_ID_FIELD_NUMBER: _ClassVar[int]
    fight_source_type: int
    source_config_id: int
    def __init__(self, fight_source_type: _Optional[int] = ..., source_config_id: _Optional[int] = ...) -> None: ...
