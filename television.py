

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

    def power(self):
        """
        Turns on/off the television by changing the value of the status variable
        :return:
        """
        pass

    def mute(self):
        """
        Mutes/unmutes the television (when it's on) by changing the value of the muted variable
        :return:
        """
        pass

    def channel_up(self):
        """
        Increase the tv channel value (when the tv is on). Will wrap around if at the maximum channel value;
        ex: max_channel + 1 = min_channel
        :return:
        """
        pass

    def channel_down(self):
        """
        Decrease the tv channel value (when the tv is on). Will wrap around if at the minimum channel value;
        ex: min_channel - 1 = max_channel
        :return:
        """
        pass

    def volume_up(self):
        """
        Increases the tv volume (when the tv is on). Does nothing if the volume value is at the maximum value.
        :return:
        """
        pass

    def volume_down(self):
        """
        Decreased the tv volume (when the tv is on). Does nothing if the volume value is at the minimum value.
        :return:
        """
        pass

    def __str__(self):
        """
        Sends the values of the tv object in the following format:
        Power = [status], Channel = [channel], Volume = [volume];
        where the items in brackets will hold the current values for those variables.
        :return:
        """
        pass
