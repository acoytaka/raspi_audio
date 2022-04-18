from machine import Pin, PWM, Timer

C5 = 523.251
D5 = 587.330
E5 = 659.255
F5 = 698.456
G5 = 783.991
A5 = 880
B5 = 987.767
C6 = 1046.502
D6 = 1174.659
E6 = 1318.510
F6 = 1396.913
G6 = 1567.982
melody = 0
# key pin settings
speaker = PWM(Pin(26, Pin.OUT))

swx = Pin(16, Pin.OUT)
swy = Pin(17, Pin.OUT)
swz = Pin(18, Pin.OUT)
swa = Pin(19, Pin.IN, Pin.PULL_DOWN)
swb = Pin(20, Pin.IN, Pin.PULL_DOWN)
swc = Pin(21, Pin.IN, Pin.PULL_DOWN)
swd = Pin(22, Pin.IN, Pin.PULL_DOWN)

led_onboard = Pin(25, Pin.OUT)

while True:
    i = 0
    # x
    swx.value(0)
    swy.value(1)
    swz.value(1)
    
    if swa.value() == 0:
        melody = C5
        i =+ 1
    elif swb.value() == 0:
        melody = D5
        i =+ 1
    elif swc.value() == 0:
        melody = E5
        i =+ 1
    elif swd.value() == 0:
        melody = F5
        i =+ 1
    
    # y
    swx.value(1)
    swy.value(0)
    swz.value(1)
    
    if swa.value() == 0:
        melody = G5
        i =+ 1
    elif swb.value() == 0:
        melody = A5
        i =+ 1
    elif swc.value() == 0:
        melody = B5
        i =+ 1
    elif swd.value() == 0:
        melody = C6
        i =+ 1
    # z
    swx.value(1)
    swy.value(1)
    swz.value(0)
    
    if swa.value() == 0:
        melody = D6
        i =+ 1
    elif swb.value() == 0:
        melody = E6
        i =+ 1
    elif swc.value() == 0:
        melody = F6
        i =+ 1
    elif swd.value() == 0:
        melody = G6
        i =+ 1
    
    if i == 0:
        speaker.duty_u16(0) # PWMのDutyを0とすることで波形は出力されずLOWとなり、音は出ない
        led_onboard.value(0)
    else:
        speaker.freq(int(melody + 0.5)) # PWMの周波数を次のメロディー音の周波数に変更する。整数で渡す必要があるので、+0.5してから小数点以下切り捨て（thanks @naohiro2g）
        speaker.duty_u16(0x8000) # PWMのDutyを50％に戻し、音を出す。Dutyは0～0xFFFFつまり65535までの間の値で設定
        led_onboard.value(1)
        


