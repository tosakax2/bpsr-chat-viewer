import stru_item_pb2 as _stru_item_pb2
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from collections.abc import Mapping as _Mapping
from typing import ClassVar as _ClassVar, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class DungeonHotKeyContext(_message.Message):
    __slots__ = ("char_id", "use_item")
    CHAR_ID_FIELD_NUMBER: _ClassVar[int]
    USE_ITEM_FIELD_NUMBER: _ClassVar[int]
    char_id: int
    use_item: _stru_item_pb2.Item
    def __init__(self, char_id: _Optional[int] = ..., use_item: _Optional[_Union[_stru_item_pb2.Item, _Mapping]] = ...) -> None: ...
