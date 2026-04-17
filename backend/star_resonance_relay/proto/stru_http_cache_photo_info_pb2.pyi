from google.protobuf.internal import containers as _containers
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from collections.abc import Mapping as _Mapping
from typing import ClassVar as _ClassVar, Optional as _Optional

DESCRIPTOR: _descriptor.FileDescriptor

class httpCachePhotoInfo(_message.Message):
    __slots__ = ("http_cache_photo_info_dict",)
    class HttpCachePhotoInfoDictEntry(_message.Message):
        __slots__ = ("key", "value")
        KEY_FIELD_NUMBER: _ClassVar[int]
        VALUE_FIELD_NUMBER: _ClassVar[int]
        key: str
        value: str
        def __init__(self, key: _Optional[str] = ..., value: _Optional[str] = ...) -> None: ...
    HTTP_CACHE_PHOTO_INFO_DICT_FIELD_NUMBER: _ClassVar[int]
    http_cache_photo_info_dict: _containers.ScalarMap[str, str]
    def __init__(self, http_cache_photo_info_dict: _Optional[_Mapping[str, str]] = ...) -> None: ...
