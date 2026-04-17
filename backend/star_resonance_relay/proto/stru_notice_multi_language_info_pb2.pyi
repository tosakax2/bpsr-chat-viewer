import stru_multi_language_content_text_info_pb2 as _stru_multi_language_content_text_info_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from collections.abc import Iterable as _Iterable, Mapping as _Mapping
from typing import ClassVar as _ClassVar, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class NoticeMultiLanguageInfo(_message.Message):
    __slots__ = ("send_time", "is_loop", "loop_number", "loop_time_interval", "end_time", "content_text_info")
    SEND_TIME_FIELD_NUMBER: _ClassVar[int]
    IS_LOOP_FIELD_NUMBER: _ClassVar[int]
    LOOP_NUMBER_FIELD_NUMBER: _ClassVar[int]
    LOOP_TIME_INTERVAL_FIELD_NUMBER: _ClassVar[int]
    END_TIME_FIELD_NUMBER: _ClassVar[int]
    CONTENT_TEXT_INFO_FIELD_NUMBER: _ClassVar[int]
    send_time: int
    is_loop: bool
    loop_number: int
    loop_time_interval: int
    end_time: int
    content_text_info: _containers.RepeatedCompositeFieldContainer[_stru_multi_language_content_text_info_pb2.MultiLanguageContentTextInfo]
    def __init__(self, send_time: _Optional[int] = ..., is_loop: bool = ..., loop_number: _Optional[int] = ..., loop_time_interval: _Optional[int] = ..., end_time: _Optional[int] = ..., content_text_info: _Optional[_Iterable[_Union[_stru_multi_language_content_text_info_pb2.MultiLanguageContentTextInfo, _Mapping]]] = ...) -> None: ...
