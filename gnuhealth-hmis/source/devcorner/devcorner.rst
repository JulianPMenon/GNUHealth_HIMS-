.. _devcorner-devcorner:developer's_corner:

Developer's Corner
==================

This chapter focus on the development of the upcoming version in different components of GNU Health

The developer's corner is **highly volatile**. It's chaotic and unstable, and we love it like that ;)

Please respect the target build of each component.

.. _devcorner-devcorner:developer's_corner-hospital_management_information_system:

Hospital Management Information System
--------------------------------------
**Target build : 4.0**

**openSUSE Leap <=15.3 and other OS using Python 3.6**
It's highly recommended to use **Python versions >=3.7**

If your distribution uses Python 3.6, then you must enforce the following dependencies versions:

* apiron==5.1.0
* beren==0.7.0

.. _devcorner-devcorner:developer's_corner-hospital_management_information_system-wishlist:

Wishlist
^^^^^^^^

* New GNU Health WebGUI which supports all GNU Health features and works as well on Tablet and Smartphone. It should have a new UX Design and clearly not replicate the GTK design
* Redesign GTK Client - Etienne mentioned some improvements
* Interface to AI providers like Planet-AI
* Integration of the Tryton pos module with the pharmacy module
* Integration with DHIS2

.. _devcorner-devcorner:developer's_corner-hospital_management_information_system-upgrade:

Upgrade
^^^^^^^


BEFORE THE UPGRADE:

#. Execute the script :code:`before.sql`
#. update tryton server (:code:`./trytond-admin --all`)

AFTER THE UPGRADE:

#. Execute the script :code:`after.sql`
#. The Calendar and Webdav menus might shown twice. Just deactivate the obsolete first instance (Administration → User Interface → Menu)

.. _devcorner-devcorner:developer's_corner-hospital_management_information_system-gtk_client:

GTK Client
^^^^^^^^^^
The GNU Health GTK client beta is at **testpypi**

You can download it using the following command:

.. code-block:: shell
        :linenos:

     
        python3 -m pip install --index-url https://test.pypi.org/simple/ --extra-index-url https://pypi.org/simple/ gnuhealth-client==4.0b1

.. _devcorner-devcorner:developer's_corner-hospital_management_information_system-gtk_client-plugins:

Plugins
"""""""
The search path for plugins goes like this:

#. **<config dir>/plugins**
        Example: /home/lfm/.config/gnuhealth/3.5/plugin
#. **<current_gnuhealth_dir>/tryton/plugins**
        Example: /home/lfm/health/gnuhealth-client/tryton/plugins
#. **$HOME/gnuhealth_plugins**
        Example: /home/lfm/gnuhealth_plugins


The third one (:code:`$HOME/gnuhealth_plugins`) is the recommended place for most users.  It makes easy automation and allows convenient drag and drop for plugins.

The first option is recommended for users that have different GH GTK client versions installed.

.. _devcorner-devcorner:developer's_corner-hospital_management_information_system-web_client:

Web Client
^^^^^^^^^^
The webclient is based on the Tryton SAO Webclient. It does not have the current functionality, desktop integration and security features as the GTK client.
For developers only...

INSTALLING SAO (as gnuhealth user)

.. code-block:: shell
        :linenos:

      
        download https://downloads.tryton.org/6.0/tryton-sao-last.tgz
        cd $HOME
        mkdir sao
        cd sao/package
        npm install
        cd /home/gnuhealth/sao/package/node_modules/.bin
        ./grunt

On the :code:`[web]` section :

.. code-block:: shell
        :linenos:

     
        root = /home/gnuhealth/sao/package

.. _devcorner-devcorner:developer's_corner-hospital_management_information_system-interfaces:

Interfaces
^^^^^^^^^^

.. _devcorner-devcorner:developer's_corner-gnu_health_federation:

GNU Health Federation
---------------------
.. _devcorner-devcorner:developer's_corner-gnu_health_federation-thalamus:

Thalamus
^^^^^^^^

.. _devcorner-devcorner:developer's_corner-gnu_health_federation-gh_federation_portal:

GH Federation Portal
^^^^^^^^^^^^^^^^^^^^
.. _devcorner-devcorner:developer's_corner-mygnuhealth_mobile_application:

MyGNUHealth mobile application
------------------------------

.. _devcorner-devcorner:developer's_corner-mygnuhealth_mobile_application-installation_of_mygnuhealth_pinephone_and_manjaro_plasma_mobile:

Installation of MyGNUHealth PinePhone and Manjaro Plasma Mobile 
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
Install requirements

