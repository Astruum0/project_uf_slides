###CONTROLLER TEST###
from inputs import get_gamepad, devices, DeviceManager
#####################


class devices:
    def controller_inputs():
        devices = DeviceManager()
        while 1:
            events = get_gamepad()
            for event in events:
                print(event.ev_type, event.code, event.state)


devices.controller_inputs()
