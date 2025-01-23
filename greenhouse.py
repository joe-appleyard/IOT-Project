import time
import thingspeak
import seeed_dht
from grove.grove_moisture_sensor import GroveMoistureSensor


channel_id = 2817296
w_key = 'PJZMK3NCK8RYT2Z0'
r_key = 'ZYXA3OPNPKC0X3EF'

def main(channel):
    from grove.helper import helper
    sensorTH = seeed_dht.DHT("11", 5)
    sensorSM = GroveMoistureSensor(2)

    while True:
        humi, temp = sensorTH.read()
        mois = sensorSM.moisture
        print('DHT{0}, humidity {1:.1f}%, temperature {2:.1f}*'.format(sensorTH.dht_type, humi, temp))
        print('moisture: {}'.format(mois))

        response = channel.update({'field1': temp, 'field2': humi, 'field3': mois})  

        time.sleep(15)


if __name__ == '__main__':
    channel = thingspeak.Channel(id=channel_id, api_key=w_key)
    while True:
        main(channel)
        time.sleep(15)
