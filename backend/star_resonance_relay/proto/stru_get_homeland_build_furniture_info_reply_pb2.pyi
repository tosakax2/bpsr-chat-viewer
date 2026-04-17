import stru_community_build_furniture_info_pb2 as _stru_community_build_furniture_info_pb2
import enum_e_error_code_pb2 as _enum_e_error_code_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from collections.abc import Iterable as _Iterable, Mapping as _Mapping
from typing import ClassVar as _ClassVar, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class GetHomelandBuildFurnitureInfoReply(_message.Message):
    __slots__ = ("furniture_info", "err_code")
    FURNITURE_INFO_FIELD_NUMBER: _ClassVar[int]
    ERR_CODE_FIELD_NUMBER: _ClassVar[int]
    furniture_info: _containers.RepeatedCompositeFieldContainer[_stru_community_build_furniture_info_pb2.CommunityBuildFurnitureInfo]
    err_code: _enum_e_error_code_pb2.EErrorCode
    def __init__(self, furniture_info: _Optional[_Iterable[_Union[_stru_community_build_furniture_info_pb2.CommunityBuildFurnitureInfo, _Mapping]]] = ..., err_code: _Optional[_Union[_enum_e_error_code_pb2.EErrorCode, str]] = ...) -> None: ...
