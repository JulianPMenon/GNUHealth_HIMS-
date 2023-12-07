.. _demo_test-livecd:the_live-cd:

The Live-CD
===========
The GNU Health Demo Database is available as Live-CD. This gives interested users the option to run GNU Health on their own PC, and, if desired, install the GNU Health demo database directly from the CD.

Similar as the demo database, the live-CD is an ongoing project and it will be adapting to the each new GNU Health version. The clinical history will also grow with time.

There is a `video tutorial <https://www.youtube.com/watch?v=QtYV0Y9tyQ8>`_ available demonstrating the installation of the GNU Health 3.0 Live CD in a Virtual Box.

.. _demo_test-livecd:the_live-cd-download_the_live-cd:

Download the Live-CD
--------------------
The Live-CD was built on `SUSEStudio <https://susestudio.com/>`_, and is currently available with the following flavours:

* GNU Health 3.0: `openSUSE Leap 42.1 / KDE5 / 64bit <https://susestudio.com/a/7hReQg/gnu-health-3-0-kde5-64bit>`_
* GNU Health 3.0: `openSUSE 13.1 / KDE4 / 32bit <https://susestudio.com/a/7hReQg/gnu-health-3-0-kde-4-32bit>`_
* GNU Health 3.0: `SLES 12SP1 / Text-based Server version / 64bit <https://susestudio.com/a/7hReQg/gnu-health-3-0-sles-12-sp1>`_ 
* GNU Health 2.8: `openSUSE Leap 42.1 / KDE / 64bit / UEFI <https://susestudio.com/a/7hReQg/gnu-health-2-8-kde-64bit-uefi>`_
* GNU Health 2.6: Archived, available on request
* GNU Health 2.4: Archived, available on request

Please note: The user name and password necessary to access the GNU Health server on the Live-CD can be found on that download page as well.

Unlike the full version of openSUSE, the Live-CD contains only packages that are required to run GNU Health. Feel free to add required programs later on from the openSUSE repositories.

It is recommended to use the Server version SLES 12 on a virtual machine, as it comes with no client! See :ref:`Documentation <demo_test-livecd:virtual_machine_images>`

.. _demo_test-livecd:the_live-cd-install_the_live-cd:

Install the Live-CD
-------------------
In order to use the Live-CD, you have to install it on a CD or a USB stick. 

.. _demo_test-livecd:the_live-cd-install_the_live-cd-usb-stick_/_hard_disk_image:

USB-Stick / Hard Disk Image
^^^^^^^^^^^^^^^^^^^^^^^^^^^
The hard disk image comes as packed raw format. After download, first unpack the \*.tar.gz file

* On Linux/Mac-OS, use your favorite archiving program, or use :code:`tar -xvzf *tar.gz` from the command line
* On Windows, use an advanced packer like 7-Zip

After unpacking, you have to install the RAW-file to a stick. `Create a Live USB stick using Windows <http://en.opensuse.org/Live_USB_stick>`_. `See instructions <https://en.opensuse.org/SDB:Create_a_Live_USB_stick_using_Windows>`_

Note: When booting the first time from the USB-Stick, the boot process takes a bit longer, as the stick is being optimized (data and swap space creation). Second boot will be much quicker.

.. _demo_test-livecd:the_live-cd-install_the_live-cd-iso-image_/_cd:

ISO-Image / CD
^^^^^^^^^^^^^^
If you have downloaded the ISO image to burn a CD, you can find the relevant instructions `here <http://en.opensuse.org/SDB:Download_help#.Burn_the_ISO_image.28s.29>`_.

.. _demo_test-livecd:the_live-cd-install_the_live-cd_to_your_hard_drive:

Install the Live-CD to your hard drive
--------------------------------------
The Live-CD offers the option to install the system and the GNU Health Demo-DB to your hard drive. The relevant program can be found in the *My Computer* section of the start menu (the little green button on the lower left corner of the screen).

.. _demo_test-livecd:virtual_machine_images:

Virtual Machine Images
======================

The live-CD is available in various container formats that allow easy integration into a virtual environment. Currently the following formats are published:

* Xen Guest (.img)
* OVF Virtual Machine / ESXI (.ovf)
* VMware Workstation / VirtualBox (.vmdk)
* SUSE Cloud / OpenStack / KVM (.qcow2)
* Hyper-V Virtual Hard Disk (.vhd)
* Amazon EC2 Cloud (.ami)

We have recorded a `Screencast <https://www.youtube.com/watch?v=QtYV0Y9tyQ8>`_ that shows the setup of a Virtual machine.

.. _demo_test-livecd:virtual_machine_images-running_the_virtual_machine_as_server:

Running the Virtual Machine as Server
-------------------------------------
Several times the question came up 'How can I access my Live-CD from another desktop'? This should not be too difficult if you consider some points. The following example bases on Virtualbox, but should be similar on other virtual environments:

* When setting up the network, make sure you select 'Bridged Network'. In this case the virtual box will receive the IP-Address from your DHCP-Server, not from the host-machine
* Make sure the network-name of your virtual box is updated to your DDNS-Server. Even better, you may assign a fix network address to your virtual box, say 192.168.2.100
* Try to ping the box from an external client on the network: open a console and type: ping 192.168.2.100
* If this works, and your GNUHealth server is running, check if you can access the server from outside: telnet 192.168.2.100 8000

If this works, everything is good.<br />If not, its time to check the firewall settings of your box. From the Start Menu, select *System → Administration → YaST*. Enter the password for 'root': tryton , and go to 'firewall Settings'. Check the external zone (right interface name?) or even add an exception for the 192.168.2.100/24 network

.. _demo_test-livecd:virtual_machine_images-adjustments:

Adjustments
-----------

* You may want to change the language and keyboard to your preferred setting. From the Start Menu, select *System → Administration → YaST*. Enter the password for 'root': tryton . You have reached the administration settings. From the 'System' Section select 'Language' to change the primary language.
* You may want to run an online update. From the Start Menu, select *System → Administration → YaST*. Enter the password for 'root': tryton . You have reached the administration settings. From the 'Software' Section select 'Online-Update'.
* You may want to increase the display resolution of your virtual machine (which may be as low as 640 x 480 pixel). From the Start Menu, select *System → Administration → YaST*. If the system asks you to log in, enter *root* as user and *tryton* as password. From the YaST main screen select *Software* in the left column, then *Software Management* in the right column. Then search for *virtualbox*, select all packages with the word *guest* in their name and install them. After rebooting your virtual machine you should have higher resolutions available.
* You may want to install additional software. From the Start Menu, select *System → Administration → YaST*. Enter the password for 'root': tryton . You have reached the administration settings. From the 'Software' Section select 'Software Management'.
