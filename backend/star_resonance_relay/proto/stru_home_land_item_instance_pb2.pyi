import stru_item_pb2 as _stru_item_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from collections.abc import Mapping as _Mapping
from typing import ClassVar as _ClassVar, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class HomeLandItemInstance(_message.Message):
    __slots__ = ("instance_id", "config_id", "owner_to_stack_map")
    class OwnerToStackMapEntry(_message.Message):
        __slots__ = ("key", "value")
        KEY_FIELD_NUMBER: _ClassVar[int]
        VALUE_FIELD_NUMBER: _ClassVar[int]
        key: int
        value: _stru_item_pb2.Item
        def __init__(self, key: _Optional[int] = ..., value: _Optional[_Union[_stru_item_pb2.Item, _Mapping]] = ...) -> None: ...
    INSTANCE_ID_FIELD_NUMBER: _ClassVar[int]
    CONFIG_ID_FIELD_NUMBER: _ClassVar[int]
    OWNER_TO_STACK_MAP_FIELD_NUMBER: _ClassVar[int]
    instance_id: int
    config_id: int
    owner_to_stack_map: _containers.MessageMap[int, _stru_item_pb2.Item]
    def __init__(self, instance_id: _Optional[int] = ..., config_id: _Optional[int] = ..., owner_to_stack_map: _Optional[_Mapping[int, _stru_item_pb2.Item]] = ...) -> None: ...
