# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: greet.proto
"""Generated protocol buffer code."""
from google.protobuf.internal import builder as _builder
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n\x0bgreet.proto\x12\x05greet\".\n\x0cHelloRequest\x12\x0c\n\x04name\x18\x01 \x01(\t\x12\x10\n\x08greeting\x18\x02 \x01(\t\"E\n\x12Hello_join_Request\x12\x0c\n\x04name\x18\x01 \x01(\t\x12\x10\n\x08greeting\x18\x02 \x01(\t\x12\x0f\n\x07pub_key\x18\x03 \x01(\x0c\"E\n\x12Hello_cert_Request\x12\x0c\n\x04name\x18\x01 \x01(\t\x12\x10\n\x08greeting\x18\x02 \x01(\t\x12\x0f\n\x07pub_key\x18\x03 \x01(\x0c\"\x1d\n\nHelloReply\x12\x0f\n\x07message\x18\x01 \x01(\t\"E\n\x0c\x44\x65layedReply\x12\x0f\n\x07message\x18\x01 \x01(\t\x12$\n\x07request\x18\x02 \x03(\x0b\x32\x13.greet.HelloRequest2\xf5\x02\n\x07Greeter\x12\x32\n\x08SayHello\x12\x13.greet.HelloRequest\x1a\x11.greet.HelloReply\x12;\n\x0fParrotSaysHello\x12\x13.greet.HelloRequest\x1a\x11.greet.HelloReply0\x01\x12\x43\n\x15\x43hattyClientSaysHello\x12\x13.greet.HelloRequest\x1a\x13.greet.DelayedReply(\x01\x12>\n\x10InteractingHello\x12\x13.greet.HelloRequest\x1a\x11.greet.HelloReply(\x01\x30\x01\x12\x39\n\tJoinHello\x12\x19.greet.Hello_join_Request\x1a\x11.greet.HelloReply\x12\x39\n\tCertHello\x12\x19.greet.Hello_cert_Request\x1a\x11.greet.HelloReplyb\x06proto3')

_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, globals())
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'greet_pb2', globals())
if _descriptor._USE_C_DESCRIPTORS == False:

  DESCRIPTOR._options = None
  _HELLOREQUEST._serialized_start=22
  _HELLOREQUEST._serialized_end=68
  _HELLO_JOIN_REQUEST._serialized_start=70
  _HELLO_JOIN_REQUEST._serialized_end=139
  _HELLO_CERT_REQUEST._serialized_start=141
  _HELLO_CERT_REQUEST._serialized_end=210
  _HELLOREPLY._serialized_start=212
  _HELLOREPLY._serialized_end=241
  _DELAYEDREPLY._serialized_start=243
  _DELAYEDREPLY._serialized_end=312
  _GREETER._serialized_start=315
  _GREETER._serialized_end=688
# @@protoc_insertion_point(module_scope)
