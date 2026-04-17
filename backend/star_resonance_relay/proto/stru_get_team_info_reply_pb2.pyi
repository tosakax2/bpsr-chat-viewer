import enum_e_error_code_pb2 as _enum_e_error_code_pb2
import stru_team_activity_pb2 as _stru_team_activity_pb2
import stru_team_base_info_pb2 as _stru_team_base_info_pb2
import stru_team_member_fast_sync_data_pb2 as _stru_team_member_fast_sync_data_pb2
import stru_team_mem_data_pb2 as _stru_team_mem_data_pb2
import stru_team_mem_real_time_voice_info_pb2 as _stru_team_mem_real_time_voice_info_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from collections.abc import Iterable as _Iterable, Mapping as _Mapping
from typing import ClassVar as _ClassVar, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class GetTeamInfoReply(_message.Message):
    __slots__ = ("base_info", "member_data", "team_activity", "mem_real_time_voice_infos", "mem_voice_id", "member_fast_sync_data", "err_code")
    class MemRealTimeVoiceInfosEntry(_message.Message):
        __slots__ = ("key", "value")
        KEY_FIELD_NUMBER: _ClassVar[int]
        VALUE_FIELD_NUMBER: _ClassVar[int]
        key: int
        value: _stru_team_mem_real_time_voice_info_pb2.TeamMemRealTimeVoiceInfo
        def __init__(self, key: _Optional[int] = ..., value: _Optional[_Union[_stru_team_mem_real_time_voice_info_pb2.TeamMemRealTimeVoiceInfo, _Mapping]] = ...) -> None: ...
    class MemVoiceIdEntry(_message.Message):
        __slots__ = ("key", "value")
        KEY_FIELD_NUMBER: _ClassVar[int]
        VALUE_FIELD_NUMBER: _ClassVar[int]
        key: int
        value: int
        def __init__(self, key: _Optional[int] = ..., value: _Optional[int] = ...) -> None: ...
    class MemberFastSyncDataEntry(_message.Message):
        __slots__ = ("key", "value")
        KEY_FIELD_NUMBER: _ClassVar[int]
        VALUE_FIELD_NUMBER: _ClassVar[int]
        key: int
        value: _stru_team_member_fast_sync_data_pb2.TeamMemberFastSyncData
        def __init__(self, key: _Optional[int] = ..., value: _Optional[_Union[_stru_team_member_fast_sync_data_pb2.TeamMemberFastSyncData, _Mapping]] = ...) -> None: ...
    BASE_INFO_FIELD_NUMBER: _ClassVar[int]
    MEMBER_DATA_FIELD_NUMBER: _ClassVar[int]
    TEAM_ACTIVITY_FIELD_NUMBER: _ClassVar[int]
    MEM_REAL_TIME_VOICE_INFOS_FIELD_NUMBER: _ClassVar[int]
    MEM_VOICE_ID_FIELD_NUMBER: _ClassVar[int]
    MEMBER_FAST_SYNC_DATA_FIELD_NUMBER: _ClassVar[int]
    ERR_CODE_FIELD_NUMBER: _ClassVar[int]
    base_info: _stru_team_base_info_pb2.TeamBaseInfo
    member_data: _containers.RepeatedCompositeFieldContainer[_stru_team_mem_data_pb2.TeamMemData]
    team_activity: _stru_team_activity_pb2.TeamActivity
    mem_real_time_voice_infos: _containers.MessageMap[int, _stru_team_mem_real_time_voice_info_pb2.TeamMemRealTimeVoiceInfo]
    mem_voice_id: _containers.ScalarMap[int, int]
    member_fast_sync_data: _containers.MessageMap[int, _stru_team_member_fast_sync_data_pb2.TeamMemberFastSyncData]
    err_code: _enum_e_error_code_pb2.EErrorCode
    def __init__(self, base_info: _Optional[_Union[_stru_team_base_info_pb2.TeamBaseInfo, _Mapping]] = ..., member_data: _Optional[_Iterable[_Union[_stru_team_mem_data_pb2.TeamMemData, _Mapping]]] = ..., team_activity: _Optional[_Union[_stru_team_activity_pb2.TeamActivity, _Mapping]] = ..., mem_real_time_voice_infos: _Optional[_Mapping[int, _stru_team_mem_real_time_voice_info_pb2.TeamMemRealTimeVoiceInfo]] = ..., mem_voice_id: _Optional[_Mapping[int, int]] = ..., member_fast_sync_data: _Optional[_Mapping[int, _stru_team_member_fast_sync_data_pb2.TeamMemberFastSyncData]] = ..., err_code: _Optional[_Union[_enum_e_error_code_pb2.EErrorCode, str]] = ...) -> None: ...
