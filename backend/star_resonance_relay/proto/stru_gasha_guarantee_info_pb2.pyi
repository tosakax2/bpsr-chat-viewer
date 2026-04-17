from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Optional as _Optional

DESCRIPTOR: _descriptor.FileDescriptor

class GashaGuaranteeInfo(_message.Message):
    __slots__ = ("id", "guaranteex", "guaranteey", "residue_guarantee_timex", "residue_guarantee_timey", "residue_guarantee_timez", "guaranteez")
    ID_FIELD_NUMBER: _ClassVar[int]
    GUARANTEEX_FIELD_NUMBER: _ClassVar[int]
    GUARANTEEY_FIELD_NUMBER: _ClassVar[int]
    RESIDUE_GUARANTEE_TIMEX_FIELD_NUMBER: _ClassVar[int]
    RESIDUE_GUARANTEE_TIMEY_FIELD_NUMBER: _ClassVar[int]
    RESIDUE_GUARANTEE_TIMEZ_FIELD_NUMBER: _ClassVar[int]
    GUARANTEEZ_FIELD_NUMBER: _ClassVar[int]
    id: int
    guaranteex: int
    guaranteey: int
    residue_guarantee_timex: int
    residue_guarantee_timey: int
    residue_guarantee_timez: int
    guaranteez: int
    def __init__(self, id: _Optional[int] = ..., guaranteex: _Optional[int] = ..., guaranteey: _Optional[int] = ..., residue_guarantee_timex: _Optional[int] = ..., residue_guarantee_timey: _Optional[int] = ..., residue_guarantee_timez: _Optional[int] = ..., guaranteez: _Optional[int] = ...) -> None: ...
