import math

# Define the angle in degrees
angle_degrees = 45

# Convert degrees to radians
angle_radians = math.radians(angle_degrees)

# Calculate trigonometric values
sine_val = math.sin(angle_radians)
cosine_val = math.cos(angle_radians)
tangent_val = math.tan(angle_radians)

print(f"Angle: {angle_degrees}°")
print(f"Sine: {sine_val}")
print(f"Cosine: {cosine_val}")
print(f"Tangent: {tangent_val}")
