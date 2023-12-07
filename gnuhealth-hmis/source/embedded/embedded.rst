.. _embedded-embedded:gnu_health_embedded:

GNU Health Embedded
===================
The GNU Health Embedded sub-project ("GNU Health in a Box") focuses on the installation and use of GNU Health in single-board devices.

The use of GNU Health in single board devices such as the Raspberry Pi has many advantages (in addition to the low cost) such as the easy deployment, little maintenance and low energy consumption that makes it a candidate for some of the following scenarios :

* Remote areas without Internet,
* Academic Institutions,
* Domiciliary Units,
* Vector Control,
* Nursing,
* ICU,
* Laboratory stations, and
* Personal Health Records.

The device is a full server, that has its own database, allowing storing the information locally, without the need of a network. That said, keep in mind that it is a low-resource device, so its usage must be carefully planned, and it's not suitable for high-demand, heavy-load environments, where a regular server would be needed.

.. _embedded-embedded:gnu_health_embedded-raspberry_pi:

Raspberry Pi
------------
Currently we are working on the Raspberry Pi 3 platform.

.. _embedded-embedded:gnu_health_embedded-downloading_the_images:

Downloading the images
----------------------

You can find and download the latest images for different operating systems on the GNU Health embedded project link `GNU Health embedded project <https://www.gnuhealth.org/embedded.html>`_.

The current directory shows the images that use the standard / vanilla installation, which is compatible with the installation instructions you find in this Wikibook.

Other images can be found at the community pages. For instance, Axel Braun provides an openSUSE image that uses the packages from that GNU/Linux distribution.

.. _embedded-embedded:gnu_health_embedded-downloading_the_images-standard_installations:

Standard installations
^^^^^^^^^^^^^^^^^^^^^^

The standard images for the different operating systems have the following naming convention :

:code:`gnuhealth-<**version**>-<**platform**>-<**medium**>-<**operating_system-distro-version**>.img.gz`

For example :

* :code:`gnuhealth-3.6.2-rpi3-SD-opensuse-leap15.1-e20.img.gz` or the latest image
* :code:`gnuhealth-3.6.4-rpi4-SD-opensuse-leap15.2-xfce.img.gz` for the Raspberry Pi 4.

.. _embedded-embedded:gnu_health_embedded-downloading_the_images-getting_the_image:

Getting the Image
^^^^^^^^^^^^^^^^^
You can get the latest status and download packages on the GNU health main site, under the section "GNU Health Embedded". See
`GNU Health embedded project <https://www.gnuhealth.org/embedded.html>`_.

.. _embedded-embedded:gnu_health_embedded-downloading_the_images-getting_the_image-download_the_image_locally:

Download the image locally
""""""""""""""""""""""""""

You can either download directly the image from your browser, or using wget.

For example :

.. code-block:: shell
        :linenos:

     
        $ wget https://www.gnuhealth.org/downloads/embedded/raspberry/rpi4/gnuhealth-3.6.4-rpi4-SD-opensuse-leap15.2-xfce.img.gz

.. _embedded-embedded:gnu_health_embedded-downloading_the_images-getting_the_image-uncompress_the_image:

Uncompress the image
""""""""""""""""""""

.. code-block:: shell
        :linenos:

     
        $ gunzip gnuhealth-3.6.4-rpi4-SD-opensuse-leap15.2-xfce.img.gz

.. _embedded-embedded:gnu_health_embedded-downloading_the_images-getting_the_image-burn_the_image_to_the_sd_card:

Burn the image to the SD card
"""""""""""""""""""""""""""""

#. Insert your SD card in the computer but **DO NOT** mount it!

#. Determine the block device name that has been assigned to the SD card.

        The **lsblk** command is also useful as it outputs attached devices in a pleasant format:

        .. code-block:: shell
                :linenos:

        
                
                NAME                                 MAJ:MIN RM   SIZE RO TYPE  MOUNTPOINT
                sda                                    8:0    0 931,5G  0 disk  
                └─cr_ata-ST1000LM035-1RK172_WKP1RMG3 254:0    0 931,5G  0 crypt /home
                mmcblk0                              179:0    0  14,4G  0 disk  
                ├─mmcblk0p1                          179:1    0   1,6G  0 part  
                ├─mmcblk0p2                          179:2    0     1K  0 part  
                └─mmcblk0p5                          179:5    0    32M  0 part  

        The important thing is that you find it and, again, DO NOT mount the device.
        This is the drive you will transfer the image to.

#. Initialize the SD card with GNU Health

.. warning::
        The following instruction will COMPLETELY ERASE the contents on the ENTIRE SD card!

In this example, the SD card is associated to **mmcblk0** 

.. code-block:: shell
        :linenos:

     
        dd if=gnuhealth-3.6.4-rpi4-SD-opensuse-leap15.2-xfce.img bs=4M of=/dev/mmcblk0 iflag=fullblock oflag=direct status=progress; sync

This will take a while.
It is highly recommended to use a high-speed SD card.

.. _embedded-embedded:gnu_health_embedded-downloading_the_images-getting_the_image-boot_the_raspberry_pi_with_the_gnu_health_image:

Boot the Raspberry Pi with the GNU Health image
"""""""""""""""""""""""""""""""""""""""""""""""

If the dd command finished successfully, you can now place the SD card into the Raspberry Pi device, and boot the little server.

.. _embedded-embedded:gnu_health_embedded-downloading_the_images-main_users:

Main users
^^^^^^^^^^
The two main OS users are :

- **root** : default password "freedom"<br>
- **gnuhealth** : The GNU Health admin. Default password "freedom"

.. _embedded-embedded:gnu_health_embedded-downloading_the_images-services:

Services
^^^^^^^^
The main services (PostgreSQL, GNU Health HMIS, display manager) are enabled by default.
Refer to the GNU Health and your operating system guides to manage them.