import enum_e_error_code_pb2 as _enum_e_error_code_pb2
import stru_mem_union_activity_pb2 as _stru_mem_union_activity_pb2
import stru_union_activity_pb2 as _stru_union_activity_pb2
import stru_union_target_info_pb2 as _stru_union_target_info_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from collections.abc import Iterable as _Iterable, Mapping as _Mapping
from typing import ClassVar as _ClassVar, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class GetUnionActivityInfoReply(_message.Message):
    __slots__ = ("union_activity", "self_activity", "union_target", "received_point_award_ids", "err_code")
    UNION_ACTIVITY_FIELD_NUMBER: _ClassVar[int]
    SELF_ACTIVITY_FIELD_NUMBER: _ClassVar[int]
    UNION_TARGET_FIELD_NUMBER: _ClassVar[int]
    RECEIVED_POINT_AWARD_IDS_FIELD_NUMBER: _ClassVar[int]
    ERR_CODE_FIELD_NUMBER: _ClassVar[int]
    union_activity: _stru_union_activity_pb2.UnionActivity
    self_activity: _stru_mem_union_activity_pb2.MemUnionActivity
    union_target: _containers.RepeatedCompositeFieldContainer[_stru_union_target_info_pb2.UnionTargetInfo]
    received_point_award_ids: _containers.RepeatedScalarFieldContainer[int]
    err_code: _enum_e_error_code_pb2.EErrorCode
    def __init__(self, union_activity: _Optional[_Union[_stru_union_activity_pb2.UnionActivity, _Mapping]] = ..., self_activity: _Optional[_Union[_stru_mem_union_activity_pb2.MemUnionActivity, _Mapping]] = ..., union_target: _Optional[_Iterable[_Union[_stru_union_target_info_pb2.UnionTargetInfo, _Mapping]]] = ..., received_point_award_ids: _Optional[_Iterable[int]] = ..., err_code: _Optional[_Union[_enum_e_error_code_pb2.EErrorCode, str]] = ...) -> None: ...
