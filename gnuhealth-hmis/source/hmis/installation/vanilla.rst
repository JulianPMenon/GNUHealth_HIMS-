.. _hmis-installation-vanilla:vanilla_installation:

Vanilla Installation
====================
.. _hmis-installation-vanilla:vanilla_installation-requirements:

Requirements
------------

The latest stable **GNU Health Federation** ecosystem uses these main resources:

* Operating system: GNU/Linux or FreeBSD for the server.
* RDBMS Database: :ref`PostgreSQL` **>= 10.x**
* Document-oriented Database for Health Information System / Person Master Index: PostgreSQL: **>= 10.x**
* Python: **>= 3.6**
* uwsgi : **>= 2.0**
* Flask : **1.0**
* :wikipedia:`Tryton` **6.0**
* :wikipedia:`Bash shell <Bash_(Unix_shell)>`
* PIP for **Python3**, verify through

.. code-block:: shell
    :linenos:

    pip --version

You should see *python3*, as in: :code:`pip x.x. from /usr/local/lib/python3.6/site-packages (python 3.6)`
If you see python2.x then stop and get pip for Python 3.

.. _hmis-installation-vanilla:vanilla_installation-errata:

Errata
------

Before you continue, please read the :ref:`appendix-errata:errata` chapter for the latest issues involved the installation or upgrade procedure.

.. _hmis-installation-vanilla:vanilla_installation-installing_gnu_health_on_gnu/linux_and_freebsd:

Installing GNU Health on GNU/Linux and FreeBSD
----------------------------------------------

.. _hmis-installation-vanilla:vanilla_installation-installing_gnu_health_on_gnu/linux_and_freebsd-operating_system_requirements:

Operating System requirements
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
The following table contains the instructions to setup your operating system for a standard GNU Health installation. The operating systems and their version shown in the list have been tested using the instructions for each OS.

The installation instructions for the different operating systems and distributions have been done on a fresh installation. For simplicity's sake, the server environment was installed without a GUI. No firewall was configured (we will cover this on the security section), and OpenSSH server was installed.

The instructions – written here – have been applied and verified with the following operating systems as shown below.

.. warning::
    Verify that you are using the operating system version documented on the following table

.. list-table::
    :widths: 25 25 25 10
    :header-rows: 1

    * - Operating System 
      - Version 
      - Link 
      - Notes
    * - openSUSE 
      - Leap 15.4 
      - :ref:`appendix-opsystem:operating_system-specific_notes-opensuse`  
      -
    * - FreeBSD 
      - FreeBSD 12.1 
      - :ref:`appendix-opsystem:operating_system-specific_notes-freebsd`  
      - 
    * - CentOS 
      - 7.8 
      - :ref:`appendix-opsystem:operating_system-specific_notes-centos`  
      - 
    * - Ubuntu 
      - 20.04 
      - :ref:`appendix-opsystem:operating_system-specific_notes-ubuntu`  
      - 
    * - Armbian 
      - 20.05 
      - :ref:`appendix-opsystem:operating_system-specific_notes-armbian`
      -
    * - Debian 
      - 10.1 
      - :ref:`appendix-opsystem:operating_system-specific_notes-debian`
      - 

.. _hmis-installation-vanilla:vanilla_installation-installing_gnu_health_on_gnu/linux_and_freebsd-setting_up_network_time_protocol_(ntp):

Setting up Network Time Protocol (NTP)
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
In order to properly run GNU Health, you need to make sure that the time on both the server (database and central instance) and clients are properly set and in sync. The best way to do this is to keep your clock synchronized with a :wikipedia:`NTP Server <Network_Time_Protocol>` .

This is a critical step, not only for the smooth functioning of GNU Health, but also because many documents will have a timestamp associated with them that can have legal value.

.. _hmis-installation-vanilla:vanilla_installation-installing_gnu_health_on_gnu/linux_and_freebsd-creating_the_operating_system_user:

Creating the Operating System User
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

.. warning::
    Do this step only if you **didn't** create the user during the installation of the operating system.

The following steps will create the GNU Health operating system user. Please note that many operating systems give you the option to create a regular user at installation time. If you already created the "gnuhealth" operating system user, you can skip this section, otherwise, create it now.

