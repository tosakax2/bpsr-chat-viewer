from google.protobuf.internal import enum_type_wrapper as _enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from typing import ClassVar as _ClassVar

DESCRIPTOR: _descriptor.FileDescriptor

class MahjongProtocol(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = ()
    MahjongProtocolNone: _ClassVar[MahjongProtocol]
    Sync: _ClassVar[MahjongProtocol]
    SyncOperate: _ClassVar[MahjongProtocol]
    SyncTableEnd: _ClassVar[MahjongProtocol]
    SyncShowSettle: _ClassVar[MahjongProtocol]
    SyncFinalSettle: _ClassVar[MahjongProtocol]
    SyncPlayerMessage: _ClassVar[MahjongProtocol]
    SyncPlayerEmoji: _ClassVar[MahjongProtocol]
    Handle: _ClassVar[MahjongProtocol]
    Confirm: _ClassVar[MahjongProtocol]
    TestCard: _ClassVar[MahjongProtocol]
MahjongProtocolNone: MahjongProtocol
Sync: MahjongProtocol
SyncOperate: MahjongProtocol
SyncTableEnd: MahjongProtocol
SyncShowSettle: MahjongProtocol
SyncFinalSettle: MahjongProtocol
SyncPlayerMessage: MahjongProtocol
SyncPlayerEmoji: MahjongProtocol
Handle: MahjongProtocol
Confirm: MahjongProtocol
TestCard: MahjongProtocol
