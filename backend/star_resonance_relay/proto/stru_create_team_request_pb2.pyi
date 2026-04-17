import enum_e_team_member_type_pb2 as _enum_e_team_member_type_pb2
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class CreateTeamRequest(_message.Message):
    __slots__ = ("char_id", "target_id", "is_auto_match", "is_show_in_hall", "team_member_type")
    CHAR_ID_FIELD_NUMBER: _ClassVar[int]
    TARGET_ID_FIELD_NUMBER: _ClassVar[int]
    IS_AUTO_MATCH_FIELD_NUMBER: _ClassVar[int]
    IS_SHOW_IN_HALL_FIELD_NUMBER: _ClassVar[int]
    TEAM_MEMBER_TYPE_FIELD_NUMBER: _ClassVar[int]
    char_id: int
    target_id: int
    is_auto_match: bool
    is_show_in_hall: bool
    team_member_type: _enum_e_team_member_type_pb2.ETeamMemberType
    def __init__(self, char_id: _Optional[int] = ..., target_id: _Optional[int] = ..., is_auto_match: bool = ..., is_show_in_hall: bool = ..., team_member_type: _Optional[_Union[_enum_e_team_member_type_pb2.ETeamMemberType, str]] = ...) -> None: ...
