import stru_friend_base_info_pb2 as _stru_friend_base_info_pb2
import stru_personal_info_pb2 as _stru_personal_info_pb2
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from collections.abc import Mapping as _Mapping
from typing import ClassVar as _ClassVar, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class FriendData(_message.Message):
    __slots__ = ("info", "base_info")
    INFO_FIELD_NUMBER: _ClassVar[int]
    BASE_INFO_FIELD_NUMBER: _ClassVar[int]
    info: _stru_personal_info_pb2.PersonalInfo
    base_info: _stru_friend_base_info_pb2.FriendBaseInfo
    def __init__(self, info: _Optional[_Union[_stru_personal_info_pb2.PersonalInfo, _Mapping]] = ..., base_info: _Optional[_Union[_stru_friend_base_info_pb2.FriendBaseInfo, _Mapping]] = ...) -> None: ...
