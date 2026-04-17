import enum_e_error_code_pb2 as _enum_e_error_code_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from collections.abc import Iterable as _Iterable
from typing import ClassVar as _ClassVar, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class EquipCreateReply(_message.Message):
    __slots__ = ("err_code", "item_uuids")
    ERR_CODE_FIELD_NUMBER: _ClassVar[int]
    ITEM_UUIDS_FIELD_NUMBER: _ClassVar[int]
    err_code: _enum_e_error_code_pb2.EErrorCode
    item_uuids: _containers.RepeatedScalarFieldContainer[int]
    def __init__(self, err_code: _Optional[_Union[_enum_e_error_code_pb2.EErrorCode, str]] = ..., item_uuids: _Optional[_Iterable[int]] = ...) -> None: ...
