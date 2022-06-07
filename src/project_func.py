import numpy as np, cv2

def CMY(image):
    white = np.array([255,255,255] , np.uint8)
    cmy_img = white - image
    # cv2.imshow("CMY", cmy_img)
    CMY =  cv2.split(cmy_img)
    black  = cv2.min(CMY[0], cv2.min(CMY[1], CMY[2]))
    CMY_black = CMY - black
    CMY_black = cv2.merge([CMY_black[0], CMY_black[1], CMY_black[2]])
    return CMY_black

def dark_mode(image):
    dark_img = 255 - image
    return dark_img

def grid_remove(image):
    image = cv2.GaussianBlur(image, (3,3), sigmaX= 0, sigmaY= 0).astype('uint8')
    dst = cv2.Canny(image, 200, 255)

    # cv2.imshow("dst", dst)
    return dst

# def grid_remove(image):
#     for row in range(image.shape[0]):
#         b = True
#         for col in range(0, image.shape[1] - 10, 10):
#             # print(image[row, col], image[row, col+1])
#             if not (np.array_equal(image[row, col], image[row, col + 10])):
#                 b = False
#
#         # 가로 격자 찾음
#         if b: image[row, col] = [0, 0, 0]
#         # break
#             #
#             # if b:
#             #     for row in range(image.shape[0]):
#             #         for col in range(image.shape[1]):
#             #             if (np.array_equal(image[row, col], grid_rgb)):
#             #                 image[row, col] == [0, 0, 0]
#
#         # image = grid_remove(image)
#         # cv2.imshow("grid remove", image)

# def save():
    # mask = np.array([0, 1, 0, 1, 1, 1, 0, 1, 0])
    # mask = mask.reshape(3, 3).astype('uint8')
    # dil_img = cv2.dilate(grid_img, mask)
    # cv2.imshow("dilate", dil_img)
    #
    # mask = cv2.merge([dil_img, dil_img, dil_img])
    # result = cv2.bitwise_and(image, mask)
    # cv2.imshow("result", result)
    #
    # white_mask = cv2.inRange(result, (150, 150, 150), (255, 255, 255))
    # white_mask = 255 - white_mask
    # white_img = cv2.merge([white_mask, white_mask, white_mask])
    # cv2.imshow("sdw", white_img)
    #
    # smsdsw = cv2.bitwise_and(result, white_img)
    #
    # # dark_img =  dark_mode(image)
    # cv2.imshow("image23", smsdsw)


def min_li(image, idx_min, idx_max):
    image = image[:,idx_min:idx_max]
    b = True
    min_idx, max_idx = 0, 0
    for idx in range(image.shape[1]):

        uniq = list(set(image[:, idx]))
        # print(uniq)
        if uniq[0] == 0 and b:
            b = False
            min_idx = idx

        if uniq[0] != 0 and not b:
            max_idx = idx
            return min_idx, max_idx

    return -1, -1

def min_idx(image):
    b = True
    min_idx, max_idx = 0, 0
    for idx in range(image.shape[0]):

        if image[idx] != 0 and b:
            b = False
            min_idx = idx

        if image[idx] == 0 and not b:
            max_idx = idx
            return min_idx, max_idx
            break

    return -1, -1

def contrast_max(image, threshold):
    image = np.array(image, 'float32')
    image += (image - threshold) * 255
    image += (image - (threshold+1)) * 255

    image = np.clip(image, 0, 255)
    image = np.array(image, 'uint8')

    return  image

