import stru_temp_photo_cache_info_pb2 as _stru_temp_photo_cache_info_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from collections.abc import Mapping as _Mapping
from typing import ClassVar as _ClassVar, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class tempPhotoCache(_message.Message):
    __slots__ = ("temp_photo_cache_dict",)
    class TempPhotoCacheDictEntry(_message.Message):
        __slots__ = ("key", "value")
        KEY_FIELD_NUMBER: _ClassVar[int]
        VALUE_FIELD_NUMBER: _ClassVar[int]
        key: str
        value: _stru_temp_photo_cache_info_pb2.tempPhotoCacheInfo
        def __init__(self, key: _Optional[str] = ..., value: _Optional[_Union[_stru_temp_photo_cache_info_pb2.tempPhotoCacheInfo, _Mapping]] = ...) -> None: ...
    TEMP_PHOTO_CACHE_DICT_FIELD_NUMBER: _ClassVar[int]
    temp_photo_cache_dict: _containers.MessageMap[str, _stru_temp_photo_cache_info_pb2.tempPhotoCacheInfo]
    def __init__(self, temp_photo_cache_dict: _Optional[_Mapping[str, _stru_temp_photo_cache_info_pb2.tempPhotoCacheInfo]] = ...) -> None: ...
