import os
import pandas as pd
import uuid

def randomImgID(img_name):
	'''
		generating random image id with MD5 encryption
	'''
	return uuid.uuid3(uuid.NAMESPACE_DNS, img_name)

if __name__ == "__main__":
	img_list = pd.read_csv("imgList_ref.csv", header=None)
	img_list = img_list[0].values

	img_ids = []
	for img_name in img_list:
		img_id = randomImgID(img_name)
		# print(img_name, img_id)
		img_ids.append(img_id)

	df = pd.DataFrame({"imgName": img_list, "imgID": img_ids})
	df.to_csv("imgNameID_ref.csv", index=False)