Run the following command **as root**:

.. code-block:: shell
    :linenos:


    adduser gnuhealth

.. note::
    If your Operating System **doesn't** include the adduser command, you can use the useradd command:

.. code-block:: shell
    :linenos:


    useradd -m gnuhealth

.. _hmis-installation-vanilla:vanilla_installation-installing_gnu_health_on_gnu/linux_and_freebsd-verify_postgresql_authentication_method:

Verify PostgreSQL authentication method
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

.. note::
    You can **skip** this section if you made a standard installation on **FreeBSD**

PostgreSQL uses different authentication methods (MD5, ident, trust ... ). Depending the Operating System, the postgreSQL server authentication method will vary.

The standard GNU&nbsp;Health installation uses the **trust** authentication method, so you need to check the postgreSQL authentication file configuration.

Locate the :code:`g_hba.conf` file and verify that the **trust** method is set.
The location of this configuration file varies across operating systems; under UNIX/Linux, the full pathname of the file can be obtained with the following command, to be executed as **root**:

.. code-block:: shell
    :linenos:


    su - postgres -c "psql -t -P format=unaligned -c 'show hba_file'"

You may need to start the postgres server at least one time as this file may be created during first startup. Usually this file is located at :code:`etc/postgresql/10/main` or :code:`/var/lib/pgsql/data`. 

An example configuration file entry specifying use of the **trust** method is given in the following line:

.. code-block:: shell
    :linenos:


    local all all trust

The following example in particular may address issues with establishing a working database connection as reported in the context of the creation of the GNU&nbsp;Health database upon first use of the Tryton client (see further down; Symptom: the "Create" button is not displayed):

.. code-block:: shell
    :linenos:


    host all all 127.0.0.1/32 trust
    host all all ::1/128      trust

Make sure you edit the file as user 'postgres', not root. Otherwise, postgres may have trouble reading the changed file. After any changes to the file, the postgreSQL server needs to be restarted.

Many authentication errors (e.g., database connection errors) arise because of not having correctly configured this file. Of course, you can use other authentication methods, and you can adapt the tryton / GNU Health configuration file to each of them. For the sake of simplicity, we based the documentation and sample files in this book on one specific method (trust).

Make sure you **restart your postgresql server**:

.. code-block:: shell
    :linenos:


    sudo service postgresql restart

.. _hmis-installation-vanilla:vanilla_installation-installing_gnu_health_on_gnu/linux_and_freebsd-creating_the_database_user:

Creating the Database User
^^^^^^^^^^^^^^^^^^^^^^^^^^

The following command switches to the <tt>postgres</tt> administration user and gives permissions to your newly created :code:`gnuhealth` administrator:

Execute as **root**:

.. code-block:: shell
    :linenos:


    su - postgres -c "createuser --createdb --no-createrole --no-superuser gnuhealth"

.. _hmis-installation-vanilla:vanilla_installation-installing_gnu_health_on_gnu/linux_and_freebsd-downloading_and_installing_gnu_health:

Downloading and Installing GNU Health
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
.. warning::

    Do the following steps with your newly created *gnuhealth* user, **do not** use root.

.. _hmis-installation-vanilla:vanilla_installation-installing_gnu_health_on_gnu/linux_and_freebsd-running_the_gnu_health_installer:

Running the GNU Health Installer
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

.. _hmis-installation-vanilla:vanilla_installation-installing_gnu_health_on_gnu/linux_and_freebsd-running_the_gnu_health_installer-become_user_gnuhealth:

Become user gnuhealth
"""""""""""""""""""""
.. code-block:: shell
    :linenos:


    su - gnuhealth
    cd $HOME

.. _hmis-installation-vanilla:vanilla_installation-installing_gnu_health_on_gnu/linux_and_freebsd-running_the_gnu_health_installer-download_gnu_health_from_gnu.org:

Download GNU Health from GNU.org
""""""""""""""""""""""""""""""""
.. code-block:: shell
    :linenos:


    wget https://ftp.gnu.org/gnu/health/gnuhealth-latest.tar.gz

.. _hmis-installation-vanilla:vanilla_installation-installing_gnu_health_on_gnu/linux_and_freebsd-running_the_gnu_health_installer-verify_the_package_signature:

Verify the package signature
""""""""""""""""""""""""""""
First get the signing key if you haven't done so:

