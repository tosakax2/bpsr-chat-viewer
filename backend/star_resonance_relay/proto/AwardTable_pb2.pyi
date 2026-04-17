import table_basic_pb2 as _table_basic_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from collections.abc import Mapping as _Mapping
from typing import ClassVar as _ClassVar, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class AwardTableBase(_message.Message):
    __slots__ = ("award_id", "award_type", "group_content", "group_num", "group_rates", "group_weight", "award_time", "bind_info", "pro_item", "pro_rule", "level_up_conditions", "level_up_config", "level_up_package", "preview_item", "preview_item_info", "limit_type", "limit_params", "equip_lv_limit", "attr_fix_ratio", "preview_use_limite", "sign_para", "hide_preview")
    AWARD_ID_FIELD_NUMBER: _ClassVar[int]
    AWARD_TYPE_FIELD_NUMBER: _ClassVar[int]
    GROUP_CONTENT_FIELD_NUMBER: _ClassVar[int]
    GROUP_NUM_FIELD_NUMBER: _ClassVar[int]
    GROUP_RATES_FIELD_NUMBER: _ClassVar[int]
    GROUP_WEIGHT_FIELD_NUMBER: _ClassVar[int]
    AWARD_TIME_FIELD_NUMBER: _ClassVar[int]
    BIND_INFO_FIELD_NUMBER: _ClassVar[int]
    PRO_ITEM_FIELD_NUMBER: _ClassVar[int]
    PRO_RULE_FIELD_NUMBER: _ClassVar[int]
    LEVEL_UP_CONDITIONS_FIELD_NUMBER: _ClassVar[int]
    LEVEL_UP_CONFIG_FIELD_NUMBER: _ClassVar[int]
    LEVEL_UP_PACKAGE_FIELD_NUMBER: _ClassVar[int]
    PREVIEW_ITEM_FIELD_NUMBER: _ClassVar[int]
    PREVIEW_ITEM_INFO_FIELD_NUMBER: _ClassVar[int]
    LIMIT_TYPE_FIELD_NUMBER: _ClassVar[int]
    LIMIT_PARAMS_FIELD_NUMBER: _ClassVar[int]
    EQUIP_LV_LIMIT_FIELD_NUMBER: _ClassVar[int]
    ATTR_FIX_RATIO_FIELD_NUMBER: _ClassVar[int]
    PREVIEW_USE_LIMITE_FIELD_NUMBER: _ClassVar[int]
    SIGN_PARA_FIELD_NUMBER: _ClassVar[int]
    HIDE_PREVIEW_FIELD_NUMBER: _ClassVar[int]
    award_id: int
    award_type: int
    group_content: _table_basic_pb2.int_table
    group_num: _table_basic_pb2.int_table
    group_rates: _table_basic_pb2.number_array
    group_weight: _table_basic_pb2.int_array
    award_time: int
    bind_info: _table_basic_pb2.int_array
    pro_item: _table_basic_pb2.int_table
    pro_rule: _table_basic_pb2.number_table
    level_up_conditions: int
    level_up_config: _table_basic_pb2.int_table
    level_up_package: _table_basic_pb2.int_array
    preview_item: _table_basic_pb2.int_table
    preview_item_info: _table_basic_pb2.int_table
    limit_type: _table_basic_pb2.int_array
    limit_params: _table_basic_pb2.string_table
    equip_lv_limit: _table_basic_pb2.int_array
    attr_fix_ratio: _table_basic_pb2.int_array
    preview_use_limite: int
    sign_para: _table_basic_pb2.int_array
    hide_preview: int
    def __init__(self, award_id: _Optional[int] = ..., award_type: _Optional[int] = ..., group_content: _Optional[_Union[_table_basic_pb2.int_table, _Mapping]] = ..., group_num: _Optional[_Union[_table_basic_pb2.int_table, _Mapping]] = ..., group_rates: _Optional[_Union[_table_basic_pb2.number_array, _Mapping]] = ..., group_weight: _Optional[_Union[_table_basic_pb2.int_array, _Mapping]] = ..., award_time: _Optional[int] = ..., bind_info: _Optional[_Union[_table_basic_pb2.int_array, _Mapping]] = ..., pro_item: _Optional[_Union[_table_basic_pb2.int_table, _Mapping]] = ..., pro_rule: _Optional[_Union[_table_basic_pb2.number_table, _Mapping]] = ..., level_up_conditions: _Optional[int] = ..., level_up_config: _Optional[_Union[_table_basic_pb2.int_table, _Mapping]] = ..., level_up_package: _Optional[_Union[_table_basic_pb2.int_array, _Mapping]] = ..., preview_item: _Optional[_Union[_table_basic_pb2.int_table, _Mapping]] = ..., preview_item_info: _Optional[_Union[_table_basic_pb2.int_table, _Mapping]] = ..., limit_type: _Optional[_Union[_table_basic_pb2.int_array, _Mapping]] = ..., limit_params: _Optional[_Union[_table_basic_pb2.string_table, _Mapping]] = ..., equip_lv_limit: _Optional[_Union[_table_basic_pb2.int_array, _Mapping]] = ..., attr_fix_ratio: _Optional[_Union[_table_basic_pb2.int_array, _Mapping]] = ..., preview_use_limite: _Optional[int] = ..., sign_para: _Optional[_Union[_table_basic_pb2.int_array, _Mapping]] = ..., hide_preview: _Optional[int] = ...) -> None: ...

class AwardTableMgr(_message.Message):
    __slots__ = ("datas",)
    class DatasEntry(_message.Message):
        __slots__ = ("key", "value")
        KEY_FIELD_NUMBER: _ClassVar[int]
        VALUE_FIELD_NUMBER: _ClassVar[int]
        key: int
        value: AwardTableBase
        def __init__(self, key: _Optional[int] = ..., value: _Optional[_Union[AwardTableBase, _Mapping]] = ...) -> None: ...
    DATAS_FIELD_NUMBER: _ClassVar[int]
    datas: _containers.MessageMap[int, AwardTableBase]
    def __init__(self, datas: _Optional[_Mapping[int, AwardTableBase]] = ...) -> None: ...
