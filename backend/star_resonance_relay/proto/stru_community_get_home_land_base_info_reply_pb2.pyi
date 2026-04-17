import stru_community_build_life_profession_infos_pb2 as _stru_community_build_life_profession_infos_pb2
import enum_e_error_code_pb2 as _enum_e_error_code_pb2
import stru_homeland_base_info_pb2 as _stru_homeland_base_info_pb2
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from collections.abc import Mapping as _Mapping
from typing import ClassVar as _ClassVar, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class CommunityGetHomeLandBaseInfoReply(_message.Message):
    __slots__ = ("homeland_base_info", "life_profession_infos", "err_code")
    HOMELAND_BASE_INFO_FIELD_NUMBER: _ClassVar[int]
    LIFE_PROFESSION_INFOS_FIELD_NUMBER: _ClassVar[int]
    ERR_CODE_FIELD_NUMBER: _ClassVar[int]
    homeland_base_info: _stru_homeland_base_info_pb2.HomelandBaseInfo
    life_profession_infos: _stru_community_build_life_profession_infos_pb2.CommunityBuildLifeProfessionInfos
    err_code: _enum_e_error_code_pb2.EErrorCode
    def __init__(self, homeland_base_info: _Optional[_Union[_stru_homeland_base_info_pb2.HomelandBaseInfo, _Mapping]] = ..., life_profession_infos: _Optional[_Union[_stru_community_build_life_profession_infos_pb2.CommunityBuildLifeProfessionInfos, _Mapping]] = ..., err_code: _Optional[_Union[_enum_e_error_code_pb2.EErrorCode, str]] = ...) -> None: ...
