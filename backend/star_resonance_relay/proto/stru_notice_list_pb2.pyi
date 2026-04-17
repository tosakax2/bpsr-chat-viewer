import stru_notice_info_pb2 as _stru_notice_info_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from collections.abc import Iterable as _Iterable, Mapping as _Mapping
from typing import ClassVar as _ClassVar, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class NoticeList(_message.Message):
    __slots__ = ("notices",)
    NOTICES_FIELD_NUMBER: _ClassVar[int]
    notices: _containers.RepeatedCompositeFieldContainer[_stru_notice_info_pb2.NoticeInfo]
    def __init__(self, notices: _Optional[_Iterable[_Union[_stru_notice_info_pb2.NoticeInfo, _Mapping]]] = ...) -> None: ...
