import enum_e_gm_parsing_type_pb2 as _enum_e_gm_parsing_type_pb2
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class GmCmd(_message.Message):
    __slots__ = ("command", "target_char_id", "parsing_type", "parameter")
    COMMAND_FIELD_NUMBER: _ClassVar[int]
    TARGET_CHAR_ID_FIELD_NUMBER: _ClassVar[int]
    PARSING_TYPE_FIELD_NUMBER: _ClassVar[int]
    PARAMETER_FIELD_NUMBER: _ClassVar[int]
    command: str
    target_char_id: int
    parsing_type: _enum_e_gm_parsing_type_pb2.EGmParsingType
    parameter: str
    def __init__(self, command: _Optional[str] = ..., target_char_id: _Optional[int] = ..., parsing_type: _Optional[_Union[_enum_e_gm_parsing_type_pb2.EGmParsingType, str]] = ..., parameter: _Optional[str] = ...) -> None: ...
