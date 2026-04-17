import stru_chat_hypertext_pb2 as _stru_chat_hypertext_pb2
import stru_chat_multi_lang_notice_pb2 as _stru_chat_multi_lang_notice_pb2
import stru_chat_picture_emoji_pb2 as _stru_chat_picture_emoji_pb2
import stru_chat_voice_pb2 as _stru_chat_voice_pb2
import enum_chit_chat_msg_type_pb2 as _enum_chit_chat_msg_type_pb2
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from collections.abc import Mapping as _Mapping
from typing import ClassVar as _ClassVar, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class ChatMsgInfo(_message.Message):
    __slots__ = ("msg_type", "target_id", "msg_text", "multi_lang_notice", "picture_emoji", "voice", "chat_hypertext")
    MSG_TYPE_FIELD_NUMBER: _ClassVar[int]
    TARGET_ID_FIELD_NUMBER: _ClassVar[int]
    MSG_TEXT_FIELD_NUMBER: _ClassVar[int]
    MULTI_LANG_NOTICE_FIELD_NUMBER: _ClassVar[int]
    PICTURE_EMOJI_FIELD_NUMBER: _ClassVar[int]
    VOICE_FIELD_NUMBER: _ClassVar[int]
    CHAT_HYPERTEXT_FIELD_NUMBER: _ClassVar[int]
    msg_type: _enum_chit_chat_msg_type_pb2.ChitChatMsgType
    target_id: int
    msg_text: str
    multi_lang_notice: _stru_chat_multi_lang_notice_pb2.ChatMultiLangNotice
    picture_emoji: _stru_chat_picture_emoji_pb2.ChatPictureEmoji
    voice: _stru_chat_voice_pb2.ChatVoice
    chat_hypertext: _stru_chat_hypertext_pb2.ChatHypertext
    def __init__(self, msg_type: _Optional[_Union[_enum_chit_chat_msg_type_pb2.ChitChatMsgType, str]] = ..., target_id: _Optional[int] = ..., msg_text: _Optional[str] = ..., multi_lang_notice: _Optional[_Union[_stru_chat_multi_lang_notice_pb2.ChatMultiLangNotice, _Mapping]] = ..., picture_emoji: _Optional[_Union[_stru_chat_picture_emoji_pb2.ChatPictureEmoji, _Mapping]] = ..., voice: _Optional[_Union[_stru_chat_voice_pb2.ChatVoice, _Mapping]] = ..., chat_hypertext: _Optional[_Union[_stru_chat_hypertext_pb2.ChatHypertext, _Mapping]] = ...) -> None: ...
