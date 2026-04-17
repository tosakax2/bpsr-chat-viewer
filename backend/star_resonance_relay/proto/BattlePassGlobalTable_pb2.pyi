import table_basic_pb2 as _table_basic_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from collections.abc import Mapping as _Mapping
from typing import ClassVar as _ClassVar, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class BattlePassGlobalTableBase(_message.Message):
    __slots__ = ("id", "weekly_exp_limit", "normal_pass_name", "prime_pass_name", "fashion", "fashion_level", "award_preview", "prime_pass_add_level", "prime_extra_award", "level_cost", "normal_pass_payment_id", "prime_pass_payment_id", "pass_price_diff_payment_id")
    ID_FIELD_NUMBER: _ClassVar[int]
    WEEKLY_EXP_LIMIT_FIELD_NUMBER: _ClassVar[int]
    NORMAL_PASS_NAME_FIELD_NUMBER: _ClassVar[int]
    PRIME_PASS_NAME_FIELD_NUMBER: _ClassVar[int]
    FASHION_FIELD_NUMBER: _ClassVar[int]
    FASHION_LEVEL_FIELD_NUMBER: _ClassVar[int]
    AWARD_PREVIEW_FIELD_NUMBER: _ClassVar[int]
    PRIME_PASS_ADD_LEVEL_FIELD_NUMBER: _ClassVar[int]
    PRIME_EXTRA_AWARD_FIELD_NUMBER: _ClassVar[int]
    LEVEL_COST_FIELD_NUMBER: _ClassVar[int]
    NORMAL_PASS_PAYMENT_ID_FIELD_NUMBER: _ClassVar[int]
    PRIME_PASS_PAYMENT_ID_FIELD_NUMBER: _ClassVar[int]
    PASS_PRICE_DIFF_PAYMENT_ID_FIELD_NUMBER: _ClassVar[int]
    id: int
    weekly_exp_limit: int
    normal_pass_name: _table_basic_pb2.mlstring
    prime_pass_name: _table_basic_pb2.mlstring
    fashion: _table_basic_pb2.int_table
    fashion_level: int
    award_preview: _table_basic_pb2.int_array
    prime_pass_add_level: int
    prime_extra_award: _table_basic_pb2.int_array
    level_cost: _table_basic_pb2.int_array
    normal_pass_payment_id: int
    prime_pass_payment_id: int
    pass_price_diff_payment_id: int
    def __init__(self, id: _Optional[int] = ..., weekly_exp_limit: _Optional[int] = ..., normal_pass_name: _Optional[_Union[_table_basic_pb2.mlstring, _Mapping]] = ..., prime_pass_name: _Optional[_Union[_table_basic_pb2.mlstring, _Mapping]] = ..., fashion: _Optional[_Union[_table_basic_pb2.int_table, _Mapping]] = ..., fashion_level: _Optional[int] = ..., award_preview: _Optional[_Union[_table_basic_pb2.int_array, _Mapping]] = ..., prime_pass_add_level: _Optional[int] = ..., prime_extra_award: _Optional[_Union[_table_basic_pb2.int_array, _Mapping]] = ..., level_cost: _Optional[_Union[_table_basic_pb2.int_array, _Mapping]] = ..., normal_pass_payment_id: _Optional[int] = ..., prime_pass_payment_id: _Optional[int] = ..., pass_price_diff_payment_id: _Optional[int] = ...) -> None: ...

class BattlePassGlobalTableMgr(_message.Message):
    __slots__ = ("datas",)
    class DatasEntry(_message.Message):
        __slots__ = ("key", "value")
        KEY_FIELD_NUMBER: _ClassVar[int]
        VALUE_FIELD_NUMBER: _ClassVar[int]
        key: int
        value: BattlePassGlobalTableBase
        def __init__(self, key: _Optional[int] = ..., value: _Optional[_Union[BattlePassGlobalTableBase, _Mapping]] = ...) -> None: ...
    DATAS_FIELD_NUMBER: _ClassVar[int]
    datas: _containers.MessageMap[int, BattlePassGlobalTableBase]
    def __init__(self, datas: _Optional[_Mapping[int, BattlePassGlobalTableBase]] = ...) -> None: ...
