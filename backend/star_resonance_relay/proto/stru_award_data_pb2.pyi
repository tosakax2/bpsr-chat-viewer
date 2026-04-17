import stru_item_pb2 as _stru_item_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from collections.abc import Iterable as _Iterable, Mapping as _Mapping
from typing import ClassVar as _ClassVar, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class AwardData(_message.Message):
    __slots__ = ("award_id", "items")
    AWARD_ID_FIELD_NUMBER: _ClassVar[int]
    ITEMS_FIELD_NUMBER: _ClassVar[int]
    award_id: int
    items: _containers.RepeatedCompositeFieldContainer[_stru_item_pb2.Item]
    def __init__(self, award_id: _Optional[int] = ..., items: _Optional[_Iterable[_Union[_stru_item_pb2.Item, _Mapping]]] = ...) -> None: ...
