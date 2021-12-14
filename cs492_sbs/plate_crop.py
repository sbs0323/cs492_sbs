import os, sys
from PIL import Image, ImageFile
ImageFile.LOAD_TRUNCATED_IMAGES = True

dir = "./datasets/plates/"
img = "images/"
lab = "labels/"

def crop(dir, img, lab, filename):

    ori_img = Image.open(img+filename+".jpg")
    
    # print(ori_img)
    label = open(lab+filename+".txt", 'r')
    loc = label.read()
    #print(loc.split())
    loc = loc.split()
    x = ori_img.size[0]*float(loc[1])
    y = ori_img.size[1]*float(loc[2])
    w = ori_img.size[0]*float(loc[3])
    h = ori_img.size[1]*float(loc[4])

    crop_img = ori_img.crop((int(x-w//2), int(y-h//2),int(x+w//2), int(y+h//2)))
    # print((int(x-w//2), int(y-h//2),int(x+w//2), int(y+h//2)))
    #crop_img.show()
    #crop_img.save(dir+filename+"_crop.jpg")

    resize_img = crop_img.resize((640,320))

    cr_img1 = resize_img.crop((0,0, 172, 131))
    # print(cr_img1)
    cr_img2 = resize_img.crop((172, 0, 285, 131))
    # print(cr_img2)
    cr_img3 = resize_img.crop((285, 0, 389, 131))
    cr_img4 = resize_img.crop((389, 0, 551, 131))
    cr_img5 = resize_img.crop((0, 131, 301, 320))
    cr_img6 = resize_img.crop((301, 131, 551, 320))

    cr_img1.save(dir+filename+"_crop_1.jpg")
    cr_img2.save(dir+filename+"_crop_2.jpg")
    cr_img3.save(dir+filename+"_crop_3.jpg")
    cr_img4.save(dir+filename+"_crop_4.jpg")
    cr_img5.save(dir+filename+"_crop_5.jpg")
    cr_img6.save(dir+filename+"_crop_6.jpg")
#filename = 'gaon_kaist_n11_242956007_381566233525193_1920517628080089950_n'
#crop(dir+img, dir+lab, filename )