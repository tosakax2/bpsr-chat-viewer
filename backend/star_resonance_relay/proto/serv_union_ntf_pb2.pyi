import stru_notify_building_upgrade_end_request_pb2 as _stru_notify_building_upgrade_end_request_pb2
import stru_notify_effect_buf_change_request_pb2 as _stru_notify_effect_buf_change_request_pb2
import stru_notify_invite_join_union_request_pb2 as _stru_notify_invite_join_union_request_pb2
import stru_notify_member_online_request_pb2 as _stru_notify_member_online_request_pb2
import stru_notify_official_limit_update_request_pb2 as _stru_notify_official_limit_update_request_pb2
import stru_notify_request_list_num_request_pb2 as _stru_notify_request_list_num_request_pb2
import stru_notify_union_activity_progress_request_pb2 as _stru_notify_union_activity_progress_request_pb2
import stru_notify_union_activity_request_pb2 as _stru_notify_union_activity_request_pb2
import stru_notify_union_info_request_pb2 as _stru_notify_union_info_request_pb2
import stru_notify_union_official_change_request_pb2 as _stru_notify_union_official_change_request_pb2
import stru_notify_union_resource_change_request_pb2 as _stru_notify_union_resource_change_request_pb2
import stru_notify_union_sub_func_unlock_request_pb2 as _stru_notify_union_sub_func_unlock_request_pb2
import stru_notify_update_member_request_pb2 as _stru_notify_update_member_request_pb2
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from collections.abc import Mapping as _Mapping
from typing import ClassVar as _ClassVar, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class UnionNtf(_message.Message):
    __slots__ = ()
    class NotifyUnionInfo(_message.Message):
        __slots__ = ("v_request",)
        V_REQUEST_FIELD_NUMBER: _ClassVar[int]
        v_request: _stru_notify_union_info_request_pb2.NotifyUnionInfoRequest
        def __init__(self, v_request: _Optional[_Union[_stru_notify_union_info_request_pb2.NotifyUnionInfoRequest, _Mapping]] = ...) -> None: ...
    class NotifyOfficialLimitUpdate(_message.Message):
        __slots__ = ("v_request",)
        V_REQUEST_FIELD_NUMBER: _ClassVar[int]
        v_request: _stru_notify_official_limit_update_request_pb2.NotifyOfficialLimitUpdateRequest
        def __init__(self, v_request: _Optional[_Union[_stru_notify_official_limit_update_request_pb2.NotifyOfficialLimitUpdateRequest, _Mapping]] = ...) -> None: ...
    class NotifyUpdateMember(_message.Message):
        __slots__ = ("v_request",)
        V_REQUEST_FIELD_NUMBER: _ClassVar[int]
        v_request: _stru_notify_update_member_request_pb2.NotifyUpdateMemberRequest
        def __init__(self, v_request: _Optional[_Union[_stru_notify_update_member_request_pb2.NotifyUpdateMemberRequest, _Mapping]] = ...) -> None: ...
    class NotifyRequestListNum(_message.Message):
        __slots__ = ("v_request",)
        V_REQUEST_FIELD_NUMBER: _ClassVar[int]
        v_request: _stru_notify_request_list_num_request_pb2.NotifyRequestListNumRequest
        def __init__(self, v_request: _Optional[_Union[_stru_notify_request_list_num_request_pb2.NotifyRequestListNumRequest, _Mapping]] = ...) -> None: ...
    class NotifyInviteJoinUnion(_message.Message):
        __slots__ = ("v_request",)
        V_REQUEST_FIELD_NUMBER: _ClassVar[int]
        v_request: _stru_notify_invite_join_union_request_pb2.NotifyInviteJoinUnionRequest
        def __init__(self, v_request: _Optional[_Union[_stru_notify_invite_join_union_request_pb2.NotifyInviteJoinUnionRequest, _Mapping]] = ...) -> None: ...
    class NotifyUnionActivity(_message.Message):
        __slots__ = ("v_request",)
        V_REQUEST_FIELD_NUMBER: _ClassVar[int]
        v_request: _stru_notify_union_activity_request_pb2.NotifyUnionActivityRequest
        def __init__(self, v_request: _Optional[_Union[_stru_notify_union_activity_request_pb2.NotifyUnionActivityRequest, _Mapping]] = ...) -> None: ...
    class NotifyUnionActivityProgress(_message.Message):
        __slots__ = ("v_request",)
        V_REQUEST_FIELD_NUMBER: _ClassVar[int]
        v_request: _stru_notify_union_activity_progress_request_pb2.NotifyUnionActivityProgressRequest
        def __init__(self, v_request: _Optional[_Union[_stru_notify_union_activity_progress_request_pb2.NotifyUnionActivityProgressRequest, _Mapping]] = ...) -> None: ...
    class NotifyUnionResourceChange(_message.Message):
        __slots__ = ("v_request",)
        V_REQUEST_FIELD_NUMBER: _ClassVar[int]
        v_request: _stru_notify_union_resource_change_request_pb2.NotifyUnionResourceChangeRequest
        def __init__(self, v_request: _Optional[_Union[_stru_notify_union_resource_change_request_pb2.NotifyUnionResourceChangeRequest, _Mapping]] = ...) -> None: ...
    class NotifyBuildingUpgradeEnd(_message.Message):
        __slots__ = ("v_request",)
        V_REQUEST_FIELD_NUMBER: _ClassVar[int]
        v_request: _stru_notify_building_upgrade_end_request_pb2.NotifyBuildingUpgradeEndRequest
        def __init__(self, v_request: _Optional[_Union[_stru_notify_building_upgrade_end_request_pb2.NotifyBuildingUpgradeEndRequest, _Mapping]] = ...) -> None: ...
    class NotifyEffectBufChange(_message.Message):
        __slots__ = ("v_request",)
        V_REQUEST_FIELD_NUMBER: _ClassVar[int]
        v_request: _stru_notify_effect_buf_change_request_pb2.NotifyEffectBufChangeRequest
        def __init__(self, v_request: _Optional[_Union[_stru_notify_effect_buf_change_request_pb2.NotifyEffectBufChangeRequest, _Mapping]] = ...) -> None: ...
    class NotifyUnionOfficialChange(_message.Message):
        __slots__ = ("v_request",)
        V_REQUEST_FIELD_NUMBER: _ClassVar[int]
        v_request: _stru_notify_union_official_change_request_pb2.NotifyUnionOfficialChangeRequest
        def __init__(self, v_request: _Optional[_Union[_stru_notify_union_official_change_request_pb2.NotifyUnionOfficialChangeRequest, _Mapping]] = ...) -> None: ...
    class NotifyUnionSubFuncUnlock(_message.Message):
        __slots__ = ("v_request",)
        V_REQUEST_FIELD_NUMBER: _ClassVar[int]
        v_request: _stru_notify_union_sub_func_unlock_request_pb2.NotifyUnionSubFuncUnlockRequest
        def __init__(self, v_request: _Optional[_Union[_stru_notify_union_sub_func_unlock_request_pb2.NotifyUnionSubFuncUnlockRequest, _Mapping]] = ...) -> None: ...
    class NotifyMemberOnline(_message.Message):
        __slots__ = ("v_request",)
        V_REQUEST_FIELD_NUMBER: _ClassVar[int]
        v_request: _stru_notify_member_online_request_pb2.NotifyMemberOnlineRequest
        def __init__(self, v_request: _Optional[_Union[_stru_notify_member_online_request_pb2.NotifyMemberOnlineRequest, _Mapping]] = ...) -> None: ...
    def __init__(self) -> None: ...
