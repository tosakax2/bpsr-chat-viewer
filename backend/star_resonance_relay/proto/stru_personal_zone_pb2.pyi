import stru_action_info_pb2 as _stru_action_info_pb2
import stru_editor_u_i_position_pb2 as _stru_editor_u_i_position_pb2
import stru_fashion_quality_collect_info_pb2 as _stru_fashion_quality_collect_info_pb2
import stru_ride_quality_collect_info_pb2 as _stru_ride_quality_collect_info_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from collections.abc import Iterable as _Iterable, Mapping as _Mapping
from typing import ClassVar as _ClassVar, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class PersonalZone(_message.Message):
    __slots__ = ("online_periods", "tags", "medals", "theme_id", "business_card_style_id", "avatar_frame_id", "action_info", "ui_position", "title_id", "fashion_refresh_flag", "fashion_collect_point", "fashion_collect_quality_count", "photos", "unlock_target_record", "unlock_get_reward_record", "ride_collect_point", "ride_collect_quality_count", "weapon_skin_collect_point", "photos_wall")
    class MedalsEntry(_message.Message):
        __slots__ = ("key", "value")
        KEY_FIELD_NUMBER: _ClassVar[int]
        VALUE_FIELD_NUMBER: _ClassVar[int]
        key: int
        value: int
        def __init__(self, key: _Optional[int] = ..., value: _Optional[int] = ...) -> None: ...
    class FashionCollectQualityCountEntry(_message.Message):
        __slots__ = ("key", "value")
        KEY_FIELD_NUMBER: _ClassVar[int]
        VALUE_FIELD_NUMBER: _ClassVar[int]
        key: int
        value: _stru_fashion_quality_collect_info_pb2.FashionQualityCollectInfo
        def __init__(self, key: _Optional[int] = ..., value: _Optional[_Union[_stru_fashion_quality_collect_info_pb2.FashionQualityCollectInfo, _Mapping]] = ...) -> None: ...
    class UnlockTargetRecordEntry(_message.Message):
        __slots__ = ("key", "value")
        KEY_FIELD_NUMBER: _ClassVar[int]
        VALUE_FIELD_NUMBER: _ClassVar[int]
        key: int
        value: int
        def __init__(self, key: _Optional[int] = ..., value: _Optional[int] = ...) -> None: ...
    class UnlockGetRewardRecordEntry(_message.Message):
        __slots__ = ("key", "value")
        KEY_FIELD_NUMBER: _ClassVar[int]
        VALUE_FIELD_NUMBER: _ClassVar[int]
        key: int
        value: bool
        def __init__(self, key: _Optional[int] = ..., value: bool = ...) -> None: ...
    class RideCollectQualityCountEntry(_message.Message):
        __slots__ = ("key", "value")
        KEY_FIELD_NUMBER: _ClassVar[int]
        VALUE_FIELD_NUMBER: _ClassVar[int]
        key: int
        value: _stru_ride_quality_collect_info_pb2.RideQualityCollectInfo
        def __init__(self, key: _Optional[int] = ..., value: _Optional[_Union[_stru_ride_quality_collect_info_pb2.RideQualityCollectInfo, _Mapping]] = ...) -> None: ...
    class PhotosWallEntry(_message.Message):
        __slots__ = ("key", "value")
        KEY_FIELD_NUMBER: _ClassVar[int]
        VALUE_FIELD_NUMBER: _ClassVar[int]
        key: int
        value: int
        def __init__(self, key: _Optional[int] = ..., value: _Optional[int] = ...) -> None: ...
    ONLINE_PERIODS_FIELD_NUMBER: _ClassVar[int]
    TAGS_FIELD_NUMBER: _ClassVar[int]
    MEDALS_FIELD_NUMBER: _ClassVar[int]
    THEME_ID_FIELD_NUMBER: _ClassVar[int]
    BUSINESS_CARD_STYLE_ID_FIELD_NUMBER: _ClassVar[int]
    AVATAR_FRAME_ID_FIELD_NUMBER: _ClassVar[int]
    ACTION_INFO_FIELD_NUMBER: _ClassVar[int]
    UI_POSITION_FIELD_NUMBER: _ClassVar[int]
    TITLE_ID_FIELD_NUMBER: _ClassVar[int]
    FASHION_REFRESH_FLAG_FIELD_NUMBER: _ClassVar[int]
    FASHION_COLLECT_POINT_FIELD_NUMBER: _ClassVar[int]
    FASHION_COLLECT_QUALITY_COUNT_FIELD_NUMBER: _ClassVar[int]
    PHOTOS_FIELD_NUMBER: _ClassVar[int]
    UNLOCK_TARGET_RECORD_FIELD_NUMBER: _ClassVar[int]
    UNLOCK_GET_REWARD_RECORD_FIELD_NUMBER: _ClassVar[int]
    RIDE_COLLECT_POINT_FIELD_NUMBER: _ClassVar[int]
    RIDE_COLLECT_QUALITY_COUNT_FIELD_NUMBER: _ClassVar[int]
    WEAPON_SKIN_COLLECT_POINT_FIELD_NUMBER: _ClassVar[int]
    PHOTOS_WALL_FIELD_NUMBER: _ClassVar[int]
    online_periods: _containers.RepeatedScalarFieldContainer[int]
    tags: _containers.RepeatedScalarFieldContainer[int]
    medals: _containers.ScalarMap[int, int]
    theme_id: int
    business_card_style_id: int
    avatar_frame_id: int
    action_info: _stru_action_info_pb2.ActionInfo
    ui_position: _containers.RepeatedCompositeFieldContainer[_stru_editor_u_i_position_pb2.EditorUIPosition]
    title_id: int
    fashion_refresh_flag: bool
    fashion_collect_point: int
    fashion_collect_quality_count: _containers.MessageMap[int, _stru_fashion_quality_collect_info_pb2.FashionQualityCollectInfo]
    photos: _containers.RepeatedScalarFieldContainer[int]
    unlock_target_record: _containers.ScalarMap[int, int]
    unlock_get_reward_record: _containers.ScalarMap[int, bool]
    ride_collect_point: int
    ride_collect_quality_count: _containers.MessageMap[int, _stru_ride_quality_collect_info_pb2.RideQualityCollectInfo]
    weapon_skin_collect_point: int
    photos_wall: _containers.ScalarMap[int, int]
    def __init__(self, online_periods: _Optional[_Iterable[int]] = ..., tags: _Optional[_Iterable[int]] = ..., medals: _Optional[_Mapping[int, int]] = ..., theme_id: _Optional[int] = ..., business_card_style_id: _Optional[int] = ..., avatar_frame_id: _Optional[int] = ..., action_info: _Optional[_Union[_stru_action_info_pb2.ActionInfo, _Mapping]] = ..., ui_position: _Optional[_Iterable[_Union[_stru_editor_u_i_position_pb2.EditorUIPosition, _Mapping]]] = ..., title_id: _Optional[int] = ..., fashion_refresh_flag: bool = ..., fashion_collect_point: _Optional[int] = ..., fashion_collect_quality_count: _Optional[_Mapping[int, _stru_fashion_quality_collect_info_pb2.FashionQualityCollectInfo]] = ..., photos: _Optional[_Iterable[int]] = ..., unlock_target_record: _Optional[_Mapping[int, int]] = ..., unlock_get_reward_record: _Optional[_Mapping[int, bool]] = ..., ride_collect_point: _Optional[int] = ..., ride_collect_quality_count: _Optional[_Mapping[int, _stru_ride_quality_collect_info_pb2.RideQualityCollectInfo]] = ..., weapon_skin_collect_point: _Optional[int] = ..., photos_wall: _Optional[_Mapping[int, int]] = ...) -> None: ...
