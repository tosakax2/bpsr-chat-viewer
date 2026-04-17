import enum_e_apply_ride_result_pb2 as _enum_e_apply_ride_result_pb2
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class ApplyToRideResultParam(_message.Message):
    __slots__ = ("v_orig_id", "result")
    V_ORIG_ID_FIELD_NUMBER: _ClassVar[int]
    RESULT_FIELD_NUMBER: _ClassVar[int]
    v_orig_id: int
    result: _enum_e_apply_ride_result_pb2.EApplyRideResult
    def __init__(self, v_orig_id: _Optional[int] = ..., result: _Optional[_Union[_enum_e_apply_ride_result_pb2.EApplyRideResult, str]] = ...) -> None: ...
