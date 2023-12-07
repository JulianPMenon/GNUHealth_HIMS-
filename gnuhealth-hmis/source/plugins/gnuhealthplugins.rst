.. _plugins-gnuhealthplugins:gnu_health_plugins:

GNU Health Plugins
==================
.. _plugins-gnuhealthplugins:gnu_health_plugins-introduction:

Introduction
------------
The GNU Health Plugins are client-side programs that provide extra functionality. They are installed locally.

.. _plugins-gnuhealthplugins:gnu_health_plugins-initialize_the_plugin_directory:

Initialize the plugin directory
-------------------------------
The GNU Health plugins are installed in your $HOME directory, under "gnuhealth_plugins".

.. code-block::
        :linenos:


        mkdir $HOME/gnuhealth_plugins

In order to keep the GNU Health plugins compatible with the latest client, you need to create a link to the GNU Health plugins directory

.. code-block::
        :linenos:


        ln -si $HOME/gnuhealth_plugins $HOME/.config/gnuhealth/4.0/plugins

.. _plugins-gnuhealthplugins:gnu_health_plugins-the_gnu_health_camera:

The GNU Health Camera
---------------------
The GNU Health camera plugin allows to visualize, transfer and store media from a webcam device ( camera, microscope, ... ).

There are many contexts where the camera is useful, some of them :

* Person or patient registration
* Domiciliary units surveys
* Histological studies
* EKG strips
* Telemedicine
* Dx Imaging
* ...

The information captured by the device will be transferred and stored in the GNU Health server.

.. _plugins-gnuhealthplugins:gnu_health_plugins-the_gnu_health_camera-installing_opencv:

Installing OpenCV
^^^^^^^^^^^^^^^^^
The GNU Health camera uses the excellent Open Computer Vision library ("OpenCV"). You need to install the opencv package for your operating system.

Install the Python bindings for OpenCV of your distribution. In openSUSE, the package is :code:`python3-opencv` . In Archlinux, :code:`python-opencv`

How to check the correct installation of OpenCV:
import the module CV2 in the python interpreter

.. code-block:: shell
        :linenos:


        $ python3
        Python 3.10.5 (main, Jun  6 2022, 18:49:26) [GCC 12.1.0] on linux
        Type "help", "copyright", "credits" or "license" for more information.
        >>> import cv2
        >>> 


If no errors, the installation is successful!

.. _plugins-gnuhealthplugins:gnu_health_plugins-the_gnu_health_camera-installing_the_gnu_health_camera:

Installing the GNU Health Camera
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
Download and uncompress the latest version from GNU into your home directory<br />

.. code-block:: shell
        :linenos:


        cd $HOME
        wget ftp://ftp.gnu.org/gnu/health/plugins/gnuhealth-camera-plugin-latest.tar.gz
        tar -xzvf gnuhealth-camera-plugin-latest.tar.gz

Restart the client

.. _plugins-gnuhealthplugins:gnu_health_plugins-the_gnu_health_camera-invoking_the_gnu_health_camera:

Invoking the GNU Health Camera 
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
From the client, click on the Launch action icon, and select "GNU Health Camera"

.. _plugins-gnuhealthplugins:gnu_health_plugins-the_gnu_health_camera-using_the_camera:

Using the Camera
^^^^^^^^^^^^^^^^
"**a**" : attach any media taken from the camera device into the current model.

**[SPACE]** : store the media as a binary field, for instance, as the person / patient picture. To store the media as a picture, press the SPACE bar. Currently GNU Health has the party model person picture predefined.

"**h**" : Show the help menu

"**q**" : Quit the camera

After you transfer the media, you need to refresh the current view **[CONTROL + R]**

.. _plugins-gnuhealthplugins:gnu_health_plugins-gnu_health_crypto_plugin:

GNU Health Crypto plugin
------------------------
GNU Health allows signing and encrypting documents with the GNU Privacy Guard plugin. 

The Crypto plugin works along with the :ref:`GNU Health Crypto Module <hmis-security:security-public-key_cryptography_in_gnu_health-gnu_health_cryptographic_module>`.

.. warning::
        These packages are installed in the client, NOT in the server

In order to use it, you need the following in your client:
* The **GNU Health crypto plugin** for the Tryton client, shipped with the main tarball (under the backend/plugins directory). Since 2.8.0, the GNU Health Tryton crypto plugin will be a separate package.
* The **GPG package** (comes with most modern operating systems).
* The **python-gnupg library** (https://pypi.python.org/pypi/python-gnupg).



.. _plugins-gnuhealthplugins:gnu_health_plugins-gnu_health_crypto_plugin-installation_of_the_crypto_plugin:

Installation of the Crypto plugin
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

We assume you have installed the GNU Health client using the sources.

Place the "crypto" directory containing the plugin under the "gnuhealth_plugins" of your client.

.. code-block:: shell
        :linenos:


        cp -a gnuhealth_crypto_plugin_dir $HOME/gnuhealth_plugins
