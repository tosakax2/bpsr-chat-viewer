import enum_enum_union_notify_type_pb2 as _enum_enum_union_notify_type_pb2
import stru_union_info_pb2 as _stru_union_info_pb2
import stru_union_member_pb2 as _stru_union_member_pb2
import stru_user_summary_data_pb2 as _stru_user_summary_data_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from collections.abc import Iterable as _Iterable, Mapping as _Mapping
from typing import ClassVar as _ClassVar, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class NotifyUpdateMemberRequest(_message.Message):
    __slots__ = ("info", "member_info_list", "type", "member_social_list")
    INFO_FIELD_NUMBER: _ClassVar[int]
    MEMBER_INFO_LIST_FIELD_NUMBER: _ClassVar[int]
    TYPE_FIELD_NUMBER: _ClassVar[int]
    MEMBER_SOCIAL_LIST_FIELD_NUMBER: _ClassVar[int]
    info: _stru_union_info_pb2.UnionInfo
    member_info_list: _containers.RepeatedCompositeFieldContainer[_stru_union_member_pb2.UnionMember]
    type: _enum_enum_union_notify_type_pb2.EnumUnionNotifyType
    member_social_list: _containers.RepeatedCompositeFieldContainer[_stru_user_summary_data_pb2.UserSummaryData]
    def __init__(self, info: _Optional[_Union[_stru_union_info_pb2.UnionInfo, _Mapping]] = ..., member_info_list: _Optional[_Iterable[_Union[_stru_union_member_pb2.UnionMember, _Mapping]]] = ..., type: _Optional[_Union[_enum_enum_union_notify_type_pb2.EnumUnionNotifyType, str]] = ..., member_social_list: _Optional[_Iterable[_Union[_stru_user_summary_data_pb2.UserSummaryData, _Mapping]]] = ...) -> None: ...
