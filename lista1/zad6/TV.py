class TV:
    def __init__(self, channel, volume):
        self.channel = channel
        self.volume = volume

    @property
    def channel(self):
        return self.__channel

    @property
    def volume(self):
        return self.__volume

    @channel.setter
    def channel(self, channel):
        if channel > 1000:
            self.__channel = 999
        else:
            self.__channel = channel

    @volume.setter
    def volume(self, volume):
        if volume > 100:
            self.__volume = 100
        else:
            self.__volume = volume
    def __str__(self):
        return f"{self.channel} + {self.volume} {self.__channel} + {self.__volume} "

telewizor = TV(100, 20)

print(telewizor.volume)
print(telewizor.channel)

telewizor.volume = 1230
telewizor.channel = 1230

print(telewizor.volume)
print(telewizor.channel)

telewizor.volume = 99999
telewizor.channel = 34

print(telewizor.volume)
print(telewizor.channel)

print(telewizor)