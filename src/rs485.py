#!/usr/bin/env python3

import minimalmodbus,time,sys
from periphery import GPIO

GPIO(162,"HIGH") #RS485 enable
GPIO(192,"HIGH") #LED Enable

client1 = minimalmodbus.Instrument('/dev/ttymxc3', 4, debug=False)  # port name, slave address (in decimal)
client1.serial.baudrate = 9600  # baudrate
client1.serial.bytesize = 8
client1.serial.parity   = minimalmodbus.serial.PARITY_NONE
client1.serial.stopbits = 1
client1.serial.timeout  = 0.5  # seconds
client1.address         = 4        # this is the slave address number
client1.mode = minimalmodbus.MODE_RTU # rtu or ascii mode
client1.clear_buffers_before_each_transaction = True
inc = 1
def main():
    global inc
    try:
        while(1):
            try:
                client1.write_register(1,inc)
                res = client1.read_registers(0,4)
                inc = inc + 2
                print(res)

            except minimalmodbus.ModbusException as e:
                print(e)
            time.sleep(1)
    except KeyboardInterrupt:
        print("exiting...\n")
        client1.serial.close()
        GPIO(162,"LOW")
        GPIO(192,"LOW")


if __name__ == '__main__':
    main()
