import stru_social_data_pb2 as _stru_social_data_pb2
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from collections.abc import Mapping as _Mapping
from typing import ClassVar as _ClassVar, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class DungeonPlayerInfo(_message.Message):
    __slots__ = ("char_id", "social_data")
    CHAR_ID_FIELD_NUMBER: _ClassVar[int]
    SOCIAL_DATA_FIELD_NUMBER: _ClassVar[int]
    char_id: int
    social_data: _stru_social_data_pb2.SocialData
    def __init__(self, char_id: _Optional[int] = ..., social_data: _Optional[_Union[_stru_social_data_pb2.SocialData, _Mapping]] = ...) -> None: ...
