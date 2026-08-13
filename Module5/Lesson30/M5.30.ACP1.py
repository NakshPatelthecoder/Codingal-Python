from abc import ABC, abstractmethod

class SmartDevice(ABC):

    @abstractmethod
    def turn_on(self):
        pass


class SmartLight(SmartDevice):

    def turn_on(self):
        print("Light turned on")


class SmartSpeaker(SmartDevice):

    def turn_on(self):
        print("Speaker turned on")


class SmartTV(SmartDevice):

    def turn_on(self):
        print("TV turned on")


# Command Center
devices = [
    SmartLight(),
    SmartSpeaker(),
    SmartTV()
]

for device in devices:
    device.turn_on()