import stru_player_box_data_pb2 as _stru_player_box_data_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from collections.abc import Mapping as _Mapping
from typing import ClassVar as _ClassVar, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class PlayerBox(_message.Message):
    __slots__ = ("scenes",)
    class ScenesEntry(_message.Message):
        __slots__ = ("key", "value")
        KEY_FIELD_NUMBER: _ClassVar[int]
        VALUE_FIELD_NUMBER: _ClassVar[int]
        key: int
        value: _stru_player_box_data_pb2.PlayerBoxData
        def __init__(self, key: _Optional[int] = ..., value: _Optional[_Union[_stru_player_box_data_pb2.PlayerBoxData, _Mapping]] = ...) -> None: ...
    SCENES_FIELD_NUMBER: _ClassVar[int]
    scenes: _containers.MessageMap[int, _stru_player_box_data_pb2.PlayerBoxData]
    def __init__(self, scenes: _Optional[_Mapping[int, _stru_player_box_data_pb2.PlayerBoxData]] = ...) -> None: ...
