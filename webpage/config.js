var ip='192.168.200.88'
var web_socket_port='8080'

var sensorNamespace='quad0'         // the namespace to apply to the connection
var imageTopic='/usb_cam/image_raw' // if the topics aren't relative to the namespace /topic_name otherwise topic_name -> /ns/topic_name
var gpsTopic='fix'
var sensorList=['TEMP','alpha','gamma']

var warningMin=[10,10,10]
var dangerMin=[30,30,30]
