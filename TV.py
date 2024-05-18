# Pseudocode

# 1. Create a class and define functions and methods for operating the TV

class TV:
    def __init__(self):
        self.channel = 1
        self.volume_level = 1
        self.on = False
    
    def turn_on(self):
        self.on = True
    
    def turn_off(self):
        self.on = False

    def get_channel(self):
        return self.channel
    
    def set_channel(self, channel):
        if 1 <= channel <= 120:
            self.channel = channel
    
    def get_volume(self):
        return self.volume_level
    
    def set_volume(self, volume_level):
        if 1 <= volume_level <= 7:
            self.volume_level = volume_level
    
    def channel_up(self):
        if self.channel < 120:
            self.channel += 1

    def channel_down(self):
        if self.channel > 1:
            self.channel -= 1

    def volume_up(self):
        if self.volume_level < 7:
            self.volume_level += 1

    def volume_down(self):
        if self.volume_level > 1:
            self.volume_level -= 1


# 2. When the class or the blueprint of the TV is done, create another file named test_tv.py to test and produce the channel and volume level of tv 1 and tv 2