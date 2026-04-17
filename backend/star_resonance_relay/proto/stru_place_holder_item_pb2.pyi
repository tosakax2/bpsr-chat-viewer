import stru_item_pb2 as _stru_item_pb2
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from collections.abc import Mapping as _Mapping
from typing import ClassVar as _ClassVar, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class PlaceHolderItem(_message.Message):
    __slots__ = ("config_id", "item_detail")
    CONFIG_ID_FIELD_NUMBER: _ClassVar[int]
    ITEM_DETAIL_FIELD_NUMBER: _ClassVar[int]
    config_id: int
    item_detail: _stru_item_pb2.Item
    def __init__(self, config_id: _Optional[int] = ..., item_detail: _Optional[_Union[_stru_item_pb2.Item, _Mapping]] = ...) -> None: ...