.. code-block:: shell
    :linenos:

    gpg --recv-key  --keyserver  keyserver.ubuntu.com 0xC015E1AE00989199

The key is issued by *Luis Falcon (meanmicio at GNU) <falcon@gnu.org>* and its fingerprint is *ACBF C80F C891 631C 68AA 8DC8 C015 E1AE 0098 9199*. This information can be seen issuing:

.. code-block:: shell
    :linenos:

    gpg --with-fingerprint --list-keys 0xC015E1AE00989199

Then, verify the signature, using the matching version number for the latest. For instance, if latest GNU Health version is 4.0.4, then

Download the detached signature:

.. code-block:: shell
    :linenos:


    wget https://ftp.gnu.org/gnu/health/gnuhealth-4.0.4.tar.gz.sig

Verify the package using the detached signature:

.. code-block:: shell
    :linenos:

    gpg --verify gnuhealth-4.0.4.tar.gz.sig gnuhealth-latest.tar.gz

If the file is correctly validated, the output should be something like:

.. code-block:: shell
    :linenos:

    gpg: Signature made Sat 01 Jul 2017 11:06:25 PM WEST
    gpg:                using RSA key ACBFC80FC891631C68AA8DC8C015E1AE00989199
    gpg: Good signature from "Luis Falcon (GNU) <falcon@gnu.org>" [ultimate]
    gpg:                 aka "Luis Falcon (GNU Health) <lfalcon@gnusolidario.org>" [ultimate]

The important part is the *Good signature from "Luis Falcon ...."*. The WARNING means that, even if the file and signature are OK and validated correctly, you aren't trusting that key; and it's OK. You can read more about this in `The GNU Privacy Handbook, Chapter 3. Key Management <https://www.gnupg.org/gph/en/manual/x334.html>`_.

.. _hmis-installation-vanilla:vanilla_installation-installing_gnu_health_on_gnu/linux_and_freebsd-running_the_gnu_health_installer-uncompress_gnu_health_hmis_package:

Uncompress GNU Health HMIS package
""""""""""""""""""""""""""""""""""

.. code-block:: shell
    :linenos:


    tar xzf gnuhealth-latest.tar.gz

.. _hmis-installation-vanilla:vanilla_installation-installing_gnu_health_on_gnu/linux_and_freebsd-running_the_gnu_health_installer-change_to_the_gnu_health_installation_directory_matching_your_version:

Change to the GNU Health installation directory matching your version
"""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""

.. code-block:: shell
    :linenos:


    cd gnuhealth-4.0.4

.. _hmis-installation-vanilla:vanilla_installation-installing_gnu_health_on_gnu/linux_and_freebsd-running_the_gnu_health_installer-download_the_latest_gnu_health_installer:

Download the latest GNU Health installer
""""""""""""""""""""""""""""""""""""""""
.. code-block:: shell
    :linenos:


    wget -qO- https://ftp.gnu.org/gnu/health/gnuhealth-setup-latest.tar.gz | tar -xzvf -


.. _hmis-installation-vanilla:vanilla_installation-installing_gnu_health_on_gnu/linux_and_freebsd-running_the_gnu_health_installer-run_the_gnu_health_installer:

Run the GNU Health Installer
""""""""""""""""""""""""""""

.. code-block:: shell
    :linenos:


    bash ./gnuhealth-setup install

.. _hmis-installation-vanilla:vanilla_installation-installing_gnu_health_on_gnu/linux_and_freebsd-running_the_gnu_health_installer-enable_the_bash_environment_for_the_gnu_health_admin:

