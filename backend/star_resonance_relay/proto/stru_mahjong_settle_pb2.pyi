import enum_mahjong_settle_type_pb2 as _enum_mahjong_settle_type_pb2
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class MahjongSettle(_message.Message):
    __slots__ = ("settle_type", "player_id", "yi", "han", "fushu", "seconds")
    SETTLE_TYPE_FIELD_NUMBER: _ClassVar[int]
    PLAYER_ID_FIELD_NUMBER: _ClassVar[int]
    YI_FIELD_NUMBER: _ClassVar[int]
    HAN_FIELD_NUMBER: _ClassVar[int]
    FUSHU_FIELD_NUMBER: _ClassVar[int]
    SECONDS_FIELD_NUMBER: _ClassVar[int]
    settle_type: _enum_mahjong_settle_type_pb2.MahjongSettleType
    player_id: int
    yi: int
    han: int
    fushu: int
    seconds: int
    def __init__(self, settle_type: _Optional[_Union[_enum_mahjong_settle_type_pb2.MahjongSettleType, str]] = ..., player_id: _Optional[int] = ..., yi: _Optional[int] = ..., han: _Optional[int] = ..., fushu: _Optional[int] = ..., seconds: _Optional[int] = ...) -> None: ...
