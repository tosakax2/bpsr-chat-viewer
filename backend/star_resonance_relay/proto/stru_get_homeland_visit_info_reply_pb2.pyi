import stru_community_build_life_profession_infos_pb2 as _stru_community_build_life_profession_infos_pb2
import enum_e_error_code_pb2 as _enum_e_error_code_pb2
import stru_homeland_visit_info_pb2 as _stru_homeland_visit_info_pb2
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from collections.abc import Mapping as _Mapping
from typing import ClassVar as _ClassVar, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class GetHomelandVisitInfoReply(_message.Message):
    __slots__ = ("err_code", "homeland_visit_info", "life_profession_infos")
    ERR_CODE_FIELD_NUMBER: _ClassVar[int]
    HOMELAND_VISIT_INFO_FIELD_NUMBER: _ClassVar[int]
    LIFE_PROFESSION_INFOS_FIELD_NUMBER: _ClassVar[int]
    err_code: _enum_e_error_code_pb2.EErrorCode
    homeland_visit_info: _stru_homeland_visit_info_pb2.HomelandVisitInfo
    life_profession_infos: _stru_community_build_life_profession_infos_pb2.CommunityBuildLifeProfessionInfos
    def __init__(self, err_code: _Optional[_Union[_enum_e_error_code_pb2.EErrorCode, str]] = ..., homeland_visit_info: _Optional[_Union[_stru_homeland_visit_info_pb2.HomelandVisitInfo, _Mapping]] = ..., life_profession_infos: _Optional[_Union[_stru_community_build_life_profession_infos_pb2.CommunityBuildLifeProfessionInfos, _Mapping]] = ...) -> None: ...
