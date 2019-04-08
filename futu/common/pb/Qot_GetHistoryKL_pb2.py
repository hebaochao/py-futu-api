# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: Qot_GetHistoryKL.proto

import sys
_b=sys.version_info[0]<3 and (lambda x:x) or (lambda x:x.encode('latin1'))
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
from google.protobuf import descriptor_pb2
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


import Common_pb2 as Common__pb2
import Qot_Common_pb2 as Qot__Common__pb2


DESCRIPTOR = _descriptor.FileDescriptor(
  name='Qot_GetHistoryKL.proto',
  package='Qot_GetHistoryKL',
  syntax='proto2',
  serialized_pb=_b('\n\x16Qot_GetHistoryKL.proto\x12\x10Qot_GetHistoryKL\x1a\x0c\x43ommon.proto\x1a\x10Qot_Common.proto\"\xa3\x01\n\x03\x43\x32S\x12\x11\n\trehabType\x18\x01 \x02(\x05\x12\x0e\n\x06klType\x18\x02 \x02(\x05\x12&\n\x08security\x18\x03 \x02(\x0b\x32\x14.Qot_Common.Security\x12\x11\n\tbeginTime\x18\x04 \x02(\t\x12\x0f\n\x07\x65ndTime\x18\x05 \x02(\t\x12\x13\n\x0bmaxAckKLNum\x18\x06 \x01(\x05\x12\x18\n\x10needKLFieldsFlag\x18\x07 \x01(\x03\"}\n\x03S2C\x12&\n\x08security\x18\x01 \x02(\x0b\x32\x14.Qot_Common.Security\x12!\n\x06klList\x18\x02 \x03(\x0b\x32\x11.Qot_Common.KLine\x12\x12\n\nnextKLTime\x18\x03 \x01(\t\x12\x17\n\x0fnextKLTimestamp\x18\x04 \x01(\x01\"-\n\x07Request\x12\"\n\x03\x63\x32s\x18\x01 \x02(\x0b\x32\x15.Qot_GetHistoryKL.C2S\"f\n\x08Response\x12\x15\n\x07retType\x18\x01 \x02(\x05:\x04-400\x12\x0e\n\x06retMsg\x18\x02 \x01(\t\x12\x0f\n\x07\x65rrCode\x18\x03 \x01(\x05\x12\"\n\x03s2c\x18\x04 \x01(\x0b\x32\x15.Qot_GetHistoryKL.S2C')
  ,
  dependencies=[Common__pb2.DESCRIPTOR,Qot__Common__pb2.DESCRIPTOR,])




_C2S = _descriptor.Descriptor(
  name='C2S',
  full_name='Qot_GetHistoryKL.C2S',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='rehabType', full_name='Qot_GetHistoryKL.C2S.rehabType', index=0,
      number=1, type=5, cpp_type=1, label=2,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='klType', full_name='Qot_GetHistoryKL.C2S.klType', index=1,
      number=2, type=5, cpp_type=1, label=2,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='security', full_name='Qot_GetHistoryKL.C2S.security', index=2,
      number=3, type=11, cpp_type=10, label=2,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='beginTime', full_name='Qot_GetHistoryKL.C2S.beginTime', index=3,
      number=4, type=9, cpp_type=9, label=2,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='endTime', full_name='Qot_GetHistoryKL.C2S.endTime', index=4,
      number=5, type=9, cpp_type=9, label=2,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='maxAckKLNum', full_name='Qot_GetHistoryKL.C2S.maxAckKLNum', index=5,
      number=6, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='needKLFieldsFlag', full_name='Qot_GetHistoryKL.C2S.needKLFieldsFlag', index=6,
      number=7, type=3, cpp_type=2, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  options=None,
  is_extendable=False,
  syntax='proto2',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=77,
  serialized_end=240,
)


