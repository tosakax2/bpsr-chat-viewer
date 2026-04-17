import stru_community_build_life_profession_info_pb2 as _stru_community_build_life_profession_info_pb2
import enum_e_error_code_pb2 as _enum_e_error_code_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from collections.abc import Iterable as _Iterable, Mapping as _Mapping
from typing import ClassVar as _ClassVar, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class BuildLifeProfessionInfoReply(_message.Message):
    __slots__ = ("err_code", "profession_infos")
    ERR_CODE_FIELD_NUMBER: _ClassVar[int]
    PROFESSION_INFOS_FIELD_NUMBER: _ClassVar[int]
    err_code: _enum_e_error_code_pb2.EErrorCode
    profession_infos: _containers.RepeatedCompositeFieldContainer[_stru_community_build_life_profession_info_pb2.CommunityBuildLifeProfessionInfo]
    def __init__(self, err_code: _Optional[_Union[_enum_e_error_code_pb2.EErrorCode, str]] = ..., profession_infos: _Optional[_Iterable[_Union[_stru_community_build_life_profession_info_pb2.CommunityBuildLifeProfessionInfo, _Mapping]]] = ...) -> None: ...
