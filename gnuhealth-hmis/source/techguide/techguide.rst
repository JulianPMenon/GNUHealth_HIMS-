.. _techguide-techguide:federation_technical_guide:

Federation Technical Guide
==========================
.. _techguide-techguide:federation_technical_guide-introduction:

Introduction
------------
In this chapter we will go through the technical aspects behind the GNU Health Federation.

The GNU Health Federation has three main components

* Nodes
* Message Server
* Health Information System / Person Master Index

The HMIS node installation and configuration has already been described in previous chapters. In this chapter we will mainly focus on the Health Information System and the Message / Authentication server (Thalamus).


.. warning::
        In this chapter we show users and passwords as examples. **Never use these passwords** in production.

.. _techguide-techguide:federation_technical_guide-health_information_system_server_(his)_configuration:

Health Information System Server (HIS) configuration
----------------------------------------------------
The Person Master Index and Health Information System are both included in the HIS component of the GNU Health Federation.

.. _techguide-techguide:federation_technical_guide-thalamus_configuration:

Thalamus configuration
----------------------
The Thalamus project provides a RESTful API hub to all the GNU Health Federation nodes. The main functions are:

#. **Message server**: A concentrator and message relay from and to the participating nodes in the GNU Health Federation and the GNU Health Information System. Some of the participating nodes include the GNU Health HMIS,  mobile PHR applications, laboratories, research institutions and civil offices.
#. **Authentication Server**: Thalamus also serves as an authentication and authorization server to interact with the GNUHealth Information System


.. _techguide-techguide:federation_technical_guide-thalamus_configuration-technology:

Technology
^^^^^^^^^^
RESTful API: Thalamus uses a REST (Representional State Transfer) architectural style, powered by Flask technology

Thalamus will perform CRUD (Create, Read, Update, Delete) operations. They will be achieved via the following methods upon resources and their instances.

* **GET** : Read
* **POST** : Create
* **PATCH** : Update
* **DELETE** : Delete.

The DELETE operations will be minimal.

JSON: The information will be encoded in JSON format.

.. _techguide-techguide:federation_technical_guide-thalamus_configuration-create_a_new_user_thalamus_with_postgresql_permissions:

Create a new user thalamus with PostgreSQL permissions
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

* Install PostgreSQL
* Locate the pg_hba.conf file and add the following line:

.. code-block::
        :linenos:


        local all all trust

If you don't find the file refer to :ref:`Verify PostgreSQL authentication method <hmis-installation-vanilla:vanilla_installation-installing_gnu_health_on_gnu/linux_and_freebsd-verify_postgresql_authentication_method>`
* Restart PostgreSQL:

.. code-block:: shell
        :linenos:

     
        $ sudo systemctl restart postgresql.service
        
* Give permissions to the newly created *thalamus user*:

.. code-block:: shell
        :linenos:

     
        $ sudo su - postgres -c "createuser --createdb --no-createrole --no-superuser thalamus"

.. _techguide-techguide:federation_technical_guide-thalamus_configuration-installing_thalamus:

Installing Thalamus
^^^^^^^^^^^^^^^^^^^
Thalamus is a flask application, and is pip installable. Using the *thalamus* operating system user, install Thalamus server locally.

.. code-block:: shell
        :linenos:

     
        $ pip3 install --user wheel
        $ pip3 install --user thalamus
        $ pip3 install --user flask-cors

.. _techguide-techguide:federation_technical_guide-thalamus_configuration-initializing_postgresql_for_the_his_and_person_master_index:

Initializing PostgreSQL for the HIS and Person Master Index
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

The following documentation applies to a demo / test database, that we will call "federation"

#. **Create the database**

.. code-block:: shell
        :linenos:

     
        $ createdb federation

#. **Locate thalamus**

.. code-block:: shell
        :linenos:

     
        $ pip3 show thalamus
        $ cd /path/thalamus/demo/

#. **Create the Federation HIS schema**
Inside the "demo" directory in Thalamus execute the following SQL script

.. code-block:: shell
        :linenos:

     
        $ psql -d federation < federation_schema.sql

#. **Set the PostgreSQL URI for demo data**
In :code:`import_pg.py` adjust the variable :code:`PG_URI` to fit your needs. It could be sufficient to just put :code:`dbname='federation'` into :code:`psycopg2.connect(...)` if your setup fits the default settings.

