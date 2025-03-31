import os
import flask
import grpc

import grpc_client


app = flask.Flask(__name__)


@app.post("/")
def handle():
    data = flask.request.get_json()
    if "action" in data:
        response = cl.handle(data["action"], **data)
        return flask.jsonify(response)
    else:
        flask.abort(
            400, description="Bad Request: 'action' key is missing in the request data."
        )


if __name__ == "__main__":
    GAME_SERVER_ADDRESS = os.getenv("TP_GAME_SERVER_ADDRESS")
    print(GAME_SERVER_ADDRESS)

    with grpc.insecure_channel(f"{GAME_SERVER_ADDRESS}:9990") as channel:

        cl = grpc_client.GRPCClient(channel)

        app.run(host="0.0.0.0", port=9999)
