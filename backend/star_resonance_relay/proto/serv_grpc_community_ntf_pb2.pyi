import stru_notify_community_apply_request_pb2 as _stru_notify_community_apply_request_pb2
import stru_notify_community_apply_update_request_pb2 as _stru_notify_community_apply_update_request_pb2
import stru_notify_community_check_in_change_request_pb2 as _stru_notify_community_check_in_change_request_pb2
import stru_notify_community_cleanliness_update_request_pb2 as _stru_notify_community_cleanliness_update_request_pb2
import stru_notify_community_cohabitant_info_request_pb2 as _stru_notify_community_cohabitant_info_request_pb2
import stru_notify_community_furniture_item_update_request_pb2 as _stru_notify_community_furniture_item_update_request_pb2
import stru_notify_community_global_authority_change_request_pb2 as _stru_notify_community_global_authority_change_request_pb2
import stru_notify_community_home_land_clutter_info_add_request_pb2 as _stru_notify_community_home_land_clutter_info_add_request_pb2
import stru_notify_community_home_land_clutter_info_remove_request_pb2 as _stru_notify_community_home_land_clutter_info_remove_request_pb2
import stru_notify_community_home_land_decoration_info_request_pb2 as _stru_notify_community_home_land_decoration_info_request_pb2
import stru_notify_community_home_land_sell_shop_update_request_pb2 as _stru_notify_community_home_land_sell_shop_update_request_pb2
import stru_notify_community_info_update_request_pb2 as _stru_notify_community_info_update_request_pb2
import stru_notify_community_introduction_change_request_pb2 as _stru_notify_community_introduction_change_request_pb2
import stru_notify_community_item_update_request_pb2 as _stru_notify_community_item_update_request_pb2
import stru_notify_community_level_update_request_pb2 as _stru_notify_community_level_update_request_pb2
import stru_notify_community_name_change_request_pb2 as _stru_notify_community_name_change_request_pb2
import stru_notify_community_transfer_change_request_pb2 as _stru_notify_community_transfer_change_request_pb2
import stru_notify_community_transfer_info_update_request_pb2 as _stru_notify_community_transfer_info_update_request_pb2
import stru_notify_flower_time_update_request_pb2 as _stru_notify_flower_time_update_request_pb2
import stru_notify_home_land_player_task_info_update_request_pb2 as _stru_notify_home_land_player_task_info_update_request_pb2
import stru_notify_homeland_build_furniture_op_request_pb2 as _stru_notify_homeland_build_furniture_op_request_pb2
import stru_notify_homeland_warehouse_grid_change_request_pb2 as _stru_notify_homeland_warehouse_grid_change_request_pb2
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from collections.abc import Mapping as _Mapping
from typing import ClassVar as _ClassVar, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class GrpcCommunityNtf(_message.Message):
    __slots__ = ()
    class NotifyHomelandWarehouseGridChange(_message.Message):
        __slots__ = ("request",)
        REQUEST_FIELD_NUMBER: _ClassVar[int]
        request: _stru_notify_homeland_warehouse_grid_change_request_pb2.NotifyHomelandWarehouseGridChangeRequest
        def __init__(self, request: _Optional[_Union[_stru_notify_homeland_warehouse_grid_change_request_pb2.NotifyHomelandWarehouseGridChangeRequest, _Mapping]] = ...) -> None: ...
    class NotifyCommunityApplyUpdate(_message.Message):
        __slots__ = ("request",)
        REQUEST_FIELD_NUMBER: _ClassVar[int]
        request: _stru_notify_community_apply_update_request_pb2.NotifyCommunityApplyUpdateRequest
        def __init__(self, request: _Optional[_Union[_stru_notify_community_apply_update_request_pb2.NotifyCommunityApplyUpdateRequest, _Mapping]] = ...) -> None: ...
    class NotifyCommunityInfoUpdate(_message.Message):
        __slots__ = ("request",)
        REQUEST_FIELD_NUMBER: _ClassVar[int]
        request: _stru_notify_community_info_update_request_pb2.NotifyCommunityInfoUpdateRequest
        def __init__(self, request: _Optional[_Union[_stru_notify_community_info_update_request_pb2.NotifyCommunityInfoUpdateRequest, _Mapping]] = ...) -> None: ...
    class NotifyCommunityTransferInfoUpdate(_message.Message):
        __slots__ = ("request",)
        REQUEST_FIELD_NUMBER: _ClassVar[int]
        request: _stru_notify_community_transfer_info_update_request_pb2.NotifyCommunityTransferInfoUpdateRequest
        def __init__(self, request: _Optional[_Union[_stru_notify_community_transfer_info_update_request_pb2.NotifyCommunityTransferInfoUpdateRequest, _Mapping]] = ...) -> None: ...
    class NotifyCommunityNameChange(_message.Message):
        __slots__ = ("request",)
        REQUEST_FIELD_NUMBER: _ClassVar[int]
        request: _stru_notify_community_name_change_request_pb2.NotifyCommunityNameChangeRequest
        def __init__(self, request: _Optional[_Union[_stru_notify_community_name_change_request_pb2.NotifyCommunityNameChangeRequest, _Mapping]] = ...) -> None: ...
    class NotifyCommunityIntroductionChange(_message.Message):
        __slots__ = ("request",)
        REQUEST_FIELD_NUMBER: _ClassVar[int]
        request: _stru_notify_community_introduction_change_request_pb2.NotifyCommunityIntroductionChangeRequest
        def __init__(self, request: _Optional[_Union[_stru_notify_community_introduction_change_request_pb2.NotifyCommunityIntroductionChangeRequest, _Mapping]] = ...) -> None: ...
    class NotifyCommunityCheckInChange(_message.Message):
        __slots__ = ("request",)
        REQUEST_FIELD_NUMBER: _ClassVar[int]
        request: _stru_notify_community_check_in_change_request_pb2.NotifyCommunityCheckInChangeRequest
        def __init__(self, request: _Optional[_Union[_stru_notify_community_check_in_change_request_pb2.NotifyCommunityCheckInChangeRequest, _Mapping]] = ...) -> None: ...
    class NotifyHomelandBuildFurnitureOp(_message.Message):
        __slots__ = ("request",)
        REQUEST_FIELD_NUMBER: _ClassVar[int]
        request: _stru_notify_homeland_build_furniture_op_request_pb2.NotifyHomelandBuildFurnitureOpRequest
        def __init__(self, request: _Optional[_Union[_stru_notify_homeland_build_furniture_op_request_pb2.NotifyHomelandBuildFurnitureOpRequest, _Mapping]] = ...) -> None: ...
    class NotifyCommunityCohabitantInfo(_message.Message):
        __slots__ = ("request",)
        REQUEST_FIELD_NUMBER: _ClassVar[int]
        request: _stru_notify_community_cohabitant_info_request_pb2.NotifyCommunityCohabitantInfoRequest
        def __init__(self, request: _Optional[_Union[_stru_notify_community_cohabitant_info_request_pb2.NotifyCommunityCohabitantInfoRequest, _Mapping]] = ...) -> None: ...
    class NotifyCommunityTransferChange(_message.Message):
        __slots__ = ("request",)
        REQUEST_FIELD_NUMBER: _ClassVar[int]
        request: _stru_notify_community_transfer_change_request_pb2.NotifyCommunityTransferChangeRequest
        def __init__(self, request: _Optional[_Union[_stru_notify_community_transfer_change_request_pb2.NotifyCommunityTransferChangeRequest, _Mapping]] = ...) -> None: ...
    class NotifyCommunityGlobalAuthorityChange(_message.Message):
        __slots__ = ("request",)
        REQUEST_FIELD_NUMBER: _ClassVar[int]
        request: _stru_notify_community_global_authority_change_request_pb2.NotifyCommunityGlobalAuthorityChangeRequest
        def __init__(self, request: _Optional[_Union[_stru_notify_community_global_authority_change_request_pb2.NotifyCommunityGlobalAuthorityChangeRequest, _Mapping]] = ...) -> None: ...
    class NotifyCommunityLevelUpdate(_message.Message):
        __slots__ = ("request",)
        REQUEST_FIELD_NUMBER: _ClassVar[int]
        request: _stru_notify_community_level_update_request_pb2.NotifyCommunityLevelUpdateRequest
        def __init__(self, request: _Optional[_Union[_stru_notify_community_level_update_request_pb2.NotifyCommunityLevelUpdateRequest, _Mapping]] = ...) -> None: ...
    class NotifyCommunityCleanlinessUpdate(_message.Message):
        __slots__ = ("request",)
        REQUEST_FIELD_NUMBER: _ClassVar[int]
        request: _stru_notify_community_cleanliness_update_request_pb2.NotifyCommunityCleanlinessUpdateRequest
        def __init__(self, request: _Optional[_Union[_stru_notify_community_cleanliness_update_request_pb2.NotifyCommunityCleanlinessUpdateRequest, _Mapping]] = ...) -> None: ...
    class NotifyCommunityHomeLandClutterInfoAdd(_message.Message):
        __slots__ = ("request",)
        REQUEST_FIELD_NUMBER: _ClassVar[int]
        request: _stru_notify_community_home_land_clutter_info_add_request_pb2.NotifyCommunityHomeLandClutterInfoAddRequest
        def __init__(self, request: _Optional[_Union[_stru_notify_community_home_land_clutter_info_add_request_pb2.NotifyCommunityHomeLandClutterInfoAddRequest, _Mapping]] = ...) -> None: ...
    class NotifyCommunityHomeLandClutterInfoRemove(_message.Message):
        __slots__ = ("request",)
        REQUEST_FIELD_NUMBER: _ClassVar[int]
        request: _stru_notify_community_home_land_clutter_info_remove_request_pb2.NotifyCommunityHomeLandClutterInfoRemoveRequest
        def __init__(self, request: _Optional[_Union[_stru_notify_community_home_land_clutter_info_remove_request_pb2.NotifyCommunityHomeLandClutterInfoRemoveRequest, _Mapping]] = ...) -> None: ...
    class NotifyHomeLandPlayerTaskInfoUpdate(_message.Message):
        __slots__ = ("request",)
        REQUEST_FIELD_NUMBER: _ClassVar[int]
        request: _stru_notify_home_land_player_task_info_update_request_pb2.NotifyHomeLandPlayerTaskInfoUpdateRequest
        def __init__(self, request: _Optional[_Union[_stru_notify_home_land_player_task_info_update_request_pb2.NotifyHomeLandPlayerTaskInfoUpdateRequest, _Mapping]] = ...) -> None: ...
    class NotifyCommunityHomeLandSellShopUpdate(_message.Message):
        __slots__ = ("request",)
        REQUEST_FIELD_NUMBER: _ClassVar[int]
        request: _stru_notify_community_home_land_sell_shop_update_request_pb2.NotifyCommunityHomeLandSellShopUpdateRequest
        def __init__(self, request: _Optional[_Union[_stru_notify_community_home_land_sell_shop_update_request_pb2.NotifyCommunityHomeLandSellShopUpdateRequest, _Mapping]] = ...) -> None: ...
    class NotifyCommunityHomeLandDecorationInfo(_message.Message):
        __slots__ = ("request",)
        REQUEST_FIELD_NUMBER: _ClassVar[int]
        request: _stru_notify_community_home_land_decoration_info_request_pb2.NotifyCommunityHomeLandDecorationInfoRequest
        def __init__(self, request: _Optional[_Union[_stru_notify_community_home_land_decoration_info_request_pb2.NotifyCommunityHomeLandDecorationInfoRequest, _Mapping]] = ...) -> None: ...
    class NotifyCommunityItemUpdate(_message.Message):
        __slots__ = ("request",)
        REQUEST_FIELD_NUMBER: _ClassVar[int]
        request: _stru_notify_community_item_update_request_pb2.NotifyCommunityItemUpdateRequest
        def __init__(self, request: _Optional[_Union[_stru_notify_community_item_update_request_pb2.NotifyCommunityItemUpdateRequest, _Mapping]] = ...) -> None: ...
    class NotifyCommunityFurnitureItemUpdate(_message.Message):
        __slots__ = ("request",)
        REQUEST_FIELD_NUMBER: _ClassVar[int]
        request: _stru_notify_community_furniture_item_update_request_pb2.NotifyCommunityFurnitureItemUpdateRequest
        def __init__(self, request: _Optional[_Union[_stru_notify_community_furniture_item_update_request_pb2.NotifyCommunityFurnitureItemUpdateRequest, _Mapping]] = ...) -> None: ...
    class NotifyCommunityApply(_message.Message):
        __slots__ = ("request",)
        REQUEST_FIELD_NUMBER: _ClassVar[int]
        request: _stru_notify_community_apply_request_pb2.NotifyCommunityApplyRequest
        def __init__(self, request: _Optional[_Union[_stru_notify_community_apply_request_pb2.NotifyCommunityApplyRequest, _Mapping]] = ...) -> None: ...
    class NotifyFlowerTimeUpdate(_message.Message):
        __slots__ = ("request",)
        REQUEST_FIELD_NUMBER: _ClassVar[int]
        request: _stru_notify_flower_time_update_request_pb2.NotifyFlowerTimeUpdateRequest
        def __init__(self, request: _Optional[_Union[_stru_notify_flower_time_update_request_pb2.NotifyFlowerTimeUpdateRequest, _Mapping]] = ...) -> None: ...
    def __init__(self) -> None: ...
