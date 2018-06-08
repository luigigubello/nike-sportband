import sys
import usb.core
import usb.util
import re
import os
import time
import datetime

VENDOR_ID = 0x11ac
PRODUCT_ID = 0x4269

device = usb.core.find(idVendor=VENDOR_ID, idProduct=PRODUCT_ID)

def set_weight():
	weight = raw_input("Type your weight in kg: ")
	while float(weight) < 1 or float(weight) > 300:
		weight = raw_input("Type your weight in kg (min:1 - max:300): ")
	pounds = (float(weight)*(2.20462))
	pounds_list = [0, 0]
	pounds_list[0] = (int(pounds*10))/256
	pounds_list[1] = int(pounds*10) - pounds_list[0]*256
	pounds_list = [9, 4, 234, 51] + pounds_list + [0, 0]
	device.ctrl_transfer(33, 9, 521, 0, pounds_list)

def read_weight():
	bytes_num = [9, 2, 81, 51]
	for i in range(59):
		bytes_num.append(0)
	device.ctrl_transfer(33, 9, 521, 0, bytes_num) 
	read = device.ctrl_transfer(161, 1, 257, 0, 8)
	weight = (((read[4] + 256*read[3])/10)*0.453592)
	
	print("Weight: %s kg" % (int(weight)+1))

def dump_run():
	# create a dump.txt
	file_name = str(datetime.datetime.now().isoformat())
	dump_file = open(file_name + '.txt', 'w')
	bytes_num = [9, 5, 12, 16]
	for i in range(59):
		bytes_num.append(0)
	device.ctrl_transfer(33, 9, 521, 0, bytes_num) 
	arg = 1
	while (arg == 1):
		read = device.ctrl_transfer(161, 1, 260, 0, 64)
		y = 1
		check = 1
		while y < 63:
			if read[y] == 0:
				check += 1
			y += 1
		if check == 63:
			arg = 0
			continue
		read = read[7:]
		sret = ''.join([chr(x) for x in read])
		dump_file = open(file_name + '.txt', 'a')
		dump_file.write(sret)
		dump_file.close()
	print("Created hex dump:" + file_name + ".txt")

def free_space():
	bytes_num = [9, 4, 69, 17, 238, 134, 0, 0]
	for i in range(59):
		bytes_num.append(0)
	device.ctrl_transfer(33, 9, 521, 0, bytes_num) 
	bytes_num = [9, 2, 59, 17, 0, 0, 0, 0]
	for i in range(59):
		bytes_num.append(0)
	device.ctrl_transfer(33, 9, 521, 0, bytes_num)
 
def main():
	print("[1] View weight.")
	print("[2] Set weight.")
	print("[3] Dump your runs.")
	choice = raw_input("Your choise: ")
	choice = int(choice)
	if choice == 1:
		read_weight()			
	elif choice == 2:
		set_weight()
	elif choice == 3:
		dump_run()
		question = raw_input("Do you want to free space? [y/N]")
		while ((question in ['y','Y','n','N']) == False):
			question = raw_input("Do you want to free space? [y/N]")
		if question == 'y' or question == 'Y':
			free_space()
		else:
			main()
	else:
		print("Choose a number from 1 to 3.\n")
		main()

print("\nNike+ Run - alpha\n")

if device is None:
	sys.exit("Device not found.")
else:
	print("Nike+ SportBand: %s:%s") % (hex(VENDOR_ID), hex(PRODUCT_ID))

if device.is_kernel_driver_active(0):
	try:
		device.detach_kernel_driver(0)
        #	print("Kernel driver detatched.")
	except usb.core.USBError as e:
		sys.exit("Could not detatch kernel driver: %s" % str(e))

# Set 12h/24h
set_h24 = [9, 3, 151, 49, 1, 0, 0, 0]
device.ctrl_transfer(33, 9, 521, 0, set_h24)

# Set km/miles
set_km = [9, 3, 212, 50, 1, 0, 0, 0]
device.ctrl_transfer(33, 9, 521, 0, set_km)

# Set time from OS (automatic)
ss = int(time.mktime(datetime.datetime.now().timetuple()))
hhmm = [ss-((ss/256)*256), (ss/256)-(((ss/256)/256)*256), ((ss/256)/256)-((((ss/256)/256)/256)*256), (((ss/256)/256)/256)-(((((ss/256)/256)/256)/256)*256)]
bytes_num = [10, 11, 48, 33, hhmm[3], hhmm[2], hhmm[1], hhmm[0], 0, 1, 67, 112, 1, 0, 0, 0]	
device.ctrl_transfer(33, 9, 522, 0, bytes_num)


try:
	main()
except KeyboardInterrupt:
	print "\n\nGoodbye\n"
	exit(0)
