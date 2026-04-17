import stru_duty_info_pb2 as _stru_duty_info_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from collections.abc import Mapping as _Mapping
from typing import ClassVar as _ClassVar, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class DutyList(_message.Message):
    __slots__ = ("cur_profession_duty_id", "duty_info_map")
    class DutyInfoMapEntry(_message.Message):
        __slots__ = ("key", "value")
        KEY_FIELD_NUMBER: _ClassVar[int]
        VALUE_FIELD_NUMBER: _ClassVar[int]
        key: int
        value: _stru_duty_info_pb2.DutyInfo
        def __init__(self, key: _Optional[int] = ..., value: _Optional[_Union[_stru_duty_info_pb2.DutyInfo, _Mapping]] = ...) -> None: ...
    CUR_PROFESSION_DUTY_ID_FIELD_NUMBER: _ClassVar[int]
    DUTY_INFO_MAP_FIELD_NUMBER: _ClassVar[int]
    cur_profession_duty_id: int
    duty_info_map: _containers.MessageMap[int, _stru_duty_info_pb2.DutyInfo]
    def __init__(self, cur_profession_duty_id: _Optional[int] = ..., duty_info_map: _Optional[_Mapping[int, _stru_duty_info_pb2.DutyInfo]] = ...) -> None: ...
