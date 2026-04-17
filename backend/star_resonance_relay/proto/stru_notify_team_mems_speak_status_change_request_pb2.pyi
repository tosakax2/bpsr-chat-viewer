import enum_e_speak_status_pb2 as _enum_e_speak_status_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from collections.abc import Mapping as _Mapping
from typing import ClassVar as _ClassVar, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class NotifyTeamMemsSpeakStatusChangeRequest(_message.Message):
    __slots__ = ("mem_speak_status",)
    class MemSpeakStatusEntry(_message.Message):
        __slots__ = ("key", "value")
        KEY_FIELD_NUMBER: _ClassVar[int]
        VALUE_FIELD_NUMBER: _ClassVar[int]
        key: int
        value: _enum_e_speak_status_pb2.ESpeakStatus
        def __init__(self, key: _Optional[int] = ..., value: _Optional[_Union[_enum_e_speak_status_pb2.ESpeakStatus, str]] = ...) -> None: ...
    MEM_SPEAK_STATUS_FIELD_NUMBER: _ClassVar[int]
    mem_speak_status: _containers.ScalarMap[int, _enum_e_speak_status_pb2.ESpeakStatus]
    def __init__(self, mem_speak_status: _Optional[_Mapping[int, _enum_e_speak_status_pb2.ESpeakStatus]] = ...) -> None: ...
