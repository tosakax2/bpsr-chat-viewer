import stru_drought_record_pb2 as _stru_drought_record_pb2
import enum_e_farmland_state_pb2 as _enum_e_farmland_state_pb2
import stru_home_land_item_instance_pb2 as _stru_home_land_item_instance_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from collections.abc import Iterable as _Iterable, Mapping as _Mapping
from typing import ClassVar as _ClassVar, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class StructureFarmlandInfo(_message.Message):
    __slots__ = ("operator_char_id", "seed_instance", "need_water", "farmland_state", "seeding_time", "grow_end_time", "pollinate_begin_time", "pollinate_end_time", "harvest_begin_time", "harvest_end_time", "is_end", "flower_instance", "next_segment_index", "records", "fertilizes", "pollen_instance", "pick_up_players", "new_seeding_sec", "new_grow_end_sec", "new_pollinate_begin_sec", "new_pollinate_end_sec", "new_harvest_begin_sec", "new_harvest_end_sec")
    class PickUpPlayersEntry(_message.Message):
        __slots__ = ("key", "value")
        KEY_FIELD_NUMBER: _ClassVar[int]
        VALUE_FIELD_NUMBER: _ClassVar[int]
        key: int
        value: int
        def __init__(self, key: _Optional[int] = ..., value: _Optional[int] = ...) -> None: ...
    OPERATOR_CHAR_ID_FIELD_NUMBER: _ClassVar[int]
    SEED_INSTANCE_FIELD_NUMBER: _ClassVar[int]
    NEED_WATER_FIELD_NUMBER: _ClassVar[int]
    FARMLAND_STATE_FIELD_NUMBER: _ClassVar[int]
    SEEDING_TIME_FIELD_NUMBER: _ClassVar[int]
    GROW_END_TIME_FIELD_NUMBER: _ClassVar[int]
    POLLINATE_BEGIN_TIME_FIELD_NUMBER: _ClassVar[int]
    POLLINATE_END_TIME_FIELD_NUMBER: _ClassVar[int]
    HARVEST_BEGIN_TIME_FIELD_NUMBER: _ClassVar[int]
    HARVEST_END_TIME_FIELD_NUMBER: _ClassVar[int]
    IS_END_FIELD_NUMBER: _ClassVar[int]
    FLOWER_INSTANCE_FIELD_NUMBER: _ClassVar[int]
    NEXT_SEGMENT_INDEX_FIELD_NUMBER: _ClassVar[int]
    RECORDS_FIELD_NUMBER: _ClassVar[int]
    FERTILIZES_FIELD_NUMBER: _ClassVar[int]
    POLLEN_INSTANCE_FIELD_NUMBER: _ClassVar[int]
    PICK_UP_PLAYERS_FIELD_NUMBER: _ClassVar[int]
    NEW_SEEDING_SEC_FIELD_NUMBER: _ClassVar[int]
    NEW_GROW_END_SEC_FIELD_NUMBER: _ClassVar[int]
    NEW_POLLINATE_BEGIN_SEC_FIELD_NUMBER: _ClassVar[int]
    NEW_POLLINATE_END_SEC_FIELD_NUMBER: _ClassVar[int]
    NEW_HARVEST_BEGIN_SEC_FIELD_NUMBER: _ClassVar[int]
    NEW_HARVEST_END_SEC_FIELD_NUMBER: _ClassVar[int]
    operator_char_id: int
    seed_instance: _stru_home_land_item_instance_pb2.HomeLandItemInstance
    need_water: bool
    farmland_state: _enum_e_farmland_state_pb2.EFarmlandState
    seeding_time: int
    grow_end_time: int
    pollinate_begin_time: int
    pollinate_end_time: int
    harvest_begin_time: int
    harvest_end_time: int
    is_end: bool
    flower_instance: _stru_home_land_item_instance_pb2.HomeLandItemInstance
    next_segment_index: int
    records: _containers.RepeatedCompositeFieldContainer[_stru_drought_record_pb2.DroughtRecord]
    fertilizes: _containers.RepeatedScalarFieldContainer[int]
    pollen_instance: _stru_home_land_item_instance_pb2.HomeLandItemInstance
    pick_up_players: _containers.ScalarMap[int, int]
    new_seeding_sec: int
    new_grow_end_sec: int
    new_pollinate_begin_sec: int
    new_pollinate_end_sec: int
    new_harvest_begin_sec: int
    new_harvest_end_sec: int
    def __init__(self, operator_char_id: _Optional[int] = ..., seed_instance: _Optional[_Union[_stru_home_land_item_instance_pb2.HomeLandItemInstance, _Mapping]] = ..., need_water: bool = ..., farmland_state: _Optional[_Union[_enum_e_farmland_state_pb2.EFarmlandState, str]] = ..., seeding_time: _Optional[int] = ..., grow_end_time: _Optional[int] = ..., pollinate_begin_time: _Optional[int] = ..., pollinate_end_time: _Optional[int] = ..., harvest_begin_time: _Optional[int] = ..., harvest_end_time: _Optional[int] = ..., is_end: bool = ..., flower_instance: _Optional[_Union[_stru_home_land_item_instance_pb2.HomeLandItemInstance, _Mapping]] = ..., next_segment_index: _Optional[int] = ..., records: _Optional[_Iterable[_Union[_stru_drought_record_pb2.DroughtRecord, _Mapping]]] = ..., fertilizes: _Optional[_Iterable[int]] = ..., pollen_instance: _Optional[_Union[_stru_home_land_item_instance_pb2.HomeLandItemInstance, _Mapping]] = ..., pick_up_players: _Optional[_Mapping[int, int]] = ..., new_seeding_sec: _Optional[int] = ..., new_grow_end_sec: _Optional[int] = ..., new_pollinate_begin_sec: _Optional[int] = ..., new_pollinate_end_sec: _Optional[int] = ..., new_harvest_begin_sec: _Optional[int] = ..., new_harvest_end_sec: _Optional[int] = ...) -> None: ...
