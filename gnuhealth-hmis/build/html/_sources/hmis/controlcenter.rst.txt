.. _hmis-controlcenter:the_gnu_health_control_center:

The GNU Health Control Center
=============================
.. _hmis-controlcenter:the_gnu_health_control_center-about_the_gnu_health_control_center:

About the GNU Health Control Center
-----------------------------------

The GNU Health Control Center :code:`gnuhealth-control` is the main tool for administrative tasks of the :ref:`GNU Health environment<functionality:gnu_health_hmis_functionality>`.

It can perform backups and updates of the instance, and it can be used non-interactively (e.g. as a cron job). We recommend using gnuhealth-control to perform the administrative tasks, since it also creates a log file that will be very useful in case of problems.

.. _hmis-controlcenter:the_gnu_health_control_center-invoking_gnuhealth-control:

Invoking gnuhealth-control
--------------------------

The GNU Health Control Center resides in the UTIL directory of your server.

.. code-block::
  :linenos:


  usage: gnuhealth-control command [options]

  Command:

    version : Show version
    backup  : Backup the gnuhealth kernel, attach dir and database
    update  : Download and install the patches
    getlang : Get and install / update the language pack code
    status  : Show environment and GNU Health HMIS server status

  Options:

    --backdir  : destination directory for the backup file
    --dry-run  : Check, download and preview, but don't actually run the update process
    --database : database name to use with the backup command 

.. _hmis-controlcenter:the_gnu_health_control_center-backups:

Backups
-------

When using gnuhealth-control to perform backups, the application does the following tasks :

* Perform a backup of the database.
* Perform a backup of the $HOME directory of the gnuhealth user, so it stores the kernel, rc files, modules and attach directory.

To perform a backup, you call the gnuhealth-control utility with the database name and target directory where you want to store it.

.. code-block:: shell
  :linenos:


  ./gnuhealth-control backup --backdir <directory> --database <dbname>

GNU Health control backup command creates two files on your destination backup directory :

* The compressed database dump: The format is : :code:`backup_db-name_timestamp.gz`
* The database and filesystems for GNU Health.

.. _hmis-controlcenter:the_gnu_health_control_center-updating_gnu_health_with_gnuhealth-control:

Updating GNU Health with gnuhealth-control
------------------------------------------

When gnuhealth-control is invoked with the update command, it will update GNU Health components within the same major number
The following components will be checked and updated if necessary:

* Trytond: Tryton server version
* Standard Tryton modules included the official GNU Health installation
* Security Advisories to be applied on the default Tryton kernel
* GNU Health patchsets (see :ref:`hmis-patches:patches_and_patchsets` for more information)

This will be valid for version with the same major and minor numbers, for example 3.0.x will look for the latest Tryton updates and GNU Health updates associated to that release.

.. _hmis-controlcenter:the_gnu_health_control_center-updating_gnu_health_with_gnuhealth-control-checking_for_new_updates:

Checking for new updates
^^^^^^^^^^^^^^^^^^^^^^^^
You can check the status on your Tryton and GNU Health server by running a dry-run update. Invoking the update command with the option :code:`--dry-run will` only check if your server needs to be updated, without doing any changes.

.. code-block:: shell
  :linenos:

  ./gnuhealth-control update --dry-run

.. _hmis-controlcenter:the_gnu_health_control_center-updating_gnu_health_with_gnuhealth-control-installing_the_updates:

Installing the updates
^^^^^^^^^^^^^^^^^^^^^^

.. warning::
  Stop your GNU Health instance and do a full backup before starting the update}}

**The main steps are** 
#. Stop the instance and make a backup
#. Run the kernel update with gnuhealth-control tool
#. Update the database

Once you have stopped your instance, and made a full offline backup, you are ready to perform the actual update.

With the **gnuhealth user**, execute the following command. It will download all the Tryton and GNU Health patches, and it will reload the bash environment variables right after it.

.. code-block:: shell
  :linenos:

    
  cdutil
  ./gnuhealth-control update && source $HOME/.gnuhealthrc


Finally, update your database

.. code-block:: shell
  :linenos:


  cdexe
  ./trytond-admin --all --database=name_of_your_db

If everything went well, you have updated to the latest Tryton and GNU Health patchset !
You can now restart the server.

You can get the latest version of GNU Health control center at GNU ftp://ftp.gnu.org/gnu/health

.. _hmis-controlcenter:the_gnu_health_control_center-restore:

Restore
-------

GNU Health control center allows you to restore a complete GNU Health instance, including the database and the filesystem. Of course, in order to perform a restore, you need to have a backup. I will concentrate on the backup done with the GNU Health control center.

To restore a database, connect with "gnuhealth" operating system user, and change to the directory where the database backup resides.

#. **Create a new database** 

.. code-block:: shell
  :linenos:


  $ createdb your_db_name

#. **Uncompress the database dump that was generated using GNU Health control**

.. code-block:: shell
  :linenos:


  $ gunzip backup_db-name_timestamp.gz


#. **Restore the DB using psql**

.. code-block:: shell
  :linenos:


  $ psql your_db_name < backup_db-name_timestamp

