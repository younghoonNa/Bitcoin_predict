from PIL import ImageGrab
import cv2, numpy as np
import pickle

def upbit_title_image(stock_exchange):
    path = "./" + stock_exchange +  ".p"
    string = list()

    with open(path, 'rb') as pickle_file:
        try:
            while True:
                s = (pickle.load(pickle_file))
                # print(s)
                string.append(s)
        except:
            pass

    # imgGrab = ImageGrab.grab(bbox=(260 / 1920 * screensize[0], 410 / 1080 * screensize[1],
    #                                340 / 1920 * screensize[0], 430 / 1080 * screensize[1]))
    # image_title = cv2.cvtColor(np.array(imgGrab), cv2.COLOR_RGB2GRAY)
    #
    # imgGrab = ImageGrab.grab(bbox=(260 / 1920 * screensize[0], 375 / 1080 * screensize[1],
    #                                340 / 1920 * screensize[0], 395 / 1080 * screensize[1]))
    # sub_image_title = cv2.cvtColor(np.array(imgGrab), cv2.COLOR_RGB2GRAY)

    imgGrab = ImageGrab.grab(bbox=(string[0], string[1], string[0]+100, string[1] + 30))
    image_title = cv2.cvtColor(np.array(imgGrab), cv2.COLOR_RGB2GRAY)

    imgGrab = ImageGrab.grab(bbox=(string[0], string[1]-35, string[0]+100, string[1]-5))
    sub_image_title = cv2.cvtColor(np.array(imgGrab), cv2.COLOR_RGB2GRAY)

    return image_title, sub_image_title

def upbit_coin_image(stock_exchange):

    path = "./" + stock_exchange + ".p"
    string = list()

    # imgGrab = ImageGrab.grab(bbox=(250 / 1920 * screensize[0],
    #                                400 / 1080 * screensize[1],
    #                                1155 / 1920 * screensize[0],
    #                                780 / 1080 * screensize[1],))
    # Big_img = cv2.cvtColor(np.array(imgGrab), cv2.COLOR_RGB2BGR)
    #
    # imgGrab = ImageGrab.grab(bbox=(250 / 1920 * screensize[0],
    #                                365 / 1080 * screensize[1],
    #                                1155 / 1920 * screensize[0],
    #                                745 / 1080 * screensize[1],))
    # sub_Big_img = cv2.cvtColor(np.array(imgGrab), cv2.COLOR_RGB2BGR)

    with open(path, 'rb') as pickle_file:  # james.p 파일을 바이너리 쓰기 모드(wb)로 열기
        try:
            while True:
                s = (pickle.load(pickle_file))
                # print(s)
                string.append(s)
        except:
            pass

    imgGrab = ImageGrab.grab(bbox=(string[0], string[1], string[2], string[3]))
    Big_img = cv2.cvtColor(np.array(imgGrab), cv2.COLOR_RGB2BGR)

    imgGrab = ImageGrab.grab(bbox=(string[0], string[1]+35, string[2]-15, string[3]+65))
    sub_Big_img = cv2.cvtColor(np.array(imgGrab), cv2.COLOR_RGB2BGR)

    return Big_img, sub_Big_img

def bithumb_title_image(screensize):
    stock_exchange = "bithumb"

    imgGrab = ImageGrab.grab(bbox=(735 / 1920 * screensize[0], 385 / 1080 * screensize[1],
                                   835 / 1920 * screensize[0], 405 / 1080 * screensize[1]))
    image_title = cv2.cvtColor(np.array(imgGrab), cv2.COLOR_RGB2GRAY)

    imgGrab = ImageGrab.grab(bbox=(735 / 1920 * screensize[0], 330 / 1080 * screensize[1],
                                   835 / 1920 * screensize[0], 350 / 1080 * screensize[1]))
    sub_image_title = cv2.cvtColor(np.array(imgGrab), cv2.COLOR_RGB2GRAY)

    return image_title, sub_image_title
    # path = "./" + stock_exchange +  ".p"
    # string = list()
    #
    # with open(path, 'rb') as pickle_file:
    #     try:
    #         while True:
    #             s = (pickle.load(pickle_file))
    #             # print(s)
    #             string.append(s)
    #     except:
    #         pass

    # imgGrab = ImageGrab.grab(bbox=(string[0], string[1], string[0]+100, string[1] + 30))
    # image_title = cv2.cvtColor(np.array(imgGrab), cv2.COLOR_RGB2GRAY)
    #
    # imgGrab = ImageGrab.grab(bbox=(string[0], string[1]-35, string[0]+100, string[1]-5))
    # sub_image_title = cv2.cvtColor(np.array(imgGrab), cv2.COLOR_RGB2GRAY)
    #
    # return image_title, sub_image_title

def bithumb_coin_image(screensize):
    stock_exchange = "bithumb"
    path = "./" + stock_exchange +  ".p"
    string = list()

    with open(path, 'rb') as pickle_file:
        try:
            while True:
                s = (pickle.load(pickle_file))
                # print(s)
                string.append(s)
        except:
            pass

    # imgGrab = ImageGrab.grab(bbox=(260 / 1920 * screensize[0], 410 / 1080 * screensize[1],
    #                                340 / 1920 * screensize[0], 430 / 1080 * screensize[1]))
    # image_title = cv2.cvtColor(np.array(imgGrab), cv2.COLOR_RGB2GRAY)
    #
    # imgGrab = ImageGrab.grab(bbox=(260 / 1920 * screensize[0], 375 / 1080 * screensize[1],
    #                                340 / 1920 * screensize[0], 395 / 1080 * screensize[1]))
    # sub_image_title = cv2.cvtColor(np.array(imgGrab), cv2.COLOR_RGB2GRAY)

    # imgGrab = ImageGrab.grab(bbox=(string[0], string[1], string[0]+100, string[1] + 30))
    # image_title = cv2.cvtColor(np.array(imgGrab), cv2.COLOR_RGB2GRAY)
    #
    # imgGrab = ImageGrab.grab(bbox=(string[0], string[1]-35, string[0]+100, string[1]-5))
    # sub_image_title = cv2.cvtColor(np.array(imgGrab), cv2.COLOR_RGB2GRAY)
    #
    # return image_title, sub_image_title

    imgGrab = ImageGrab.grab(bbox=(705 / 1920 * screensize[0],
                                   375 / 1080 * screensize[1],
                                   1545 / 1920 * screensize[0],
                                   710 / 1080 * screensize[1],))
    Big_img = cv2.cvtColor(np.array(imgGrab), cv2.COLOR_RGB2BGR)

    imgGrab = ImageGrab.grab(bbox=(705 / 1920 * screensize[0],
                                   350 / 1080 * screensize[1],
                                   1515 / 1920 * screensize[0],
                                   655 / 1080 * screensize[1],))
    sub_Big_img = cv2.cvtColor(np.array(imgGrab), cv2.COLOR_RGB2BGR)

    return Big_img, sub_Big_img