from abc import abstractmethod, ABC


class Duck(ABC):
    @staticmethod
    @abstractmethod
    def quack():
        pass

    @staticmethod
    @abstractmethod
    def walk():
        pass

    @staticmethod
    @abstractmethod
    def fly():
        pass


class RubberDuck:
    @staticmethod
    def quack() -> str:
        return 'Squeek'


class RobotDuck(Duck):
    HEIGHT = 50

    def __init__(self) -> None:
        self.height = 0

    @staticmethod
    def quack() -> str:
        return 'Robotic quacking'

    @staticmethod
    def walk() -> str:
        return 'Robotic walking'

    def fly(self):
        """can only fly to specific height but
        when it reaches it starts landing automatically"""
        if self.height == RobotDuck.HEIGHT:
            self.land()
        else:
            self.height += 1

    def land(self) -> None:
        self.height = 0
