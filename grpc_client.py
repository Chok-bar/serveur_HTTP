import json
from typing import Any, Dict

import grpc

import server_pb2
import server_pb2_grpc


class GRPCClient:
    def __init__(self, channel: grpc.Channel):
        self.channel = channel
        self.stub = server_pb2_grpc.GameServerStub(channel)

        self.action_map = {
            "list": self.game_list,
            "subscribe": self.game_subscribe,
            "party_status": self.get_game_status,
            "gameboard_status": self.get_gameboard_status,
            "move": self.move,
        }

    def game_list(self) -> Dict[str, Any]:
        res: server_pb2.GameListReply = self.stub.GameList(server_pb2.GameListRequest())
        return {
            "status": res.status is True and "OK" or "KO",
            "response": {
                "id_parties": list(res.id_games),
            },
        }

    def game_subscribe(self, id_game: int) -> Dict[str, Any]:
        res: server_pb2.GameSubscribeReply = self.stub.GameSubscribe(
            server_pb2.GameSubscribeRequest(id_game=id_game)
        )
        return {
            "id_player": res.id_player,
            "role": server_pb2.Role.Name(res.role),
            "status": res.status,
        }

    def get_game_status(self) -> Dict[str, Any]:
        return {"status": True}

    def get_gameboard_status(self) -> Dict[str, Any]:
        return {"status": True}

    def move(self) -> Dict[str, Any]:
        return {"status": True}

    def handle(self, action: str, **kwargs) -> Dict[str, Any]:
        return self.action_map[action](**kwargs)
