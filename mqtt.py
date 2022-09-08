import paho.mqtt.client as paho_mqtt
import json


# The callback for when the client receives a CONNACK response from the server.
def on_connect(client, userdata, flags, rc):
    #self.append_to_log("Connected with result code " + str(rc))
    print("Connected with result code " + str(rc))
    ui.append_to_log('Connected with result code ' + str(rc))

    # Subscribing in on_connect() means that if we lose the connection and
    # reconnect then subscriptions will be renewed.
    client.subscribe("tasmota/discovery/#")


# The callback for when a PUBLISH message is received from the server.
def on_message(client, userdata, msg):
    msg.payload = str(msg.payload.decode("utf-8"))
    print("topic:'" + msg.topic + "' msg:" + msg.payload)
    if 'tasmota/discovery' in msg.topic:
        x = json.loads(msg.payload)
        try:
            ui.cmb_devices.addItem(x['hn']+'/'+x['dn']+'/'+x['ip'])             # add to cmb box
            ui.tasmota_devices[x['hn']] = x['t']        # hn = hostname, t = topic
            ui.append_to_log("Found '" + x['hn'] + "' with topic:'" + x['t'] + "'")
            ui.cmb_devices.setCurrentIndex(0)
        except Exception as e:
            return
        #print(ui.tasmota_devices)
        return
    ui.append_to_log("RX:topic:'" + msg.topic + "' msg:" + msg.payload)
    try:
        payload = json.loads(msg.payload)
        ui.draw_data_table(payload)
    except Exception as e:
        pass

def connect_mqtt():
    init_mqtt(ui)
    try:
        if ui.txt_user.text() != '' and ui.txt_pass.text() != '':
            client.username_pw_set(username=ui.txt_user.text(), password=ui.txt_pass.text())
        client.connect(ui.txt_ip.text(), int(ui.mqtt_port.text()), 60)
        ui.btn_connect_mqtt.setDisabled(True)
        ui.btn_link_device.setDisabled(False)
        ui.cmb_devices.setDisabled(False)
        client.loop_start()
    except Exception as e:
        ui.append_to_log(str(e) + " for "+ui.txt_ip.text()+":"+ui.mqtt_port.text())


def disconnect_mqtt():
    ui.device_connected = False
    ui.btn_link_device.setText('Connect to ...')
    ui.current_cmd_topic = ""
    ui.current_state_topic = ""
    client.disconnect()
    ui.btn_connect_mqtt.setDisabled(False)
    ui.btn_link_device.setDisabled(True)
    ui.response_dict.clear()
    ui.tasmota_devices = {}
    ui.cmb_devices.clear()
    ui.append_to_log("Diconnected ...")


def init_mqtt(ui_class):
    global ui
    global client
    ui = ui_class
    client = paho_mqtt.Client(clean_session=True)
    client.on_connect = on_connect
    client.on_message = on_message

