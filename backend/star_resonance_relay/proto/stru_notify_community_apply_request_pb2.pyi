import stru_community_apply_info_pb2 as _stru_community_apply_info_pb2
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from collections.abc import Mapping as _Mapping
from typing import ClassVar as _ClassVar, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class NotifyCommunityApplyRequest(_message.Message):
    __slots__ = ("apply_info",)
    APPLY_INFO_FIELD_NUMBER: _ClassVar[int]
    apply_info: _stru_community_apply_info_pb2.CommunityApplyInfo
    def __init__(self, apply_info: _Optional[_Union[_stru_community_apply_info_pb2.CommunityApplyInfo, _Mapping]] = ...) -> None: ...
