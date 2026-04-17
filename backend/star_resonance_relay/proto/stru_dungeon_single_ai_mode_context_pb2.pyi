import enum_e_dungeon_enter_select_type_pb2 as _enum_e_dungeon_enter_select_type_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from collections.abc import Mapping as _Mapping
from typing import ClassVar as _ClassVar, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class DungeonSingleAiModeContext(_message.Message):
    __slots__ = ("scene_id", "select_type", "ai_config_id_map")
    class AiConfigIdMapEntry(_message.Message):
        __slots__ = ("key", "value")
        KEY_FIELD_NUMBER: _ClassVar[int]
        VALUE_FIELD_NUMBER: _ClassVar[int]
        key: int
        value: int
        def __init__(self, key: _Optional[int] = ..., value: _Optional[int] = ...) -> None: ...
    SCENE_ID_FIELD_NUMBER: _ClassVar[int]
    SELECT_TYPE_FIELD_NUMBER: _ClassVar[int]
    AI_CONFIG_ID_MAP_FIELD_NUMBER: _ClassVar[int]
    scene_id: int
    select_type: _enum_e_dungeon_enter_select_type_pb2.EDungeonEnterSelectType
    ai_config_id_map: _containers.ScalarMap[int, int]
    def __init__(self, scene_id: _Optional[int] = ..., select_type: _Optional[_Union[_enum_e_dungeon_enter_select_type_pb2.EDungeonEnterSelectType, str]] = ..., ai_config_id_map: _Optional[_Mapping[int, int]] = ...) -> None: ...
