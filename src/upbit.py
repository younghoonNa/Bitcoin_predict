import numpy as np, cv2
from PIL import ImageGrab
from filter_use import alp
# from project_func import grid_remove, contrast_max, find_title, min_idx, min_li, coin__pred_algorithm
from img_pop import upbit_coin_image, upbit_title_image
from project_func import *
import argparse
import ctypes
import os
import sys
import pyupbit

np.set_printoptions(threshold=np.inf, linewidth=np.inf) # 출력 제한 없음.

user32 = ctypes.windll.user32
screensize = user32.GetSystemMetrics(0), user32.GetSystemMetrics(1)

def runs(
    stock_exchange = "upbit",
    Access_key = "Input Your Access Key",
    Secret_key = "Input Your Secret Key",
    balance = 10000,
    Mode = None
):
    Access_key = "Input Your Access Key"
    Secret_key = "Input Your Secret Key"

    title_img, sub_title_img = upbit_title_image(stock_exchange)
    coin_img, sub_coin_img = upbit_coin_image(stock_exchange)

    if Mode == "dark":
        title_img = 255 - title_img
        sub_title_img = 255 - sub_title_img
        coin_img =  255 - coin_img
        sub_coin_img = 255 - sub_coin_img

        threshold = 120
    else:
        threshold = 150

    title_img = contrast_max(title_img, threshold)
    sub_title_img = contrast_max(sub_title_img, threshold)

    if Mode == "dark":
        if (title_img[:, 0:20] == 255).all():
            title_img = sub_title_img

        else:
            # Dark Mode 일 경우에는 삼각형이 대비 줄이는 과정에서 없어져버림
            # Bright Mode에서는 인식 잘 됌
            pass


    ####################################################
    # tickter(title) 구하기
    ####################################################
    sub_row_li = np.argmin(sub_title_img, axis=1)
    sub_row_min, sub_row_max = min_idx(sub_row_li)

    row_li = np.argmin(title_img, axis=1)
    row_min, row_max = min_idx(row_li)



    title_img = title_img[row_min:row_min + 10]
    sub_title_img = sub_title_img[sub_row_min:sub_row_min + 10]

    title, use_sub = upbit_find_title(title_img, sub_title_img, alp())
    title = "KRW-" + title
    print(title)

    new_title = title

    # 맞지 않는 문자열이 들어올 경우, O 와 Q를 구분 못해서 발생하는 참사를 막기 위해 만듬
    if not (title in pyupbit.get_tickers(fiat = "KRW")):

        if "LT" in title: new_title = "KRW-POLY"
        elif "AV" in title: new_title = title.replace('AV', "AT")
        elif "O" in title: new_title = title.replace('O', "Q")

        print(title, "에 해당하는 종목이 없어", new_title, "로 대체합니다.")
        title = new_title

        if not (title in pyupbit.get_tickers(fiat = "KRW")):
            print("ERROR")
            return 0


    ####################################################
    # coin 예측 Algorithm 구현
    ####################################################
    if use_sub: coin_img = sub_coin_img
    investment = coin__pred_algorithm(coin_img, Mode)
    if not investment:
        print("하락 예측입니다.")
        return 0
    else:
        print("상승 예측이므로 매수를 진행합니다.")


    print("Current", title, "Price : " ,pyupbit.get_current_price(title))
    price = pyupbit.get_current_price(title)

    upbit = pyupbit.Upbit(access= Access_key , secret= Secret_key)

    # 현재 내 잔고 확인
    # print(upbit.get_balances())
    ret = upbit.buy_limit_order(title, price, 1)

    if ret == None:
        print("매수 실패.")

    # cv2.imshow("sd", title_img)
    # cv2.imshow("sdasd", coin_img)
    pass

def parse_opt():
    parser = argparse.ArgumentParser()
    parser.add_argument('--stock_exchange', default="upbit", type= str)
    parser.add_argument('--Access_key', default=None, type=str)
    parser.add_argument('--Secret_key', default=None, type=str)
    parser.add_argument('--Mode', default="bright", type=str)
    parser.add_argument('--balance', default= 10000, type=str)

    opt, _ = parser.parse_known_args()
    return opt

def main(opt):
    runs(**vars(opt))

if __name__ == "__main__":
    opt = parse_opt()
    main(opt)
