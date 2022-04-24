class Television:
    MIN_CHANNEL = 0     # Minimum TV channel
    MAX_CHANNEL = 3     # Maximum TV channel

    MIN_VOLUME = 0      # Minimum TV volume
    MAX_VOLUME = 2      # Maximum TV volume

    def __init__(self) -> None:
        """
        This method initializes all changeable variables for the object
        """
        self.pow: bool = False
        self.chan: int = self.MIN_CHANNEL
        self.vol: int = self.MIN_VOLUME

    def power(self) -> None:
        """
        This method reverses the power state when called; true of on, false for off
        """
        if self.pow == True:
            self.pow = False
        else:
            self.pow = True

    def channel_up(self) -> None:
        """
        This method increments the channel by 1 if power is on; it loops to min if channel is at max when called
        """
        if self.pow == True:
            if self.chan == self.MAX_CHANNEL:
                self.chan = self.MIN_CHANNEL
            else:
                self.chan += 1
        else:
            pass

    def channel_down(self) -> None:
        """
        this method decrements channel by 1 if power is on; loops to max if channel is min when called
        """
        if self.pow == True:
            if self.chan == self.MIN_CHANNEL:
                self.chan = self.MAX_CHANNEL
            else:
                self.chan -= 1
        else:
            pass

    def volume_up(self) -> None:
        """
        This increment volume by 1 if power is on; stays at max if volume is max when called
        """
        if self.pow == True:
            if self.vol == self.MAX_VOLUME:
                pass
            else:
                self.vol += 1
        else:
            pass

    def volume_down(self) -> None:
        """
        This method decrements the volume by 1 if power is on; stays at min if volume is at min when called
        """
        if self.pow == True:
            if self.vol == self.MIN_VOLUME:
                pass
            else:
                self.vol -= 1
        else:
            pass

    def __str__(self) -> str:
        """
        This method creates a string of the current attributes when the object is printed
        :return: string that contains attributes of the object
        """
        return str(f'TV status: Is on = {self.pow}, Channel = {self.chan}, Volume = {self.vol}')
