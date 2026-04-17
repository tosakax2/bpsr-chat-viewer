import enum_e_error_code_pb2 as _enum_e_error_code_pb2
import stru_friendliness_pb2 as _stru_friendliness_pb2
import stru_total_friendliness_pb2 as _stru_total_friendliness_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from collections.abc import Mapping as _Mapping
from typing import ClassVar as _ClassVar, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class GetFriendlinessReply(_message.Message):
    __slots__ = ("friendliness_list", "total_friendliness", "err_code")
    class FriendlinessListEntry(_message.Message):
        __slots__ = ("key", "value")
        KEY_FIELD_NUMBER: _ClassVar[int]
        VALUE_FIELD_NUMBER: _ClassVar[int]
        key: int
        value: _stru_friendliness_pb2.Friendliness
        def __init__(self, key: _Optional[int] = ..., value: _Optional[_Union[_stru_friendliness_pb2.Friendliness, _Mapping]] = ...) -> None: ...
    FRIENDLINESS_LIST_FIELD_NUMBER: _ClassVar[int]
    TOTAL_FRIENDLINESS_FIELD_NUMBER: _ClassVar[int]
    ERR_CODE_FIELD_NUMBER: _ClassVar[int]
    friendliness_list: _containers.MessageMap[int, _stru_friendliness_pb2.Friendliness]
    total_friendliness: _stru_total_friendliness_pb2.TotalFriendliness
    err_code: _enum_e_error_code_pb2.EErrorCode
    def __init__(self, friendliness_list: _Optional[_Mapping[int, _stru_friendliness_pb2.Friendliness]] = ..., total_friendliness: _Optional[_Union[_stru_total_friendliness_pb2.TotalFriendliness, _Mapping]] = ..., err_code: _Optional[_Union[_enum_e_error_code_pb2.EErrorCode, str]] = ...) -> None: ...
