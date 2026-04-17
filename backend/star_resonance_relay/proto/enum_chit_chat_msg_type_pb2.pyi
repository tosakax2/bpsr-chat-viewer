from google.protobuf.internal import enum_type_wrapper as _enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from typing import ClassVar as _ClassVar

DESCRIPTOR: _descriptor.FileDescriptor

class ChitChatMsgType(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = ()
    ChatMsgTextMessage: _ClassVar[ChitChatMsgType]
    ChatMsgTextNotice: _ClassVar[ChitChatMsgType]
    ChatMsgMultiLangNotice: _ClassVar[ChitChatMsgType]
    ChatMsgPictureEmoji: _ClassVar[ChitChatMsgType]
    ChatMsgPicture: _ClassVar[ChitChatMsgType]
    ChatMsgVoice: _ClassVar[ChitChatMsgType]
    ChatMsgHypertext: _ClassVar[ChitChatMsgType]
ChatMsgTextMessage: ChitChatMsgType
ChatMsgTextNotice: ChitChatMsgType
ChatMsgMultiLangNotice: ChitChatMsgType
ChatMsgPictureEmoji: ChitChatMsgType
ChatMsgPicture: ChitChatMsgType
ChatMsgVoice: ChitChatMsgType
ChatMsgHypertext: ChitChatMsgType
