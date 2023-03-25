# Project Structure

This project consists of two main files, namely 'sub.py' and 'pub.py', and a utility file 'utils/smart_light_bulb.py'.

- sub.py: It contains a client that represents a smart light bulb. The client subscribe two topics to receive messages that control state and brightness of the bulb.
- pub.py: It contains a client that represents a controller(switch) to control the bulb's state and brightness. User should input its state and brightness that the user wants to switch its state/brightness to.
- utils/smart_light_bulb.py: It contains a class for a simulated device that represents the smart light bulb.

# MQTT Topics

The two MQTT topics used in this project are 'smart-light-bulb/state' and 'smart-light-bulb/brightness'. The bulb subscribes to these topics to receive messages that control its state and brightness. The controller, on the other hand, publishes messages to these topics to control the state and brightness of the bulb.

# Set up

Before running the code, ensure that the paho-mqtt library is installed. To install, run the following command in your terminal:

```
pip install paho-mqtt
```

# How to run

To run the smart light bulb simulation, follow the steps below:

1. Open two terminal windows.
2. In the first terminal window, navigate to the project directory and run the following command:

   ```
   python sub.py
   ```

   This will display whether the bulb has successfully connected to the MQTT broker, as well as the initial state and brightness level of the bulb. Whenever the state or brightness of the bulb changes, the current state will be printed to the console.

3. In the second terminal window, navigate to the project directory and run the following command:
   ```
   python pub.py
   ```
   This will display a prompt that allows you to input the desired state and brightness level of the bulb. If the input is "on," the client will also ask for the desired brightness level. If the input is "off," the brightness level will be set to zero. The client will not publish any messages for invalid inputs and will ask for another input.
