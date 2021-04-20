def method_one():
    import cv2
    import os
    import numpy as np
    from skimage.metrics import structural_similarity as ssim

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


# def method_two():
# import the necessary packages
from imutils import paths
import argparse
import cv2
def variance_of_laplacian(image):
    # compute the Laplacian of the image and then return the focus
    # measure, which is simply the variance of the Laplacian
    return cv2.Laplacian(image, cv2.CV_64F).var()

# construct the argument parse and parse the arguments
ap = argparse.ArgumentParser()
ap.add_argument("-i", "--images", required=True,
                help="path to input directory of images")
ap.add_argument("-t", "--threshold", type=float, default=1200.0,
                help="focus measures that fall below this value will be considered 'blurry'")
args = vars(ap.parse_args())

# loop over the input images
for imagePath in paths.list_images(args["images"]):
    # load the image, convert it to grayscale, and compute the
    # focus measure of the image using the Variance of Laplacian
    # method
    image = cv2.imread(imagePath)
    gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    fm = variance_of_laplacian(gray)
    text = "Not Blurry"
    # if the focus measure is less than the supplied threshold,
    # then the image should be considered "blurry"
    if fm < args["threshold"]:
        text = "Blurry"
    # show the image
    cv2.putText(image, "{}: {:.2f}".format(text, fm), (10, 30),
                cv2.FONT_HERSHEY_SIMPLEX, 0.8, (0, 0, 255), 3)
    cv2.imshow("Image", image)
    key = cv2.waitKey(0)
