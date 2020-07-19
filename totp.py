import os
import pyotp
import pyautogui as pg

try:
	privateKey = os.environ["UEC_2FACTOR_PRIVATEKEY"]
except:
	print("UEC_2FACTOR_PRIVATEKEYを取得できません。\n設定してください。")
	exit()

try:
	key = pyotp.TOTP(privateKey).now()
except:
	print("設定したUEC_2FACTOR_PRIVATEKEYが正しくありません。\n再設定してください。")
	exit()

pg.click()
pg.typewrite(key)

#made by hageron