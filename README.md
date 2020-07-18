[説明]<br>
キーからTOTPを生成して、入力してくれるやつです。
モジュール流用しただけだし、電通大生しかみてないんでUEC 2FACTORなんとかって名づけました。

windows以外の人は自力で頑張ってね☆

[使い方]<br>
1.Python3系をインストール（してある人は2へ）
https://www.python.jp/install/windows/install_py3.html
そのまま従って

2.pyotpモジュールとpyautoguiモジュールをインストール(してある人は３へ）
「pip3 install pyotp」と「pip3 install pyautogui」をコマンドライン上で実行するだけ

3.環境変数「UEC_2FACTOR_PRIVATEKEY」に秘密鍵設定
https://www.cc.uec.ac.jp/ug/ja/account/index.html#uec-account-2fa
からトークンアプリを利用する→パスワード変更ページ→ログイン→二段階認証→URIのsecret=から&issuer~の間をコピー
この値をUEC_2FACTOR_PRIVATEKEYとして環境変数に登録してください。

4.totp.pyを保存して、保存したディレクトリで「python3 totp.py」ってやったらカーソルがあるところにパスワードが自動入力されます。実行してから入力されるまで時間を空けたい人はtimeモジュールでもインポートして自分でやってね。
https://techplay.jp/column/575
こんな面倒なことするより、ショートカットキー割り当てた方がいい気がするけど
それどうやってやるんだよハゲってひとは、run.vbsとdo.batをtotp.pyと同じディレクトリに入れてrun.vbsのプロパティを開いてショートカットキー割り当てておしまい。

[文句]<br>
・pythonインストールするの面倒
→あきらめましょう

・実行可能ファイルを見せろ
→python布教したいのでいやだ

・よくわからんから代わりに全部やれ
→ハーゲンダッツと引き換え

