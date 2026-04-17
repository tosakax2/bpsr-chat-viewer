import stru_item_pb2 as _stru_item_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from collections.abc import Iterable as _Iterable, Mapping as _Mapping
from typing import ClassVar as _ClassVar, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class CommunityBuildLifeProfessionInfo(_message.Message):
    __slots__ = ("build_uuid", "char_id", "start_time", "item_id", "item_count", "consume_items", "reduce_time")
    BUILD_UUID_FIELD_NUMBER: _ClassVar[int]
    CHAR_ID_FIELD_NUMBER: _ClassVar[int]
    START_TIME_FIELD_NUMBER: _ClassVar[int]
    ITEM_ID_FIELD_NUMBER: _ClassVar[int]
    ITEM_COUNT_FIELD_NUMBER: _ClassVar[int]
    CONSUME_ITEMS_FIELD_NUMBER: _ClassVar[int]
    REDUCE_TIME_FIELD_NUMBER: _ClassVar[int]
    build_uuid: int
    char_id: int
    start_time: int
    item_id: int
    item_count: int
    consume_items: _containers.RepeatedCompositeFieldContainer[_stru_item_pb2.Item]
    reduce_time: int
    def __init__(self, build_uuid: _Optional[int] = ..., char_id: _Optional[int] = ..., start_time: _Optional[int] = ..., item_id: _Optional[int] = ..., item_count: _Optional[int] = ..., consume_items: _Optional[_Iterable[_Union[_stru_item_pb2.Item, _Mapping]]] = ..., reduce_time: _Optional[int] = ...) -> None: ...
