class MicroConfiguration:
    def __init__(self, image_name, exposed_port, container_port, name):
        self.image_name = image_name
        self.exposed_port = exposed_port
        self. container_port = container_port
        self.name = name