def upbit_find_title(image, sub_img, alphabets):
    use_sub = False
    col_num = 0
    event_name = ""
    while col_num < image.shape[1]:
        col_min, col_max = min_li(image, col_num, image.shape[1])
        if col_max == -1 and col_max == -1: break
        al = (255 - image[:, col_min + col_num:col_max + col_num]) / 255

        resize = np.zeros((10, 6), 'float32')
        ratioX = al.shape[0] / resize.shape[0]
        ratioY = al.shape[1] / resize.shape[1]

        for row in range(resize.shape[0]):
            for col in range(resize.shape[1]):
                temp_x = int(row * ratioX)
                temp_y = int(col * ratioY)
                if row * ratioX >= 10:
                    continue
                if temp_y >= 5:
                    temp_y = al.shape[1] - 1

                resize[row, col] = al[temp_x, temp_y]

        # print(resize)

        for alpha, beta in alphabets:
            exit = False

            if np.array_equal(alpha, resize):
                # print("============",beta)
                if beta == "/":
                    exit = True
                    break

                elif beta == "restart":
                    image = sub_img
                    use_sub = True
                    col_num = 0
                    col_max = 0

                else:
                    event_name += beta
                    break

        if exit:
            break

        # print(event_name)
        col_num += col_max

    # print(event_name)
    return event_name, use_sub


def bithumb_find_title(image, sub_img, alphabets):
    col_num = 0
    event_name = ""
    while col_num < image.shape[1]:
        col_min, col_max = min_li(image, col_num, image.shape[1])

        if col_max == -1 and col_max == -1: break
        al = (255 - image[:, col_min + col_num:col_max + col_num]) / 255

        resize = np.zeros((10, 6), 'float32')
        ratioX = al.shape[0] / resize.shape[0]
        ratioY = al.shape[1] / resize.shape[1]

        for row in range(resize.shape[0]):
            for col in range(resize.shape[1]):
                temp_x = int(row * ratioX)
                temp_y = int(col * ratioY)
                if row * ratioX >= 12:
                    continue
                if col * ratioY >= 6:
                    temp_y -= 1

                if int(row * ratioX) == 10:
                    temp_x = 11

                resize[row, col] = al[temp_x, temp_y]


        for alpha, beta in alphabets:
            exit = False

            alpha = np.array(alpha, 'float32')
            alpha = alpha.reshape(10, -1)

            if np.array_equal(alpha, resize):
                if beta == "/":
                    exit = True
                    break

                else:
                    event_name += beta
                    break

        if exit:
            break

        col_num += col_max

    return event_name

def coin__pred_algorithm(image, Mode):

    if Mode != "dark":
        image = 255 - image
    else: image = contrast_max(image, 120)

    black_mask = cv2.inRange(image, (0, 0,0), (20, 20, 20))
    white_mask = cv2.inRange(image, (250, 250, 250), (255, 255, 255))
    cyan_mask = cv2.inRange(image, (110, 110, 0), (255, 255, 50))
    magenta_mask = cv2.inRange(image, (110, 0, 110), (255, 50, 255))

    if Mode == "dark": white_mask = black_mask

    current_price = white_mask[:, -1].argmax()
    days20 = cyan_mask[:, -1].argmax()
    days20_5_Days_ago = cyan_mask[:, -5].argmax()
    days224_20_Days_ago = magenta_mask[:, -20].argmax()
    days224 = magenta_mask[:, -1].argmax()

    # gradient = (y2 - y1) / (x2 - x1)
    gradient_224 = (days224_20_Days_ago - days224) / (20)
    gradient_20 = (days20_5_Days_ago - days20) / (5)




    img_mask = cv2.merge([white_mask, cyan_mask, magenta_mask])
    # # print("20 Days Mean : " ,cyan_mask[:, -1].argmax()) # 20일선 위치
    # # print("224 Days Mean : " ,magenta_mask[:, -1].argmax()) # 224일선 위치
    # # print("Price Mean : " ,white_mask[:, -1].argmax()) # 현재 가격

    # cv2.imshow("image", img_mask)
    #
    # cv2.imshow("black maks ", white_mask)
    # cv2.imshow("cyan maks ", cyan_mask)
    # cv2.imshow("red maks ", magenta_mask)

    li = [current_price, days20, days224]
    li = sorted(li)

    # 0이 아닌 값 중 224일 선이 가장 높은 값과 작은 값 => 224일 선이 중간에 있는지 & 기울기가 양수인지
    days224_min = (list(set(magenta_mask.argmax(axis = 0)))[1])
    days224_max =(list(set(magenta_mask.argmax(axis=0)))[-1])

    if  li[0] == current_price and  li[1] == days20 and li[2] == days224:
        return True

    if days224_min < days224 and days224_max > days224 and gradient_224 > 0 and gradient_20 > 0:
        return True

    return False

