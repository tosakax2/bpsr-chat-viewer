import stru_buff_attr_show_info_pb2 as _stru_buff_attr_show_info_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from collections.abc import Iterable as _Iterable, Mapping as _Mapping
from typing import ClassVar as _ClassVar, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class BuffAttrEffect(_message.Message):
    __slots__ = ("attr_show_info",)
    ATTR_SHOW_INFO_FIELD_NUMBER: _ClassVar[int]
    attr_show_info: _containers.RepeatedCompositeFieldContainer[_stru_buff_attr_show_info_pb2.BuffAttrShowInfo]
    def __init__(self, attr_show_info: _Optional[_Iterable[_Union[_stru_buff_attr_show_info_pb2.BuffAttrShowInfo, _Mapping]]] = ...) -> None: ...
