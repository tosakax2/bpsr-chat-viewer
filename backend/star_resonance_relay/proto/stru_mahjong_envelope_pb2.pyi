import enum_mahjong_protocol_pb2 as _enum_mahjong_protocol_pb2
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class MahjongEnvelope(_message.Message):
    __slots__ = ("protocol", "message_id", "data", "final_sync_time_sec")
    PROTOCOL_FIELD_NUMBER: _ClassVar[int]
    MESSAGE_ID_FIELD_NUMBER: _ClassVar[int]
    DATA_FIELD_NUMBER: _ClassVar[int]
    FINAL_SYNC_TIME_SEC_FIELD_NUMBER: _ClassVar[int]
    protocol: _enum_mahjong_protocol_pb2.MahjongProtocol
    message_id: int
    data: bytes
    final_sync_time_sec: int
    def __init__(self, protocol: _Optional[_Union[_enum_mahjong_protocol_pb2.MahjongProtocol, str]] = ..., message_id: _Optional[int] = ..., data: _Optional[bytes] = ..., final_sync_time_sec: _Optional[int] = ...) -> None: ...
