import stru_tips_info_pb2 as _stru_tips_info_pb2
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from collections.abc import Mapping as _Mapping
from typing import ClassVar as _ClassVar, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class NotifyShowTipsRequest(_message.Message):
    __slots__ = ("tips_info",)
    TIPS_INFO_FIELD_NUMBER: _ClassVar[int]
    tips_info: _stru_tips_info_pb2.TipsInfo
    def __init__(self, tips_info: _Optional[_Union[_stru_tips_info_pb2.TipsInfo, _Mapping]] = ...) -> None: ...
