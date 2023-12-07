.. _appendix-opsystem:operating_system-specific_notes:

Operating System-Specific Notes
===============================
|version3.6|

.. _appendix-opsystem:operating_system-specific_notes-opensuse:

openSUSE
--------

.. note::
        This section provides the instructions for the official and standard (vanilla) installation on openSUSE.
        If you want to use the openSUSE package based installation, please refer to the :ref:`appendix-community:community_pages`

.. _appendix-opsystem:operating_system-specific_notes-opensuse-download_and_install_the_operating_system:

Download and install the Operating System 
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

* Download the openSUSE Leap Network `CD image <https://software.opensuse.org/distributions/leap>`_ 
* Check the partitioning and FS options (we use ext4 filesystem)
* Select SERVER (text only) installation
* Enable SSHD server
* Create the user "gnuhealth" when prompted at installation time.<br>

.. _appendix-opsystem:operating_system-specific_notes-opensuse-install_the_requirements:

Install the requirements
^^^^^^^^^^^^^^^^^^^^^^^^

.. code-block:: shell
        :linenos:


        sudo zypper in patch gcc libxml2-devel  postgresql postgresql-server unoconv python3-pip python3-devel


Initialize the PostgreSQL environment. The next systemctl start command will generate the initial pg cluster.

.. code-block:: shell
        :linenos:


        systemctl start postgresql

.. _appendix-opsystem:operating_system-specific_notes-opensuse-update_locally_pip3:

Update locally pip3
^^^^^^^^^^^^^^^^^^^

.. code-block:: shell
        :linenos:


        su - gnuhealth
        pip3 install --upgrade --user pip

:ref:`hmis-installation-vanilla:vanilla_installation-installing_gnu_health_on_gnu/linux_and_freebsd-creating_the_operating_system_user`

.. _appendix-opsystem:operating_system-specific_notes-debian:

Debian
------
|version3.6|

.. _appendix-opsystem:operating_system-specific_notes-debian-download_and_install_the_operating_system:

Download and install the Operating System 
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

* Download the Debian OS  `image <https://www.debian.org>`_ 
* Check the partitioning and FS options (we use ext4 filesystem)
* Deselect the "Debian desktop environment" if you just want a server (no graphical interface)
* Enable SSHD server
* Create the user "gnuhealth" when prompted at installation time.<br>

.. _appendix-opsystem:operating_system-specific_notes-debian-install_the_requirements:

Install the requirements
^^^^^^^^^^^^^^^^^^^^^^^^

.. code-block:: shell
        :linenos:


        apt-get install postgresql patch python3-pip unoconv

:ref:`hmis-installation-vanilla:vanilla_installation-installing_gnu_health_on_gnu/linux_and_freebsd-creating_the_operating_system_user`

.. _appendix-opsystem:operating_system-specific_notes-freebsd:

FreeBSD
-------

|version3.6|

.. _appendix-opsystem:operating_system-specific_notes-freebsd-at_operating_system_installation:

At Operating System installation
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

* Select SSHD
* Create the gnuhealth user at installation time

.. _appendix-opsystem:operating_system-specific_notes-freebsd-install_requirements:

Install requirements 
^^^^^^^^^^^^^^^^^^^^

.. code-block:: shell
        :linenos:


        pkg install postgresql13-server wget bash py37-pip \
        py37-lxml py37-pillow patch rust

.. _appendix-opsystem:operating_system-specific_notes-freebsd-initialize_postgresql:

Initialize PostgreSQL
^^^^^^^^^^^^^^^^^^^^^

.. code-block:: shell
        :linenos:


        /usr/local/etc/rc.d/postgresql oneinitdb
        sysrc postgresql_enable=yes
        service postgresql start

.. _appendix-opsystem:operating_system-specific_notes-freebsd-create_python3_links:

Create Python3 links
^^^^^^^^^^^^^^^^^^^^

.. code-block:: shell
        :linenos:


        ln -si /usr/local/bin/python3.7 /usr/local/bin/python3
        ln -si /usr/local/bin/python3 /usr/local/bin/python

.. _appendix-opsystem:operating_system-specific_notes-freebsd-change_/bin/bash_to_/usr/local/bin/bash:

Change /bin/bash to /usr/local/bin/bash
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

The first line of script that starts gnuhealth (:code:`start_gnuhealth.sh`) is pointing to /bin/bash. On FreeBSD you have to change that to /usr/local/bin/bash.


:ref:`hmis-installation-vanilla:vanilla_installation-installing_gnu_health_on_gnu/linux_and_freebsd-creating_the_operating_system_user`

.. _appendix-opsystem:operating_system-specific_notes-centos:

CentOS
------

.. _appendix-opsystem:operating_system-specific_notes-centos-install_python_3.8:

Install Python 3.8
^^^^^^^^^^^^^^^^^^

.. code-block:: shell
        :linenos:


        yum install python3
        yum install python3-devel

.. _appendix-opsystem:operating_system-specific_notes-centos-install_postgresql_12:

Install PostgreSQL 12
^^^^^^^^^^^^^^^^^^^^^

.. code-block:: shell
        :linenos:


        yum -y install https://download.postgresql.org/pub/repos/yum/reporpms/EL-7-x86_64/pgdg-redhat-repo-latest.noarch.rpm
        yum -y install epel-release yum-utils sudo yum-config-manager ^^enable pgdg12 sudo yum install postgresql12-server postgresql12

:ref:`hmis-installation-vanilla:vanilla_installation-installing_gnu_health_on_gnu/linux_and_freebsd-creating_the_operating_system_user`

.. _appendix-opsystem:operating_system-specific_notes-ubuntu:

Ubuntu
------

* These instructions apply to **Ubuntu 20.04** and **Armbian 20.05** version
* Create the gnuhealth user at installation time

.. _appendix-opsystem:operating_system-specific_notes-ubuntu-update_the_sources:

Update the Sources 
^^^^^^^^^^^^^^^^^^

.. code-block:: shell

        :linenos:

        apt-get update

.. _appendix-opsystem:operating_system-specific_notes-ubuntu-install_requirements:

Install requirements
^^^^^^^^^^^^^^^^^^^^

.. code-block:: shell
        :linenos:


        apt-get install postgresql-server-dev-12 libxml2-dev libxslt-dev python3-dev pkg-config libfreetype6-dev postgresql patch python3-pip unoconv libpng-dev libjpeg8-dev

:ref:`hmis-installation-vanilla:vanilla_installation-installing_gnu_health_on_gnu/linux_and_freebsd-creating_the_operating_system_user`

.. _appendix-opsystem:operating_system-specific_notes-armbian:

Armbian
-------

* These instructions apply to **Armbian 20.05** version
* Create the gnuhealth user at installation time

.. _appendix-opsystem:operating_system-specific_notes-armbian-update_the_sources:

Update the Sources 
^^^^^^^^^^^^^^^^^^

.. code-block:: shell
        :linenos:


        apt-get update

.. _appendix-opsystem:operating_system-specific_notes-armbian-install_requirements:

Install requirements
^^^^^^^^^^^^^^^^^^^^

.. code-block:: shell
        :linenos:


        apt-get install postgresql-server-dev-12 libxml2-dev libxslt-dev python3-dev pkg-config libfreetype6-dev postgresql patch python3-pip unoconv libpng-dev libjpeg8-dev

:ref:`hmis-installation-vanilla:vanilla_installation-installing_gnu_health_on_gnu/linux_and_freebsd-creating_the_operating_system_user`
