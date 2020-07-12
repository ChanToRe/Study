import cv2
import numpy as np
import matplotlib.pyplot as plt

image1 = np.full((512, 512, 3), 255, np.uint8)
image_line = cv2.line(image1, (0, 0), (255, 255), (255, 0, 0), 3)
plt.imshow(image_line)
plt.show()

image2 = np.full((512, 512, 3), 255, np.uint8)
image_rectangle = cv2.rectangle(image2, (20, 20), (255,255), (255, 0, 0), 3)
plt.imshow(image_rectangle)
plt.show()

image3 = np.full((512, 512, 3), 255, np.uint8)
image_circle = cv2.circle(image3, (255, 255), 40, (255, 0, 0), 3)
plt.imshow(image_circle)
plt.show()

image4 = np.full((512, 512, 3), 255, np.uint8)
points = np.array([[5, 5], [10, 392], [283, 293], [382, 492]])
image_polylines = cv2.polylines(image4, [points], True, [255, 0, 0], 3)
plt.imshow(image_polylines)
plt.show()

image5 = np.full((512, 512, 3), 255, np.uint8)
image_text = cv2.putText(image5, 'Hi', (10, 255), cv2.FONT_ITALIC, 2, (255, 0, 0), 3)
plt.imshow(image_text)
plt.show()