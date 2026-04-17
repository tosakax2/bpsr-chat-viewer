import stru_mahjong_config_info_pb2 as _stru_mahjong_config_info_pb2
import stru_player_mahjong_data_pb2 as _stru_player_mahjong_data_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from collections.abc import Iterable as _Iterable, Mapping as _Mapping
from typing import ClassVar as _ClassVar, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class StartMessage(_message.Message):
    __slots__ = ("players", "config")
    PLAYERS_FIELD_NUMBER: _ClassVar[int]
    CONFIG_FIELD_NUMBER: _ClassVar[int]
    players: _containers.RepeatedCompositeFieldContainer[_stru_player_mahjong_data_pb2.PlayerMahjongData]
    config: _containers.RepeatedCompositeFieldContainer[_stru_mahjong_config_info_pb2.MahjongConfigInfo]
    def __init__(self, players: _Optional[_Iterable[_Union[_stru_player_mahjong_data_pb2.PlayerMahjongData, _Mapping]]] = ..., config: _Optional[_Iterable[_Union[_stru_mahjong_config_info_pb2.MahjongConfigInfo, _Mapping]]] = ...) -> None: ...
