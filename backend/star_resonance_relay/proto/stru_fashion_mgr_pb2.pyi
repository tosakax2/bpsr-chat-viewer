import stru_fashion_advance_info_pb2 as _stru_fashion_advance_info_pb2
import stru_fashion_color_info_pb2 as _stru_fashion_color_info_pb2
import stru_unlock_color_info_pb2 as _stru_unlock_color_info_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from collections.abc import Mapping as _Mapping
from typing import ClassVar as _ClassVar, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class FashionMgr(_message.Message):
    __slots__ = ("wear_info", "fashion_datas", "unlock_color", "fashion_reward", "all_fashion", "all_ride", "all_weapon_skin", "fashion_advance", "fashion_collect_point", "ride_collect_point", "weapon_skin_collect_point", "all_fashion_num", "all_ride_num", "all_weapon_skin_num", "is_fashion_init", "is_ride_init", "is_weapon_skin_init", "fashion_unlock_fix_flag")
    class WearInfoEntry(_message.Message):
        __slots__ = ("key", "value")
        KEY_FIELD_NUMBER: _ClassVar[int]
        VALUE_FIELD_NUMBER: _ClassVar[int]
        key: int
        value: int
        def __init__(self, key: _Optional[int] = ..., value: _Optional[int] = ...) -> None: ...
    class FashionDatasEntry(_message.Message):
        __slots__ = ("key", "value")
        KEY_FIELD_NUMBER: _ClassVar[int]
        VALUE_FIELD_NUMBER: _ClassVar[int]
        key: int
        value: _stru_fashion_color_info_pb2.FashionColorInfo
        def __init__(self, key: _Optional[int] = ..., value: _Optional[_Union[_stru_fashion_color_info_pb2.FashionColorInfo, _Mapping]] = ...) -> None: ...
    class UnlockColorEntry(_message.Message):
        __slots__ = ("key", "value")
        KEY_FIELD_NUMBER: _ClassVar[int]
        VALUE_FIELD_NUMBER: _ClassVar[int]
        key: int
        value: _stru_unlock_color_info_pb2.UnlockColorInfo
        def __init__(self, key: _Optional[int] = ..., value: _Optional[_Union[_stru_unlock_color_info_pb2.UnlockColorInfo, _Mapping]] = ...) -> None: ...
    class FashionRewardEntry(_message.Message):
        __slots__ = ("key", "value")
        KEY_FIELD_NUMBER: _ClassVar[int]
        VALUE_FIELD_NUMBER: _ClassVar[int]
        key: int
        value: bool
        def __init__(self, key: _Optional[int] = ..., value: bool = ...) -> None: ...
    class AllFashionEntry(_message.Message):
        __slots__ = ("key", "value")
        KEY_FIELD_NUMBER: _ClassVar[int]
        VALUE_FIELD_NUMBER: _ClassVar[int]
        key: int
        value: bool
        def __init__(self, key: _Optional[int] = ..., value: bool = ...) -> None: ...
    class AllRideEntry(_message.Message):
        __slots__ = ("key", "value")
        KEY_FIELD_NUMBER: _ClassVar[int]
        VALUE_FIELD_NUMBER: _ClassVar[int]
        key: int
        value: bool
        def __init__(self, key: _Optional[int] = ..., value: bool = ...) -> None: ...
    class AllWeaponSkinEntry(_message.Message):
        __slots__ = ("key", "value")
        KEY_FIELD_NUMBER: _ClassVar[int]
        VALUE_FIELD_NUMBER: _ClassVar[int]
        key: int
        value: bool
        def __init__(self, key: _Optional[int] = ..., value: bool = ...) -> None: ...
    class FashionAdvanceEntry(_message.Message):
        __slots__ = ("key", "value")
        KEY_FIELD_NUMBER: _ClassVar[int]
        VALUE_FIELD_NUMBER: _ClassVar[int]
        key: int
        value: _stru_fashion_advance_info_pb2.FashionAdvanceInfo
        def __init__(self, key: _Optional[int] = ..., value: _Optional[_Union[_stru_fashion_advance_info_pb2.FashionAdvanceInfo, _Mapping]] = ...) -> None: ...
    class AllFashionNumEntry(_message.Message):
        __slots__ = ("key", "value")
        KEY_FIELD_NUMBER: _ClassVar[int]
        VALUE_FIELD_NUMBER: _ClassVar[int]
        key: int
        value: int
        def __init__(self, key: _Optional[int] = ..., value: _Optional[int] = ...) -> None: ...
    class AllRideNumEntry(_message.Message):
        __slots__ = ("key", "value")
        KEY_FIELD_NUMBER: _ClassVar[int]
        VALUE_FIELD_NUMBER: _ClassVar[int]
        key: int
        value: int
        def __init__(self, key: _Optional[int] = ..., value: _Optional[int] = ...) -> None: ...
    class AllWeaponSkinNumEntry(_message.Message):
        __slots__ = ("key", "value")
        KEY_FIELD_NUMBER: _ClassVar[int]
        VALUE_FIELD_NUMBER: _ClassVar[int]
        key: int
        value: int
        def __init__(self, key: _Optional[int] = ..., value: _Optional[int] = ...) -> None: ...
    WEAR_INFO_FIELD_NUMBER: _ClassVar[int]
    FASHION_DATAS_FIELD_NUMBER: _ClassVar[int]
    UNLOCK_COLOR_FIELD_NUMBER: _ClassVar[int]
    FASHION_REWARD_FIELD_NUMBER: _ClassVar[int]
    ALL_FASHION_FIELD_NUMBER: _ClassVar[int]
    ALL_RIDE_FIELD_NUMBER: _ClassVar[int]
    ALL_WEAPON_SKIN_FIELD_NUMBER: _ClassVar[int]
    FASHION_ADVANCE_FIELD_NUMBER: _ClassVar[int]
    FASHION_COLLECT_POINT_FIELD_NUMBER: _ClassVar[int]
    RIDE_COLLECT_POINT_FIELD_NUMBER: _ClassVar[int]
    WEAPON_SKIN_COLLECT_POINT_FIELD_NUMBER: _ClassVar[int]
    ALL_FASHION_NUM_FIELD_NUMBER: _ClassVar[int]
    ALL_RIDE_NUM_FIELD_NUMBER: _ClassVar[int]
    ALL_WEAPON_SKIN_NUM_FIELD_NUMBER: _ClassVar[int]
    IS_FASHION_INIT_FIELD_NUMBER: _ClassVar[int]
    IS_RIDE_INIT_FIELD_NUMBER: _ClassVar[int]
    IS_WEAPON_SKIN_INIT_FIELD_NUMBER: _ClassVar[int]
    FASHION_UNLOCK_FIX_FLAG_FIELD_NUMBER: _ClassVar[int]
    wear_info: _containers.ScalarMap[int, int]
    fashion_datas: _containers.MessageMap[int, _stru_fashion_color_info_pb2.FashionColorInfo]
    unlock_color: _containers.MessageMap[int, _stru_unlock_color_info_pb2.UnlockColorInfo]
    fashion_reward: _containers.ScalarMap[int, bool]
    all_fashion: _containers.ScalarMap[int, bool]
    all_ride: _containers.ScalarMap[int, bool]
    all_weapon_skin: _containers.ScalarMap[int, bool]
    fashion_advance: _containers.MessageMap[int, _stru_fashion_advance_info_pb2.FashionAdvanceInfo]
    fashion_collect_point: int
    ride_collect_point: int
    weapon_skin_collect_point: int
    all_fashion_num: _containers.ScalarMap[int, int]
    all_ride_num: _containers.ScalarMap[int, int]
    all_weapon_skin_num: _containers.ScalarMap[int, int]
    is_fashion_init: bool
    is_ride_init: bool
    is_weapon_skin_init: bool
    fashion_unlock_fix_flag: int
    def __init__(self, wear_info: _Optional[_Mapping[int, int]] = ..., fashion_datas: _Optional[_Mapping[int, _stru_fashion_color_info_pb2.FashionColorInfo]] = ..., unlock_color: _Optional[_Mapping[int, _stru_unlock_color_info_pb2.UnlockColorInfo]] = ..., fashion_reward: _Optional[_Mapping[int, bool]] = ..., all_fashion: _Optional[_Mapping[int, bool]] = ..., all_ride: _Optional[_Mapping[int, bool]] = ..., all_weapon_skin: _Optional[_Mapping[int, bool]] = ..., fashion_advance: _Optional[_Mapping[int, _stru_fashion_advance_info_pb2.FashionAdvanceInfo]] = ..., fashion_collect_point: _Optional[int] = ..., ride_collect_point: _Optional[int] = ..., weapon_skin_collect_point: _Optional[int] = ..., all_fashion_num: _Optional[_Mapping[int, int]] = ..., all_ride_num: _Optional[_Mapping[int, int]] = ..., all_weapon_skin_num: _Optional[_Mapping[int, int]] = ..., is_fashion_init: bool = ..., is_ride_init: bool = ..., is_weapon_skin_init: bool = ..., fashion_unlock_fix_flag: _Optional[int] = ...) -> None: ...
