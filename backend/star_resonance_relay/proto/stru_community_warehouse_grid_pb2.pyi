import stru_item_pb2 as _stru_item_pb2
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from collections.abc import Mapping as _Mapping
from typing import ClassVar as _ClassVar, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class CommunityWarehouseGrid(_message.Message):
    __slots__ = ("owner_char_id", "item_info", "pos")
    OWNER_CHAR_ID_FIELD_NUMBER: _ClassVar[int]
    ITEM_INFO_FIELD_NUMBER: _ClassVar[int]
    POS_FIELD_NUMBER: _ClassVar[int]
    owner_char_id: int
    item_info: _stru_item_pb2.Item
    pos: int
    def __init__(self, owner_char_id: _Optional[int] = ..., item_info: _Optional[_Union[_stru_item_pb2.Item, _Mapping]] = ..., pos: _Optional[int] = ...) -> None: ...
