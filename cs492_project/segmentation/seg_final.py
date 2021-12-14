import cv2

def final_step(im_o, im):
	# im_o = cv2.imread('./data/images/1209_noon_crop_'+str(k+1)+'.jpg')
	h_o, w_o, _ = im_o.shape
	# print(im_o.shape)
	# im = cv2.imread('./legend'+str(k+1)+'.jpg')
	im = cv2.resize(im, (w_o, h_o), interpolation = cv2.INTER_CUBIC)
	# print(im.shape)
	h, w, c = im.shape 
	cnt = 0
	for i in range(h):
		for j in range(w):
			if(im[i,j,0] <= 240 and im[i,j,1] <= 240 and im[i,j,2] <= 240 ): 
				im[i,j] = [0,0,0]
				cnt = cnt+1

	im = cv2.addWeighted(im_o, 1, im, 0.5, 0)
	# cv2.imwrite('./segresult_'+str(k+1)+'.jpg', im)
	foodarea = float((h*w - cnt) / (h*w) * 100).__round__(2)
	# print( str(cnt) + 'pixels : food area percent' + str(foodarea) + '%')
	return im, cnt, foodarea

