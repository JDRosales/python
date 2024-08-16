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
    """
    Changes status
    """
    def power(self):
        self.__status = not self.__status
    """
    turns mute on and off
    """
    def mute(self):
        if self.__status:
            if not self.__muted:
                self.__muted = True
            else:
                self.__muted = False
        else:
            pass
    """
    turns the channel up 
    """
    def channel_up(self):
        if self.__status:
            if self.__channel == Television.MAX_CHANNEL:
                self.__channel = Television.MIN_CHANNEL
            else:
                self.__channel += 1
    """
    turns the channel down
    """
    def channel_down(self):
        if self.__status:
            if self.__channel == Television.MIN_CHANNEL:
                self.__channel = Television.MAX_CHANNEL
            else:
                self.__channel -= 1
    """
    turns the volume up 
    """
    def volume_up(self):
        if self.__status:
            self.__muted = False
            if self.__volume < Television.MAX_VOLUME:
                self.__volume += 1
            else:
                self.__volume = Television.MAX_VOLUME
        else:
            pass
    """
    turns the volume down
    """
    def volume_down(self):
        if self.__status:
            self.__muted = False
            if self.__volume > Television.MIN_VOLUME:
                self.__volume -= 1
            else:
                self.__volume = Television.MIN_VOLUME
        else:
            pass
    """
    returns the values
    """
    def __str__(self):
        if self.__muted:
            return f"Power = {self.__status}, Channel = {self.__channel}, Volume = {self.MIN_VOLUME}"
        else:
            return f"Power = {self.__status}, Channel = {self.__channel}, Volume = {self.__volume}"