* Update de system (:code:`pacman -Syu`)
* Install gcc (:code:`pacman -S gcc`)
* Install base devel tools (:code:`pacman -S base-devel`)
* Install pyside2 package (:code:`pacman -S pyside2-es2`) (Make sure you use this package! The regular "pyside2" won't work. Thanks Anupam!)

.. code-block:: shell
        :linenos:

     
        pacman -Syu # Update de system
        pacman -S gcc # Install gcc
        pacman -S base-devel # Install base devel tools
        pacman -S pyside2-es2 # Install pyside2 package; Make sure you use this package! Regular pyside2 won't work. Thanks Anupam!

.. _devcorner-devcorner:developer's_corner-mygnuhealth_mobile_application-installation_on_pinephone_and_kde_neon:

Installation on PinePhone and KDE Neon
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

* Install in a SD card the plasma-mobile latest image  (https://images.plasma-mobile.org/pinephone/)

Install required packages

.. code-block:: shell
        :linenos:

     
        apt-get install  python3-pip
        apt-get install qt5-qmake
        apt-get install cmake
        apt-get install qtbase5-dev
        apt-get install clang clang libclang-6.0-dev
        apt-get install qtbase5-private-dev
        apt-get install qtdeclarative5-dev qtdeclarative5-private-dev


Create a swapfile (it will be needed during the building process)

.. code-block:: shell
        :linenos:

     
        sudo bash
        cd /opt
        dd if=/dev/zero of=swapfile bs=1G count=1
        mkswap swapfile
        swapon swapfile

(you can later add it to the fstab if you want to have it permanent)
add  to :code:`/etc/fstab`

.. code-block:: shell
        :linenos:

     
        /opt/swapfile            swap    swap    defaults        0       0

Download,extract and build PySide2
https://doc.qt.io/qtforpython/gettingstarted-linux.html#.getting-pyside2

Fix the following symlinks that are broken:

.. code-block:: shell
        :linenos:

     
        $ cd pyside2/pyside-setup/pyside3_install/py3.6-qt5.14.2-64bit-release/bin$

        $ ln -si /usr/bin/qtchooser ./designe
        $ ln -si /usr/bin/qtchooser ./rc
        $ ln -si /usr/bin/qtchooser ./ui

.. _devcorner-devcorner:developer's_corner-mygnuhealth_mobile_application-installation_on_the_desktop:

Installation on the Desktop
^^^^^^^^^^^^^^^^^^^^^^^^^^^

Nightly Builds to install MyGNHealth on a GNU/Linux Desktop are available at `OpenBuildService <https://build.opensuse.org/package/show/Application:ERP:GNUHealth:3.6/mygnuhealth>`_

.. _devcorner-devcorner:developer's_corner-orthanc_integration:

Orthanc integration
-------------------

Notes obtained from C:

PACS / DICOM goals

For providers:

    * Consistent access to imaging studies in multiple views / tabs

        * Including accurate imaging information including type of imaging (CT, MRI, ultrasound, etc), date/time, location, and final report (essential if available)
        * Quickly copy/paste images and reports (eg, into notes)
    * Easy imaging viewing through a robust PACS viewer
    * Upload new (or newly obtained) imaging studies to local PACS server from outside sources

        * Patients frequently bring imaging discs with previous studies which should be stored for better continuity of care and medical decision-making. Furthermore, outside images should be able to be stored for quicker access and local evaluation.
    * Send imaging studies to other locations and / or patients

        * CD / DVD saving / “burning” (likely location specific)
        * Send to outside medical office / provider via network (or CD/DVD)
        * This assists in transfers of care and patient access to medical records.
    * Notify provider on new imaging results (configurable as appropriate)

For developers (see implementing the above goals with some notable details below)
    * Synchronization of relevant data in fault-tolerant and error-free way

        * Reliability and accuracy are much more important than speed
        * Support Orthanc and other servers (as possible)
    * Providers should interface with data in intuitive manner with appropriate data viewers

        * Zero config for the providers
        * Imaging studies → PACS viewer
        * Final reports / etc→ PACS viewer or PDF / text viewer (if not built-in to PACS viewer)
    * Bidirectional interactions with PACS server

        * PACS authentication should be seamless for the multiple types of users (providers, admin, etc)
        * Connecting remote studies to local patients
        * Uploading imaging studies (as above) should be attached to local patient
        * Expose multiple PACS endpoints / tasks to administrators
    * Other:

        * Appropriate access restrictions for data and tasks
        * Continuous access to data for providers (no downtime for updates or similar)
        * Minimize bandwidth used (via avoiding unnecessary transfers) given resource restricted environments
        * Network interactions should be encrypted via TLS or other similarly appropriate mechanism

Ideas from G, rather details than general concept:

* Target error codes, until here only 401, "Invalid Domain" or "Success"
* When creating a patient in HMIS from patient in Orthanc: Adopt/suggest name, dob & ID automatically
* Support DICOM preview inside client (Orthanc: Only link to open in browser yet, health_imaging: DICOM not supported)
* Add series & instances as ressources? Orthanc module supports only patients & studies, but Orthanc itself has patients, studies, series & instances as ressources

Open task/bug:

* “When requesting a DX image, have the possibility to send this to Orthanc “
* “When creating the DX imaging result, have the possibility to link the images/studies to data coming from orthanc”

Bug #.59872
