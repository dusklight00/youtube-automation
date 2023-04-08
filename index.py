from wrappers.vidgear_wrapper import create_write_gear_instance
import cv2
from tqdm import tqdm

image = cv2.imread("background.png")

writer = create_write_gear_instance("output1.mp4")

for i in tqdm(range(1000)):
    writer.write(image)

writer.close()
