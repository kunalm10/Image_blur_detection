import cv2
import os
import numpy as np
font = cv2.FONT_HERSHEY_SIMPLEX
def check_blur(img, filename):
    color_img = cv2.imread(img)
    gray_img = cv2.imread(img, cv2.IMREAD_GRAYSCALE)
    laplacian_var = cv2.Laplacian(gray_img, cv2.CV_64F).var()
    if laplacian_var < 900:
        print("Image blurry")
    print(f'{laplacian_var}\n')
    cv2.putText(color_img, f'laplacian_var = {laplacian_var}', (50, 210), font, 1.7, (0, 0, 255), 6, cv2.LINE_4)
    cv2.imshow("img", color_img)
    cv2.waitKey(700)
    cv2.imwrite(str(filename),color_img)
    cv2.destroyAllWindows()

images_path = list()

# path = os.path.join(os.getcwd(), 'test_sharp_images')
# images = os.listdir(os.path.join(os.getcwd(), 'test_sharp_images'))
# print(images)
path = os.path.join(os.getcwd(), 'test_blurry_images')
images = os.listdir(os.path.join(os.getcwd(), 'test_blurry_images'))

for image in images:
    image_path = os.path.join(path, image)
    images_path.append(image_path)
# print(images_path)

# print(image_path)
for index, image in enumerate(images_path):
    print(images[index])
    print(image)
    check_blur(image, images[index])
# for image in os.listdir('/'.join(os.getcwd(), 'test_sharp_images')):
#     print(image)