

class Television:
    MIN_VOLUME = 0
    MAX_VOLUME = 2
    MIN_CHANNEL = 0
    MAX_CHANNEL = 3

    def __init__(self):
        self.__status = False
        self.__muted = False
        self.__volume = Television.MIN_VOLUME
        self.__channel = Television.MIN_CHANNEL

        self.__volume_muted_at = self.__volume

    def power(self):
        self.__status = not self.__status

    def mute(self):
        if self.__status:
            if not self.__muted:
                self.__volume_muted_at = self.__volume  # records the volume muted at if not already muted
            self.__muted = not self.__muted

            if self.__muted:
                # I'm assuming the value here is desired to be 0, and that min_volume will always be 0
                self.__volume = Television.MIN_VOLUME
            else:
                self.__volume = self.__volume_muted_at

    def channel_up(self):
        if self.__status:
            self.__channel = (self.__channel + 1) if self.__channel < Television.MAX_CHANNEL else Television.MIN_CHANNEL

    def channel_down(self):
        if self.__status:
            self.__channel = (self.__channel - 1) if self.__channel > Television.MIN_CHANNEL else Television.MAX_CHANNEL

    def volume_up(self):
        if self.__status:
            if self.__muted:
                self.__muted = False
                self.__volume = self.__volume_muted_at
            if self.__volume < Television.MAX_VOLUME:
                self.__volume += 1

    def volume_down(self):
        if self.__status:
            if self.__muted:
                self.__muted = False
                self.__volume = self.__volume_muted_at
            if self.__volume > Television.MIN_VOLUME:
                self.__volume -= 1

    def __str__(self):
        return f'Power = {self.__status}, Channel = {self.__channel}, Volume = {self.__volume}'