#. **Initialize the Federation Demo database**

.. code-block:: shell
        :linenos:

     
        $ bash ./populate.sh

#. **Set the PostgreSQL URI for runtime**

Just like in the second step either modify :code:`POSTGRESQL_URI` in :code:`etc/thalamus.cfg` or modify :code:`psycopg2.connect(...)` directly in :code:`thalamus.py` (not in the demo directory).

At this point you can run and test Thalamus directly from the Flask Werkzeug server,:

.. code-block:: shell
        :linenos:

     
        $ python3 ./thalamus.py

This is ok for development and testing environments, but for production sites, always run Thalamus from a WSGI container, as described in the next section. 

.. _techguide-techguide:federation_technical_guide-thalamus_configuration-running_thalamus_from_a_wsgi_container:

Running Thalamus from a WSGI Container
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
In production settings, for performance reasons you should use a HTTP server. 
You will find examples on running Thalamus from **uWSGI** and **gunicorn**. 

.. _techguide-techguide:federation_technical_guide-thalamus_configuration-running_thalamus_from_a_wsgi_container-running_thalamus_from_uwsgi:

Running Thalamus from uWSGI
"""""""""""""""""""""""""""
uWSGI is a very robust and fast application that is used as a Web Server Gateway Interface in the context of Thalamus, to forward requests to Thalamus coming from other applications (eg, the Federation Portal or the HMIS node).

First of all install uWSGI and its plugins for HTTP & Python your operating system. For example on Ubuntu:

.. code-block:: shell
        :linenos:

     
        $ sudo apt install uwsgi uwsgi-plugin-router-access uwsgi-plugin-python3

We have included a uwsgi sample configuration file (etc/thalamus_uwsgi.ini). In order to test uWSGI with HTTP change it into the following:

.. code-block::
        :linenos:

        
        [uwsgi]
        master = 1
        #. https = 0.0.0.0:8443,/opt/gnuhealth/certs/gnuhealthfed.crt,/opt/gnuhealth/certs/gnuhealthfed.key
        http = 0.0.0.0:8080
        wsgi-file = thalamus.py 
        callable = app 
        processes = 4 
        threads = 2 
        block-size = 32000 
        stats = 127.0.0.1:9191
        plugins = http,python

To execute Thalamus with the default configuration file:

.. code-block:: shell
        :linenos:

     
        $ uwsgi --ini etc/thalamus_uwsgi.ini

All these arguments can also be passed to the command line.

.. _techguide-techguide:federation_technical_guide-thalamus_configuration-running_thalamus_from_a_wsgi_container-running_thalamus_from_gunicorn:

Running Thalamus from Gunicorn
""""""""""""""""""""""""""""""
Note: There are some issues with delay on requests and closing connections when using SSL from the vueJS portal on gunicorn.

Gunicorn supports WSGI natively and it comes as Python package. We have included a simple, default config file (:code:`etc/gunicorn.cfg`) to run Thalamus from Gunicorn with SSL enabled.

For example, you can run the Thalamus application from Gunicorn as follows. The default configuration file uses secure (SSL) connections:

.. code-block:: shell
        :linenos:

     
        $ gunicorn --config etc/gunicorn.cfg thalamus:app

.. _techguide-techguide:federation_technical_guide-thalamus_configuration-enable_ssl_for_encrypted_communication:

Enable SSL for encrypted communication
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Either get an official certificate or generate a self-signed certificate and private key

.. code-block:: shell
        :linenos:

     
        $ sudo openssl req -newkey rsa:2048 -new -x509 -days 3650 -nodes -out gnuhealthfed.crt -keyout gnuhealthfed.key

If uWSGI should handle HTTPS, place the certificate (:code:`gnuhealthfed.crt`) and private key (:code:`gnuhealthfed.key`) in a directory where the *thalamus* user has read permissions. Afterwards change etc/thalamus_uwsgi from HTTP to HTTPS using the correct paths.
Keep a backup of them in a safe place.

Alternatively keep uWSGI as internal HTTP server and configure a HTTPS reverse proxy. Using apache2 you can create a file thalamus.conf as site with the following content:

.. code-block::
        :linenos:

     
        <IfModule mod_ssl.c>
        <VirtualHost *:443>
        SSLEngine on
        SSLCertificateFile /etc/ssl/certs/gnuhealthfed.crt
        SSLCertificateKeyFile /etc/ssl/private/gnuhealthfed.key
        ServerName domain
        ProxyPass / http://your_host:8080/
        ProxyPassReverse / http://your_host:8080/
        </VirtualHost>
        </IfModule>

Depending on the operating system place this inside :code:`/etc/apache2/vhosts.d/` (openSUSE) or :code:`/etc/apache2/sites-available/` (Debian/Ubuntu). For the last case enable it afterwards using the *a2ensite* command. Finally enable some modules and restart apache:

.. code-block:: shell
        :linenos:

     
        $ sudo a2enmod headers ssl proxy proxy_http
        $ sudo systemctl restart apache2.service

.. _techguide-techguide:federation_technical_guide-thalamus_configuration-create_a_systemd_service:

Create a systemd service
^^^^^^^^^^^^^^^^^^^^^^^^
In order to control Thalamus with systemctl and enable it to be activated after startup create a service file thalamus.service with the following content:

.. code-block::
        :linenos:

     
        [Unit]
        Description=Thalamus Server
        After=network.target
        
        [Service]
        User=thalamus
        WorkingDirectory=/path/thalamus 
        ExecStart=uwsgi --ini etc/thalamus_uwsgi.ini
        Restart=on-abort 
        Type=notify
        KillSignal=SIGQUIT
        StandardError=syslog

        [Install]
        WantedBy=multi-user.target 

For the working directory take the path from above for the pip directory.
Put this in the appropriate directory for your operating system: For example :code:`/etc/systemd/system/` on Debian/Ubuntu or :code:`/usr/lib/systemd/system/` on openSUSE. Afterwards start and enable the service:

.. code-block:: shell
        :linenos:

     
        $ sudo systemctl start thalamus.service
        $ sudo systemctl enable thalamus.service


.. _techguide-techguide:federation_technical_guide-thalamus_configuration-using_a_virtual_environment:

Using a virtual environment
^^^^^^^^^^^^^^^^^^^^^^^^^^^
If you want to use a virtual environment create and activate the virtual environment before installing Thalamus:

.. code-block:: shell
        :linenos:

     
        python3 -m venv /home/thalamus/venv
        source /home/thalamus/venv/bin/activate

Besides add the following line to :code:`etc/thalamus_uwsgi.ini`:

.. code-block:: shell
        :linenos:

     
        venv = /home/thalamus/venv/

.. _techguide-techguide:federation_technical_guide-access_control:

Access Control
--------------
Thalamus uses a “role” approach related to Authorization. It’s basic, yet versatile.

Each role has the following methods permissions: GET, PATCH, POST, DELETE

The permissions work at *endpoint* level. Examples of endpoints are "person" or "page" of life.

Following there is sample of the “roles.cfg” file, which shows three main roles:  :code:`end_user`, :code:`health_professional` and :code:`root`.

.. code-block:: javascript
        :linenos:

     
        [
                {
                "role": "end_user", 
                "permissions": {
                        "GET": ["person", "book","page","password"],
                        "PATCH": ["person","page"],
                        "POST": ["page", "password"],
                        "DELETE": [],
                        "global": "False"
                        }
                },

                {
                "role": "health_professional",
                "permissions": {
                        "GET": ["people","person","book","page"],
                        "PATCH": ["person", "page"],
                        "POST": ["person", "page"],
                        "DELETE": [],
                        "global": "True"
                        }
                },

                {
                "role": "root",
                "permissions": {
                        "GET": ["people","person","book", "page","password"],
                        "PATCH": ["person","page"],
                        "POST": ["person","page",  "password"],
                        "DELETE": ["person","page"],
                        "global": "True"
                        }
                }
        ]

Once the user has provided the right credentials, she / he will have the access level to the documents associated to the roles. A user can have one or multiple roles. For example, a health professional usually belongs to two groups:

* *person* : she create and read her documents, change her password, etc. Usually her domain is restricted to herself. She can not act on others documents

* *health_professional* : She can see her patient medical history, but she can not change her password.

If you executed :code:`populate.sh` you can use the user/password combination ITAPYT999HON:gnusolidario to test the connection.
