import enum_e_microphone_status_pb2 as _enum_e_microphone_status_pb2
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class SetMicrophoneStatusRequest(_message.Message):
    __slots__ = ("microphone_status",)
    MICROPHONE_STATUS_FIELD_NUMBER: _ClassVar[int]
    microphone_status: _enum_e_microphone_status_pb2.EMicrophoneStatus
    def __init__(self, microphone_status: _Optional[_Union[_enum_e_microphone_status_pb2.EMicrophoneStatus, str]] = ...) -> None: ...
