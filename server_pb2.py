# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# NO CHECKED-IN PROTOBUF GENCODE
# source: server.proto
# Protobuf Python Version: 5.29.0
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import runtime_version as _runtime_version
from google.protobuf import symbol_database as _symbol_database
from google.protobuf.internal import builder as _builder
_runtime_version.ValidateProtobufRuntimeVersion(
    _runtime_version.Domain.PUBLIC,
    5,
    29,
    0,
    '',
    'server.proto'
)
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n\x0cserver.proto\"\x11\n\x0fGameListRequest\"1\n\rGameListReply\x12\x0e\n\x06status\x18\x01 \x01(\x08\x12\x10\n\x08id_games\x18\x02 \x03(\x05\"7\n\x14GameSubscribeRequest\x12\x0e\n\x06player\x18\x01 \x01(\t\x12\x0f\n\x07id_game\x18\x02 \x01(\x05\"L\n\x12GameSubscribeReply\x12\x0e\n\x06status\x18\x01 \x01(\x08\x12\x13\n\x04role\x18\x02 \x01(\x0e\x32\x05.Role\x12\x11\n\tid_player\x18\x03 \x01(\x05\":\n\x14GetGameStatusRequest\x12\x11\n\tid_player\x18\x01 \x01(\x05\x12\x0f\n\x07id_game\x18\x02 \x01(\x05\"$\n\x12GetGameStatusReply\x12\x0e\n\x06status\x18\x01 \x01(\x08\"V\n\x04Game\x12\x0f\n\x07id_game\x18\x01 \x01(\x05\x12\x11\n\tid_player\x18\x02 \x01(\x05\x12\x0f\n\x07started\x18\x03 \x01(\x08\x12\x19\n\x11round_in_progress\x18\x04 \x01(\x05\"(\n\x04Move\x12 \n\rnext_position\x18\x01 \x01(\x0b\x32\t.Position\"$\n\x08Position\x12\x0b\n\x03row\x18\x01 \x01(\x05\x12\x0b\n\x03\x63ol\x18\x02 \x01(\x05\"@\n\x19GetGameboardStatusRequest\x12\x10\n\x08id_party\x18\x01 \x01(\x05\x12\x11\n\tid_player\x18\x02 \x01(\x05\"@\n\x17GetGameboardStatusReply\x12\x0e\n\x06status\x18\x01 \x01(\x08\x12\x15\n\rvisible_cells\x18\x02 \x01(\t\"@\n\x0bMoveRequest\x12\x10\n\x08id_party\x18\x01 \x01(\x05\x12\x11\n\tid_player\x18\x02 \x01(\x05\x12\x0c\n\x04move\x18\x03 \x01(\t\"N\n\x0cMoveResponse\x12\x0e\n\x06status\x18\x01 \x01(\x08\x12\x19\n\x11round_in_progress\x18\x02 \x01(\x05\x12\x13\n\x04move\x18\x03 \x01(\x0b\x32\x05.Move*\x1e\n\x04Role\x12\x08\n\x04Wolf\x10\x00\x12\x0c\n\x08Villager\x10\x01\x32\xaf\x02\n\nGameServer\x12.\n\x08GameList\x12\x10.GameListRequest\x1a\x0e.GameListReply\"\x00\x12=\n\rGameSubscribe\x12\x15.GameSubscribeRequest\x1a\x13.GameSubscribeReply\"\x00\x12=\n\rGetGameStatus\x12\x15.GetGameStatusRequest\x1a\x13.GetGameStatusReply\"\x00\x12L\n\x12GetGameboardStatus\x12\x1a.GetGameboardStatusRequest\x1a\x18.GetGameboardStatusReply\"\x00\x12%\n\x04Move\x12\x0c.MoveRequest\x1a\r.MoveResponse\"\x00\x62\x06proto3')

_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'server_pb2', _globals)
if not _descriptor._USE_C_DESCRIPTORS:
  DESCRIPTOR._loaded_options = None
  _globals['_ROLE']._serialized_start=765
  _globals['_ROLE']._serialized_end=795
  _globals['_GAMELISTREQUEST']._serialized_start=16
  _globals['_GAMELISTREQUEST']._serialized_end=33
  _globals['_GAMELISTREPLY']._serialized_start=35
  _globals['_GAMELISTREPLY']._serialized_end=84
  _globals['_GAMESUBSCRIBEREQUEST']._serialized_start=86
  _globals['_GAMESUBSCRIBEREQUEST']._serialized_end=141
  _globals['_GAMESUBSCRIBEREPLY']._serialized_start=143
  _globals['_GAMESUBSCRIBEREPLY']._serialized_end=219
  _globals['_GETGAMESTATUSREQUEST']._serialized_start=221
  _globals['_GETGAMESTATUSREQUEST']._serialized_end=279
  _globals['_GETGAMESTATUSREPLY']._serialized_start=281
  _globals['_GETGAMESTATUSREPLY']._serialized_end=317
  _globals['_GAME']._serialized_start=319
  _globals['_GAME']._serialized_end=405
  _globals['_MOVE']._serialized_start=407
  _globals['_MOVE']._serialized_end=447
  _globals['_POSITION']._serialized_start=449
  _globals['_POSITION']._serialized_end=485
  _globals['_GETGAMEBOARDSTATUSREQUEST']._serialized_start=487
  _globals['_GETGAMEBOARDSTATUSREQUEST']._serialized_end=551
  _globals['_GETGAMEBOARDSTATUSREPLY']._serialized_start=553
  _globals['_GETGAMEBOARDSTATUSREPLY']._serialized_end=617
  _globals['_MOVEREQUEST']._serialized_start=619
  _globals['_MOVEREQUEST']._serialized_end=683
  _globals['_MOVERESPONSE']._serialized_start=685
  _globals['_MOVERESPONSE']._serialized_end=763
  _globals['_GAMESERVER']._serialized_start=798
  _globals['_GAMESERVER']._serialized_end=1101
# @@protoc_insertion_point(module_scope)
