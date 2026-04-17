import stru_union_activity_progress_info_pb2 as _stru_union_activity_progress_info_pb2
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from collections.abc import Mapping as _Mapping
from typing import ClassVar as _ClassVar, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class NotifyUnionActivityProgressRequest(_message.Message):
    __slots__ = ("progress_info",)
    PROGRESS_INFO_FIELD_NUMBER: _ClassVar[int]
    progress_info: _stru_union_activity_progress_info_pb2.UnionActivityProgressInfo
    def __init__(self, progress_info: _Optional[_Union[_stru_union_activity_progress_info_pb2.UnionActivityProgressInfo, _Mapping]] = ...) -> None: ...
