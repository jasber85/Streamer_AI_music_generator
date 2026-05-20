from twitchAPI.twitch import Twitch
import imutils
import cv2
import os
import glob


my_app_id = "2cycuwui7dpel8ifi37kekgi7pc2xm"
my_app_secret = "zexwnwnif9x79hwoiuryd9qr3no7f6"

def get_twitch_user(APP_ID, APP_SECRET, STREAMER_NAME):
	# create instance of twitch API and create app authentication
	twitch = Twitch(APP_ID, APP_SECRET)
	try:
		# get user info
		user_info = twitch.get_users(logins=[STREAMER_NAME])
	except:
		print("except")
		user_info = ""
		return user_info
	if user_info != "":
		# get user profile image url
		user_profile_image_url = user_info["data"][0]["profile_image_url"]
		# print(user_profile_image_url)
		save_image(user_profile_image_url, STREAMER_NAME)
	
def save_image(IMAGE_URL, STREAMER_NAME):
	# 刪除profile_image下的所有png檔案
	py_files = glob.glob('profile_image/*.png')
	for py_file in py_files:
		try:
			os.remove(py_file)
		except OSError as e:
			print(f"Error:{ e.strerror}")
	# 儲存profile image至profile_image資料夾
	save_path = "profile_image/profile.png"
	image = imutils.url_to_image(IMAGE_URL)
	cv2.imwrite(save_path, image)
	
# 輸入三個參數(twitch應用程式ID, twitch應用程式密碼, 實況頻道ID)
#get_twitch_user(my_app_id, my_app_secret, "userID")