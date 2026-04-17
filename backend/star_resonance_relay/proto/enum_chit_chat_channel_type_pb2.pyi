from google.protobuf.internal import enum_type_wrapper as _enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from typing import ClassVar as _ClassVar

DESCRIPTOR: _descriptor.FileDescriptor

class ChitChatChannelType(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = ()
    ChannelNull: _ClassVar[ChitChatChannelType]
    ChannelWorld: _ClassVar[ChitChatChannelType]
    ChannelScene: _ClassVar[ChitChatChannelType]
    ChannelTeam: _ClassVar[ChitChatChannelType]
    ChannelUnion: _ClassVar[ChitChatChannelType]
    ChannelPrivate: _ClassVar[ChitChatChannelType]
    ChannelGroup: _ClassVar[ChitChatChannelType]
    ChannelTopNotice: _ClassVar[ChitChatChannelType]
    ChannelSystem: _ClassVar[ChitChatChannelType]
ChannelNull: ChitChatChannelType
ChannelWorld: ChitChatChannelType
ChannelScene: ChitChatChannelType
ChannelTeam: ChitChatChannelType
ChannelUnion: ChitChatChannelType
ChannelPrivate: ChitChatChannelType
ChannelGroup: ChitChatChannelType
ChannelTopNotice: ChitChatChannelType
ChannelSystem: ChitChatChannelType
