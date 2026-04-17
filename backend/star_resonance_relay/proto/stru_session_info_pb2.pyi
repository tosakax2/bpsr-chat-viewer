from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Optional as _Optional

DESCRIPTOR: _descriptor.FileDescriptor

class SessionInfo(_message.Message):
    __slots__ = ("peer_id", "char_id", "account_id", "trace_id", "remote_ip", "agent_guid", "is_robot")
    PEER_ID_FIELD_NUMBER: _ClassVar[int]
    CHAR_ID_FIELD_NUMBER: _ClassVar[int]
    ACCOUNT_ID_FIELD_NUMBER: _ClassVar[int]
    TRACE_ID_FIELD_NUMBER: _ClassVar[int]
    REMOTE_IP_FIELD_NUMBER: _ClassVar[int]
    AGENT_GUID_FIELD_NUMBER: _ClassVar[int]
    IS_ROBOT_FIELD_NUMBER: _ClassVar[int]
    peer_id: int
    char_id: int
    account_id: str
    trace_id: int
    remote_ip: str
    agent_guid: str
    is_robot: bool
    def __init__(self, peer_id: _Optional[int] = ..., char_id: _Optional[int] = ..., account_id: _Optional[str] = ..., trace_id: _Optional[int] = ..., remote_ip: _Optional[str] = ..., agent_guid: _Optional[str] = ..., is_robot: bool = ...) -> None: ...
