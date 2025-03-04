/*
 * CLIENT SIDE CODE (TO BE CONNECTED WITH PYGAME BASED GUI)
 * Main Program functioning of maixduino with farmsight rover
 * Video transmition with udp
 * Author: Pavan Kalsariya
 * MADE WIH MULTIPLE ITTRATIONS OF TRIALS AND ERRORS... AS NO RESOURCES AND REFERENCES AVAILABLE AT THE TIME OF DEVLOPMENT
 */


#network_wiznet5k()

SSID = "0000"
PASW = "12121212"

def enable_esp32():
    from network_esp32 import wifi
    if wifi.isconnected() == False:
        for i in range(5):
            try:
                # Running within 3 seconds of power-up can cause an SD load error
                # wifi.reset(is_hard=False)
                wifi.reset(is_hard=True)
                print('try AT connect wifi...')
                wifi.connect(SSID, PASW)
                if wifi.isconnected():
                    break
            except Exception as e:
                print(e)
    print('network state:', wifi.isconnected(), wifi.ifconfig())

enable_esp32()

def enable_espat():
    from network_espat import wifi
    if wifi.isconnected() == False:
        for i in range(5):
            try:
                # Running within 3 seconds of power-up can cause an SD load error
                # wifi.reset(is_hard=False)
                wifi.reset()
                print('try AT connect wifi...')
                wifi.connect(SSID, PASW)
                if wifi.isconnected():
                    break
            except Exception as e:
                print(e)
    print('network state:', wifi.isconnected(), wifi.ifconfig())

#enable_espat()

def network_wiznet5k():
    from network_wiznet5k import lan
    from machine import SPI
    from Maix import GPIO
    if lan.isconnected() == False:
        WIZNET5K_SPI_SCK = 21
        WIZNET5K_SPI_MOSI = 8
        WIZNET5K_SPI_MISO = 15
        WIZNET5K_SPI_CS = 20
        spi1 = SPI(4, mode=SPI.MODE_MASTER, baudrate=600 * 1000,
                    polarity=0, phase=0, bits=8, firstbit=SPI.MSB, sck=WIZNET5K_SPI_SCK, mosi=WIZNET5K_SPI_MOSI, miso=WIZNET5K_SPI_MISO)
        for i in range(5):
            try:
                lan.reset(spi1, WIZNET5K_SPI_CS)
                print('try connect lan...')
                if lan.isconnected():
                    break
            except Exception as e:
                print(e)
    print('network state:', lan.isconnected(), lan.ifconfig())

# network_wiznet5k()

########## server config ################
# Send image(jpeg) to server and display on server(PC),
# server code refer to ../demo_recv_pic_server.py
WIFI_SSID   = "0000"
WIFI_PASSWD = "12121212"
addr        = ("192.168.16.192", 3456)
##################################

import socket, time, sensor, image
import lcd

clock = time.clock()
lcd.init()
sensor.reset()
sensor.set_pixformat(sensor.RGB565)
sensor.set_framesize(sensor.QVGA)
sensor.skip_frames(time = 2000)

while True:
    # send pic
    while True:
        try:
            sock = socket.socket()
            print(sock)
            sock.connect(addr)
            break
        except Exception as e:
            print("connect error:", e)
            sock.close()
            continue
    sock.settimeout(5)

    send_len, count, err = 0, 0, 0
    while True:
        clock.tick()
        if err >=10:
            print("socket broken")
            break
        img = sensor.snapshot()
        img = img.compress(quality=60)
        img_bytes = img.to_bytes()
        print("send len: ", len(img_bytes))
        try:
            block = int(len(img_bytes)/2048)
            #for i in range(block):
                #send_len = sock.send(img_bytes[i*2048:(i+1)*2048])
                #time.sleep_ms(10)
            send_len = sock.send(img_bytes[block*2048:])
            #send_len = sock.send(img_bytes[0:2048])
            #send_len = sock.send(img_bytes[2048:])
            #time.sleep_ms(500)
            if send_len == 0:
                raise Exception("send fail")
        except OSError as e:
            if e.args[0] == 128:
                print("connection closed")
                break
        except Exception as e:
            print("send fail:", e)
            time.sleep(1)
            err += 1
            continue
        count += 1
        print("send:", count)
        print("fps:", clock.fps())
        #time.sleep_ms(500)
    print("close now")
    sock.close()

)
    >>>
'''
