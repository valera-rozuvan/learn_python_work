# From "A Byte of Python"
# Source: http://files.swaroopch.com/python/byte_of_python.pdf


class Robot:
    """Represents a robot, with a name."""

    # A class variable.
    population = 0

    def __init__(self, name):
        """Initializes the data."""
        self.name = name
        print("(Initializing {0})".format(self.name))

        # When this person is created, the robot
        # adds to the population.
        Robot.population += 1

    def die(self):
        """I am flying."""
        print("{0} is being destroyed.".format(self.name))

        Robot.population -= 1

        if Robot.population == 0:
            print("{0} was the last one.".format(self.name))
        else:
            print("There are still {0:d} robots working.".format(
                Robot.population))

    def sayHi(self):
        """Greetings by the robot.
        Yeah, they can do that."""
        print("Greetings, my masters call me {0}.".format(self.name))

    @classmethod
    def howMany(cls):
        """Prints the current population."""
        print("We have {0:d} robots.".format(cls.population))


droid1 = Robot("R2-D2")
droid1.sayHi()
Robot.howMany()

droid2 = Robot("C-3PO")
droid2.sayHi()
Robot.howMany()

print("\nRobots can do some work here.\n")

print("Robots have finished their work. So let's destroy them.")
droid1.die();
droid2.die()

Robot.howMany()
