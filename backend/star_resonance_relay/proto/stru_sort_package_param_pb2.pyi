import stru_sort_item_param_pb2 as _stru_sort_item_param_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from collections.abc import Iterable as _Iterable, Mapping as _Mapping
from typing import ClassVar as _ClassVar, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class SortPackageParam(_message.Message):
    __slots__ = ("package_type", "item_params")
    PACKAGE_TYPE_FIELD_NUMBER: _ClassVar[int]
    ITEM_PARAMS_FIELD_NUMBER: _ClassVar[int]
    package_type: int
    item_params: _containers.RepeatedCompositeFieldContainer[_stru_sort_item_param_pb2.SortItemParam]
    def __init__(self, package_type: _Optional[int] = ..., item_params: _Optional[_Iterable[_Union[_stru_sort_item_param_pb2.SortItemParam, _Mapping]]] = ...) -> None: ...
