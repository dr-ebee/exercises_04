################################# Question 5 ###################################
#
# Write a function that takes as input 2 coordinates and returns True if those
# coordinates are inside a circle of radius 100 and False if the coordinates
# are outside the circle. Assume the circle is centered at the origin (0, 0).
#
# HINT: If a point is inside a circle, then the distance between that point and
# the center of the circle is less than or equal to the radius.
#
# ANOTHER HINT: The distance between a point and the origin (0, 0) can be found
# using the Pythagorean theorem:
#     distance = sqrt( x^2 + y^2 )

def is_in_circle(x, y):
    radius = 100

print(is_in_circle(90, 90)) # Should be False
print(is_in_circle(-30, 10)) # Should be True
