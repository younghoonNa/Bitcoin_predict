import numpy as np
import cv2
from PIL import ImageGrab
import ctypes
import pickle
import argparse


np.set_printoptions(threshold=np.inf, linewidth=np.inf) # 출력 제한 없음.

user32 = ctypes.windll.user32
screensize = user32.GetSystemMetrics(0), user32.GetSystemMetrics(1)

imgGrab = ImageGrab.grab(bbox=(0, 0, screensize[0], screensize[1],))
image = cv2.cvtColor(np.array(imgGrab), cv2.COLOR_RGB2BGR)
count = 0
cro_list = []

def onMouse(event, x,y, flags, param):
    global count, image


    if count > 1:
        cv2.destroyWindow("image")

    if event == cv2.EVENT_LBUTTONDOWN:
        image = cv2.circle(image, (x,y), 5, (0,0, 255))
        cro_list.append((x,y))
        count += 1


    cv2.imshow("image", image)

def run(
    stock_exchange="upbit",
):

    cv2.imshow("image", image)
    cv2.setMouseCallback("image",  onMouse)
    cv2.waitKey(0)

    th = 0
    if stock_exchange == "bithumb":
        th = -5


    new_list = []
    for element in range(2):
        for idx in range(2):

            if cro_list[element][idx] >= 10: mod = 10
            elif cro_list[element][idx] >= 100: mod = 100
            elif cro_list[element][idx] >= 1000: mode = 1000
            if cro_list[element][idx] % mod > 5:
                new_list.append((cro_list[element][idx] + th + (10 - cro_list[element][idx] % mod)))
            else:
                new_list.append((cro_list[element][idx] + th - cro_list[element][idx] % mod))

    path = "./" + stock_exchange + ".p"
    print(len(new_list))
    with open(path, 'wb') as file:  # seatData.p 파일을 바이너리 쓰기 모드(wb)로 열기
        for i in range(len(new_list)):
            # print(new_list[i])
            pickle.dump(new_list[i], file)
        print("File Write finish, Croodinates is", new_list)

    # string = list()
    # with open(path, 'rb') as pickle_file:  # james.p 파일을 바이너리 쓰기 모드(wb)로 열기
    #     print("pickle")
    #     try:
    #         while True:
    #             s = (pickle.load(pickle_file))
    #             print(s)
    #             string.append(s)
    #             # string
    #             # string += [pickle.load(pickle_file)]
    #     except:
    #         pass
    # print(string)


def parse_opt():
    parser = argparse.ArgumentParser()
    parser.add_argument('--stock_exchange', default="upbit", type= str)

    opt, _ = parser.parse_known_args()
    return opt

def main(opt):
    run(**vars(opt))

if __name__ == "__main__":
    opt = parse_opt()
    main(opt)
