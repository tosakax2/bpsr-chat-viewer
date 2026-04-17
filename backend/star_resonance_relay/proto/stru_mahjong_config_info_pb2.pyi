import enum_mahjong_config_type_pb2 as _enum_mahjong_config_type_pb2
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class MahjongConfigInfo(_message.Message):
    __slots__ = ("config_type", "value")
    CONFIG_TYPE_FIELD_NUMBER: _ClassVar[int]
    VALUE_FIELD_NUMBER: _ClassVar[int]
    config_type: _enum_mahjong_config_type_pb2.MahjongConfigType
    value: str
    def __init__(self, config_type: _Optional[_Union[_enum_mahjong_config_type_pb2.MahjongConfigType, str]] = ..., value: _Optional[str] = ...) -> None: ...
