import stru_mahjong_player_show_pb2 as _stru_mahjong_player_show_pb2
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from collections.abc import Mapping as _Mapping
from typing import ClassVar as _ClassVar, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class MahjongPlayerSelf(_message.Message):
    __slots__ = ("player_show", "can_do", "operation_time", "left_thinking_time")
    PLAYER_SHOW_FIELD_NUMBER: _ClassVar[int]
    CAN_DO_FIELD_NUMBER: _ClassVar[int]
    OPERATION_TIME_FIELD_NUMBER: _ClassVar[int]
    LEFT_THINKING_TIME_FIELD_NUMBER: _ClassVar[int]
    player_show: _stru_mahjong_player_show_pb2.MahjongPlayerShow
    can_do: int
    operation_time: int
    left_thinking_time: int
    def __init__(self, player_show: _Optional[_Union[_stru_mahjong_player_show_pb2.MahjongPlayerShow, _Mapping]] = ..., can_do: _Optional[int] = ..., operation_time: _Optional[int] = ..., left_thinking_time: _Optional[int] = ...) -> None: ...
