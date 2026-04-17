import enum_chit_chat_channel_type_pb2 as _enum_chit_chat_channel_type_pb2
import enum_share_object_type_pb2 as _enum_share_object_type_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from collections.abc import Iterable as _Iterable
from typing import ClassVar as _ClassVar, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class ShareObjectInChatRequest(_message.Message):
    __slots__ = ("channel_type", "object_type", "object_uu_id", "before_desc", "after_desc", "target_char_id", "param_list")
    CHANNEL_TYPE_FIELD_NUMBER: _ClassVar[int]
    OBJECT_TYPE_FIELD_NUMBER: _ClassVar[int]
    OBJECT_UU_ID_FIELD_NUMBER: _ClassVar[int]
    BEFORE_DESC_FIELD_NUMBER: _ClassVar[int]
    AFTER_DESC_FIELD_NUMBER: _ClassVar[int]
    TARGET_CHAR_ID_FIELD_NUMBER: _ClassVar[int]
    PARAM_LIST_FIELD_NUMBER: _ClassVar[int]
    channel_type: _enum_chit_chat_channel_type_pb2.ChitChatChannelType
    object_type: _enum_share_object_type_pb2.ShareObjectType
    object_uu_id: int
    before_desc: str
    after_desc: str
    target_char_id: int
    param_list: _containers.RepeatedScalarFieldContainer[int]
    def __init__(self, channel_type: _Optional[_Union[_enum_chit_chat_channel_type_pb2.ChitChatChannelType, str]] = ..., object_type: _Optional[_Union[_enum_share_object_type_pb2.ShareObjectType, str]] = ..., object_uu_id: _Optional[int] = ..., before_desc: _Optional[str] = ..., after_desc: _Optional[str] = ..., target_char_id: _Optional[int] = ..., param_list: _Optional[_Iterable[int]] = ...) -> None: ...