Enable the BASH environment for the GNU Health admin
""""""""""""""""""""""""""""""""""""""""""""""""""""

Finally, enable the BASH environment for the gnuhealth user.

.. code-block:: shell
    :linenos:


    source ${HOME}/.gnuhealthrc

.. _hmis-installation-vanilla:vanilla_installation-installing_gnu_health_on_gnu/linux_and_freebsd-running_the_gnu_health_installer-activate_network_devices_for_the_json-rpc_protocol:

Activate Network Devices for the JSON-RPC Protocol
""""""""""""""""""""""""""""""""""""""""""""""""""

The Tryton GNU Health server listens to localhost at port 8000, not allowing direct connections from other workstations. If necessary, enter the following:

.. code-block:: shell
    :linenos:

    editconf

You can edit the parameter *listen* in the :code:`[web]` section, to activate the network device so workstations in your net can connect. For example, the following block

.. code-block:: shell
    :linenos:


    [web]
    listen = *:8000

will allow to connect to the server in the different devices of your system.

.. _hmis-installation-vanilla:vanilla_installation-installing_gnu_health_on_gnu/linux_and_freebsd-running_the_gnu_health_installer-setting_up_a_local_directory_for_attachments:

Setting up a Local Directory for Attachments
""""""""""""""""""""""""""""""""""""""""""""

By default, Tryton uses a system-wide directory to store the attachments. It is advisable, in GNUHealth to keep the attachments in the *gnuhealth* user space.

If necessary, edit the server configuration file trytond.conf and enter the attach directory under the :code:`[database]` section, for instance:

.. code-block:: shell
    :linenos:

 
    editconf

.. code-block::
    :linenos:

    [database]
    path = /home/gnuhealth/attach

Since debian systems connect to database over a UNIX socket, add an extra **/** under the :code:`[database]` section, for instance:

.. code-block::
    :linenos:

    [database]
    uri = postgresql:///localhost:5432

.. _hmis-installation-vanilla:vanilla_installation-installing_gnu_health_on_gnu/linux_and_freebsd-running_the_gnu_health_installer-configuring_the_log_file_(optional):

Configuring the log file (optional)
"""""""""""""""""""""""""""""""""""

The way the server logs and tracks events is based on a log configuration file, that resides in the config directory :code:`"${GNUHEALTH_DIR}"/tryton/server/config/`.

A default version is shipped, called <tt>gnuhealth_log.conf</tt>. If necessary, enter the following into <tt>gnuhealth_log.conf</tt>:

.. code-block::
    :linenos:

    [formatters]
    keys: simple

    [handlers]
    keys: rotate, console

    [loggers]
    keys: root

    [formatter_simple]
    format: [%(asctime)s] %(levelname)s:%(name)s:%(message)s
    datefmt: %a %b %d %H:%M:%S %Y

    [handler_rotate]
    class: handlers.TimedRotatingFileHandler
    args: ('/home/gnuhealth/gnuhealth/logs/gnuhealth.log', 'D', 1, 30)
    formatter: simple

    [handler_console]
    class: StreamHandler
    formatter: simple
    args: (sys.stdout,)

    [logger_root]
    level: WARNING
    handlers: rotate, console

In this example (and in the standard file) the log file is written in the default logs directory. You can change it to fit your specific installation.

In order to use logging, you need to provide the *--logconf* option, along with the path to the log configuration file <tt>gnuhealth_log.conf</tt> as argument, when invoking the Tryton server in the next section (e.g. :code:`trytond --logconf "${GNUHEALTH_DIR}"/tryton/server/config/gnuhealth_log.conf`).

For more information, check the following resources:

* Python logging facility logging tutorial: https://docs.python.org/3/howto/logging.html#.logging-basic-tutorial
* Tryton Server logging documentation: http://trytond.readthedocs.org/en/latest/topics/logs.html

.. _hmis-installation-vanilla:vanilla_installation-initialize_the_database_instance:

Initialize the database instance
--------------------------------

Create the database

.. code-block:: shell
    :linenos:

    createdb health

.. note::
    We use "health" as an example, choose the name of your database, but keep it short and only alphanumeric chars

Change to your newly installed system (use the alias *cdexe*):

.. code-block:: shell
    :linenos:

    cdexe

and initialize the instance:

.. code-block:: shell
    :linenos:


    python3 ./trytond-admin --all --database=health


You will be asked to provide a password for the "admin" user.

If everything goes well, you are ready to start the GNU Health HMIS node server.

Start the GNU Health HMIS node

.. code-block:: shell
    :linenos:


    cd ./start_gnuhealth.sh

.. note::
    As mentioned in the previous section, use the ''--logconf [path]'' option to specify the path of the logging configuration

