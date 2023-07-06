### Snowfall

import cv2
import numpy as np

# Define the video dimensions
width, height = 640, 480

# Define the number of snowflakes
num_snowflakes = 100

# Create an empty black canvas
canvas = np.zeros((height, width, 3), np.uint8)

# Create random positions and velocities for the snowflakes
positions = np.random.uniform(low=0, high=width, size=(num_snowflakes, 2))
velocities = np.random.uniform(low=1, high=5, size=(num_snowflakes, 2))

# Define the video codec and create a VideoWriter object
fourcc = cv2.VideoWriter_fourcc(*'mp4v')
out = cv2.VideoWriter('snowfall.mp4', fourcc, 30.0, (width, height))

# Loop to simulate snowfall
while True:
    # Generate a new frame
    canvas.fill(0)

    # Update the snowflake positions
    positions += velocities

    # Wrap the snowflakes around the edges of the canvas
    positions %= (width, height)

    # Draw the snowflakes on the canvas
    for (x, y) in positions:
        cv2.circle(canvas, (int(x), int(y)), 3, (255, 255, 255), -1)

    # Write the frame to the video file
    out.write(canvas)

    # Display the frame
    cv2.imshow('Snowfall', canvas)

    # Check if the 'q' key is pressed to exit
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# Release the VideoWriter and close the windows
out.release()
cv2.destroyAllWindows()
