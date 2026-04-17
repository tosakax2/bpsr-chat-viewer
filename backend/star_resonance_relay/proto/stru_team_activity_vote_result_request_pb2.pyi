import enum_e_team_vote_ret_pb2 as _enum_e_team_vote_ret_pb2
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class TeamActivityVoteResultRequest(_message.Message):
    __slots__ = ("code", "v_char_id")
    CODE_FIELD_NUMBER: _ClassVar[int]
    V_CHAR_ID_FIELD_NUMBER: _ClassVar[int]
    code: _enum_e_team_vote_ret_pb2.ETeamVoteRet
    v_char_id: int
    def __init__(self, code: _Optional[_Union[_enum_e_team_vote_ret_pb2.ETeamVoteRet, str]] = ..., v_char_id: _Optional[int] = ...) -> None: ...
