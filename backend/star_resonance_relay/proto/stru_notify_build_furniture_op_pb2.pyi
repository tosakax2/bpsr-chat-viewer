import enum_build_furniture_op_type_pb2 as _enum_build_furniture_op_type_pb2
import stru_community_build_furniture_info_pb2 as _stru_community_build_furniture_info_pb2
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from collections.abc import Mapping as _Mapping
from typing import ClassVar as _ClassVar, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class NotifyBuildFurnitureOp(_message.Message):
    __slots__ = ("op_type", "furniture")
    OP_TYPE_FIELD_NUMBER: _ClassVar[int]
    FURNITURE_FIELD_NUMBER: _ClassVar[int]
    op_type: _enum_build_furniture_op_type_pb2.BuildFurnitureOpType
    furniture: _stru_community_build_furniture_info_pb2.CommunityBuildFurnitureInfo
    def __init__(self, op_type: _Optional[_Union[_enum_build_furniture_op_type_pb2.BuildFurnitureOpType, str]] = ..., furniture: _Optional[_Union[_stru_community_build_furniture_info_pb2.CommunityBuildFurnitureInfo, _Mapping]] = ...) -> None: ...
