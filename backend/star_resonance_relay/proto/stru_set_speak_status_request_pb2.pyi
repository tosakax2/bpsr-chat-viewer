import enum_e_speak_status_pb2 as _enum_e_speak_status_pb2
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class SetSpeakStatusRequest(_message.Message):
    __slots__ = ("speak_status",)
    SPEAK_STATUS_FIELD_NUMBER: _ClassVar[int]
    speak_status: _enum_e_speak_status_pb2.ESpeakStatus
    def __init__(self, speak_status: _Optional[_Union[_enum_e_speak_status_pb2.ESpeakStatus, str]] = ...) -> None: ...
