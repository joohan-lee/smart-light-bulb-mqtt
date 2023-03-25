import paho.mqtt.client as mqtt
import time

'''
Publish messages here.
Messages are printed every time the loop runs, indicating whether the bulb is on or off and its current brightness level. 
Additionally, the code will publish the bulb's state and brightness level to the smart-light-bulb/state and smart-light-bulb/brightness topics on the MQTT broker.
'''


def on_connect(client, userdata, flags, rc):
    if rc == 0:
        # Successfully connected
        print("completely connected")
    else:
        print("Bad connection Returned code=", rc)


def on_disconnect(client, userdata, flags, rc=0):
    print(str(rc))


def on_publish(client, userdata, mid):
    print("In on_pub callback mid= ", mid)


if __name__ == "__main__":
    # Create client
    client = mqtt.Client()

    # Set up callback functions.
    # on_connect(connect to the broker), on_disconnect(disconnect from broker), on_subscribe(subscribe a topic),
    # on_message(When receiving messeages published)
    client.on_connect = on_connect
    client.on_disconnect = on_disconnect
    client.on_publish = on_publish

    # Connect to remote mqtt broker
    # address : broker.hivemq.com
    # port: 1883
    client.connect('broker.hivemq.com', 1883)

    # Loop forever to publish bulb state and brightness level
    while True:
        # Update bulb state and brightness level based on user input every 5 seconds
        user_input_state = input('Input bulb_state(on/off) : ')
        if user_input_state == 'on':
            user_input_brightness = int(
                input('Input brightness level(0~100) : '))
        elif user_input_state == 'off':
            user_input_brightness = 0
        else:
            print(f'Invalid input. Bulb state should be on or off.')
            continue

        # Publish current state and brightness level to MQTT broker
        client.publish('smart-light-bulb/state', user_input_state, 1)
        client.publish('smart-light-bulb/brightness', user_input_brightness, 1)
