import enum_e_homeland_lamplight_state_pb2 as _enum_e_homeland_lamplight_state_pb2
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class StructureLamplightInfo(_message.Message):
    __slots__ = ("state",)
    STATE_FIELD_NUMBER: _ClassVar[int]
    state: _enum_e_homeland_lamplight_state_pb2.EHomelandLamplightState
    def __init__(self, state: _Optional[_Union[_enum_e_homeland_lamplight_state_pb2.EHomelandLamplightState, str]] = ...) -> None: ...
