import enum_e_error_code_pb2 as _enum_e_error_code_pb2
import stru_item_pb2 as _stru_item_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from collections.abc import Iterable as _Iterable, Mapping as _Mapping
from typing import ClassVar as _ClassVar, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class LifeProfessionRDAlchemyRet(_message.Message):
    __slots__ = ("is_unlock_recipe", "unlock_recipe_id", "items", "err_code")
    IS_UNLOCK_RECIPE_FIELD_NUMBER: _ClassVar[int]
    UNLOCK_RECIPE_ID_FIELD_NUMBER: _ClassVar[int]
    ITEMS_FIELD_NUMBER: _ClassVar[int]
    ERR_CODE_FIELD_NUMBER: _ClassVar[int]
    is_unlock_recipe: bool
    unlock_recipe_id: int
    items: _containers.RepeatedCompositeFieldContainer[_stru_item_pb2.Item]
    err_code: _enum_e_error_code_pb2.EErrorCode
    def __init__(self, is_unlock_recipe: bool = ..., unlock_recipe_id: _Optional[int] = ..., items: _Optional[_Iterable[_Union[_stru_item_pb2.Item, _Mapping]]] = ..., err_code: _Optional[_Union[_enum_e_error_code_pb2.EErrorCode, str]] = ...) -> None: ...
