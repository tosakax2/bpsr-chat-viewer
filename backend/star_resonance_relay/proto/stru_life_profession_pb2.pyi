import stru_life_profession_alchemy_info_pb2 as _stru_life_profession_alchemy_info_pb2
import stru_life_profession_basic_pb2 as _stru_life_profession_basic_pb2
import stru_life_profession_recipe_pb2 as _stru_life_profession_recipe_pb2
import stru_life_profession_target_info_pb2 as _stru_life_profession_target_info_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from collections.abc import Mapping as _Mapping
from typing import ClassVar as _ClassVar, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class LifeProfession(_message.Message):
    __slots__ = ("profession_info", "life_target_info", "life_profession_recipe", "life_profession_alchemy_info", "spare_energy", "point")
    class ProfessionInfoEntry(_message.Message):
        __slots__ = ("key", "value")
        KEY_FIELD_NUMBER: _ClassVar[int]
        VALUE_FIELD_NUMBER: _ClassVar[int]
        key: int
        value: _stru_life_profession_basic_pb2.LifeProfessionBasic
        def __init__(self, key: _Optional[int] = ..., value: _Optional[_Union[_stru_life_profession_basic_pb2.LifeProfessionBasic, _Mapping]] = ...) -> None: ...
    class LifeTargetInfoEntry(_message.Message):
        __slots__ = ("key", "value")
        KEY_FIELD_NUMBER: _ClassVar[int]
        VALUE_FIELD_NUMBER: _ClassVar[int]
        key: int
        value: _stru_life_profession_target_info_pb2.LifeProfessionTargetInfo
        def __init__(self, key: _Optional[int] = ..., value: _Optional[_Union[_stru_life_profession_target_info_pb2.LifeProfessionTargetInfo, _Mapping]] = ...) -> None: ...
    class LifeProfessionRecipeEntry(_message.Message):
        __slots__ = ("key", "value")
        KEY_FIELD_NUMBER: _ClassVar[int]
        VALUE_FIELD_NUMBER: _ClassVar[int]
        key: int
        value: _stru_life_profession_recipe_pb2.LifeProfessionRecipe
        def __init__(self, key: _Optional[int] = ..., value: _Optional[_Union[_stru_life_profession_recipe_pb2.LifeProfessionRecipe, _Mapping]] = ...) -> None: ...
    class SpareEnergyEntry(_message.Message):
        __slots__ = ("key", "value")
        KEY_FIELD_NUMBER: _ClassVar[int]
        VALUE_FIELD_NUMBER: _ClassVar[int]
        key: int
        value: int
        def __init__(self, key: _Optional[int] = ..., value: _Optional[int] = ...) -> None: ...
    PROFESSION_INFO_FIELD_NUMBER: _ClassVar[int]
    LIFE_TARGET_INFO_FIELD_NUMBER: _ClassVar[int]
    LIFE_PROFESSION_RECIPE_FIELD_NUMBER: _ClassVar[int]
    LIFE_PROFESSION_ALCHEMY_INFO_FIELD_NUMBER: _ClassVar[int]
    SPARE_ENERGY_FIELD_NUMBER: _ClassVar[int]
    POINT_FIELD_NUMBER: _ClassVar[int]
    profession_info: _containers.MessageMap[int, _stru_life_profession_basic_pb2.LifeProfessionBasic]
    life_target_info: _containers.MessageMap[int, _stru_life_profession_target_info_pb2.LifeProfessionTargetInfo]
    life_profession_recipe: _containers.MessageMap[int, _stru_life_profession_recipe_pb2.LifeProfessionRecipe]
    life_profession_alchemy_info: _stru_life_profession_alchemy_info_pb2.LifeProfessionAlchemyInfo
    spare_energy: _containers.ScalarMap[int, int]
    point: int
    def __init__(self, profession_info: _Optional[_Mapping[int, _stru_life_profession_basic_pb2.LifeProfessionBasic]] = ..., life_target_info: _Optional[_Mapping[int, _stru_life_profession_target_info_pb2.LifeProfessionTargetInfo]] = ..., life_profession_recipe: _Optional[_Mapping[int, _stru_life_profession_recipe_pb2.LifeProfessionRecipe]] = ..., life_profession_alchemy_info: _Optional[_Union[_stru_life_profession_alchemy_info_pb2.LifeProfessionAlchemyInfo, _Mapping]] = ..., spare_energy: _Optional[_Mapping[int, int]] = ..., point: _Optional[int] = ...) -> None: ...