You can execute the GNU Health server in the background (:code:`using nohup ./start_gnuhealth.sh &`) and check the output in the file :code:`nohup.out`.

.. _hmis-installation-vanilla:vanilla_installation-creating_a_systemd_service_for_the_gnu_health_server:

Creating a Systemd service for the GNU Health server
----------------------------------------------------

If you use the standard installation method, you can use the following scripts to automate the startup/stop of the GNU Health instance using systemd services.

.. _hmis-installation-vanilla:vanilla_installation-creating_a_systemd_service_for_the_gnu_health_server-gnu_health_service_unit_file:

GNU Health service unit file
^^^^^^^^^^^^^^^^^^^^^^^^^^^^
Create the GNU Health Unit file under :code:`/usr/lib/systemd/system/gnuhealth.service`:

For Ubuntu 18.04 LTS users: :code:`/etc/systemd/system/gnuhealth.service`:

.. code-block::
    :linenos:

    [Unit]
    Description=GNU Health Server
    After=network.target

    [Service]
    Type=simple
    User=gnuhealth
    WorkingDirectory=/home/gnuhealth
    ExecStart=/home/gnuhealth/start_gnuhealth.sh
    Restart=on-abort

    [Install]
    WantedBy=multi-user.target



.. _hmis-installation-vanilla:vanilla_installation-creating_a_systemd_service_for_the_gnu_health_server-starting_and_stopping_the_gnu_health_service:

Starting and Stopping the GNU Health service
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

You can issue the commands:

.. code-block:: shell
    :linenos:

    systemctl start gnuhealth

or:

.. code-block:: shell
    :linenos:

 
    systemctl stop gnuhealth


.. _hmis-installation-vanilla:vanilla_installation-creating_a_systemd_service_for_the_gnu_health_server-enable_the_service_to_start_at_boot_time:

Enable the service to start at boot time
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

If you want to automatically start the GNU Health server whenever you start the operating system, you can enable the service with the following command:

.. code-block:: shell
    :linenos:


    systemctl enable gnuhealth


.. _hmis-installation-vanilla:vanilla_installation-using_a_wsgi_server_for_gnu_health_hospital_management_component:

Using a WSGI Server for GNU Health Hospital Management Component
----------------------------------------------------------------

GNU Health HMIS uses by default the werkzeug server. This should be valid only for development scenarios.
For production servers, GNU Health HMIS will benefit from a Web Server Gateway Interface (WSGI), such as uWSGI and a web server that supports reverse proxy, as NGINX. 

.. _hmis-installation-vanilla:vanilla_installation-using_a_wsgi_server_for_gnu_health_hospital_management_component-your_trytond_configuration_file:

Your Trytond configuration file
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Edit your trytond.conf file to meet the requirements. You can edit this file directly using the alias :code:`editconf` with the gnuhealth user.

This sample enables access both to the GTK and webclient.

.. code-block::
    :linenos:

    [database]
    uri = postgresql://localhost:5432
    path = /home/gnuhealth/attach

    [web]
    listen = localhost:8000
    root = /home/gnuhealth/sao/package 


.. _hmis-installation-vanilla:vanilla_installation-using_a_wsgi_server_for_gnu_health_hospital_management_component-uwsgi_configuration_file:

uWSGI configuration file
^^^^^^^^^^^^^^^^^^^^^^^^

This is a sample for the gnuhealth uwsgi .ini (:code:`gh.ini`) file. Make sure NINGX user has the appropriate permissions to the uwsgi socket.

.. code-block::
    :linenos:

    [uwsgi]

    master = true
    processes = 5
    plugins = python3

    socket = /tmp/uwsgi.sock
    chmod-socket=660

    module=trytond.application:app 


.. _hmis-installation-vanilla:vanilla_installation-using_a_wsgi_server_for_gnu_health_hospital_management_component-configuring_nginx_as_a_reverse_proxy_for_gnu_health_hmis:

Configuring NGINX as a reverse proxy for GNU Health HMIS
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

In this sample, NINGX will listen to 8100 in HTTPS mode, to requests coming from the web clients.
It also listens to port 8000 for the native GTK client.

