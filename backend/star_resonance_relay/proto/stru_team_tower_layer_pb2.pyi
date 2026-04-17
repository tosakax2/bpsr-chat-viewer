import enum_e_error_code_pb2 as _enum_e_error_code_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from collections.abc import Mapping as _Mapping
from typing import ClassVar as _ClassVar, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class TeamTowerLayer(_message.Message):
    __slots__ = ("enter_climb_up_id", "mem_id_max_climb_id", "err_code")
    class MemIdMaxClimbIdEntry(_message.Message):
        __slots__ = ("key", "value")
        KEY_FIELD_NUMBER: _ClassVar[int]
        VALUE_FIELD_NUMBER: _ClassVar[int]
        key: int
        value: int
        def __init__(self, key: _Optional[int] = ..., value: _Optional[int] = ...) -> None: ...
    ENTER_CLIMB_UP_ID_FIELD_NUMBER: _ClassVar[int]
    MEM_ID_MAX_CLIMB_ID_FIELD_NUMBER: _ClassVar[int]
    ERR_CODE_FIELD_NUMBER: _ClassVar[int]
    enter_climb_up_id: int
    mem_id_max_climb_id: _containers.ScalarMap[int, int]
    err_code: _enum_e_error_code_pb2.EErrorCode
    def __init__(self, enter_climb_up_id: _Optional[int] = ..., mem_id_max_climb_id: _Optional[_Mapping[int, int]] = ..., err_code: _Optional[_Union[_enum_e_error_code_pb2.EErrorCode, str]] = ...) -> None: ...
