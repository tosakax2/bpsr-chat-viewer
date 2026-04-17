import enum_e_platform_func_type_pb2 as _enum_e_platform_func_type_pb2
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class GetFuncPhotoListRequest(_message.Message):
    __slots__ = ("func_type", "owner_id")
    FUNC_TYPE_FIELD_NUMBER: _ClassVar[int]
    OWNER_ID_FIELD_NUMBER: _ClassVar[int]
    func_type: _enum_e_platform_func_type_pb2.EPlatformFuncType
    owner_id: int
    def __init__(self, func_type: _Optional[_Union[_enum_e_platform_func_type_pb2.EPlatformFuncType, str]] = ..., owner_id: _Optional[int] = ...) -> None: ...
