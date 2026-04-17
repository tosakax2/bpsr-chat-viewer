import stru_notify_warehouse_grid_change_request_pb2 as _stru_notify_warehouse_grid_change_request_pb2
import stru_notify_warehouse_invite_request_pb2 as _stru_notify_warehouse_invite_request_pb2
import stru_notify_warehouse_new_joiner_request_pb2 as _stru_notify_warehouse_new_joiner_request_pb2
import stru_notify_warehouse_passive_exist_request_pb2 as _stru_notify_warehouse_passive_exist_request_pb2
import stru_notify_warehouse_refuse_to_join_request_pb2 as _stru_notify_warehouse_refuse_to_join_request_pb2
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from collections.abc import Mapping as _Mapping
from typing import ClassVar as _ClassVar, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class GrpcWarehouseNtf(_message.Message):
    __slots__ = ()
    class NotifyWarehouseInvite(_message.Message):
        __slots__ = ("request",)
        REQUEST_FIELD_NUMBER: _ClassVar[int]
        request: _stru_notify_warehouse_invite_request_pb2.NotifyWarehouseInviteRequest
        def __init__(self, request: _Optional[_Union[_stru_notify_warehouse_invite_request_pb2.NotifyWarehouseInviteRequest, _Mapping]] = ...) -> None: ...
    class NotifyWarehouseGridChange(_message.Message):
        __slots__ = ("request",)
        REQUEST_FIELD_NUMBER: _ClassVar[int]
        request: _stru_notify_warehouse_grid_change_request_pb2.NotifyWarehouseGridChangeRequest
        def __init__(self, request: _Optional[_Union[_stru_notify_warehouse_grid_change_request_pb2.NotifyWarehouseGridChangeRequest, _Mapping]] = ...) -> None: ...
    class NotifyWarehousePassiveExist(_message.Message):
        __slots__ = ("request",)
        REQUEST_FIELD_NUMBER: _ClassVar[int]
        request: _stru_notify_warehouse_passive_exist_request_pb2.NotifyWarehousePassiveExistRequest
        def __init__(self, request: _Optional[_Union[_stru_notify_warehouse_passive_exist_request_pb2.NotifyWarehousePassiveExistRequest, _Mapping]] = ...) -> None: ...
    class NotifyWarehouseNewJoiner(_message.Message):
        __slots__ = ("request",)
        REQUEST_FIELD_NUMBER: _ClassVar[int]
        request: _stru_notify_warehouse_new_joiner_request_pb2.NotifyWarehouseNewJoinerRequest
        def __init__(self, request: _Optional[_Union[_stru_notify_warehouse_new_joiner_request_pb2.NotifyWarehouseNewJoinerRequest, _Mapping]] = ...) -> None: ...
    class NotifyWarehouseRefuseToJoin(_message.Message):
        __slots__ = ("request",)
        REQUEST_FIELD_NUMBER: _ClassVar[int]
        request: _stru_notify_warehouse_refuse_to_join_request_pb2.NotifyWarehouseRefuseToJoinRequest
        def __init__(self, request: _Optional[_Union[_stru_notify_warehouse_refuse_to_join_request_pb2.NotifyWarehouseRefuseToJoinRequest, _Mapping]] = ...) -> None: ...
    def __init__(self) -> None: ...
