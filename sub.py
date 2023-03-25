import paho.mqtt.client as mqtt
from utils.smart_light_bulb import SmartLightBulb

'''
This client represents a smart light bulb.
It subscribes to two MQTT topics and displays its state and brightness by messages received. 
'''


def on_connect(client, userdata, flags, rc):
    '''
    The callback for when the client receives a CONNACK response from the server.
    '''
    if rc == 0:
        print("connected OK")
        print(f'Initial state: {bulb.bulb_state}')
        print(f'Initial brightness level: {bulb.brightness_level}')
    else:
        print("Bad connection Returned code=", rc)


def on_disconnect(client, userdata, flags, rc=0):
    print(str(rc))


def on_subscribe(client, userdata, mid, granted_qos):
    print("subscribed: " + str(mid) + " " + str(granted_qos))


def on_message(client, userdata, msg):
    '''
    The callback for when a PUBLISH message is received from the server.
    '''
    payload = msg.payload.decode("utf-8")
    if msg.topic == 'smart-light-bulb/state':
        if payload.lower() == 'on':
            bulb.turn_on()
        elif payload.lower() == 'off':
            bulb.turn_off()
        else:
            print(f'Invalid payload for smart-light-bulb/state topic')
    elif msg.topic == 'smart-light-bulb/brightness':
        try:
            brightness_level = int(payload)
            if brightness_level < 0 or brightness_level > 100:
                print("Brightness level must be between 0 and 100")
            else:
                bulb.set_brightness(brightness_level)
        except ValueError:
            print("Invalid payload for smart-light-bulb/brightness topic")


if __name__ == "__main__":
    # create a smart light bulb
    bulb = SmartLightBulb()

    # Create new client
    client = mqtt.Client()

    # Set up callback functions.
    # on_connect(connect to the broker), on_disconnect(disconnect from broker), on_subscribe(subscribe a topic),
    # on_message(When receiving messeages published)
    client.on_connect = on_connect
    client.on_disconnect = on_disconnect
    client.on_subscribe = on_subscribe
    client.on_message = on_message

    # Connect to remote mqtt broker
    # address : broker.hivemq.com
    # port: 1883
    client.connect('broker.hivemq.com', 1883)

    # Subscribe two topics, 'smart-light-bulb/state', 'smart-light-bulb/brightness'
    client.subscribe([('smart-light-bulb/state', 1),
                     ('smart-light-bulb/brightness', 1)])
    client.loop_forever()
