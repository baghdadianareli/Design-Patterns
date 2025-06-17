class TypeCPlugInterface:
    def plug_in_type_c(self):
        pass

class TypeADevice:
    def plug_in_type_a(self):
        return "Device plugged in with Type A plug"

class TypeAtoTypeCAdapter(TypeCPlugInterface):
    def __init__(self, device: TypeADevice): # The device parameter should be an instance of the class TypeADevice
        self.device = device

    def plug_in_type_c(self):
        return self.device.plug_in_type_a()

class TypeCSocket:
    def plug_in(self, plug: TypeCPlugInterface):
        print(plug.plug_in_type_c())


# Usage example
if __name__ == "__main__":
    device_a = TypeADevice()
    adapter = TypeAtoTypeCAdapter(device_a)
    socket_c = TypeCSocket()

    socket_c.plug_in(adapter)