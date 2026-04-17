import stru_community_transfer_pb2 as _stru_community_transfer_pb2
import stru_home_land_clutter_generation_record_pb2 as _stru_home_land_clutter_generation_record_pb2
import stru_home_land_clutter_info_pb2 as _stru_home_land_clutter_info_pb2
import stru_home_land_item_instance_pb2 as _stru_home_land_item_instance_pb2
import stru_home_land_sell_shop_info_pb2 as _stru_home_land_sell_shop_info_pb2
import stru_homeland_visit_info_pb2 as _stru_homeland_visit_info_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from collections.abc import Mapping as _Mapping
from typing import ClassVar as _ClassVar, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class HomelandBaseInfo(_message.Message):
    __slots__ = ("visit_info", "exp", "home_resource", "lastsubtractcleanlinesstime", "home_land_clutter", "home_land_clutter_generation_record", "home_land_sell_shop_info", "items", "slots", "item_to_slot", "capacity", "used_slots", "check_in_content", "transfer_community")
    class ItemsEntry(_message.Message):
        __slots__ = ("key", "value")
        KEY_FIELD_NUMBER: _ClassVar[int]
        VALUE_FIELD_NUMBER: _ClassVar[int]
        key: int
        value: _stru_home_land_item_instance_pb2.HomeLandItemInstance
        def __init__(self, key: _Optional[int] = ..., value: _Optional[_Union[_stru_home_land_item_instance_pb2.HomeLandItemInstance, _Mapping]] = ...) -> None: ...
    class SlotsEntry(_message.Message):
        __slots__ = ("key", "value")
        KEY_FIELD_NUMBER: _ClassVar[int]
        VALUE_FIELD_NUMBER: _ClassVar[int]
        key: int
        value: int
        def __init__(self, key: _Optional[int] = ..., value: _Optional[int] = ...) -> None: ...
    class ItemToSlotEntry(_message.Message):
        __slots__ = ("key", "value")
        KEY_FIELD_NUMBER: _ClassVar[int]
        VALUE_FIELD_NUMBER: _ClassVar[int]
        key: int
        value: int
        def __init__(self, key: _Optional[int] = ..., value: _Optional[int] = ...) -> None: ...
    VISIT_INFO_FIELD_NUMBER: _ClassVar[int]
    EXP_FIELD_NUMBER: _ClassVar[int]
    HOME_RESOURCE_FIELD_NUMBER: _ClassVar[int]
    LASTSUBTRACTCLEANLINESSTIME_FIELD_NUMBER: _ClassVar[int]
    HOME_LAND_CLUTTER_FIELD_NUMBER: _ClassVar[int]
    HOME_LAND_CLUTTER_GENERATION_RECORD_FIELD_NUMBER: _ClassVar[int]
    HOME_LAND_SELL_SHOP_INFO_FIELD_NUMBER: _ClassVar[int]
    ITEMS_FIELD_NUMBER: _ClassVar[int]
    SLOTS_FIELD_NUMBER: _ClassVar[int]
    ITEM_TO_SLOT_FIELD_NUMBER: _ClassVar[int]
    CAPACITY_FIELD_NUMBER: _ClassVar[int]
    USED_SLOTS_FIELD_NUMBER: _ClassVar[int]
    CHECK_IN_CONTENT_FIELD_NUMBER: _ClassVar[int]
    TRANSFER_COMMUNITY_FIELD_NUMBER: _ClassVar[int]
    visit_info: _stru_homeland_visit_info_pb2.HomelandVisitInfo
    exp: int
    home_resource: int
    lastsubtractcleanlinesstime: int
    home_land_clutter: _stru_home_land_clutter_info_pb2.HomeLandClutterInfo
    home_land_clutter_generation_record: _stru_home_land_clutter_generation_record_pb2.HomeLandClutterGenerationRecord
    home_land_sell_shop_info: _stru_home_land_sell_shop_info_pb2.HomeLandSellShopInfo
    items: _containers.MessageMap[int, _stru_home_land_item_instance_pb2.HomeLandItemInstance]
    slots: _containers.ScalarMap[int, int]
    item_to_slot: _containers.ScalarMap[int, int]
    capacity: int
    used_slots: int
    check_in_content: str
    transfer_community: _stru_community_transfer_pb2.CommunityTransfer
    def __init__(self, visit_info: _Optional[_Union[_stru_homeland_visit_info_pb2.HomelandVisitInfo, _Mapping]] = ..., exp: _Optional[int] = ..., home_resource: _Optional[int] = ..., lastsubtractcleanlinesstime: _Optional[int] = ..., home_land_clutter: _Optional[_Union[_stru_home_land_clutter_info_pb2.HomeLandClutterInfo, _Mapping]] = ..., home_land_clutter_generation_record: _Optional[_Union[_stru_home_land_clutter_generation_record_pb2.HomeLandClutterGenerationRecord, _Mapping]] = ..., home_land_sell_shop_info: _Optional[_Union[_stru_home_land_sell_shop_info_pb2.HomeLandSellShopInfo, _Mapping]] = ..., items: _Optional[_Mapping[int, _stru_home_land_item_instance_pb2.HomeLandItemInstance]] = ..., slots: _Optional[_Mapping[int, int]] = ..., item_to_slot: _Optional[_Mapping[int, int]] = ..., capacity: _Optional[int] = ..., used_slots: _Optional[int] = ..., check_in_content: _Optional[str] = ..., transfer_community: _Optional[_Union[_stru_community_transfer_pb2.CommunityTransfer, _Mapping]] = ...) -> None: ...
