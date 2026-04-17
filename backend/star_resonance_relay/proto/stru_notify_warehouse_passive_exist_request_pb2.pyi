import enum_warehouse_exit_type_pb2 as _enum_warehouse_exit_type_pb2
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class NotifyWarehousePassiveExistRequest(_message.Message):
    __slots__ = ("exit_type", "char_id")
    EXIT_TYPE_FIELD_NUMBER: _ClassVar[int]
    CHAR_ID_FIELD_NUMBER: _ClassVar[int]
    exit_type: _enum_warehouse_exit_type_pb2.WarehouseExitType
    char_id: int
    def __init__(self, exit_type: _Optional[_Union[_enum_warehouse_exit_type_pb2.WarehouseExitType, str]] = ..., char_id: _Optional[int] = ...) -> None: ...
