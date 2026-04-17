import table_basic_pb2 as _table_basic_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from collections.abc import Mapping as _Mapping
from typing import ClassVar as _ClassVar, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class WeaponSkinTableBase(_message.Message):
    __slots__ = ("id", "name", "icon", "intro", "weapon_model_id", "weapon_id", "original", "unlock", "unlock_des")
    ID_FIELD_NUMBER: _ClassVar[int]
    NAME_FIELD_NUMBER: _ClassVar[int]
    ICON_FIELD_NUMBER: _ClassVar[int]
    INTRO_FIELD_NUMBER: _ClassVar[int]
    WEAPON_MODEL_ID_FIELD_NUMBER: _ClassVar[int]
    WEAPON_ID_FIELD_NUMBER: _ClassVar[int]
    ORIGINAL_FIELD_NUMBER: _ClassVar[int]
    UNLOCK_FIELD_NUMBER: _ClassVar[int]
    UNLOCK_DES_FIELD_NUMBER: _ClassVar[int]
    id: int
    name: _table_basic_pb2.mlstring
    icon: str
    intro: _table_basic_pb2.mlstring
    weapon_model_id: _table_basic_pb2.int_array
    weapon_id: int
    original: int
    unlock: int
    unlock_des: _table_basic_pb2.mlstring
    def __init__(self, id: _Optional[int] = ..., name: _Optional[_Union[_table_basic_pb2.mlstring, _Mapping]] = ..., icon: _Optional[str] = ..., intro: _Optional[_Union[_table_basic_pb2.mlstring, _Mapping]] = ..., weapon_model_id: _Optional[_Union[_table_basic_pb2.int_array, _Mapping]] = ..., weapon_id: _Optional[int] = ..., original: _Optional[int] = ..., unlock: _Optional[int] = ..., unlock_des: _Optional[_Union[_table_basic_pb2.mlstring, _Mapping]] = ...) -> None: ...

class WeaponSkinTableMgr(_message.Message):
    __slots__ = ("datas",)
    class DatasEntry(_message.Message):
        __slots__ = ("key", "value")
        KEY_FIELD_NUMBER: _ClassVar[int]
        VALUE_FIELD_NUMBER: _ClassVar[int]
        key: int
        value: WeaponSkinTableBase
        def __init__(self, key: _Optional[int] = ..., value: _Optional[_Union[WeaponSkinTableBase, _Mapping]] = ...) -> None: ...
    DATAS_FIELD_NUMBER: _ClassVar[int]
    datas: _containers.MessageMap[int, WeaponSkinTableBase]
    def __init__(self, datas: _Optional[_Mapping[int, WeaponSkinTableBase]] = ...) -> None: ...
