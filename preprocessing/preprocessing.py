import cv2
import numpy as np


def scaleImage(image,a,b):
    """
    Image scaling can be achieved using the open cv resize function
    If you don't specify a size (by using None), then it expects the X and Y scaling factors.
    In our example, the image will be enlarged by a factor of 1.2.
    If we do the same enlargement using cubic interpolation, we can see that the quality improves,
    as seen in the following figure.
    For more information:
    https://subscription.packtpub.com/book/application_development/9781785283932/1/ch01lvl1sec13/image-scaling
    :param image: input image
    :return: scaled image
    """
    image = cv2.resize(image, None, fx=a, fy=b, interpolation=cv2.INTER_LINEAR)
    return image


def binarizeImage(image):
    """
    For more information:
    https://note.nkmk.me/en/python-numpy-opencv-image-binarization/#:~:text=Image%20binarization%20with%20OpenCV%3A%20cv2.,-threshold()&text=You%20can%20binarize%20an%20image,threshold()%20.&text=If%20type%20is%20set%20to,values%20are%20replaced%20with%200%20.
    :param image: any or scaled Image
    :return: binarized image
    """
    threshold_value, image = cv2.threshold(image, 128, 255, cv2.THRESH_OTSU)
    return image


def gaussianFilter(image):
    """
    For more information:
    https://opencv24-python-tutorials.readthedocs.io/en/stable/py_tutorials/py_imgproc/py_filtering/py_filtering.html
    :param image:
    :return:
    """
    image = cv2.GaussianBlur(image,(5,5),0)
    return image


def morphImage(image):
    """
    For detailed information:
    https://opencv-python-tutroals.readthedocs.io/en/latest/py_tutorials/py_imgproc/py_morphological_ops/py_morphological_ops.html
    :param image:
    :return:
    """
    kernel_1 = np.ones((7,7),np.uint8)
    kernel_2 = np.ones((3,3), np.uint8)
    image = cv2.erode(image, kernel_1, iterations=1)
    image = cv2.dilate(image, kernel_1, iterations=1)

    return image


def paddingLeft(image):
    image = cv2.copyMakeBorder(image,10,10,10,10,cv2.BORDER_CONSTANT,value=(255,0,0))
    return image


def preprocessing(image):
    """
    This function is called in order to process the 5 basic operations on any image
    :param image: image
    :return: processed image
    """

    image = np.array(image)
    image = scaleImage(image, 1.2, 1.1)
    image = binarizeImage(image)
    # image = gaussianFilter(image)
    image = morphImage(image)
    # image = scaleImage(image, 0.8, 1)
    # image = paddingLeft(image)
    cv2.imshow('frame1', image)
    cv2.waitKey(0)
    cv2.destroyAllWindows()
    return image