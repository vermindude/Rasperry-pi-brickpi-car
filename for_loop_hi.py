import time


print("starting.....")
try:
    for x in  range(20):
        # BP.get_sensor retrieves a sensor value.
        # BP.PORT_1 specifies that we are looking for the value of sensor port 1.
        # BP.get_sensor returns the sensor value.
        try:
            value = BP.get_sensor(BP.PORT_1)
            print("VAL CHANGED TO ", value)
        except brickpi3.SensorError as error:
            print("ERROR:", error)
            value = 0

        if value:  # if the touch sensor is pressed
            speed = 50
            BP.set_motor_power(BP.PORT_A, speed)

        try:
            # Each of the following BP.get_motor_encoder functions returns the encoder value (what we want to display).
            print("Encoder A: %6d  B: %6d  C: %6d  D: %6d" % (
                BP.get_motor_encoder(BP.PORT_A), BP.get_motor_encoder(BP.PORT_B), BP.get_motor_encoder(BP.PORT_C),
                BP.get_motor_encoder(BP.PORT_D)))
        except IOError as error:
            print(error)

except KeyboardInterrupt:
    print("IM DONE")