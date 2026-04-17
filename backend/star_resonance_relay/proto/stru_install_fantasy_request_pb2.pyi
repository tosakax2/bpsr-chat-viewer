from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Optional as _Optional

DESCRIPTOR: _descriptor.FileDescriptor

class InstallFantasyRequest(_message.Message):
    __slots__ = ("node_id", "fantasy_config_id")
    NODE_ID_FIELD_NUMBER: _ClassVar[int]
    FANTASY_CONFIG_ID_FIELD_NUMBER: _ClassVar[int]
    node_id: int
    fantasy_config_id: int
    def __init__(self, node_id: _Optional[int] = ..., fantasy_config_id: _Optional[int] = ...) -> None: ...
