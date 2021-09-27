import docker

class MicroDockerClient:
    def __init__(self, micro_configuration):
       self.client = docker.from_env()
       self.config = micro_configuration

    def pull(self):
        self.client.images.pull(self.config.image_name)

    def run(self):
        self.client.containers.run(
            self.config.image_name,
            ports={F'{self.config.container_port}/tcp':str(self.config.exposed_port)},
            name=self.config.name,
            detach=True)

    def delete(self):
        try:
            ctr = self.client.containers.list(filters={'name':self.config.name})[0]
            ctr.kill()
            ctr.remove()
        except Exception :
            print("No ctr to delete")