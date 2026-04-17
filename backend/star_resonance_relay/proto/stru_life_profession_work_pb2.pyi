import stru_life_profession_work_info_pb2 as _stru_life_profession_work_info_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from collections.abc import Iterable as _Iterable, Mapping as _Mapping
from typing import ClassVar as _ClassVar, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class LifeProfessionWork(_message.Message):
    __slots__ = ("life_profession_work_info", "life_profession_work_history_info")
    LIFE_PROFESSION_WORK_INFO_FIELD_NUMBER: _ClassVar[int]
    LIFE_PROFESSION_WORK_HISTORY_INFO_FIELD_NUMBER: _ClassVar[int]
    life_profession_work_info: _stru_life_profession_work_info_pb2.LifeProfessionWorkInfo
    life_profession_work_history_info: _containers.RepeatedCompositeFieldContainer[_stru_life_profession_work_info_pb2.LifeProfessionWorkInfo]
    def __init__(self, life_profession_work_info: _Optional[_Union[_stru_life_profession_work_info_pb2.LifeProfessionWorkInfo, _Mapping]] = ..., life_profession_work_history_info: _Optional[_Iterable[_Union[_stru_life_profession_work_info_pb2.LifeProfessionWorkInfo, _Mapping]]] = ...) -> None: ...
