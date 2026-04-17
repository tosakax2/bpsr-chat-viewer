import stru_session_info_pb2 as _stru_session_info_pb2
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from collections.abc import Mapping as _Mapping
from typing import ClassVar as _ClassVar, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class NotifyTeamMemVoiceIdChangeRequest(_message.Message):
    __slots__ = ("session", "member_id", "voice_id")
    SESSION_FIELD_NUMBER: _ClassVar[int]
    MEMBER_ID_FIELD_NUMBER: _ClassVar[int]
    VOICE_ID_FIELD_NUMBER: _ClassVar[int]
    session: _stru_session_info_pb2.SessionInfo
    member_id: int
    voice_id: int
    def __init__(self, session: _Optional[_Union[_stru_session_info_pb2.SessionInfo, _Mapping]] = ..., member_id: _Optional[int] = ..., voice_id: _Optional[int] = ...) -> None: ...
