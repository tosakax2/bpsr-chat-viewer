import stru_mod_part_upgrade_record_pb2 as _stru_mod_part_upgrade_record_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from collections.abc import Iterable as _Iterable, Mapping as _Mapping
from typing import ClassVar as _ClassVar, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class ModInfo(_message.Message):
    __slots__ = ("part_ids", "upgrade_records", "success_rate", "init_link_nums")
    PART_IDS_FIELD_NUMBER: _ClassVar[int]
    UPGRADE_RECORDS_FIELD_NUMBER: _ClassVar[int]
    SUCCESS_RATE_FIELD_NUMBER: _ClassVar[int]
    INIT_LINK_NUMS_FIELD_NUMBER: _ClassVar[int]
    part_ids: _containers.RepeatedScalarFieldContainer[int]
    upgrade_records: _containers.RepeatedCompositeFieldContainer[_stru_mod_part_upgrade_record_pb2.ModPartUpgradeRecord]
    success_rate: int
    init_link_nums: _containers.RepeatedScalarFieldContainer[int]
    def __init__(self, part_ids: _Optional[_Iterable[int]] = ..., upgrade_records: _Optional[_Iterable[_Union[_stru_mod_part_upgrade_record_pb2.ModPartUpgradeRecord, _Mapping]]] = ..., success_rate: _Optional[int] = ..., init_link_nums: _Optional[_Iterable[int]] = ...) -> None: ...
