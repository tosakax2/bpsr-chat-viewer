import enum_system_type_pb2 as _enum_system_type_pb2
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class AccountData(_message.Message):
    __slots__ = ("open_id", "sdk_type", "account_id", "account_uuid", "os")
    OPEN_ID_FIELD_NUMBER: _ClassVar[int]
    SDK_TYPE_FIELD_NUMBER: _ClassVar[int]
    ACCOUNT_ID_FIELD_NUMBER: _ClassVar[int]
    ACCOUNT_UUID_FIELD_NUMBER: _ClassVar[int]
    OS_FIELD_NUMBER: _ClassVar[int]
    open_id: str
    sdk_type: int
    account_id: str
    account_uuid: str
    os: _enum_system_type_pb2.SystemType
    def __init__(self, open_id: _Optional[str] = ..., sdk_type: _Optional[int] = ..., account_id: _Optional[str] = ..., account_uuid: _Optional[str] = ..., os: _Optional[_Union[_enum_system_type_pb2.SystemType, str]] = ...) -> None: ...
