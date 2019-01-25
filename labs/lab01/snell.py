import math
incidentAngle = float (input("Input incident angle: "))
incidentAngle = math.radians(incidentAngle)
n1 = float (input("Input index of refraction of first medium: "))
n2 = float (input("Input index of refraction of second medium: "))
angleOfRefraction = math.asin(math.sin(incidentAngle) * n1/n2)
print("Angle of Refraction: ", math.degrees(angleOfRefraction))
