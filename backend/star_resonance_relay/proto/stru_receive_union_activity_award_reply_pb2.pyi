import enum_e_error_code_pb2 as _enum_e_error_code_pb2
import stru_item_pb2 as _stru_item_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from collections.abc import Iterable as _Iterable, Mapping as _Mapping
from typing import ClassVar as _ClassVar, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class ReceiveUnionActivityAwardReply(_message.Message):
    __slots__ = ("received_point_award_ids", "items", "union_last_refresh_time", "union_current_refresh_time", "last_point", "current_point", "err_code")
    RECEIVED_POINT_AWARD_IDS_FIELD_NUMBER: _ClassVar[int]
    ITEMS_FIELD_NUMBER: _ClassVar[int]
    UNION_LAST_REFRESH_TIME_FIELD_NUMBER: _ClassVar[int]
    UNION_CURRENT_REFRESH_TIME_FIELD_NUMBER: _ClassVar[int]
    LAST_POINT_FIELD_NUMBER: _ClassVar[int]
    CURRENT_POINT_FIELD_NUMBER: _ClassVar[int]
    ERR_CODE_FIELD_NUMBER: _ClassVar[int]
    received_point_award_ids: _containers.RepeatedScalarFieldContainer[int]
    items: _containers.RepeatedCompositeFieldContainer[_stru_item_pb2.Item]
    union_last_refresh_time: int
    union_current_refresh_time: int
    last_point: int
    current_point: int
    err_code: _enum_e_error_code_pb2.EErrorCode
    def __init__(self, received_point_award_ids: _Optional[_Iterable[int]] = ..., items: _Optional[_Iterable[_Union[_stru_item_pb2.Item, _Mapping]]] = ..., union_last_refresh_time: _Optional[int] = ..., union_current_refresh_time: _Optional[int] = ..., last_point: _Optional[int] = ..., current_point: _Optional[int] = ..., err_code: _Optional[_Union[_enum_e_error_code_pb2.EErrorCode, str]] = ...) -> None: ...
