import stru_slot_info_pb2 as _stru_slot_info_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from collections.abc import Mapping as _Mapping
from typing import ClassVar as _ClassVar, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class Slot(_message.Message):
    __slots__ = ("slots",)
    class SlotsEntry(_message.Message):
        __slots__ = ("key", "value")
        KEY_FIELD_NUMBER: _ClassVar[int]
        VALUE_FIELD_NUMBER: _ClassVar[int]
        key: int
        value: _stru_slot_info_pb2.SlotInfo
        def __init__(self, key: _Optional[int] = ..., value: _Optional[_Union[_stru_slot_info_pb2.SlotInfo, _Mapping]] = ...) -> None: ...
    SLOTS_FIELD_NUMBER: _ClassVar[int]
    slots: _containers.MessageMap[int, _stru_slot_info_pb2.SlotInfo]
    def __init__(self, slots: _Optional[_Mapping[int, _stru_slot_info_pb2.SlotInfo]] = ...) -> None: ...
