from google.protobuf.internal import containers as _containers
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from collections.abc import Mapping as _Mapping
from typing import ClassVar as _ClassVar, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class ElementalRestraintTableBase(_message.Message):
    __slots__ = ("id", "property_id", "defense_general", "defense_fire", "defense_water", "defense_electricity", "defense_wood", "defense_wind", "defense_rock", "defense_light", "defense_dark")
    ID_FIELD_NUMBER: _ClassVar[int]
    PROPERTY_ID_FIELD_NUMBER: _ClassVar[int]
    DEFENSE_GENERAL_FIELD_NUMBER: _ClassVar[int]
    DEFENSE_FIRE_FIELD_NUMBER: _ClassVar[int]
    DEFENSE_WATER_FIELD_NUMBER: _ClassVar[int]
    DEFENSE_ELECTRICITY_FIELD_NUMBER: _ClassVar[int]
    DEFENSE_WOOD_FIELD_NUMBER: _ClassVar[int]
    DEFENSE_WIND_FIELD_NUMBER: _ClassVar[int]
    DEFENSE_ROCK_FIELD_NUMBER: _ClassVar[int]
    DEFENSE_LIGHT_FIELD_NUMBER: _ClassVar[int]
    DEFENSE_DARK_FIELD_NUMBER: _ClassVar[int]
    id: int
    property_id: int
    defense_general: int
    defense_fire: int
    defense_water: int
    defense_electricity: int
    defense_wood: int
    defense_wind: int
    defense_rock: int
    defense_light: int
    defense_dark: int
    def __init__(self, id: _Optional[int] = ..., property_id: _Optional[int] = ..., defense_general: _Optional[int] = ..., defense_fire: _Optional[int] = ..., defense_water: _Optional[int] = ..., defense_electricity: _Optional[int] = ..., defense_wood: _Optional[int] = ..., defense_wind: _Optional[int] = ..., defense_rock: _Optional[int] = ..., defense_light: _Optional[int] = ..., defense_dark: _Optional[int] = ...) -> None: ...

class ElementalRestraintTableMgr(_message.Message):
    __slots__ = ("datas",)
    class DatasEntry(_message.Message):
        __slots__ = ("key", "value")
        KEY_FIELD_NUMBER: _ClassVar[int]
        VALUE_FIELD_NUMBER: _ClassVar[int]
        key: int
        value: ElementalRestraintTableBase
        def __init__(self, key: _Optional[int] = ..., value: _Optional[_Union[ElementalRestraintTableBase, _Mapping]] = ...) -> None: ...
    DATAS_FIELD_NUMBER: _ClassVar[int]
    datas: _containers.MessageMap[int, ElementalRestraintTableBase]
    def __init__(self, datas: _Optional[_Mapping[int, ElementalRestraintTableBase]] = ...) -> None: ...
