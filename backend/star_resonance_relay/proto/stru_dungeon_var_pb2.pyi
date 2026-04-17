import stru_dungeon_var_data_pb2 as _stru_dungeon_var_data_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from collections.abc import Iterable as _Iterable, Mapping as _Mapping
from typing import ClassVar as _ClassVar, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class DungeonVar(_message.Message):
    __slots__ = ("dungeon_var_data",)
    DUNGEON_VAR_DATA_FIELD_NUMBER: _ClassVar[int]
    dungeon_var_data: _containers.RepeatedCompositeFieldContainer[_stru_dungeon_var_data_pb2.DungeonVarData]
    def __init__(self, dungeon_var_data: _Optional[_Iterable[_Union[_stru_dungeon_var_data_pb2.DungeonVarData, _Mapping]]] = ...) -> None: ...
