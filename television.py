

class Television:
    MIN_VOLUME = 0
    MAX_VOLUME = 2
    MIN_CHANNEL = 0
    MAX_CHANNEL = 3

    def __init__(self) -> None:
        self.__status = False
        self.__muted = False
        self.__volume = Television.MIN_VOLUME
        self.__channel = Television.MIN_CHANNEL

        self.__volume_muted_at = self.__volume

    def power(self) -> None:
        """
        Turns on/off the television by changing the value of the status variable
        """
        self.__status = not self.__status

    def mute(self) -> None:
        """
        Mutes/unmutes the television (when it's on) by changing the value of the muted variable
        """
        if self.__status:
            if not self.__muted:
                self.__volume_muted_at = self.__volume  # records the volume muted at if not already muted
            self.__muted = not self.__muted

            if self.__muted:
                # I'm assuming the value here is desired to be 0, and that min_volume will always be 0
                self.__volume = Television.MIN_VOLUME
            else:
                self.__volume = self.__volume_muted_at

    def channel_up(self) -> None:
        """
        Increase the tv channel value (when the tv is on). Will wrap around if at the maximum channel value;
        ex: max_channel + 1 = min_channel
        """
        if self.__status:
            self.__channel = (self.__channel + 1) if self.__channel < Television.MAX_CHANNEL else Television.MIN_CHANNEL

    def channel_down(self) -> None:
        """
        Decrease the tv channel value (when the tv is on). Will wrap around if at the minimum channel value;
        ex: min_channel - 1 = max_channel
        """
        if self.__status:
            self.__channel = (self.__channel - 1) if self.__channel > Television.MIN_CHANNEL else Television.MAX_CHANNEL

    def volume_up(self) -> None:
        """
        Increases the tv volume (when the tv is on). Does nothing if the volume value is at the maximum value.
        """
        if self.__status:
            if self.__muted:
                self.__muted = False
                self.__volume = self.__volume_muted_at
            if self.__volume < Television.MAX_VOLUME:
                self.__volume += 1

    def volume_down(self) -> None:
        """
        Decreased the tv volume (when the tv is on). Does nothing if the volume value is at the minimum value.
        """
        if self.__status:
            if self.__muted:
                self.__muted = False
                self.__volume = self.__volume_muted_at
            if self.__volume > Television.MIN_VOLUME:
                self.__volume -= 1

    def __str__(self) -> str:
        """
        Sends the values of the tv object in the following format:
        Power = [status], Channel = [channel], Volume = [volume];
        where the items in brackets will hold the current values for those variables.
        :return: String representation of the tv object.
        """
        return f'Power = {self.__status}, Channel = {self.__channel}, Volume = {self.__volume}'
