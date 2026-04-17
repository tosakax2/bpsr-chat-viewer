import enum_e_error_code_pb2 as _enum_e_error_code_pb2
import enum_e_team_member_type_pb2 as _enum_e_team_member_type_pb2
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class NotifyTeamChangeMemberTypeRequest(_message.Message):
    __slots__ = ("error_code", "team_member_type", "target_id")
    ERROR_CODE_FIELD_NUMBER: _ClassVar[int]
    TEAM_MEMBER_TYPE_FIELD_NUMBER: _ClassVar[int]
    TARGET_ID_FIELD_NUMBER: _ClassVar[int]
    error_code: _enum_e_error_code_pb2.EErrorCode
    team_member_type: _enum_e_team_member_type_pb2.ETeamMemberType
    target_id: int
    def __init__(self, error_code: _Optional[_Union[_enum_e_error_code_pb2.EErrorCode, str]] = ..., team_member_type: _Optional[_Union[_enum_e_team_member_type_pb2.ETeamMemberType, str]] = ..., target_id: _Optional[int] = ...) -> None: ...