.. code-block:: shell
    :linenos:


    # Virtual host for demo web client using TLS and listening in 8100
        server {
            listen       8100 ssl;
            server_name  your_hostname;

            ssl_certificate      /path/to/your/gnuhealth.crt;
            ssl_certificate_key  /path/to/your/gnuhealth.key;

            ssl_session_cache    shared:SSL:1m;
            ssl_session_timeout  5m;

            ssl_ciphers  HIGH:!aNULL:!MD5;
            ssl_prefer_server_ciphers  on;

            location / {
                include         uwsgi_params;
                uwsgi_pass      unix:/tmp/uwsgi.sock;
            }

        # Virtual host for GNU Health GTK Client on 8000 
        server {
            listen       8000;

            location / {
                include         uwsgi_params;
                uwsgi_pass      unix:/tmp/uwsgi.sock;
            }
        }
    }



.. _hmis-installation-vanilla:vanilla_installation-using_a_wsgi_server_for_gnu_health_hospital_management_component-putting_everything_together_and_booting_the_gnu_health_server:

Putting everything together and booting the GNU Health Server
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Once you have configured the three elements (Trytond server, uwsgi and NGINX) is time to put in into production

* Make sure your NGINX server is running:
* Start uWSGI with the corresponding gnuhealth .ini file:

.. code-block:: shell
    :linenos:

    uwsgi $HOME/gh.ini --enable-threads &


.. _hmis-installation-vanilla:vanilla_installation-installation_of_the_gnu_health_client:

Installation of the GNU Health Client
-------------------------------------

.. _hmis-installation-vanilla:vanilla_installation-installation_of_the_gnu_health_client-requirements:

Requirements
^^^^^^^^^^^^

.. _hmis-installation-vanilla:vanilla_installation-installation_of_the_gnu_health_client-requirements-opensuse:

openSUSE
""""""""

**Tested on openSUSE Leap 15.1 and Tumbleweed**

* Disable Non-OSS repositoriess
* Desktop with KDE Plasma
* Create user "gnuhealth"
* Login as "gnuhealth" user
* Get the required packages / dependencies

.. code-block:: shell
    :linenos:

    $ sudo zypper install cairo-devel pkg-config python3-devel gcc gobject-introspection-devel python3-cairo python3-gobject-cairo python3-gobject-Gdk typelib-1_0-Gtk-3_0

.. _hmis-installation-vanilla:vanilla_installation-installation_of_the_gnu_health_client-gnu_health_client_installation_with_pip3:

GNU Health Client installation with pip3
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

* Update PATH. To make changes permanent, add this line in :code:`$HOME/.bashrc`

.. code-block:: shell
    :linenos:

    $ export PATH=$HOME/.local/bin:$PATH

* Update pip3

.. code-block:: shell
    :linenos:

    $ pip3 install --upgrade --user pip

* Install GNU Health client

.. code-block:: shell
    :linenos:

    $ pip3 install --user --upgrade gnuhealth-client


The following command will boot your GNU Health client:

.. code-block:: shell
    :linenos:

    gnuhealth-client

.. _hmis-installation-vanilla:vanilla_installation-installation_of_the_gnu_health_client-alternative_methods:

Alternative Methods
^^^^^^^^^^^^^^^^^^^
.. _hmis-installation-vanilla:vanilla_installation-installation_of_the_gnu_health_client-alternative_methods-system_packages:

System Packages
"""""""""""""""
Instead from source as described above, you can install the GNU Health Client from pre-build packages as well. 
openSUSE offer packages that you can install with your systems package manager. Make sure you get the current **gnuhealth-client version 4.0.x**

.. _hmis-installation-vanilla:vanilla_installation-installation_of_the_gnu_health_client-alternative_methods-microsoft_windows_and_macos:

Microsoft Windows and macOS
"""""""""""""""""""""""""""

.. note:: As GNU Health is free/libre software, developed primarily for free/libre operating systems and with the philosophy of free software in mind, it is recommended to use free/libre software with GNU Health, and GNU/Linux or other free/libre operating system for the client. The development of all GNU Health components (server, client, plugins, Thalamus, GNU Health Federation) is done and focused on Free / Libre  operating systems.

