import enum_e_union_activity_rank_type_pb2 as _enum_e_union_activity_rank_type_pb2
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class ReqUnionActivityRankRequest(_message.Message):
    __slots__ = ("union_id", "activity_id", "rank_type")
    UNION_ID_FIELD_NUMBER: _ClassVar[int]
    ACTIVITY_ID_FIELD_NUMBER: _ClassVar[int]
    RANK_TYPE_FIELD_NUMBER: _ClassVar[int]
    union_id: int
    activity_id: int
    rank_type: _enum_e_union_activity_rank_type_pb2.EUnionActivityRankType
    def __init__(self, union_id: _Optional[int] = ..., activity_id: _Optional[int] = ..., rank_type: _Optional[_Union[_enum_e_union_activity_rank_type_pb2.EUnionActivityRankType, str]] = ...) -> None: ...
