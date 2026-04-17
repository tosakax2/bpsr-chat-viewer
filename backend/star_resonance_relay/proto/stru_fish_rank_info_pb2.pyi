import stru_user_summary_data_pb2 as _stru_user_summary_data_pb2
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from collections.abc import Mapping as _Mapping
from typing import ClassVar as _ClassVar, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class FishRankInfo(_message.Message):
    __slots__ = ("millisecond", "size", "player_data")
    MILLISECOND_FIELD_NUMBER: _ClassVar[int]
    SIZE_FIELD_NUMBER: _ClassVar[int]
    PLAYER_DATA_FIELD_NUMBER: _ClassVar[int]
    millisecond: int
    size: int
    player_data: _stru_user_summary_data_pb2.UserSummaryData
    def __init__(self, millisecond: _Optional[int] = ..., size: _Optional[int] = ..., player_data: _Optional[_Union[_stru_user_summary_data_pb2.UserSummaryData, _Mapping]] = ...) -> None: ...
