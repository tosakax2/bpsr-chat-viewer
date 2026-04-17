import enum_e_error_code_pb2 as _enum_e_error_code_pb2
import stru_item_pb2 as _stru_item_pb2
import stru_replace_item_data_pb2 as _stru_replace_item_data_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from collections.abc import Iterable as _Iterable, Mapping as _Mapping
from typing import ClassVar as _ClassVar, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class GashaDrawReply(_message.Message):
    __slots__ = ("items", "replace_items", "err_code")
    class ReplaceItemsEntry(_message.Message):
        __slots__ = ("key", "value")
        KEY_FIELD_NUMBER: _ClassVar[int]
        VALUE_FIELD_NUMBER: _ClassVar[int]
        key: int
        value: _stru_replace_item_data_pb2.ReplaceItemData
        def __init__(self, key: _Optional[int] = ..., value: _Optional[_Union[_stru_replace_item_data_pb2.ReplaceItemData, _Mapping]] = ...) -> None: ...
    ITEMS_FIELD_NUMBER: _ClassVar[int]
    REPLACE_ITEMS_FIELD_NUMBER: _ClassVar[int]
    ERR_CODE_FIELD_NUMBER: _ClassVar[int]
    items: _containers.RepeatedCompositeFieldContainer[_stru_item_pb2.Item]
    replace_items: _containers.MessageMap[int, _stru_replace_item_data_pb2.ReplaceItemData]
    err_code: _enum_e_error_code_pb2.EErrorCode
    def __init__(self, items: _Optional[_Iterable[_Union[_stru_item_pb2.Item, _Mapping]]] = ..., replace_items: _Optional[_Mapping[int, _stru_replace_item_data_pb2.ReplaceItemData]] = ..., err_code: _Optional[_Union[_enum_e_error_code_pb2.EErrorCode, str]] = ...) -> None: ...
