# -*- coding: utf-8 -*-
"""
Messenger Thread.

@auteur: Darkness4
"""
from threading import Thread
from time import asctime, sleep, time


def progress(i: int) -> bytes:
    """
    Progress bar, for arduino 5px large.

    Parameters
    ----------
    i : int
        Select which character to send to Arduino.

    Returns
    -------
    bytes : Character send to Arduino.

    """
    switcher = {i <= 0: b"\x07",
                i == 1: b"\x02",
                i == 2: b"\x03",
                i == 3: b"\x04",
                i == 4: b"\x05",
                i >= 5: b"\x06"}
    return switcher[True]


class Messenger(Thread):
    """
    Give order to the arduino.

    Attributes
    ----------
    __armor : int
        Armor points.
    __health : int
        Health points.
    __kills : tuple
        Number of kills and heads.
    __money : int
        Money left.
    __refresh : bool
        Status of the refresher.
    __start : bool
        Status of Messenger.
    __status : string
        Status of the round.
    ser_arduino : Serial
        Serial class of the Arduino.

    Methods
    -------
    bomb_timer()
        Start a bomb timer.
    idle()
        Put Messenger on idle and write a message.
    run()
        Start the Thread and run Messenger.
    shutdown()
        Shutdown Messenger.
    write_player_stats()
        Write the player stats on Arduino.

    """
    __armor = None
    __health = None
    __kills = None  # tuple (total kills - hs, hs)
    __money = None
    __refresh = False  # Order to refresh informations
    __start = True  # Order to start/stop
    __status = "None"

    def __init__(self, ser_arduino) -> None:
        """Init save."""
        super(Messenger, self).__init__()
        self.ser_arduino = ser_arduino

    @property
    def armor(self) -> int:
        """Get the armor."""
        return self.__armor #error: Incompatible return value type (got "None", expected "int")

    @armor.setter
    def armor(self, armor: int) -> None:
        """Set the armor."""
        self.__armor = armor

    @property
    def money(self) -> int:
        """Get the money."""
        return self.__money #error: Incompatible return value type (got "None", expected "int") 

    @money.setter
    def money(self, money: int) -> None:
        """Set the money."""
        self.__money = money

    @property
    def health(self) -> int:
        """Get the health."""
        return self.__health #error: Incompatible return value type (got "None", expected "int")

    @health.setter
    def health(self, health: int) -> None:
        """Set the health."""
        self.__health = health

    @property
    def status(self) -> str:
        """Get the status."""
        return self.__status

    @status.setter
    def status(self, status: str) -> None:
        """
        Change Messenger behavior.

        Available status:
        'None'
        'Bomb'
        '!Freezetime'
        'Freezetime'
        'Defused'
        'Exploded'
        """
        self.__status = status
        self.__refresh = True  # Informations need to be refreshed

    @property
    def kills(self) -> tuple:
        """Get the kills (K, HS)."""
        return self.__kills #error: Incompatible return value type (got "None", expected "Tuple[Any, ...]")

    @kills.setter
    def kills(self, kills_heads: tuple) -> None:
        """Set the number of kills (K, HS)."""
        self.__kills = (int(kills_heads[0])-int(kills_heads[1]),
                        int(kills_heads[1]))

    def run(self) -> None:
        """Thread start."""
        while self.__start:
            if self.__refresh:
                self.__refresh = False  # Has refreshed
                if self.status in ("Bomb", "Defused", "Exploded"):  # Bomb
                    self.bomb_timer()

                elif self.status == "None":
                    self.idle()

                else:  # Default status
                    self.write_player_stats()
            else:
                sleep(0.1)  # Saving consumption
        print(asctime(), "-", "Messenger is dead.")

    def bomb_timer(self) -> None:
        """40 sec bomb timer on arduino."""
        offset = time()
        actualtime = 40 - time() + offset
        while actualtime > 0 and self.status == "Bomb":
            oldtime = int(actualtime)
            sleep(0.1)
            actualtime = 40 - time() + offset
            if oldtime != int(actualtime):  # Actualization only integer change
                self.ser_arduino.write(b'BOMB PLANTED')
                # Wait for second line
                sleep(0.1)
                self.ser_arduino.write(progress(int(actualtime)))  # 5s
                self.ser_arduino.write(progress(int(actualtime - 5)))  # 10s
                self.ser_arduino.write(progress(int(actualtime - 10)))  # 15s
                self.ser_arduino.write(progress(int(actualtime - 15)))  # 20s
                self.ser_arduino.write(progress(int(actualtime - 20)))  # 25s
                self.ser_arduino.write(progress(int(actualtime - 25)))
                self.ser_arduino.write(progress(int(actualtime - 30)))
                self.ser_arduino.write(progress(int(actualtime - 35)))
                self.ser_arduino.write(bytes(str(int(actualtime)).encode()))
                sleep(0.1)
        if self.status == "Defused":
            self.ser_arduino.write(b'BOMB DEFUSED')
            # Wait for second line
            sleep(0.1)
            self.ser_arduino.write(b' ')
            sleep(0.1)
        elif self.status == "Exploded":
            self.ser_arduino.write(b'BOMB EXPLODED')
            # Wait for second line
            sleep(0.1)
            self.ser_arduino.write(b' ')
            sleep(0.1)

    def write_player_stats(self) -> None:
        """Player stats writer."""
        # Not too fast
        sleep(0.1)

        # Writing health and armor in Serial
        self.ser_arduino.write(b'H: ')
        self.ser_arduino.write(progress(int(self.health / 5)))
        self.ser_arduino.write(progress(int((self.health - 25) / 5)))
        self.ser_arduino.write(progress(int((self.health - 50) / 5)))
        self.ser_arduino.write(progress(int((self.health - 75) / 5)))
        self.ser_arduino.write(b' A: ')
        self.ser_arduino.write(progress(int(self.armor / 5)))
        self.ser_arduino.write(progress(int((self.armor - 25) / 5)))
        self.ser_arduino.write(progress(int((self.armor - 50) / 5)))
        self.ser_arduino.write(progress(int((self.armor - 75) / 5)))

        # Wait for second line
        sleep(0.1)

        # Kill or Money
        if self.status == "!Freezetime":
            # HS and Kill counter
            self.ser_arduino.write(b'K: ')
            for _ in range(self.kills[0]):  # counting
                self.ser_arduino.write(b'\x00')  # Byte 0 char : kill no HS
            for _ in range(self.kills[1]):  # counting
                self.ser_arduino.write(b'\x01')  # Byte 1 char : HS
        # Not kill streak
        elif self.status == "Freezetime":
            self.ser_arduino.write(
                bytes('M: {}'.format(self.money).encode()))
        sleep(0.1)

    def idle(self) -> None:
        """Print text while idling."""
        self.ser_arduino.write(b'Waiting for')
        sleep(0.1)
        self.ser_arduino.write(b'matches')

    def shutdown(self) -> None:
        """Stop Messenger."""
        self.__start = False
