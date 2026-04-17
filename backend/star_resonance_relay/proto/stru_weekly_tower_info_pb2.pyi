import stru_dungeon_random_entity_config_id_info_pb2 as _stru_dungeon_random_entity_config_id_info_pb2
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from collections.abc import Mapping as _Mapping
from typing import ClassVar as _ClassVar, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class WeeklyTowerInfo(_message.Message):
    __slots__ = ("climb_up_id", "continuous", "rand_entities")
    CLIMB_UP_ID_FIELD_NUMBER: _ClassVar[int]
    CONTINUOUS_FIELD_NUMBER: _ClassVar[int]
    RAND_ENTITIES_FIELD_NUMBER: _ClassVar[int]
    climb_up_id: int
    continuous: bool
    rand_entities: _stru_dungeon_random_entity_config_id_info_pb2.DungeonRandomEntityConfigIdInfo
    def __init__(self, climb_up_id: _Optional[int] = ..., continuous: bool = ..., rand_entities: _Optional[_Union[_stru_dungeon_random_entity_config_id_info_pb2.DungeonRandomEntityConfigIdInfo, _Mapping]] = ...) -> None: ...