_S2C = _descriptor.Descriptor(
  name='S2C',
  full_name='Qot_GetHistoryKL.S2C',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='security', full_name='Qot_GetHistoryKL.S2C.security', index=0,
      number=1, type=11, cpp_type=10, label=2,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='klList', full_name='Qot_GetHistoryKL.S2C.klList', index=1,
      number=2, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='nextKLTime', full_name='Qot_GetHistoryKL.S2C.nextKLTime', index=2,
      number=3, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='nextKLTimestamp', full_name='Qot_GetHistoryKL.S2C.nextKLTimestamp', index=3,
      number=4, type=1, cpp_type=5, label=1,
      has_default_value=False, default_value=float(0),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  options=None,
  is_extendable=False,
  syntax='proto2',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=242,
  serialized_end=367,
)


_REQUEST = _descriptor.Descriptor(
  name='Request',
  full_name='Qot_GetHistoryKL.Request',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='c2s', full_name='Qot_GetHistoryKL.Request.c2s', index=0,
      number=1, type=11, cpp_type=10, label=2,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  options=None,
  is_extendable=False,
  syntax='proto2',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=369,
  serialized_end=414,
)


_RESPONSE = _descriptor.Descriptor(
  name='Response',
  full_name='Qot_GetHistoryKL.Response',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='retType', full_name='Qot_GetHistoryKL.Response.retType', index=0,
      number=1, type=5, cpp_type=1, label=2,
      has_default_value=True, default_value=-400,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='retMsg', full_name='Qot_GetHistoryKL.Response.retMsg', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='errCode', full_name='Qot_GetHistoryKL.Response.errCode', index=2,
      number=3, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='s2c', full_name='Qot_GetHistoryKL.Response.s2c', index=3,
      number=4, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  options=None,
  is_extendable=False,
  syntax='proto2',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=416,
  serialized_end=518,
)

_C2S.fields_by_name['security'].message_type = Qot__Common__pb2._SECURITY
_S2C.fields_by_name['security'].message_type = Qot__Common__pb2._SECURITY
_S2C.fields_by_name['klList'].message_type = Qot__Common__pb2._KLINE
_REQUEST.fields_by_name['c2s'].message_type = _C2S
_RESPONSE.fields_by_name['s2c'].message_type = _S2C
DESCRIPTOR.message_types_by_name['C2S'] = _C2S
DESCRIPTOR.message_types_by_name['S2C'] = _S2C
DESCRIPTOR.message_types_by_name['Request'] = _REQUEST
DESCRIPTOR.message_types_by_name['Response'] = _RESPONSE
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

C2S = _reflection.GeneratedProtocolMessageType('C2S', (_message.Message,), dict(
  DESCRIPTOR = _C2S,
  __module__ = 'Qot_GetHistoryKL_pb2'
  # @@protoc_insertion_point(class_scope:Qot_GetHistoryKL.C2S)
  ))
_sym_db.RegisterMessage(C2S)

S2C = _reflection.GeneratedProtocolMessageType('S2C', (_message.Message,), dict(
  DESCRIPTOR = _S2C,
  __module__ = 'Qot_GetHistoryKL_pb2'
  # @@protoc_insertion_point(class_scope:Qot_GetHistoryKL.S2C)
  ))
_sym_db.RegisterMessage(S2C)

Request = _reflection.GeneratedProtocolMessageType('Request', (_message.Message,), dict(
  DESCRIPTOR = _REQUEST,
  __module__ = 'Qot_GetHistoryKL_pb2'
  # @@protoc_insertion_point(class_scope:Qot_GetHistoryKL.Request)
  ))
_sym_db.RegisterMessage(Request)

Response = _reflection.GeneratedProtocolMessageType('Response', (_message.Message,), dict(
  DESCRIPTOR = _RESPONSE,
  __module__ = 'Qot_GetHistoryKL_pb2'
  # @@protoc_insertion_point(class_scope:Qot_GetHistoryKL.Response)
  ))
_sym_db.RegisterMessage(Response)


# @@protoc_insertion_point(module_scope)
