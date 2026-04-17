import stru_avatar_info_pb2 as _stru_avatar_info_pb2
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from collections.abc import Mapping as _Mapping
from typing import ClassVar as _ClassVar, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class UnionActivityRankInfo(_message.Message):
    __slots__ = ("char_id", "char_name", "avatar_info", "rank_idx", "value")
    CHAR_ID_FIELD_NUMBER: _ClassVar[int]
    CHAR_NAME_FIELD_NUMBER: _ClassVar[int]
    AVATAR_INFO_FIELD_NUMBER: _ClassVar[int]
    RANK_IDX_FIELD_NUMBER: _ClassVar[int]
    VALUE_FIELD_NUMBER: _ClassVar[int]
    char_id: int
    char_name: str
    avatar_info: _stru_avatar_info_pb2.AvatarInfo
    rank_idx: int
    value: int
    def __init__(self, char_id: _Optional[int] = ..., char_name: _Optional[str] = ..., avatar_info: _Optional[_Union[_stru_avatar_info_pb2.AvatarInfo, _Mapping]] = ..., rank_idx: _Optional[int] = ..., value: _Optional[int] = ...) -> None: ...
