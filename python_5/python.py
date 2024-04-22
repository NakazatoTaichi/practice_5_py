import cv2
import numpy as np

def crop_circular(image_path):
    # 画像を読み込む
    image = cv2.imread(image_path)

    # 画像の中心座標を計算
    center_x = image.shape[1] // 2
    center_y = image.shape[0] // 2

    # 切り取り半径を計算（画像の横幅の1/4）
    radius = image.shape[1] // 4

    # 円形のマスクを作成
    mask = np.zeros_like(image)
    cv2.circle(mask, (center_x, center_y), radius, (255, 255, 255), -1)

    # 画像とマスクを結合して円形に切り出す
    cropped_image = np.bitwise_and(image, mask)

    return cropped_image

# 入力画像のパス
input_image_path = "/Users/nakazatotaichi/Desktop/practice_5_py/python_5/img/IMG_9248.jpg"

# 円形に切り出した画像を取得
cropped_image = crop_circular(input_image_path)

# 切り出した画像を表示
cv2.imshow("Cropped Image", cropped_image)
cv2.waitKey(0)
cv2.destroyAllWindows()

