import stru_community_char_basic_data_pb2 as _stru_community_char_basic_data_pb2
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from collections.abc import Mapping as _Mapping
from typing import ClassVar as _ClassVar, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class CommunityBulletinBoardOperatorChar(_message.Message):
    __slots__ = ("char_id", "char_basic_data")
    CHAR_ID_FIELD_NUMBER: _ClassVar[int]
    CHAR_BASIC_DATA_FIELD_NUMBER: _ClassVar[int]
    char_id: int
    char_basic_data: _stru_community_char_basic_data_pb2.CommunityCharBasicData
    def __init__(self, char_id: _Optional[int] = ..., char_basic_data: _Optional[_Union[_stru_community_char_basic_data_pb2.CommunityCharBasicData, _Mapping]] = ...) -> None: ...
