.. _demo_test-testgnuhealth:different_ways_to_test_gnu_health:

Different ways to test GNU Health
=================================
.. _demo_test-testgnuhealth:different_ways_to_test_gnu_health-about_this_page:

About this page
---------------
Are you a doctor, a nurse, a hospital administrator or a representative of a health department? Do you want to try out GNU Health by yourself? Then you have several options described on this page. Each option has its advantages and disadvantages. Some of them are simpler than others, but you don't have to be a programmer or system administrator to use them.

Please note that the only purpose of this page is to give you an overview and to allow you to choose the option that fits your needs best. For detailed instructions please follow the indicated links.

.. _demo_test-testgnuhealth:different_ways_to_test_gnu_health-option_1:_connect_to_the_demo_database:

Option 1: Connect to the Demo Database
--------------------------------------

.. _demo_test-testgnuhealth:different_ways_to_test_gnu_health-option_1:_connect_to_the_demo_database-what_to_do:

What to do
^^^^^^^^^^

* Download and install the free Tryton client software on your computer.
* Start the Tryton client software and connect to the GNU Health Demo Database over the Internet.

:ref:`Please refer to this chapter <demo_test-demodb:the_demo_database>` for more information.

.. _demo_test-testgnuhealth:different_ways_to_test_gnu_health-option_1:_connect_to_the_demo_database-advantages:

Advantages
^^^^^^^^^^

* This option is the quickest and simplest way for your first hands-on experience with GNU Health.
* The Tryton client is available for Windows, Mac OS and GNU/Linux.

.. _demo_test-testgnuhealth:different_ways_to_test_gnu_health-option_1:_connect_to_the_demo_database-disadvantages:

Disadvantages
^^^^^^^^^^^^^

* You have to be connected to the Internet.
* The Demo Database will be reset periodically, which is not ideal for a long-term test.
* You are sharing the Demo Database with other users, so they might interfere with your data.

.. _demo_test-testgnuhealth:different_ways_to_test_gnu_health-option_2:_run_gnu_health_from_cd/dvd_or_usb_stick:

Option 2: Run GNU Health from CD/DVD or USB Stick
-------------------------------------------------

.. _demo_test-testgnuhealth:different_ways_to_test_gnu_health-option_2:_run_gnu_health_from_cd/dvd_or_usb_stick-what_to_do:

What to do
^^^^^^^^^^

* Download the Live CD image and burn it to a CD/DVD or write it to an USB stick.
* Boot your computer from this CD/DVD or USB stick. This will turn your Windows computer temporarily into a GNU/Linux computer (e.g., an openSUSE operation system with KDE desktop environment) with a preinstalled GNU Health server including the Demo Database. 

:ref:`Please refer to this chapter <demo_test-livecd:the_live-cd>` for more information.

.. _demo_test-testgnuhealth:different_ways_to_test_gnu_health-option_2:_run_gnu_health_from_cd/dvd_or_usb_stick-advantages:

Advantages
^^^^^^^^^^

* After the download you will not need an Internet connection anymore.
* This option gives you full access to the GNU Health server.
* You can install the system from the running Live-CD to your computer
* It is possible to setup your own database(s) besides the demo database (USB only)

.. _demo_test-testgnuhealth:different_ways_to_test_gnu_health-option_2:_run_gnu_health_from_cd/dvd_or_usb_stick-disadvantages:

Disadvantages
^^^^^^^^^^^^^

* Booting and running a computer from a CD/DVD is slow. (It's quicker from the USB stick but still slow.)
* CD's cannot store much data(up to 650 MB/4.7-9.4 GB for DVD). This means that even if you do use a rewritable CD, you will be space-limited on what you can save.
* You need to know how to write a CD image to a CD or USB stick and how to change the boot sequence in the BIOS settings of your computer.
* Some computers do not allow for booting from CD or USB.
* While using the Live CD you don't have access to the programs on your computer, so you can't test GNU Health and work with your Windows applications in parallel.
* This method may not work on Apple-brand PCs.

.. _demo_test-testgnuhealth:different_ways_to_test_gnu_health-option_3:_run_gnu_health_in_a_virtual_machine:

Option 3: Run GNU Health in a Virtual Machine
---------------------------------------------

.. _demo_test-testgnuhealth:different_ways_to_test_gnu_health-option_3:_run_gnu_health_in_a_virtual_machine-what_to_do:

What to do
^^^^^^^^^^

* Download the virtual machine image to your harddisk and unpack it. (The virtual machine image can be found on the same webpage like the Live CD image – see option 2.)
* Download and install the VirtualBox software (or any other emulator) on your computer.
* Run VirtualBox, locate the virtual machine image and start your virtual machine.

:ref:`Please refer to this chapter <demo_test-livecd:virtual_machine_images>` for more information.

.. _demo_test-testgnuhealth:different_ways_to_test_gnu_health-option_3:_run_gnu_health_in_a_virtual_machine-advantages:

Advantages
^^^^^^^^^^

* This option gives you all advantages of the Live CD (option 2) without its disadvantages.
* The VM can serve as a base for a later production use.

.. _demo_test-testgnuhealth:different_ways_to_test_gnu_health-option_3:_run_gnu_health_in_a_virtual_machine-disadvantages:

Disadvantages
^^^^^^^^^^^^^

* The virtual machine is stored on your harddrive. Therefore it needs a bit more effort to pass the test installation to someone else compared to the Live CD.
* The performance will be slower as the virtual machine is also sharing the power of your machine.
