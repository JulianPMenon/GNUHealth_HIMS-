.. _hmis-upgrade:upgrade:

Upgrade
=======
.. _hmis-upgrade:upgrade-about_gnu_health_upgrades:

About GNU Health Upgrades
-------------------------

GNU Health is in constant development. Upgrades fix bugs and keep your system with the latest functionality. Therefore, you are advised to keep your production system with the latest version.

GNU Health will always provide the scripts and tools for you to keep your health center updated.

.. _hmis-upgrade:upgrade-gathering_information:

Gathering Information
---------------------

**Get the latest GNU Health versions and announces**: A key point to keep your GNU Health environment in good shape is to become part of the community. We publish GNU Health version updates and other relevant news in different media. Make sure you subscribe at least to the General users and to the health announce mailing lists.
 
**Verify your current GNU Health version**: You can check your current GNU Health database version from the client, via *Administration → Modules*.


**Always upgrade all the GNU Health modules**: When we release a version, we always pack all the official modules on it. This is important, because we test the integrity and cross-functionality among modules. So, **you should never use modules from different versions**. For example, you should not use :code:`health_genetics` version 1.6.3 with :code:`health` 1.6.2 . This is not supported and can create serious inconsistencies on your database!

.. _hmis-upgrade:upgrade-prepare_your_upgrade:

Prepare your Upgrade
--------------------

**Plan your upgrade process, resources and downtime**: Upgrading a hospital information system requires careful planning. Make sure you choose the right time, and notice your colleagues about the new release. 

**Test the upgrade process in another computer**: It is highly recommended that you count with a separate server, where you can test your upgrade process in a controlled environment, without impacting your production installation. Write down all the steps and issues that you run into.

.. _hmis-upgrade:upgrade-the_upgrade_process:

The Upgrade Process
-------------------

This section summarizes the upgrade process steps for a standard installation, using the modules included in the official release at GNU.org FTP site. Any version specific information will sent via the '''health-announce@gnu.org''' mailing list, along the new release announcement, so make sure you are subscribed!

.. important:: 
        Backup the database, attachments and kernel (modules)

**Step 1:** Stop your Tryton server.

**Step 2:** Backup your database and GNU Health directories

.. code-block:: shell
        :linenos:


        ./gnuhealth-control backup --backdir <directory> --database <dbname>

**Step 3:** Rename the current kernel directory, with *gnuhealth* user:

.. code-block:: shell
        :linenos:


        cd $HOME
        mv gnuhealth gnuhealth_your_current_version_number

**Step 4:** Download the new GNU Health version. The official GNU Health tar file contains all the modules.

**Step 5:** Extract the kernel and follow the instructions as in a new :ref:`hmis-installation-vanilla:vanilla_installation`.

**Step 6:** Update the Tryton configuration file :code:`trytond.conf` to fit your needs. Make sure you have the right values for your installation. Compare the values with your current version, they should match. Some critical variables are:

* :code:`path`

The best way to edit the configuration file is to use the GNU Health user alias :code:`editconf`:

.. code-block:: shell
        :linenos:


        editconf

**Step 7:** Upgrade the database: 

.. code-block:: shell
        :linenos:


        cdexe
        ./trytond-admin --all --database=your_database_name 


**Step 8:** Apply possible post-upgrade scripts at PostgreSQL level (one-time process)

You apply this step if you are upgrading from 3.0 to 3.2. Please remember **to apply this script only once !**

.. code-block:: shell
        :linenos:


        cd gnuhealth-3.2.0/scripts/upgrade/3.2
        psql your_db_name < upgrade_32.sql

**Step 9:** Start the Tryton server:

.. code-block:: shell
        :linenos:


        cdexe
        nohup ./trytond &

You should be now in your new GNU Health version!
