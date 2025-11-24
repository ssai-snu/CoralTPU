Mount Drives on Linux

$ sudo mount <device> <dir>

$ sudo -l
$ lsblk -f

$ mkdir ~/usb
$ sudo mount /dev/sda1 ~/usb
$ lsblk -f

Unmounting drives on Linux using umount

$ sudo umount /dev/sdc1