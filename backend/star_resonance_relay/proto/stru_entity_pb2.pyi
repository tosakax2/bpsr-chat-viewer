import stru_attr_collection_pb2 as _stru_attr_collection_pb2
import stru_temp_attr_collection_pb2 as _stru_temp_attr_collection_pb2
import stru_actor_body_part_infos_pb2 as _stru_actor_body_part_infos_pb2
import stru_seq_passive_skill_info_pb2 as _stru_seq_passive_skill_info_pb2
import stru_buff_info_sync_pb2 as _stru_buff_info_sync_pb2
import stru_buff_effect_sync_pb2 as _stru_buff_effect_sync_pb2
import enum_e_entity_type_pb2 as _enum_e_entity_type_pb2
import enum_e_appear_type_pb2 as _enum_e_appear_type_pb2
import stru_magnetic_queue_appear_info_pb2 as _stru_magnetic_queue_appear_info_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from collections.abc import Mapping as _Mapping
from typing import ClassVar as _ClassVar, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class Entity(_message.Message):
    __slots__ = ("uuid", "ent_type", "attrs", "temp_attrs", "body_part_infos", "passive_skill_infos", "buff_infos", "buff_effect", "appear_type", "magnetic_ride_queue_change_info_dict")
    class MagneticRideQueueChangeInfoDictEntry(_message.Message):
        __slots__ = ("key", "value")
        KEY_FIELD_NUMBER: _ClassVar[int]
        VALUE_FIELD_NUMBER: _ClassVar[int]
        key: int
        value: _stru_magnetic_queue_appear_info_pb2.MagneticQueueAppearInfo
        def __init__(self, key: _Optional[int] = ..., value: _Optional[_Union[_stru_magnetic_queue_appear_info_pb2.MagneticQueueAppearInfo, _Mapping]] = ...) -> None: ...
    UUID_FIELD_NUMBER: _ClassVar[int]
    ENT_TYPE_FIELD_NUMBER: _ClassVar[int]
    ATTRS_FIELD_NUMBER: _ClassVar[int]
    TEMP_ATTRS_FIELD_NUMBER: _ClassVar[int]
    BODY_PART_INFOS_FIELD_NUMBER: _ClassVar[int]
    PASSIVE_SKILL_INFOS_FIELD_NUMBER: _ClassVar[int]
    BUFF_INFOS_FIELD_NUMBER: _ClassVar[int]
    BUFF_EFFECT_FIELD_NUMBER: _ClassVar[int]
    APPEAR_TYPE_FIELD_NUMBER: _ClassVar[int]
    MAGNETIC_RIDE_QUEUE_CHANGE_INFO_DICT_FIELD_NUMBER: _ClassVar[int]
    uuid: int
    ent_type: _enum_e_entity_type_pb2.EEntityType
    attrs: _stru_attr_collection_pb2.AttrCollection
    temp_attrs: _stru_temp_attr_collection_pb2.TempAttrCollection
    body_part_infos: _stru_actor_body_part_infos_pb2.ActorBodyPartInfos
    passive_skill_infos: _stru_seq_passive_skill_info_pb2.SeqPassiveSkillInfo
    buff_infos: _stru_buff_info_sync_pb2.BuffInfoSync
    buff_effect: _stru_buff_effect_sync_pb2.BuffEffectSync
    appear_type: _enum_e_appear_type_pb2.EAppearType
    magnetic_ride_queue_change_info_dict: _containers.MessageMap[int, _stru_magnetic_queue_appear_info_pb2.MagneticQueueAppearInfo]
    def __init__(self, uuid: _Optional[int] = ..., ent_type: _Optional[_Union[_enum_e_entity_type_pb2.EEntityType, str]] = ..., attrs: _Optional[_Union[_stru_attr_collection_pb2.AttrCollection, _Mapping]] = ..., temp_attrs: _Optional[_Union[_stru_temp_attr_collection_pb2.TempAttrCollection, _Mapping]] = ..., body_part_infos: _Optional[_Union[_stru_actor_body_part_infos_pb2.ActorBodyPartInfos, _Mapping]] = ..., passive_skill_infos: _Optional[_Union[_stru_seq_passive_skill_info_pb2.SeqPassiveSkillInfo, _Mapping]] = ..., buff_infos: _Optional[_Union[_stru_buff_info_sync_pb2.BuffInfoSync, _Mapping]] = ..., buff_effect: _Optional[_Union[_stru_buff_effect_sync_pb2.BuffEffectSync, _Mapping]] = ..., appear_type: _Optional[_Union[_enum_e_appear_type_pb2.EAppearType, str]] = ..., magnetic_ride_queue_change_info_dict: _Optional[_Mapping[int, _stru_magnetic_queue_appear_info_pb2.MagneticQueueAppearInfo]] = ...) -> None: ...
