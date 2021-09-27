#!/usr/bin/env python3
from micro_docker_client import MicroDockerClient
from micro_configuration import MicroConfiguration
import docker
from flask import Flask


# Expose an endpoint
# Pull image -> deploy ctr / compose / swarm stack

app = Flask(__name__)


@app.route("/micro-cd/reload", methods=['PUT'])
def reload():
    try:
        config = MicroConfiguration(image_name='nginx', exposed_port=8080, container_port=80, name='SDK_TEST')
        micro_client = MicroDockerClient(micro_configuration=config)
        micro_client.delete()
        micro_client.pull()
        micro_client.run()
        return "Done"
    except Exception as err:
        return err

if __name__ == '__main__':
    from waitress import serve
    serve(app, host="0.0.0.0", port=4321)
    # app.run(host="localhost", port=4321, debug=True)