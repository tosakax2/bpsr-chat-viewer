import enum_leave_mahjong_table_reason_pb2 as _enum_leave_mahjong_table_reason_pb2
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class LeaveMahjongTableRequest(_message.Message):
    __slots__ = ("table_guid", "reason")
    TABLE_GUID_FIELD_NUMBER: _ClassVar[int]
    REASON_FIELD_NUMBER: _ClassVar[int]
    table_guid: str
    reason: _enum_leave_mahjong_table_reason_pb2.LeaveMahjongTableReason
    def __init__(self, table_guid: _Optional[str] = ..., reason: _Optional[_Union[_enum_leave_mahjong_table_reason_pb2.LeaveMahjongTableReason, str]] = ...) -> None: ...
