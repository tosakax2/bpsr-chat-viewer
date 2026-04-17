import stru_item_pb2 as _stru_item_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from collections.abc import Iterable as _Iterable, Mapping as _Mapping
from typing import ClassVar as _ClassVar, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class CommunityBuildFurnitureInfo(_message.Message):
    __slots__ = ("build_uuid", "furniture_id", "furniture_count", "char_id", "start_time", "end_time", "accelerate_count", "accelerate_items", "consume_items")
    class AccelerateItemsEntry(_message.Message):
        __slots__ = ("key", "value")
        KEY_FIELD_NUMBER: _ClassVar[int]
        VALUE_FIELD_NUMBER: _ClassVar[int]
        key: int
        value: int
        def __init__(self, key: _Optional[int] = ..., value: _Optional[int] = ...) -> None: ...
    BUILD_UUID_FIELD_NUMBER: _ClassVar[int]
    FURNITURE_ID_FIELD_NUMBER: _ClassVar[int]
    FURNITURE_COUNT_FIELD_NUMBER: _ClassVar[int]
    CHAR_ID_FIELD_NUMBER: _ClassVar[int]
    START_TIME_FIELD_NUMBER: _ClassVar[int]
    END_TIME_FIELD_NUMBER: _ClassVar[int]
    ACCELERATE_COUNT_FIELD_NUMBER: _ClassVar[int]
    ACCELERATE_ITEMS_FIELD_NUMBER: _ClassVar[int]
    CONSUME_ITEMS_FIELD_NUMBER: _ClassVar[int]
    build_uuid: int
    furniture_id: int
    furniture_count: int
    char_id: int
    start_time: int
    end_time: int
    accelerate_count: int
    accelerate_items: _containers.ScalarMap[int, int]
    consume_items: _containers.RepeatedCompositeFieldContainer[_stru_item_pb2.Item]
    def __init__(self, build_uuid: _Optional[int] = ..., furniture_id: _Optional[int] = ..., furniture_count: _Optional[int] = ..., char_id: _Optional[int] = ..., start_time: _Optional[int] = ..., end_time: _Optional[int] = ..., accelerate_count: _Optional[int] = ..., accelerate_items: _Optional[_Mapping[int, int]] = ..., consume_items: _Optional[_Iterable[_Union[_stru_item_pb2.Item, _Mapping]]] = ...) -> None: ...
