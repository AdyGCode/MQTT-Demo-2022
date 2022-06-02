# MQTT and MongoDB Demo (Adafruit)

This project demonstrates a simple MQTT Pub-Sub system that stores data in an
external
MongoDB database. The MQTT broker used is adafruit.io's free service.

The data published is 'faked' using randomised 'temperatures' from two '
locations', inside
and outside an address.

## Update Pip, SetupTools & Wheel

Upgrade Pip and SetUpTools using:

```shell
python -m pip install --upgrade pip setuptools wheel
```

## Requirements

Requirements are given in the [requirements.txt](requirements.txt) file.

Install the required packages using:

```shell
pip install -r requirements.txt
```

## Services Used

This sample uses a number of services, including MQTT. Details follow.

### MQTT Brokers

This example project uses a local MQTT broker.

#### MQTT at TAFE

At TAFE in Room 3-06 we have an MQTT broker running on `l306-01` (lower case L,
306 - 01).

At time of writing this did not require username/password to use.

#### MQTT at Home

Details for installing and running at home are to be added.

- TODO: Running Own MQTT Broker

#### MQTT via Free Service

The following brokers provide free services for testing / low data volume:

- test.mosquitto.org
- broker.hivemq.com
- iot.eclipse.org

You should be able to replace L306-01 with one of the above 'addresses'.

## References and Readings

The following articles were used to assist in the creation of this example code:

- [MQTT Beginners Guide - Medium - Code & Dogs](https://medium.com/python-point/mqtt-basics-with-python-examples-7c758e605d4)
- [How to use MQTT in Python (Paho) - EMQX](https://www.emqx.com/en/blog/how-to-use-mqtt-in-python?msclkid=fcb9d9bbcffb11ec9c672d70a8558bcd)
- [How to Use The Paho MQTT Python Client for Beginners - Steve's Internet Guide](http://www.steves-internet-guide.com/into-mqtt-python-client/)
- [Python Database Programming with MongoDB](https://voiptuts.com/python-database-programming-with-mongodb)
- [Python Database Programming with MongoDB for Beginners - Developer.com - Phil Hajjar](https://www.developer.com/languages/python-mongodb/)
- [Python and MongoDB Database Development - Developer.com - Phil Hajjar](https://www.developer.com/database/python-mongodb-no-sql/)
- [How to Use Python with MongoDB](https://www.mongodb.com/languages/python)

## Plans

- add testing
- add flask based front end
- organise into sections using folders
