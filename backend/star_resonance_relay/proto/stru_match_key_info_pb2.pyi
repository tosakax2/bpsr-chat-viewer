import enum_e_match_type_pb2 as _enum_e_match_type_pb2
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class MatchKeyInfo(_message.Message):
    __slots__ = ("match_id", "match_type", "match_type_uuid")
    MATCH_ID_FIELD_NUMBER: _ClassVar[int]
    MATCH_TYPE_FIELD_NUMBER: _ClassVar[int]
    MATCH_TYPE_UUID_FIELD_NUMBER: _ClassVar[int]
    match_id: int
    match_type: _enum_e_match_type_pb2.EMatchType
    match_type_uuid: int
    def __init__(self, match_id: _Optional[int] = ..., match_type: _Optional[_Union[_enum_e_match_type_pb2.EMatchType, str]] = ..., match_type_uuid: _Optional[int] = ...) -> None: ...
