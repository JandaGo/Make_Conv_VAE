from PIL import Image
from tqdm import tqdm
import glob
import cv2
import numpy as np
# filename_list = glob.glob('./01.jpg')
# PATH = saved_loc + '/' #'/home/jaehan/vae_pytorch_custom/caveweight/'

# /home/pojaehanwer/Downloads/DATASET_PCB/test/PCB_DATASET/images

# /home/pojaehanwer/Downloads/DATASET_PCB/test/crop
PATH = '/home/pojaehanwer/Downloads/DATASET_PCB/test/'
defect = 'Spurious_copper'
filename_list = glob.glob(PATH + "PCB_DATASET/images/" + defect +'/'+'./*.jpg')
# filename_list = glob.glob('/home/pojaehanwer/Downloads/DATASET_PCB/test/PCB_DATASET/images/Missing_hole/' +'./*.jpg')

filename_list.sort()
 
fill_number = len(str(len(filename_list)))
a = 0
# print(fill_number)
for idx, filename in enumerate(tqdm(filename_list), 1):
    im = Image.open(filename)

    # cv2.imshow('window',im)
    # cv2.waitKey(0)

    print(np.shape(im))
    print(a)
    # i = 0
    h, w, c = np.shape(im)
    for i in range(1,5):
        for j in range(1,5):
            area = ((i-1)*(1/4)*w, (j-1)*(1/4)*h, i*(1/4)*w, j*(1/4)*h)
            crop_image = im.crop(area)
            savename = PATH+'crop/'+defect+'/'+'crop_' +str(a)+str(i)+str(j)+ '.jpg'
            # savename = '/home/pojaehanwer/Downloads/DATASET_PCB/test/crop/Missing_hole/'+'crop_' +str(a)+str(i)+str(j)+ '.jpg'
            # savename = './save/crop_' +str(i)+ str(j)+str(idx).zfill(fill_number) + '.jpg'

            crop_image.save(savename)
    a+=1
