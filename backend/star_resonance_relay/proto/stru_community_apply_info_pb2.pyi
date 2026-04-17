import stru_community_char_basic_data_pb2 as _stru_community_char_basic_data_pb2
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from collections.abc import Mapping as _Mapping
from typing import ClassVar as _ClassVar, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class CommunityApplyInfo(_message.Message):
    __slots__ = ("time", "char_id", "home_id", "char_basic_data", "community_id")
    TIME_FIELD_NUMBER: _ClassVar[int]
    CHAR_ID_FIELD_NUMBER: _ClassVar[int]
    HOME_ID_FIELD_NUMBER: _ClassVar[int]
    CHAR_BASIC_DATA_FIELD_NUMBER: _ClassVar[int]
    COMMUNITY_ID_FIELD_NUMBER: _ClassVar[int]
    time: int
    char_id: int
    home_id: int
    char_basic_data: _stru_community_char_basic_data_pb2.CommunityCharBasicData
    community_id: int
    def __init__(self, time: _Optional[int] = ..., char_id: _Optional[int] = ..., home_id: _Optional[int] = ..., char_basic_data: _Optional[_Union[_stru_community_char_basic_data_pb2.CommunityCharBasicData, _Mapping]] = ..., community_id: _Optional[int] = ...) -> None: ...
