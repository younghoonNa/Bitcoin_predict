import numpy as np, cv2
from PIL import ImageGrab
from filter_use import alp
# from project_func import grid_remove, contrast_max, find_title, min_idx, min_li, coin__pred_algorithm
from img_pop import bithumb_coin_image, bithumb_title_image
from project_func import *
import argparse
import ctypes
import os
import sys
import pybithumb

np.set_printoptions(threshold=np.inf, linewidth=np.inf) # 출력 제한 없음.

# user32 = ctypes.windll.user32
# screensize = user32.GetSystemMetrics(0), user32.GetSystemMetrics(1)

def runs(
    stock_exchange = "bithumb",
    Access_key = "Input Your Access Key",
    Secret_key = "Input Your Secret Key",
    balance = 10000,
    Mode = None,
    view = None
):
    Access_key = "Input Your Access Key"
    Secret_key = "Input Your Secret Key"

    title_img, sub_title_img = bithumb_title_image()
    coin_img,sub_coin_img = bithumb_coin_image()
    # title_img = sub_title_img
    # coin_img = sub_coin_img

    if view == "True":
        cv2.imshow("title_img", title_img)
        cv2.imshow("coin_img", coin_img)


    title_img = contrast_max(title_img, 150)



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
    row_li = np.argmin(title_img, axis=1)
    row_min, row_max = min_idx(row_li)

    title_img = title_img[row_min+1:row_min + 13]

    title = bithumb_find_title(title_img, sub_title_img, alp(), view)
    print(title)

    if view == "True":
        cv2.imshow("title_img", title_img)

    if not (title in pybithumb.get_tickers()):
        print(title, "에 해당하는 종목이 없습니다.")
        return 0
    else: print(title, "종목의 그림을 분석합니다.")


    ####################################################
    # coin 예측 Algorithm 구현
    ####################################################
    investment = bithumb_coin__pred_algorithm(coin_img, Mode, view)
    if not investment:
        print("하락 예측입니다.")
        return 0
    else:
        print("상승 예측이므로 매수를 진행합니다.")


    print("Current", title, "Price : " ,pybithumb.get_current_price(title))
    price = pybithumb.get_current_price(title)

    bithumb = pybithumb.Bithumb(Access_key , Secret_key)

    # 현재 내 잔고 확인
    # print(upbit.get_balances())
    ret = bithumb.buy_limit_order(title, price, 1)
    print(ret)
    if ret["message"] == "Invalid Apikey":
        print("매수 실패, API 키가 다릅니다.")

    return 0