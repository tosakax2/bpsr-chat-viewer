import enum_e_error_code_pb2 as _enum_e_error_code_pb2
import enum_e_platform_func_type_pb2 as _enum_e_platform_func_type_pb2
import stru_image_cos_key_pb2 as _stru_image_cos_key_pb2
import stru_tmp_token_result_pb2 as _stru_tmp_token_result_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from collections.abc import Iterable as _Iterable, Mapping as _Mapping
from typing import ClassVar as _ClassVar, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class GetPhotoTokenNtfRequest(_message.Message):
    __slots__ = ("err_code", "result", "cos_keys", "func_type")
    ERR_CODE_FIELD_NUMBER: _ClassVar[int]
    RESULT_FIELD_NUMBER: _ClassVar[int]
    COS_KEYS_FIELD_NUMBER: _ClassVar[int]
    FUNC_TYPE_FIELD_NUMBER: _ClassVar[int]
    err_code: _enum_e_error_code_pb2.EErrorCode
    result: _stru_tmp_token_result_pb2.TmpTokenResult
    cos_keys: _containers.RepeatedCompositeFieldContainer[_stru_image_cos_key_pb2.ImageCosKey]
    func_type: _enum_e_platform_func_type_pb2.EPlatformFuncType
    def __init__(self, err_code: _Optional[_Union[_enum_e_error_code_pb2.EErrorCode, str]] = ..., result: _Optional[_Union[_stru_tmp_token_result_pb2.TmpTokenResult, _Mapping]] = ..., cos_keys: _Optional[_Iterable[_Union[_stru_image_cos_key_pb2.ImageCosKey, _Mapping]]] = ..., func_type: _Optional[_Union[_enum_e_platform_func_type_pb2.EPlatformFuncType, str]] = ...) -> None: ...