def bithumb_coin__pred_algorithm(image, Mode):
    image = 255 - image

    # Blur + Canny Edge를 통한 잡음 제거 후 엣지 검출
    Big_img = cv2.GaussianBlur(image, ksize=(3, 3), sigmaY=0, sigmaX=0)
    Big_img = cv2.Canny(Big_img, 220, 255)


    bit_image = cv2.bitwise_and(image, image, mask=Big_img)     # bitwise_and 해서 다시 칼라 입히기

    image_gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY) # 모폴로지 팽창 연산을 통해 선 굵게 만들기
    mask = np.array([0, 0, 1, 0, 0,
                     0, 1, 1, 1, 0,
                     1, 1, 1, 1, 1,
                     0, 1, 1, 1, 0,
                     0, 0, 1, 0, 0]).astype('uint8')
    mask = mask.reshape(5, 5).astype('uint8')
    dst = cv2.dilate(bit_image, mask)

    dst = np.array(dst, 'float32')
    dst = (dst - 50) * 255
    dst = (dst - 51) * 255
    dst = np.clip(dst, 0, 255)
    dst = np.array(dst, 'uint8')


    zero_img = np.zeros(image.shape[:2]).astype('uint8')
    # print(image)
    white_mask = cv2.inRange(image, (230, 230, 230), (255, 255, 255))
    green_mask = cv2.inRange(image, (30, 30, 0), (255, 255, 30))
    yellow_mask = cv2.inRange(image, (0, 50, 50), (30, 255, 255))
    # black_mask = cv2.inRange(image, (0, 0,0), (30, 30, 30))
    red_mask = cv2.inRange(image, (0, 0, 100), (90, 90, 255))
    img_mask = cv2.merge([white_mask, green_mask, red_mask])
    bolinger_mask = cv2.merge([zero_img, yellow_mask, yellow_mask])

    s = cv2.add(img_mask, bolinger_mask)
    cv2.imshow("sd,", s)
    cv2.waitKey(0)

    current_price = white_mask[:, -1].argmax()
    days20 = green_mask[:, -1].argmax()
    days20_5_Days_ago = green_mask[:, -5].argmax()
    days224_20_Days_ago = red_mask[:, -20].argmax()
    days224 = red_mask[:, -1].argmax()

    # gradient = (y2 - y1) / (x2 - x1)
    gradient_224 = (days224_20_Days_ago - days224) / (20)
    gradient_20 = (days20_5_Days_ago - days20) / (5)

    li = [current_price, days20, days224]
    li = sorted(li)

    # 0이 아닌 값 중 224일 선이 가장 높은 값과 작은 값 => 224일 선이 중간에 있는지 & 기울기가 양수인지
    days224_min = (list(set(red_mask.argmax(axis = 0)))[1])
    days224_max =(list(set(red_mask.argmax(axis=0)))[-1])

    # print("Bolinger High : ", yellow_mask[:, -1].argmax())  # 볼린저 밴드의 윗부분
    # print("Bolinger Low : ", yellow_mask.shape[0] - 1 - yellow_mask[:, -1][::-1].argmax())  # 볼린저 밴드의 아랫부분

    if  li[0] == current_price and  li[1] == days20 and li[2] == days224:
        return True

    if days224_min < days224 and days224_max > days224 and gradient_224 > 0 and gradient_20 > 0:
        return True

    if  yellow_mask.shape[0] - 1 - yellow_mask[:, -1][::-1].argmax():
        return True

    return False


