import enum_e_homeland_lamplight_state_pb2 as _enum_e_homeland_lamplight_state_pb2
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class HomelandSwitchAllLamplightRequest(_message.Message):
    __slots__ = ("lamplight_state", "is_outer")
    LAMPLIGHT_STATE_FIELD_NUMBER: _ClassVar[int]
    IS_OUTER_FIELD_NUMBER: _ClassVar[int]
    lamplight_state: _enum_e_homeland_lamplight_state_pb2.EHomelandLamplightState
    is_outer: bool
    def __init__(self, lamplight_state: _Optional[_Union[_enum_e_homeland_lamplight_state_pb2.EHomelandLamplightState, str]] = ..., is_outer: bool = ...) -> None: ...
