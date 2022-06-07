import numpy as np, cv2
from PIL import ImageGrab
import bithumb
import upbit
from filter_use import alp
# from project_func import grid_remove, contrast_max, find_title, min_idx, min_li, coin__pred_algorithm
from img_pop import bithumb_coin_image, bithumb_title_image
from project_func import *
import argparse
import ctypes
from upbit import runs
from bithumb import runs
import os
import sys
import pybithumb

np.set_printoptions(threshold=np.inf, linewidth=np.inf) # 출력 제한 없음.

user32 = ctypes.windll.user32
screensize = user32.GetSystemMetrics(0), user32.GetSystemMetrics(1)

def runs(
    stock_exchange = "upbit",
    Access_key = "GPbxsMmlg9PvWjTqjW8crOixD2XP2kOTkLE5NG5j",
    Secret_key = "9xMxzlZARpYRw0xf7IR8rxxAHlZ8aszXxkH8PoAa",
    balance = 10000,
    Mode = None
):
    # Mode = "bright"
    Access_key = "GPbxsMmlg9PvWjTqjW8crOixD2XP2kOTkLE5NG5j"
    Secret_key = "9xMxzlZARpYRw0xf7IR8rxxAHlZ8aszXxkH8PoAa"

    if stock_exchange == "upbit": upbit.runs("upbit", Access_key, Secret_key, Mode)
    elif stock_exchange == "bithumb" : bithumb.runs("bithumb", Access_key, Secret_key, Mode)


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
