import enum_e_error_code_pb2 as _enum_e_error_code_pb2
import stru_season_dungeon_affix_pb2 as _stru_season_dungeon_affix_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from collections.abc import Iterable as _Iterable, Mapping as _Mapping
from typing import ClassVar as _ClassVar, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class GetSeasonDungeonListReply(_message.Message):
    __slots__ = ("dungeon_id_list", "dungeon_affixes", "err_code")
    class DungeonAffixesEntry(_message.Message):
        __slots__ = ("key", "value")
        KEY_FIELD_NUMBER: _ClassVar[int]
        VALUE_FIELD_NUMBER: _ClassVar[int]
        key: int
        value: _stru_season_dungeon_affix_pb2.SeasonDungeonAffix
        def __init__(self, key: _Optional[int] = ..., value: _Optional[_Union[_stru_season_dungeon_affix_pb2.SeasonDungeonAffix, _Mapping]] = ...) -> None: ...
    DUNGEON_ID_LIST_FIELD_NUMBER: _ClassVar[int]
    DUNGEON_AFFIXES_FIELD_NUMBER: _ClassVar[int]
    ERR_CODE_FIELD_NUMBER: _ClassVar[int]
    dungeon_id_list: _containers.RepeatedScalarFieldContainer[int]
    dungeon_affixes: _containers.MessageMap[int, _stru_season_dungeon_affix_pb2.SeasonDungeonAffix]
    err_code: _enum_e_error_code_pb2.EErrorCode
    def __init__(self, dungeon_id_list: _Optional[_Iterable[int]] = ..., dungeon_affixes: _Optional[_Mapping[int, _stru_season_dungeon_affix_pb2.SeasonDungeonAffix]] = ..., err_code: _Optional[_Union[_enum_e_error_code_pb2.EErrorCode, str]] = ...) -> None: ...
