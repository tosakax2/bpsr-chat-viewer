import enum_e_apply_ride_result_pb2 as _enum_e_apply_ride_result_pb2
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class NotifyRideIsAgreeParam(_message.Message):
    __slots__ = ("char_id", "char_name", "result")
    CHAR_ID_FIELD_NUMBER: _ClassVar[int]
    CHAR_NAME_FIELD_NUMBER: _ClassVar[int]
    RESULT_FIELD_NUMBER: _ClassVar[int]
    char_id: int
    char_name: str
    result: _enum_e_apply_ride_result_pb2.EApplyRideResult
    def __init__(self, char_id: _Optional[int] = ..., char_name: _Optional[str] = ..., result: _Optional[_Union[_enum_e_apply_ride_result_pb2.EApplyRideResult, str]] = ...) -> None: ...
