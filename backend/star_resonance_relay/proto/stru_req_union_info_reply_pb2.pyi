import enum_e_error_code_pb2 as _enum_e_error_code_pb2
import stru_mem_union_activity_pb2 as _stru_mem_union_activity_pb2
import stru_recruit_info_pb2 as _stru_recruit_info_pb2
import stru_union_activity_pb2 as _stru_union_activity_pb2
import stru_union_building_pb2 as _stru_union_building_pb2
import stru_union_effect_buff_pb2 as _stru_union_effect_buff_pb2
import stru_union_info_pb2 as _stru_union_info_pb2
import stru_union_resource_pb2 as _stru_union_resource_pb2
import stru_user_summary_data_pb2 as _stru_user_summary_data_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from collections.abc import Iterable as _Iterable, Mapping as _Mapping
from typing import ClassVar as _ClassVar, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class ReqUnionInfoReply(_message.Message):
    __slots__ = ("info", "recruit_info", "president_info", "union_buildings", "union_activity", "self_activity", "union_resource_lib", "self_speed_times", "effect_buffs", "received_point_award_ids", "err_code")
    class UnionBuildingsEntry(_message.Message):
        __slots__ = ("key", "value")
        KEY_FIELD_NUMBER: _ClassVar[int]
        VALUE_FIELD_NUMBER: _ClassVar[int]
        key: int
        value: _stru_union_building_pb2.UnionBuilding
        def __init__(self, key: _Optional[int] = ..., value: _Optional[_Union[_stru_union_building_pb2.UnionBuilding, _Mapping]] = ...) -> None: ...
    class UnionResourceLibEntry(_message.Message):
        __slots__ = ("key", "value")
        KEY_FIELD_NUMBER: _ClassVar[int]
        VALUE_FIELD_NUMBER: _ClassVar[int]
        key: int
        value: _stru_union_resource_pb2.UnionResource
        def __init__(self, key: _Optional[int] = ..., value: _Optional[_Union[_stru_union_resource_pb2.UnionResource, _Mapping]] = ...) -> None: ...
    INFO_FIELD_NUMBER: _ClassVar[int]
    RECRUIT_INFO_FIELD_NUMBER: _ClassVar[int]
    PRESIDENT_INFO_FIELD_NUMBER: _ClassVar[int]
    UNION_BUILDINGS_FIELD_NUMBER: _ClassVar[int]
    UNION_ACTIVITY_FIELD_NUMBER: _ClassVar[int]
    SELF_ACTIVITY_FIELD_NUMBER: _ClassVar[int]
    UNION_RESOURCE_LIB_FIELD_NUMBER: _ClassVar[int]
    SELF_SPEED_TIMES_FIELD_NUMBER: _ClassVar[int]
    EFFECT_BUFFS_FIELD_NUMBER: _ClassVar[int]
    RECEIVED_POINT_AWARD_IDS_FIELD_NUMBER: _ClassVar[int]
    ERR_CODE_FIELD_NUMBER: _ClassVar[int]
    info: _stru_union_info_pb2.UnionInfo
    recruit_info: _stru_recruit_info_pb2.RecruitInfo
    president_info: _stru_user_summary_data_pb2.UserSummaryData
    union_buildings: _containers.MessageMap[int, _stru_union_building_pb2.UnionBuilding]
    union_activity: _stru_union_activity_pb2.UnionActivity
    self_activity: _stru_mem_union_activity_pb2.MemUnionActivity
    union_resource_lib: _containers.MessageMap[int, _stru_union_resource_pb2.UnionResource]
    self_speed_times: int
    effect_buffs: _containers.RepeatedCompositeFieldContainer[_stru_union_effect_buff_pb2.UnionEffectBuff]
    received_point_award_ids: _containers.RepeatedScalarFieldContainer[int]
    err_code: _enum_e_error_code_pb2.EErrorCode
    def __init__(self, info: _Optional[_Union[_stru_union_info_pb2.UnionInfo, _Mapping]] = ..., recruit_info: _Optional[_Union[_stru_recruit_info_pb2.RecruitInfo, _Mapping]] = ..., president_info: _Optional[_Union[_stru_user_summary_data_pb2.UserSummaryData, _Mapping]] = ..., union_buildings: _Optional[_Mapping[int, _stru_union_building_pb2.UnionBuilding]] = ..., union_activity: _Optional[_Union[_stru_union_activity_pb2.UnionActivity, _Mapping]] = ..., self_activity: _Optional[_Union[_stru_mem_union_activity_pb2.MemUnionActivity, _Mapping]] = ..., union_resource_lib: _Optional[_Mapping[int, _stru_union_resource_pb2.UnionResource]] = ..., self_speed_times: _Optional[int] = ..., effect_buffs: _Optional[_Iterable[_Union[_stru_union_effect_buff_pb2.UnionEffectBuff, _Mapping]]] = ..., received_point_award_ids: _Optional[_Iterable[int]] = ..., err_code: _Optional[_Union[_enum_e_error_code_pb2.EErrorCode, str]] = ...) -> None: ...
