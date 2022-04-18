from machine import Pin # クラスPin -- I/Oピンの制御
import utime    # 時間関連のモジュール

# ピン #25 を出力ピンとして作成, Picoの25にはLEDが最初から実装されている。
led = Pin(25, Pin.OUT)  

while True: # 無限ループ
    led.toggle()    # onとoffを切り替える
    utime.sleep(0.1)    # 0.1秒停止