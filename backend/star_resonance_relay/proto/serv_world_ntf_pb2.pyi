import enum_e_error_code_pb2 as _enum_e_error_code_pb2
import enum_e_picture_type_pb2 as _enum_e_picture_type_pb2
import stru_award_data_pb2 as _stru_award_data_pb2
import stru_card_info_pb2 as _stru_card_info_pb2
import stru_char_serialize_pb2 as _stru_char_serialize_pb2
import stru_client_custom_event_params_pb2 as _stru_client_custom_event_params_pb2
import stru_debug_message_tip_info_pb2 as _stru_debug_message_tip_info_pb2
import stru_driver_apply_ride_param_pb2 as _stru_driver_apply_ride_param_pb2
import stru_dungeon_ready_info_pb2 as _stru_dungeon_ready_info_pb2
import stru_dungeon_sync_data_pb2 as _stru_dungeon_sync_data_pb2
import stru_enter_match_result_ntf_request_pb2 as _stru_enter_match_result_ntf_request_pb2
import stru_entry_random_data_param_pb2 as _stru_entry_random_data_param_pb2
import stru_invite_apply_ride_param_pb2 as _stru_invite_apply_ride_param_pb2
import stru_notice_info_pb2 as _stru_notice_info_pb2
import stru_notice_multi_language_info_pb2 as _stru_notice_multi_language_info_pb2
import stru_notify_all_source_privilege_effect_data_pb2 as _stru_notify_all_source_privilege_effect_data_pb2
import stru_notify_all_valid_battle_pass_data_pb2 as _stru_notify_all_valid_battle_pass_data_pb2
import stru_notify_award_all_item_info_pb2 as _stru_notify_award_all_item_info_pb2
import stru_notify_buy_shop_result_param_pb2 as _stru_notify_buy_shop_result_param_pb2
import stru_notify_function_params_pb2 as _stru_notify_function_params_pb2
import stru_notify_life_profession_unlock_recipe_info_pb2 as _stru_notify_life_profession_unlock_recipe_info_pb2
import stru_notify_life_profession_work_history_change_info_pb2 as _stru_notify_life_profession_work_history_change_info_pb2
import stru_notify_pay_param_pb2 as _stru_notify_pay_param_pb2
import stru_notify_quest_accept_param_pb2 as _stru_notify_quest_accept_param_pb2
import stru_notify_quest_change_step_param_pb2 as _stru_notify_quest_change_step_param_pb2
import stru_notify_quest_complete_param_pb2 as _stru_notify_quest_complete_param_pb2
import stru_notify_quest_give_up_param_pb2 as _stru_notify_quest_give_up_param_pb2
import stru_notify_ride_is_agree_param_pb2 as _stru_notify_ride_is_agree_param_pb2
import stru_notify_shop_item_can_buy_param_pb2 as _stru_notify_shop_item_can_buy_param_pb2
import stru_parkour_record_pb2 as _stru_parkour_record_pb2
import stru_payment_result_pb2 as _stru_payment_result_pb2
import stru_show_items_info_pb2 as _stru_show_items_info_pb2
import stru_sign_reward_notify_request_pb2 as _stru_sign_reward_notify_request_pb2
import stru_start_playing_dungeon_param_pb2 as _stru_start_playing_dungeon_param_pb2
import stru_switch_info_pb2 as _stru_switch_info_pb2
import stru_sync_invite_request_pb2 as _stru_sync_invite_request_pb2
import stru_tips_info_pb2 as _stru_tips_info_pb2
import stru_unlock_cook_book_info_pb2 as _stru_unlock_cook_book_info_pb2
import stru_world_boss_rank_info_param_pb2 as _stru_world_boss_rank_info_param_pb2
import stru_skill_c_d_info_pb2 as _stru_skill_c_d_info_pb2
import stru_attr_collection_pb2 as _stru_attr_collection_pb2
import stru_temp_attr_collection_pb2 as _stru_temp_attr_collection_pb2
import stru_event_data_list_pb2 as _stru_event_data_list_pb2
import stru_bullet_event_pb2 as _stru_bullet_event_pb2
import stru_actor_body_part_infos_pb2 as _stru_actor_body_part_infos_pb2
import stru_seq_passive_skill_info_pb2 as _stru_seq_passive_skill_info_pb2
import stru_seq_passive_skill_end_info_pb2 as _stru_seq_passive_skill_end_info_pb2
import stru_buff_info_sync_pb2 as _stru_buff_info_sync_pb2
import stru_skill_effect_pb2 as _stru_skill_effect_pb2
import stru_buff_effect_sync_pb2 as _stru_buff_effect_sync_pb2
import stru_fake_bullet_info_pb2 as _stru_fake_bullet_info_pb2
import stru_magnetic_ride_queue_change_info_pb2 as _stru_magnetic_ride_queue_change_info_pb2
import stru_fight_res_c_d_pb2 as _stru_fight_res_c_d_pb2
import stru_buffer_stream_pb2 as _stru_buffer_stream_pb2
import stru_disappear_entity_pb2 as _stru_disappear_entity_pb2
import stru_entity_pb2 as _stru_entity_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from collections.abc import Iterable as _Iterable, Mapping as _Mapping
from typing import ClassVar as _ClassVar, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class WorldNtf(_message.Message):
    __slots__ = ()
    class AoiSyncDelta(_message.Message):
        __slots__ = ("Uuid", "Attrs", "TempAttrs", "EventDataList", "BulletEvent", "BodyPartInfos", "SkillEffects", "PassiveSkillInfos", "PassiveSkillEndInfos", "BuffInfos", "BuffEffect", "FakeBullets", "MagneticRideQueueChangeInfoList")
        UUID_FIELD_NUMBER: _ClassVar[int]
        ATTRS_FIELD_NUMBER: _ClassVar[int]
        TEMPATTRS_FIELD_NUMBER: _ClassVar[int]
        EVENTDATALIST_FIELD_NUMBER: _ClassVar[int]
        BULLETEVENT_FIELD_NUMBER: _ClassVar[int]
        BODYPARTINFOS_FIELD_NUMBER: _ClassVar[int]
        SKILLEFFECTS_FIELD_NUMBER: _ClassVar[int]
        PASSIVESKILLINFOS_FIELD_NUMBER: _ClassVar[int]
        PASSIVESKILLENDINFOS_FIELD_NUMBER: _ClassVar[int]
        BUFFINFOS_FIELD_NUMBER: _ClassVar[int]
        BUFFEFFECT_FIELD_NUMBER: _ClassVar[int]
        FAKEBULLETS_FIELD_NUMBER: _ClassVar[int]
        MAGNETICRIDEQUEUECHANGEINFOLIST_FIELD_NUMBER: _ClassVar[int]
        Uuid: int
        Attrs: _stru_attr_collection_pb2.AttrCollection
        TempAttrs: _stru_temp_attr_collection_pb2.TempAttrCollection
        EventDataList: _stru_event_data_list_pb2.EventDataList
        BulletEvent: _stru_bullet_event_pb2.BulletEvent
        BodyPartInfos: _stru_actor_body_part_infos_pb2.ActorBodyPartInfos
        SkillEffects: _stru_skill_effect_pb2.SkillEffect
        PassiveSkillInfos: _stru_seq_passive_skill_info_pb2.SeqPassiveSkillInfo
        PassiveSkillEndInfos: _stru_seq_passive_skill_end_info_pb2.SeqPassiveSkillEndInfo
        BuffInfos: _stru_buff_info_sync_pb2.BuffInfoSync
        BuffEffect: _stru_buff_effect_sync_pb2.BuffEffectSync
        FakeBullets: _containers.RepeatedCompositeFieldContainer[_stru_fake_bullet_info_pb2.FakeBulletInfo]
        MagneticRideQueueChangeInfoList: _containers.RepeatedCompositeFieldContainer[_stru_magnetic_ride_queue_change_info_pb2.MagneticRideQueueChangeInfo]
        def __init__(self, Uuid: _Optional[int] = ..., Attrs: _Optional[_Union[_stru_attr_collection_pb2.AttrCollection, _Mapping]] = ..., TempAttrs: _Optional[_Union[_stru_temp_attr_collection_pb2.TempAttrCollection, _Mapping]] = ..., EventDataList: _Optional[_Union[_stru_event_data_list_pb2.EventDataList, _Mapping]] = ..., BulletEvent: _Optional[_Union[_stru_bullet_event_pb2.BulletEvent, _Mapping]] = ..., BodyPartInfos: _Optional[_Union[_stru_actor_body_part_infos_pb2.ActorBodyPartInfos, _Mapping]] = ..., SkillEffects: _Optional[_Union[_stru_skill_effect_pb2.SkillEffect, _Mapping]] = ..., PassiveSkillInfos: _Optional[_Union[_stru_seq_passive_skill_info_pb2.SeqPassiveSkillInfo, _Mapping]] = ..., PassiveSkillEndInfos: _Optional[_Union[_stru_seq_passive_skill_end_info_pb2.SeqPassiveSkillEndInfo, _Mapping]] = ..., BuffInfos: _Optional[_Union[_stru_buff_info_sync_pb2.BuffInfoSync, _Mapping]] = ..., BuffEffect: _Optional[_Union[_stru_buff_effect_sync_pb2.BuffEffectSync, _Mapping]] = ..., FakeBullets: _Optional[_Iterable[_Union[_stru_fake_bullet_info_pb2.FakeBulletInfo, _Mapping]]] = ..., MagneticRideQueueChangeInfoList: _Optional[_Iterable[_Union[_stru_magnetic_ride_queue_change_info_pb2.MagneticRideQueueChangeInfo, _Mapping]]] = ...) -> None: ...
    class AoiSyncToMeDelta(_message.Message):
        __slots__ = ("BaseDelta", "SyncHateIds", "SyncSkillCDs", "FightResCDs", "Uuid")
        BASEDELTA_FIELD_NUMBER: _ClassVar[int]
        SYNCHATEIDS_FIELD_NUMBER: _ClassVar[int]
        SYNCSKILLCDS_FIELD_NUMBER: _ClassVar[int]
        FIGHTRESCDS_FIELD_NUMBER: _ClassVar[int]
        UUID_FIELD_NUMBER: _ClassVar[int]
        BaseDelta: WorldNtf.AoiSyncDelta
        SyncHateIds: _containers.RepeatedScalarFieldContainer[int]
        SyncSkillCDs: _containers.RepeatedCompositeFieldContainer[_stru_skill_c_d_info_pb2.SkillCDInfo]
        FightResCDs: _containers.RepeatedCompositeFieldContainer[_stru_fight_res_c_d_pb2.FightResCD]
        Uuid: int
        def __init__(self, BaseDelta: _Optional[_Union[WorldNtf.AoiSyncDelta, _Mapping]] = ..., SyncHateIds: _Optional[_Iterable[int]] = ..., SyncSkillCDs: _Optional[_Iterable[_Union[_stru_skill_c_d_info_pb2.SkillCDInfo, _Mapping]]] = ..., FightResCDs: _Optional[_Iterable[_Union[_stru_fight_res_c_d_pb2.FightResCD, _Mapping]]] = ..., Uuid: _Optional[int] = ...) -> None: ...
    class SyncPioneerInfo(_message.Message):
        __slots__ = ("target_id", "target_num")
        TARGET_ID_FIELD_NUMBER: _ClassVar[int]
        TARGET_NUM_FIELD_NUMBER: _ClassVar[int]
        target_id: int
        target_num: int
        def __init__(self, target_id: _Optional[int] = ..., target_num: _Optional[int] = ...) -> None: ...
    class SyncSwitchChange(_message.Message):
        __slots__ = ("id", "on_off")
        ID_FIELD_NUMBER: _ClassVar[int]
        ON_OFF_FIELD_NUMBER: _ClassVar[int]
        id: int
        on_off: int
        def __init__(self, id: _Optional[int] = ..., on_off: _Optional[int] = ...) -> None: ...
    class SyncSwitchInfo(_message.Message):
        __slots__ = ("info",)
        INFO_FIELD_NUMBER: _ClassVar[int]
        info: _stru_switch_info_pb2.SwitchInfo
        def __init__(self, info: _Optional[_Union[_stru_switch_info_pb2.SwitchInfo, _Mapping]] = ...) -> None: ...
    class SyncContainerData(_message.Message):
        __slots__ = ("v_data",)
        V_DATA_FIELD_NUMBER: _ClassVar[int]
        v_data: _stru_char_serialize_pb2.CharSerialize
        def __init__(self, v_data: _Optional[_Union[_stru_char_serialize_pb2.CharSerialize, _Mapping]] = ...) -> None: ...
    class SyncContainerDirtyData(_message.Message):
        __slots__ = ("VData",)
        VDATA_FIELD_NUMBER: _ClassVar[int]
        VData: _stru_buffer_stream_pb2.BufferStream
        def __init__(self, VData: _Optional[_Union[_stru_buffer_stream_pb2.BufferStream, _Mapping]] = ...) -> None: ...
    class SyncNearDeltaInfo(_message.Message):
        __slots__ = ("DeltaInfos",)
        DELTAINFOS_FIELD_NUMBER: _ClassVar[int]
        DeltaInfos: _containers.RepeatedCompositeFieldContainer[WorldNtf.AoiSyncDelta]
        def __init__(self, DeltaInfos: _Optional[_Iterable[_Union[WorldNtf.AoiSyncDelta, _Mapping]]] = ...) -> None: ...
    class SyncNearEntities(_message.Message):
        __slots__ = ("appear", "disappear")
        APPEAR_FIELD_NUMBER: _ClassVar[int]
        DISAPPEAR_FIELD_NUMBER: _ClassVar[int]
        appear: _containers.RepeatedCompositeFieldContainer[_stru_entity_pb2.Entity]
        disappear: _containers.RepeatedCompositeFieldContainer[_stru_disappear_entity_pb2.DisappearEntity]
        def __init__(self, appear: _Optional[_Iterable[_Union[_stru_entity_pb2.Entity, _Mapping]]] = ..., disappear: _Optional[_Iterable[_Union[_stru_disappear_entity_pb2.DisappearEntity, _Mapping]]] = ...) -> None: ...
    class SyncToMeDeltaInfo(_message.Message):
        __slots__ = ("DeltaInfo",)
        DELTAINFO_FIELD_NUMBER: _ClassVar[int]
        DeltaInfo: WorldNtf.AoiSyncToMeDelta
        def __init__(self, DeltaInfo: _Optional[_Union[WorldNtf.AoiSyncToMeDelta, _Mapping]] = ...) -> None: ...
    class SyncDungeonData(_message.Message):
        __slots__ = ("v_data",)
        V_DATA_FIELD_NUMBER: _ClassVar[int]
        v_data: _stru_dungeon_sync_data_pb2.DungeonSyncData
        def __init__(self, v_data: _Optional[_Union[_stru_dungeon_sync_data_pb2.DungeonSyncData, _Mapping]] = ...) -> None: ...
    class AwardNotify(_message.Message):
        __slots__ = ("award",)
        AWARD_FIELD_NUMBER: _ClassVar[int]
        award: _stru_award_data_pb2.AwardData
        def __init__(self, award: _Optional[_Union[_stru_award_data_pb2.AwardData, _Mapping]] = ...) -> None: ...
    class CardInfoAck(_message.Message):
        __slots__ = ("char_id", "info")
        CHAR_ID_FIELD_NUMBER: _ClassVar[int]
        INFO_FIELD_NUMBER: _ClassVar[int]
        char_id: int
        info: _stru_card_info_pb2.CardInfo
        def __init__(self, char_id: _Optional[int] = ..., info: _Optional[_Union[_stru_card_info_pb2.CardInfo, _Mapping]] = ...) -> None: ...
    class SyncSeason(_message.Message):
        __slots__ = ("v_season",)
        V_SEASON_FIELD_NUMBER: _ClassVar[int]
        v_season: int
        def __init__(self, v_season: _Optional[int] = ...) -> None: ...
    class UserAction(_message.Message):
        __slots__ = ("v_char_id", "v_action_id")
        V_CHAR_ID_FIELD_NUMBER: _ClassVar[int]
        V_ACTION_ID_FIELD_NUMBER: _ClassVar[int]
        v_char_id: int
        v_action_id: int
        def __init__(self, v_char_id: _Optional[int] = ..., v_action_id: _Optional[int] = ...) -> None: ...
    class NotifyDisplayPlayHelp(_message.Message):
        __slots__ = ("v_play_help_id",)
        V_PLAY_HELP_ID_FIELD_NUMBER: _ClassVar[int]
        v_play_help_id: int
        def __init__(self, v_play_help_id: _Optional[int] = ...) -> None: ...
    class NotifyApplicationInteraction(_message.Message):
        __slots__ = ("v_orig_id", "v_action_id")
        V_ORIG_ID_FIELD_NUMBER: _ClassVar[int]
        V_ACTION_ID_FIELD_NUMBER: _ClassVar[int]
        v_orig_id: int
        v_action_id: int
        def __init__(self, v_orig_id: _Optional[int] = ..., v_action_id: _Optional[int] = ...) -> None: ...
    class NotifyIsAgree(_message.Message):
        __slots__ = ("v_invitee_id", "v_action_id", "v_is_agree")
        V_INVITEE_ID_FIELD_NUMBER: _ClassVar[int]
        V_ACTION_ID_FIELD_NUMBER: _ClassVar[int]
        V_IS_AGREE_FIELD_NUMBER: _ClassVar[int]
        v_invitee_id: int
        v_action_id: int
        v_is_agree: bool
        def __init__(self, v_invitee_id: _Optional[int] = ..., v_action_id: _Optional[int] = ..., v_is_agree: bool = ...) -> None: ...
    class NotifyCancelAction(_message.Message):
        __slots__ = ("v_cancel_char_id",)
        V_CANCEL_CHAR_ID_FIELD_NUMBER: _ClassVar[int]
        v_cancel_char_id: int
        def __init__(self, v_cancel_char_id: _Optional[int] = ...) -> None: ...
    class NotifyUploadPictureResult(_message.Message):
        __slots__ = ("success", "photo_type", "photo_id", "photo_name")
        SUCCESS_FIELD_NUMBER: _ClassVar[int]
        PHOTO_TYPE_FIELD_NUMBER: _ClassVar[int]
        PHOTO_ID_FIELD_NUMBER: _ClassVar[int]
        PHOTO_NAME_FIELD_NUMBER: _ClassVar[int]
        success: bool
        photo_type: _enum_e_picture_type_pb2.EPictureType
        photo_id: int
        photo_name: str
        def __init__(self, success: bool = ..., photo_type: _Optional[_Union[_enum_e_picture_type_pb2.EPictureType, str]] = ..., photo_id: _Optional[int] = ..., photo_name: _Optional[str] = ...) -> None: ...
    class SyncInvite(_message.Message):
        __slots__ = ("v_request",)
        V_REQUEST_FIELD_NUMBER: _ClassVar[int]
        v_request: _stru_sync_invite_request_pb2.SyncInviteRequest
        def __init__(self, v_request: _Optional[_Union[_stru_sync_invite_request_pb2.SyncInviteRequest, _Mapping]] = ...) -> None: ...
    class NotifyRedDotChange(_message.Message):
        __slots__ = ("v_red_dot_id", "v_value")
        V_RED_DOT_ID_FIELD_NUMBER: _ClassVar[int]
        V_VALUE_FIELD_NUMBER: _ClassVar[int]
        v_red_dot_id: int
        v_value: int
        def __init__(self, v_red_dot_id: _Optional[int] = ..., v_value: _Optional[int] = ...) -> None: ...
    class ChangeNameResultNtf(_message.Message):
        __slots__ = ("v_code",)
        V_CODE_FIELD_NUMBER: _ClassVar[int]
        v_code: int
        def __init__(self, v_code: _Optional[int] = ...) -> None: ...
    class NotifyReviveUser(_message.Message):
        __slots__ = ("v_actor_uuid",)
        V_ACTOR_UUID_FIELD_NUMBER: _ClassVar[int]
        v_actor_uuid: int
        def __init__(self, v_actor_uuid: _Optional[int] = ...) -> None: ...
    class NotifyParkourRankInfo(_message.Message):
        __slots__ = ("v_rank_id",)
        V_RANK_ID_FIELD_NUMBER: _ClassVar[int]
        v_rank_id: int
        def __init__(self, v_rank_id: _Optional[int] = ...) -> None: ...
    class NotifyParkourRecordInfo(_message.Message):
        __slots__ = ("result", "v_record")
        RESULT_FIELD_NUMBER: _ClassVar[int]
        V_RECORD_FIELD_NUMBER: _ClassVar[int]
        result: int
        v_record: _stru_parkour_record_pb2.ParkourRecord
        def __init__(self, result: _Optional[int] = ..., v_record: _Optional[_Union[_stru_parkour_record_pb2.ParkourRecord, _Mapping]] = ...) -> None: ...
    class NotifyShowTips(_message.Message):
        __slots__ = ("v_tips",)
        V_TIPS_FIELD_NUMBER: _ClassVar[int]
        v_tips: _stru_tips_info_pb2.TipsInfo
        def __init__(self, v_tips: _Optional[_Union[_stru_tips_info_pb2.TipsInfo, _Mapping]] = ...) -> None: ...
    class NotifyNoticeInfo(_message.Message):
        __slots__ = ("v_info",)
        V_INFO_FIELD_NUMBER: _ClassVar[int]
        v_info: _stru_notice_info_pb2.NoticeInfo
        def __init__(self, v_info: _Optional[_Union[_stru_notice_info_pb2.NoticeInfo, _Mapping]] = ...) -> None: ...
    class NotifyClientKickOff(_message.Message):
        __slots__ = ("err_code",)
        ERR_CODE_FIELD_NUMBER: _ClassVar[int]
        err_code: _enum_e_error_code_pb2.EErrorCode
        def __init__(self, err_code: _Optional[_Union[_enum_e_error_code_pb2.EErrorCode, str]] = ...) -> None: ...
    class PaymentResponse(_message.Message):
        __slots__ = ("v_request",)
        V_REQUEST_FIELD_NUMBER: _ClassVar[int]
        v_request: _stru_payment_result_pb2.PaymentResult
        def __init__(self, v_request: _Optional[_Union[_stru_payment_result_pb2.PaymentResult, _Mapping]] = ...) -> None: ...
    class NotifyUnlockCookBook(_message.Message):
        __slots__ = ("v_info",)
        V_INFO_FIELD_NUMBER: _ClassVar[int]
        v_info: _stru_unlock_cook_book_info_pb2.UnlockCookBookInfo
        def __init__(self, v_info: _Optional[_Union[_stru_unlock_cook_book_info_pb2.UnlockCookBookInfo, _Mapping]] = ...) -> None: ...
    class NotifyCustomEvent(_message.Message):
        __slots__ = ("event_params",)
        EVENT_PARAMS_FIELD_NUMBER: _ClassVar[int]
        event_params: _stru_client_custom_event_params_pb2.ClientCustomEventParams
        def __init__(self, event_params: _Optional[_Union[_stru_client_custom_event_params_pb2.ClientCustomEventParams, _Mapping]] = ...) -> None: ...
    class NotifyStartPlayingDungeon(_message.Message):
        __slots__ = ("v_param",)
        V_PARAM_FIELD_NUMBER: _ClassVar[int]
        v_param: _stru_start_playing_dungeon_param_pb2.StartPlayingDungeonParam
        def __init__(self, v_param: _Optional[_Union[_stru_start_playing_dungeon_param_pb2.StartPlayingDungeonParam, _Mapping]] = ...) -> None: ...
    class ChangeShowIdResultNtf(_message.Message):
        __slots__ = ("err_code",)
        ERR_CODE_FIELD_NUMBER: _ClassVar[int]
        err_code: _enum_e_error_code_pb2.EErrorCode
        def __init__(self, err_code: _Optional[_Union[_enum_e_error_code_pb2.EErrorCode, str]] = ...) -> None: ...
    class NotifyShowItems(_message.Message):
        __slots__ = ("v_info",)
        V_INFO_FIELD_NUMBER: _ClassVar[int]
        v_info: _stru_show_items_info_pb2.ShowItemsInfo
        def __init__(self, v_info: _Optional[_Union[_stru_show_items_info_pb2.ShowItemsInfo, _Mapping]] = ...) -> None: ...
    class NotifySeasonActivationTargetInfo(_message.Message):
        __slots__ = ("v_season_id", "is_refresh")
        V_SEASON_ID_FIELD_NUMBER: _ClassVar[int]
        IS_REFRESH_FIELD_NUMBER: _ClassVar[int]
        v_season_id: int
        is_refresh: bool
        def __init__(self, v_season_id: _Optional[int] = ..., is_refresh: bool = ...) -> None: ...
    class NotifyTextCheckResult(_message.Message):
        __slots__ = ("err_code",)
        ERR_CODE_FIELD_NUMBER: _ClassVar[int]
        err_code: _enum_e_error_code_pb2.EErrorCode
        def __init__(self, err_code: _Optional[_Union[_enum_e_error_code_pb2.EErrorCode, str]] = ...) -> None: ...
    class NotifyDebugMessageTip(_message.Message):
        __slots__ = ("v_info",)
        V_INFO_FIELD_NUMBER: _ClassVar[int]
        v_info: _stru_debug_message_tip_info_pb2.DebugMessageTipInfo
        def __init__(self, v_info: _Optional[_Union[_stru_debug_message_tip_info_pb2.DebugMessageTipInfo, _Mapping]] = ...) -> None: ...
    class NotifyUserCloseFunction(_message.Message):
        __slots__ = ("v_param",)
        V_PARAM_FIELD_NUMBER: _ClassVar[int]
        v_param: _stru_notify_function_params_pb2.NotifyFunctionParams
        def __init__(self, v_param: _Optional[_Union[_stru_notify_function_params_pb2.NotifyFunctionParams, _Mapping]] = ...) -> None: ...
    class NotifyServerCloseFunction(_message.Message):
        __slots__ = ("v_param",)
        V_PARAM_FIELD_NUMBER: _ClassVar[int]
        v_param: _stru_notify_function_params_pb2.NotifyFunctionParams
        def __init__(self, v_param: _Optional[_Union[_stru_notify_function_params_pb2.NotifyFunctionParams, _Mapping]] = ...) -> None: ...
    class NotifyAwardAllItems(_message.Message):
        __slots__ = ("v_all_item",)
        V_ALL_ITEM_FIELD_NUMBER: _ClassVar[int]
        v_all_item: _stru_notify_award_all_item_info_pb2.NotifyAwardAllItemInfo
        def __init__(self, v_all_item: _Optional[_Union[_stru_notify_award_all_item_info_pb2.NotifyAwardAllItemInfo, _Mapping]] = ...) -> None: ...
    class NotifyAllMemberReady(_message.Message):
        __slots__ = ("v_open_or_close",)
        V_OPEN_OR_CLOSE_FIELD_NUMBER: _ClassVar[int]
        v_open_or_close: bool
        def __init__(self, v_open_or_close: bool = ...) -> None: ...
    class NotifyCaptainReady(_message.Message):
        __slots__ = ("v_member_name", "v_char_id", "v_ready_info")
        V_MEMBER_NAME_FIELD_NUMBER: _ClassVar[int]
        V_CHAR_ID_FIELD_NUMBER: _ClassVar[int]
        V_READY_INFO_FIELD_NUMBER: _ClassVar[int]
        v_member_name: str
        v_char_id: int
        v_ready_info: _stru_dungeon_ready_info_pb2.DungeonReadyInfo
        def __init__(self, v_member_name: _Optional[str] = ..., v_char_id: _Optional[int] = ..., v_ready_info: _Optional[_Union[_stru_dungeon_ready_info_pb2.DungeonReadyInfo, _Mapping]] = ...) -> None: ...
    class NotifyUserAllSourcePrivilegeEffectData(_message.Message):
        __slots__ = ("v_all_privilege_effects",)
        V_ALL_PRIVILEGE_EFFECTS_FIELD_NUMBER: _ClassVar[int]
        v_all_privilege_effects: _stru_notify_all_source_privilege_effect_data_pb2.NotifyAllSourcePrivilegeEffectData
        def __init__(self, v_all_privilege_effects: _Optional[_Union[_stru_notify_all_source_privilege_effect_data_pb2.NotifyAllSourcePrivilegeEffectData, _Mapping]] = ...) -> None: ...
    class NotifyQuestAccept(_message.Message):
        __slots__ = ("v_param",)
        V_PARAM_FIELD_NUMBER: _ClassVar[int]
        v_param: _stru_notify_quest_accept_param_pb2.NotifyQuestAcceptParam
        def __init__(self, v_param: _Optional[_Union[_stru_notify_quest_accept_param_pb2.NotifyQuestAcceptParam, _Mapping]] = ...) -> None: ...
    class NotifyQuestChangeStep(_message.Message):
        __slots__ = ("v_param",)
        V_PARAM_FIELD_NUMBER: _ClassVar[int]
        v_param: _stru_notify_quest_change_step_param_pb2.NotifyQuestChangeStepParam
        def __init__(self, v_param: _Optional[_Union[_stru_notify_quest_change_step_param_pb2.NotifyQuestChangeStepParam, _Mapping]] = ...) -> None: ...
    class NotifyQuestGiveUp(_message.Message):
        __slots__ = ("v_param",)
        V_PARAM_FIELD_NUMBER: _ClassVar[int]
        v_param: _stru_notify_quest_give_up_param_pb2.NotifyQuestGiveUpParam
        def __init__(self, v_param: _Optional[_Union[_stru_notify_quest_give_up_param_pb2.NotifyQuestGiveUpParam, _Mapping]] = ...) -> None: ...
    class NotifyQuestComplete(_message.Message):
        __slots__ = ("v_param",)
        V_PARAM_FIELD_NUMBER: _ClassVar[int]
        v_param: _stru_notify_quest_complete_param_pb2.NotifyQuestCompleteParam
        def __init__(self, v_param: _Optional[_Union[_stru_notify_quest_complete_param_pb2.NotifyQuestCompleteParam, _Mapping]] = ...) -> None: ...
    class NotifyUserAllValidBattlePassData(_message.Message):
        __slots__ = ("valid_battle_pass_data",)
        VALID_BATTLE_PASS_DATA_FIELD_NUMBER: _ClassVar[int]
        valid_battle_pass_data: _stru_notify_all_valid_battle_pass_data_pb2.NotifyAllValidBattlePassData
        def __init__(self, valid_battle_pass_data: _Optional[_Union[_stru_notify_all_valid_battle_pass_data_pb2.NotifyAllValidBattlePassData, _Mapping]] = ...) -> None: ...
    class NotifyNoticeMultiLanguageInfo(_message.Message):
        __slots__ = ("v_info",)
        V_INFO_FIELD_NUMBER: _ClassVar[int]
        v_info: _stru_notice_multi_language_info_pb2.NoticeMultiLanguageInfo
        def __init__(self, v_info: _Optional[_Union[_stru_notice_multi_language_info_pb2.NoticeMultiLanguageInfo, _Mapping]] = ...) -> None: ...
    class QteBegin(_message.Message):
        __slots__ = ("qte_id",)
        QTE_ID_FIELD_NUMBER: _ClassVar[int]
        qte_id: int
        def __init__(self, qte_id: _Optional[int] = ...) -> None: ...
    class QuestAbort(_message.Message):
        __slots__ = ("quest_id",)
        QUEST_ID_FIELD_NUMBER: _ClassVar[int]
        quest_id: int
        def __init__(self, quest_id: _Optional[int] = ...) -> None: ...
    class NotifyBuyShopResult(_message.Message):
        __slots__ = ("param",)
        PARAM_FIELD_NUMBER: _ClassVar[int]
        param: _stru_notify_buy_shop_result_param_pb2.NotifyBuyShopResultParam
        def __init__(self, param: _Optional[_Union[_stru_notify_buy_shop_result_param_pb2.NotifyBuyShopResultParam, _Mapping]] = ...) -> None: ...
    class NotifyShopItemCanBuy(_message.Message):
        __slots__ = ("param",)
        PARAM_FIELD_NUMBER: _ClassVar[int]
        param: _stru_notify_shop_item_can_buy_param_pb2.NotifyShopItemCanBuyParam
        def __init__(self, param: _Optional[_Union[_stru_notify_shop_item_can_buy_param_pb2.NotifyShopItemCanBuyParam, _Mapping]] = ...) -> None: ...
    class WorldBossRankInfoNtf(_message.Message):
        __slots__ = ("rank_info",)
        RANK_INFO_FIELD_NUMBER: _ClassVar[int]
        rank_info: _stru_world_boss_rank_info_param_pb2.WorldBossRankInfoParam
        def __init__(self, rank_info: _Optional[_Union[_stru_world_boss_rank_info_param_pb2.WorldBossRankInfoParam, _Mapping]] = ...) -> None: ...
    class EnterMatchResultNtf(_message.Message):
        __slots__ = ("v_request",)
        V_REQUEST_FIELD_NUMBER: _ClassVar[int]
        v_request: _stru_enter_match_result_ntf_request_pb2.EnterMatchResultNtfRequest
        def __init__(self, v_request: _Optional[_Union[_stru_enter_match_result_ntf_request_pb2.EnterMatchResultNtfRequest, _Mapping]] = ...) -> None: ...
    class NotifyDriverApplyRide(_message.Message):
        __slots__ = ("param",)
        PARAM_FIELD_NUMBER: _ClassVar[int]
        param: _stru_driver_apply_ride_param_pb2.DriverApplyRideParam
        def __init__(self, param: _Optional[_Union[_stru_driver_apply_ride_param_pb2.DriverApplyRideParam, _Mapping]] = ...) -> None: ...
    class NotifyInviteApplyRide(_message.Message):
        __slots__ = ("param",)
        PARAM_FIELD_NUMBER: _ClassVar[int]
        param: _stru_invite_apply_ride_param_pb2.InviteApplyRideParam
        def __init__(self, param: _Optional[_Union[_stru_invite_apply_ride_param_pb2.InviteApplyRideParam, _Mapping]] = ...) -> None: ...
    class NotifyRideIsAgree(_message.Message):
        __slots__ = ("param",)
        PARAM_FIELD_NUMBER: _ClassVar[int]
        param: _stru_notify_ride_is_agree_param_pb2.NotifyRideIsAgreeParam
        def __init__(self, param: _Optional[_Union[_stru_notify_ride_is_agree_param_pb2.NotifyRideIsAgreeParam, _Mapping]] = ...) -> None: ...
    class NotifyPayInfo(_message.Message):
        __slots__ = ("param",)
        PARAM_FIELD_NUMBER: _ClassVar[int]
        param: _stru_notify_pay_param_pb2.NotifyPayParam
        def __init__(self, param: _Optional[_Union[_stru_notify_pay_param_pb2.NotifyPayParam, _Mapping]] = ...) -> None: ...
    class NotifyLifeProfessionWorkHistoryChange(_message.Message):
        __slots__ = ("info",)
        INFO_FIELD_NUMBER: _ClassVar[int]
        info: _stru_notify_life_profession_work_history_change_info_pb2.NotifyLifeProfessionWorkHistoryChangeInfo
        def __init__(self, info: _Optional[_Union[_stru_notify_life_profession_work_history_change_info_pb2.NotifyLifeProfessionWorkHistoryChangeInfo, _Mapping]] = ...) -> None: ...
    class NotifyLifeProfessionUnlockRecipe(_message.Message):
        __slots__ = ("info",)
        INFO_FIELD_NUMBER: _ClassVar[int]
        info: _stru_notify_life_profession_unlock_recipe_info_pb2.NotifyLifeProfessionUnlockRecipeInfo
        def __init__(self, info: _Optional[_Union[_stru_notify_life_profession_unlock_recipe_info_pb2.NotifyLifeProfessionUnlockRecipeInfo, _Mapping]] = ...) -> None: ...
    class SignRewardNotify(_message.Message):
        __slots__ = ("v_request",)
        V_REQUEST_FIELD_NUMBER: _ClassVar[int]
        v_request: _stru_sign_reward_notify_request_pb2.SignRewardNotifyRequest
        def __init__(self, v_request: _Optional[_Union[_stru_sign_reward_notify_request_pb2.SignRewardNotifyRequest, _Mapping]] = ...) -> None: ...
    class NotifyEntryRandomData(_message.Message):
        __slots__ = ("param",)
        PARAM_FIELD_NUMBER: _ClassVar[int]
        param: _stru_entry_random_data_param_pb2.EntryRandomDataParam
        def __init__(self, param: _Optional[_Union[_stru_entry_random_data_param_pb2.EntryRandomDataParam, _Mapping]] = ...) -> None: ...
    def __init__(self) -> None: ...
