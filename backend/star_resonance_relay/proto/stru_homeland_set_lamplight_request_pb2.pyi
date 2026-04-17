import stru_int_vec3_pb2 as _stru_int_vec3_pb2
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from collections.abc import Mapping as _Mapping
from typing import ClassVar as _ClassVar, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class HomelandSetLamplightRequest(_message.Message):
    __slots__ = ("lamplight_level", "lamplight_color", "day_night_id", "mode", "is_outer")
    LAMPLIGHT_LEVEL_FIELD_NUMBER: _ClassVar[int]
    LAMPLIGHT_COLOR_FIELD_NUMBER: _ClassVar[int]
    DAY_NIGHT_ID_FIELD_NUMBER: _ClassVar[int]
    MODE_FIELD_NUMBER: _ClassVar[int]
    IS_OUTER_FIELD_NUMBER: _ClassVar[int]
    lamplight_level: int
    lamplight_color: _stru_int_vec3_pb2.IntVec3
    day_night_id: int
    mode: int
    is_outer: bool
    def __init__(self, lamplight_level: _Optional[int] = ..., lamplight_color: _Optional[_Union[_stru_int_vec3_pb2.IntVec3, _Mapping]] = ..., day_night_id: _Optional[int] = ..., mode: _Optional[int] = ..., is_outer: bool = ...) -> None: ...
