from tensorflow.keras.preprocessing.image import ImageDataGenerator
from tensorflow.keras.utils import img_to_array
from tensorflow.keras.utils import load_img
from numpy import expand_dims
import cv2 as cv
import os
os.environ['TF_CPP_MIN_LOG_LEVEL'] = '2'


def createDirectory(directory):
    try:
        if not os.path.exists(directory):
            os.makedirs(directory)
    except OSError:
        print("Error: Failed to create the directory.")


def data_augmenter(img, dir, file_name):
    data = img_to_array(img)
    samples = expand_dims(data, 0)

    size_aug = ImageDataGenerator(width_shift_range=[-20, 20])

    datagen = [size_aug]

    count = 1

    for dg in datagen:
        it = dg.flow(samples, batch_size=1)
        for i in range(1):
            batch = it.next()
            image = batch[0].astype('uint8')
            image = cv.cvtColor(image, cv.COLOR_BGR2RGB)
            cv.imwrite(dir+'\\' + file_name + str(count)+'.jpg', image)
            count += 1


def file_search(alcohol):
    root_path = 'C:\\Users\\IBK\\Documents\\kyx\\elice\\aiproject\\crawl\\train\\'

    al_path = root_path + alcohol
    img_path_list = []
    possible_img_extension = ['.jpg']  # 이미지 확장자들

    dir = ".\\dataset\\{}".format(alcohol)
    createDirectory(dir)
    fn = []

    for (root, dirs, files) in os.walk(al_path):
        if len(files) > 0:
            for file_name in files:
                if os.path.splitext(file_name)[1] in possible_img_extension:
                    img_path = root + '\\' + file_name
                    fn.append(file_name)
                    # 경로에서 \를 모두 /로 바꿔줘야함
                    # img_path = img_path.replace('\\', '/')  # \는 \\로 나타내야함
                    img_path_list.append(img_path)

    for i in range(len(img_path_list)):
        img = load_img(img_path_list[i])
        data_augmenter(img, dir, fn[i])


al_list = ['dry vermouth']
for i in al_list:
    file_search(i)
