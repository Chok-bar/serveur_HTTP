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




DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n\x0cserver.proto\"$\n\x08Position\x12\x0b\n\x03row\x18\x01 \x01(\x05\x12\x0b\n\x03\x63ol\x18\x02 \x01(\x05\"(\n\x04Move\x12 \n\rnext_position\x18\x01 \x01(\x0b\x32\t.Position\"\x11\n\x0fGameListRequest\"1\n\rGameListReply\x12\x0e\n\x06status\x18\x01 \x01(\x08\x12\x10\n\x08id_games\x18\x02 \x03(\x05\"7\n\x14GameSubscribeRequest\x12\x0e\n\x06player\x18\x01 \x01(\t\x12\x0f\n\x07id_game\x18\x02 \x01(\x05\"R\n\x12GameSubscribeReply\x12\x0e\n\x06status\x18\x01 \x01(\x08\x12\x19\n\x04role\x18\x02 \x01(\x0e\x32\x0b.PlayerRole\x12\x11\n\tid_player\x18\x03 \x01(\x05\":\n\x14GetGameStatusRequest\x12\x0f\n\x07id_game\x18\x01 \x01(\x05\x12\x11\n\tid_player\x18\x02 \x01(\x05\"o\n\x12GetGameStatusReply\x12\x0e\n\x06status\x18\x01 \x01(\x08\x12\x0f\n\x07started\x18\x02 \x01(\x08\x12\x19\n\x11round_in_progress\x18\x03 \x01(\x05\x12\x0e\n\x06winner\x18\x04 \x01(\t\x12\r\n\x05\x61live\x18\x05 \x01(\x08\"@\n\x19GetGameboardStatusRequest\x12\x10\n\x08id_party\x18\x01 \x01(\x05\x12\x11\n\tid_player\x18\x02 \x01(\x05\"@\n\x17GetGameboardStatusReply\x12\x0e\n\x06status\x18\x01 \x01(\x08\x12\x15\n\rvisible_cells\x18\x02 \x01(\t\"@\n\x0bMoveRequest\x12\x10\n\x08id_party\x18\x01 \x01(\x05\x12\x11\n\tid_player\x18\x02 \x01(\x05\x12\x0c\n\x04move\x18\x03 \x01(\t\"N\n\x0cMoveResponse\x12\x0e\n\x06status\x18\x01 \x01(\x08\x12\x19\n\x11round_in_progress\x18\x02 \x01(\x05\x12\x13\n\x04move\x18\x03 \x01(\x0b\x32\x05.Move\"\x13\n\x11\x43reateGameRequest\"M\n\x12\x43reateGameResponse\x12\x0f\n\x07game_id\x18\x01 \x01(\t\x12\x0f\n\x07success\x18\x02 \x01(\x08\x12\x15\n\rerror_message\x18\x03 \x01(\t*$\n\nPlayerRole\x12\x0c\n\x08Villager\x10\x00\x12\x08\n\x04Wolf\x10\x01\x32\xe8\x02\n\nGameServer\x12.\n\x08GameList\x12\x10.GameListRequest\x1a\x0e.GameListReply\"\x00\x12=\n\rGameSubscribe\x12\x15.GameSubscribeRequest\x1a\x13.GameSubscribeReply\"\x00\x12=\n\rGetGameStatus\x12\x15.GetGameStatusRequest\x1a\x13.GetGameStatusReply\"\x00\x12L\n\x12GetGameboardStatus\x12\x1a.GetGameboardStatusRequest\x1a\x18.GetGameboardStatusReply\"\x00\x12%\n\x04Move\x12\x0c.MoveRequest\x1a\r.MoveResponse\"\x00\x12\x37\n\nCreateGame\x12\x12.CreateGameRequest\x1a\x13.CreateGameResponse\"\x00\x62\x06proto3')

_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'server_pb2', _globals)
if not _descriptor._USE_C_DESCRIPTORS:
  DESCRIPTOR._loaded_options = None
  _globals['_PLAYERROLE']._serialized_start=858
  _globals['_PLAYERROLE']._serialized_end=894
  _globals['_POSITION']._serialized_start=16
  _globals['_POSITION']._serialized_end=52
  _globals['_MOVE']._serialized_start=54
  _globals['_MOVE']._serialized_end=94
  _globals['_GAMELISTREQUEST']._serialized_start=96
  _globals['_GAMELISTREQUEST']._serialized_end=113
  _globals['_GAMELISTREPLY']._serialized_start=115
  _globals['_GAMELISTREPLY']._serialized_end=164
  _globals['_GAMESUBSCRIBEREQUEST']._serialized_start=166
  _globals['_GAMESUBSCRIBEREQUEST']._serialized_end=221
  _globals['_GAMESUBSCRIBEREPLY']._serialized_start=223
  _globals['_GAMESUBSCRIBEREPLY']._serialized_end=305
  _globals['_GETGAMESTATUSREQUEST']._serialized_start=307
  _globals['_GETGAMESTATUSREQUEST']._serialized_end=365
  _globals['_GETGAMESTATUSREPLY']._serialized_start=367
  _globals['_GETGAMESTATUSREPLY']._serialized_end=478
  _globals['_GETGAMEBOARDSTATUSREQUEST']._serialized_start=480
  _globals['_GETGAMEBOARDSTATUSREQUEST']._serialized_end=544
  _globals['_GETGAMEBOARDSTATUSREPLY']._serialized_start=546
  _globals['_GETGAMEBOARDSTATUSREPLY']._serialized_end=610
  _globals['_MOVEREQUEST']._serialized_start=612
  _globals['_MOVEREQUEST']._serialized_end=676
  _globals['_MOVERESPONSE']._serialized_start=678
  _globals['_MOVERESPONSE']._serialized_end=756
  _globals['_CREATEGAMEREQUEST']._serialized_start=758
  _globals['_CREATEGAMEREQUEST']._serialized_end=777
  _globals['_CREATEGAMERESPONSE']._serialized_start=779
  _globals['_CREATEGAMERESPONSE']._serialized_end=856
  _globals['_GAMESERVER']._serialized_start=897
  _globals['_GAMESERVER']._serialized_end=1257
# @@protoc_insertion_point(module_scope)
