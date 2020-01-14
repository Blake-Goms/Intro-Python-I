# Make a class LatLon that can be passed parameters `lat` and `lon` to the
# constructor

# YOUR CODE HERE


class LatLon:
    def __init__(self, lat, lon=0):
        self.lat = lat
        self.lon = lon

# Make a class Waypoint that can be passed parameters `name`, `lat`, and `lon` to the
# constructor. It should inherit from LatLon. Look up the `super` method.

# YOUR CODE HERE


class Waypoint(LatLon):
    # default constructor
    def __init__(self, name):
        self.name = name
        # LatLon is being represensted by super()
        super().__init__(self)

    # parameterized constructor
    # __str__ (dunder str) is converting object to string
    def __str__(self):
        # do something
        return f"Name: {self.name}, lon: {self.lon}, lat: {self.lat}"

# Make a class Geocache that can be passed parameters `name`, `difficulty`,
# `size`, `lat`, and `lon` to the constructor. What should it inherit from?

# YOUR CODE HERE


class Geocache(LatLon):
    # default constructor
    def __init__(self, difficulty, size):
        self.difficulty = difficulty
        self.size = size
        # LatLon is being represensted by super()
        super().__init__(self)

    def __str__(self):
        # do something
        return f"Name: {self.name}, lon: {self.lon}, lat: {self.lat}, difficulty: {self.difficulty}, size: {self.size}"


# Make a new waypoint and print it out: "Catacombs", 41.70505, -121.51521
# YOUR CODE HERE

# Waypoint only has name, so set name. Assign lat/lon through super
waypoint = Waypoint("Catacombs")
waypoint.lat = 41.70505
waypoint.lon = -121.51521

# Without changing the following line, how can you make it print into something
# more human-readable? Hint: Look up the `object.__str__` method
print(waypoint.__str__())

# Make a new geocache "Newberry Views", diff 1.5, size 2, 44.052137, -121.41556
# YOUR CODE HERE

# Geocache only has values diff and size, assign other values through Super
geocache = Geocache(1.5, 2)
geocache.name = "Newberry Views"
geocache.lat = 44.052137
geocache.lon = -121.41556

# Print it--also make this print more nicely
print(geocache.__str__())
# calling __str__ in the class def itself handles this for us
