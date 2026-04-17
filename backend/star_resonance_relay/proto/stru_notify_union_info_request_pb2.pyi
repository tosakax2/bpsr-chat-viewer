import enum_enum_union_notify_type_pb2 as _enum_enum_union_notify_type_pb2
import stru_union_info_pb2 as _stru_union_info_pb2
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from collections.abc import Mapping as _Mapping
from typing import ClassVar as _ClassVar, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class NotifyUnionInfoRequest(_message.Message):
    __slots__ = ("info", "type")
    INFO_FIELD_NUMBER: _ClassVar[int]
    TYPE_FIELD_NUMBER: _ClassVar[int]
    info: _stru_union_info_pb2.UnionInfo
    type: _enum_enum_union_notify_type_pb2.EnumUnionNotifyType
    def __init__(self, info: _Optional[_Union[_stru_union_info_pb2.UnionInfo, _Mapping]] = ..., type: _Optional[_Union[_enum_enum_union_notify_type_pb2.EnumUnionNotifyType, str]] = ...) -> None: ...