If you use Microsoft Windows or macOS, you can try using the Tryton 6.0 client, which may be compatible with GNU Health 4.0. Keep in mind that the windows client does not have the GNU Health commands, nor the plugins like GNU Health GNUPG crypto or GNU Health Camera and Federation Resource Locator.

`Download the Tryton client executable (Windows) <https://downloads.tryton.org/6.0/tryton-64bit-last.exe>`_ and follow the instructions.

.. _hmis-installation-vanilla:vanilla_installation-logging_into_the_application:

Logging into the Application
----------------------------

Now that you're back at the login screen, you'll notice that the selected profile is the one you've just created. Fill in the login form:

* User name: the one you used previously (usually :code:`admin`)
* Password: the one entered twice in the previous section

Login credentials for The Demo database: :ref:`demo_test-demodb:the_demo_database-online_community_servers-gnu_health_federation_community_hub-connection_to_the_gnu_health_hmis_and_lims`

.. _hmis-installation-vanilla:vanilla_installation-installing_the_default_modules:

Installing the Default Modules
------------------------------
From this point on, you will use the client for almost every process. Start with the installation of the basic functionality:

#. After you've created the database, the system will ask you to create some new users. You can skip this step for now.
#. You are then presented with a list of modules that will provide the functionality you desire. If you don't see the *Modules* window, navigate to it on the left side: *Administration → Modules → Modules*.
#. Select the :code:`health_profile` module, and click on **Mark for installation**.
#. Click on the **Action** icon (two cogwweels, previous versions used a blue rotated square) and select **Perform Pending Installation/Upgrade**:
#. Tryton will automatically select all the dependent modules required for the installation:
#. Click on **Start Upgrade**. This process will take a while, depending on the computer where GNU Health is being installed on. Once it's done, the following message appears.

.. _hmis-installation-vanilla:vanilla_installation-creating_a_company:

Creating a Company
------------------

The next thing you need to do is to create the initial company, that will be your health center. You will be presented with a wizard to create it.


Press :code:`F3` to create a new company.

.. note::
    At the party form, please make sure you **set the institution attribute**. You will link this company to your main health institution later on. Please refer to the screenshot provided in this section for details.


.. _hmis-installation-vanilla:vanilla_installation-disabling_demo_users_in_production_environments:

Disabling demo users in production environments
-----------------------------------------------

.. warning::
    For security reasons, you **must** deactivate demo users in production environments.

GNU Health comes with a set of pre-defined users for demo purposes. They all have the prefix :code:`demo_` (:code:`demo_doctor`, :code:`demo_front_desk`, :code:`demo_nurse`... ).

To deactivate the users:

#. Navigate to Administration > Users > Users in the sidebar.
#. In filters, choose :code:`Login: demo_` and :code:`Active: True`
#. Unset the "active" flag of each of them (untick the "Active" boxes). The demo users are now de-activated in your environment.


Look at the screenshot captioned *Deactivation of demo users in production environments* for an example (the Active checkboxes haven't been unticked).

.. _hmis-installation-vanilla:vanilla_installation-customizing_the_gnu_health_client:

Customizing the GNU Health Client
---------------------------------
For GNU/Linux and other free operating systems, the GNU Health GTK client configuration file can be found at:

.. code-block:: shell
    :linenos:


    $HOME/.config/gnuhealth/<VERSION>/gnuhealth-client.conf

For example:

.. code-block:: shell
    :linenos:


    $HOME/.config/gnuhealth/4.0/gnuhealth-client.conf



.. _hmis-installation-vanilla:vanilla_installation-customizing_the_gnu_health_client-using_a_custom_greeter_/_banner:

Using a custom greeter / banner
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

You can customize the login greeter banner to fit your institution.

In the section :code:`[client]`, include the banner parameter with the absolute path of the png file.

Something like:

.. code-block::
    :linenos:

    [client]
    banner = /home/yourlogin/myhospitalbanner.png

The default resolution of the banner is 500 x 128 pixels. Adjust yours to approximately this size.

.. _hmis-installation-vanilla:vanilla_installation-completion:

Completion
----------
Congratulations! You have completed the initial installation of GNU Health. In the next chapter we will discuss how to add functionality by installing additional modules.
