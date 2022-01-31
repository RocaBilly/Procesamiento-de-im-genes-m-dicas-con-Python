import machine
import utime

led = machine.Pin(15,machine.Pin.OUT)
herradura = machine.Pin(14,machine.Pin.IN)

while True:
	if herradura.value() == 1:
		print("Esta algo en la herradura")
		led.value(1)
		utime.sleep(2)
	else:
		print("No hay nada en la herradura")
		led.value(0)
		utime.sleep(2)
	

    