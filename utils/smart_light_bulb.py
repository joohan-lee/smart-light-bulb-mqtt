class SmartLightBulb:
    def __init__(self):
        self.bulb_state = "off"  # on/off
        self.brightness_level = 0  # 0 ~ 100

    def turn_on(self):
        self.bulb_state = "on"
        print("*The bulb state switched to 'on'.")

    def turn_off(self):
        self.bulb_state = "off"
        self.brightness_level = 0
        print("*The bulb state switched to 'off'.")

    def set_brightness(self, brightness_level):
        assert brightness_level >= 0 and brightness_level <= 100, 'brightness_level should be between 0 and 100 including both endpoints.'
        self.brightness_level = brightness_level
        print(
            f"*The brightness level of bulb set to '{str(brightness_level)}'.")
