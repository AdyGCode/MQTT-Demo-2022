import json
import os
import sys
import time
from os.path import join, dirname
from random import randrange, uniform

from dotenv import load_dotenv
from paho.mqtt import client as mqtt_client

dotenv_path = join(dirname(__file__), '../.env')
load_dotenv(dotenv_path)

MQTT_BROKER = os.environ.get('MQTT_BROKER', "l306-01")
MQTT_TOPIC = os.environ.get('MQTT_TOPIC', "nmt-test")
MQTT_USERNAME = os.environ.get('MQTT_USERNAME', "")
MQTT_PASSWORD = os.environ.get('MQTT_PASSWORD', "")
MQTT_KEY = os.environ.get('MQTT_KEY')
MQTT_PORT = os.environ.get('MQTT_PORT', "1883")
MQTT_CLIENT = os.environ.get('PUB_MQTT_CLIENT_01',
                             f"anonymous-{randrange(1000, 9999)}")

DELAY_TIME = 5
MAX_CONNECTION_ATTEMPTS = 2

connection_codes = {
    0: "Connection Accepted",
    1: "Connection Refused, unacceptable protocol version",
    2: "Connection Refused, identifier rejected",
    3: "Connection Refused, Server unavailable",
    4: "Connection Refused, bad user name or password",
    5: "Connection Refused, not authorized",
}

attempt = 0
connected = False


def connect_mqtt():
    """
    Connect to the MQTT server using the settings from the .env or operating
    system environment

    :return: mqtt client
    """

    def on_connect(client, userdata, flags, rc):
        """
        Listen for a connection event

        :param client:
        :param userdata:
        :param flags:
        :param rc:
        :return:
        """

        check_connection()

        if rc == 0:
            connected = True
            print(f"Connected to {MQTT_BROKER}!")
        else:
            print(f"Attempt {attempt} failed to connect, return code {rc} "
                  f"{connection_codes[rc]}\n")

    # Set Connecting Client ID
    client = mqtt_client.Client(MQTT_CLIENT)
    client.username_pw_set(MQTT_USERNAME, MQTT_PASSWORD)
    client.on_connect = on_connect
    client.connect(MQTT_BROKER, int(MQTT_PORT))
    return client


def check_connection():
    global attempt
    global connected
    attempt += 1

    if attempt >= MAX_CONNECTION_ATTEMPTS:
        print(f"Unable to connect to MQTT broker {MQTT_BROKER}, please "
              f"check the settings and authentication requirements")

    if not connected and attempt >= MAX_CONNECTION_ATTEMPTS:
        exit(0)


def publish(client):
    topic = MQTT_TOPIC
    msg_count = 0

    while True:
        check_connection()
        date_time = time.time()
        time.sleep(DELAY_TIME)
        randNumber = round(uniform(20.0, 21.0), 2)
        # Fake sensor data for testing
        data = {
            'location': 306,
            'device': MQTT_CLIENT,
            'address': {
                'building': '1',
                'street': '30 Aberdeen St',
                'suburb': 'PERTH'
            },
            'data': {
                'date_time': date_time,
                'temp': randNumber
            },
            'message_num': msg_count
        }

        msg = json.dumps(data)

        result = client.publish(topic, msg)
        # result: [0, 1]
        status = result[0]
        if status == 0:
            print(f"Send `{msg}` to topic `{topic}`")
        else:
            print(f"Failed to send message to topic {topic}")
        msg_count += 1


def handle_disconnect(client):
    # Disconnected function will be called when the client disconnects.
    print(f'Disconnected from {MQTT_BROKER}')
    sys.exit(1)


def handle_subscribe(client, userdata, mid, granted_qos):
    # This method is called when the client subscribes to a new feed.
    print(f"Subscribed to {MQTT_TOPIC} with QoS {granted_qos[0]}")


def handle_message(client, userdata, message):
    """
    Callback function used to work with messages received from the
    MQTT broker.

    :param client:
    :param userdata:
    :param message:
    :return:
    """
    print(f"Message: {message} from {client}")


# Create an MQTT client instance (
client = connect_mqtt()

client.on_disconnect = handle_disconnect
client.on_subscribe = handle_subscribe
client.on_message = handle_message


def show_settings():
    print(
        f"MQTT_BROKER: {MQTT_BROKER} \n"
        f"MQTT_TOPIC: {MQTT_TOPIC} \n"
        f"MQTT_USERNAME: {MQTT_USERNAME}\n"
        f"MQTT_PASSWORD: {MQTT_PASSWORD} \n"
        f"MQTT_KEY: {MQTT_KEY} \n"
        f"MQTT_PORT: {MQTT_PORT} \n"
        f"MQTT_CLIENT: {MQTT_CLIENT} \n")


def run():
    show_settings()
    client = connect_mqtt()
    client.loop_start()

    print(
        f"Publishing a new message every {DELAY_TIME} seconds (press "
        f"Ctrl-C to quit)...")

    publish(client)


if __name__ == '__main__':
    run()
