import os
import pyotp
import message
import webbrowser
import pyautogui

environ_name = "UEC_2FACTOR_PRIVATEKEY"

url_help = ""

if os.environ.get(environ_name)==None:
	message.warning(f"環境変数「{environ_name}」が設定されていません。\n設定してください。")
	webbrowser.open(url_help)
	exit()

try:
	totp = pyotp.TOTP(os.environ.get(environ_name)).now()
except:
	message.warning(f"環境変数「{environ_name}」の値が不正です。\n正しい値をセットしてください。")
	webbrowser.open(url_help)
	exit()

pyautogui.click()
pyautogui.typewrite(str(totp))