.. _hmis-security:security:

Security
========
.. _hmis-security:security-securing_your_gnu_health_environment:

Securing Your GNU Health Environment
------------------------------------

Security is a multi disciplinary task, involving components from networking, operating system, database and application (Tryton), to human resources, to name a few.

This page will try to give an overview of some basic concepts that will help you to enhance the access control to your system. We will also talk about enabling :wikipedia:`Public-key cryptography` to sign documents and records from different models.

.. warning::
        By no means this introductory page will replace the advice of computer security specialists for your specific installation

.. _hmis-security:security-gnu_health_security_advisories:

GNU Health Security Advisories
------------------------------

GNU Health releases Security Advisories (SA) anytime a vulnerability is found. The security advisory format is inspired on FreeBSD.

The GNU Health security advisories are sent to all subscribers in the "health-security" mailing list. See the "Resources" chapter to subscribe.

You can check the current security advisory list in https://ftp.gnu.org/gnu/health/security/security_advisories.html


.. _hmis-security:security-access_control:

Access Control
--------------

.. _hmis-security:security-access_control-default_server_ports:

Default server Ports
^^^^^^^^^^^^^^^^^^^^

The Tryton server JSON-RPC listens by default in port 8000. It's a advisable to change to another port in production environments.

The server super user encrypted password has been updated, in the corresponding section of the trytond.conf file. Here is a sample of such file

.. code-block::
        :linenos:


        [database]
        uri = postgresql://localhost:5432
        path = /home/gnuhealth/attach
        [session]
        '''super_pwd = JonB./CoLl8F6'''

.. _hmis-security:security-disable_demo_users_in_production_environments:

Disable demo users in Production environments
---------------------------------------------

.. warning::
         For security reasons, deactivate demo users in production environments

GNU Health comes with a set of pre-defined users for demo purposes. They all have the suffix :code:`demo_` ( :code:`demo_doctor`, :code:`demo_front_desk`, :code:`demo_nurse`... ).

Please deactivate them in production environments.

To deactivate the users, follow the following path :
Administration → Users → Users


In filters, you can choose : 
login name : :code:`demo_`

Unset the "active" flag of each of them. The demo users are now de-activated in your environment.

.. _hmis-security:security-public-key_cryptography_in_gnu_health:

Public-key Cryptography in GNU Health
-------------------------------------

.. _hmis-security:security-public-key_cryptography_in_gnu_health-gnu_health_cryptographic_module:

GNU Health Cryptographic Module
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

The module goal is to achieve the concepts of confidentiality, integrity and non-repudiation in GNU Health.

The :code:`health_crypto` module currently provides the following functionality:

* Document Serialization
* Document hashing (MD)
* Document signing
* Document verification

The module will work on records from models that will need this functionality such as prescription, patient evaluations, surgeries or lab tests.

The Serialization includes the information in a predefined format (JSON) and encoding (UTF8).

There will be a field that will contain the Message digest of the serialization process, and that will check for any changes. If the case of alteration of any fields 

The signing process will be upon that Message Digest field, whereas the encryption process will work on row or column level.

Public-key / asymmetric cryptography will be used for signing the documents.


The standard models that are included are Prescription, Birth Certificate and Death Certificate.  Of course, you can apply the functionality to any model that you feel like is necessary. In addition, and based on the community requests, we will incorporate new models in the next versions.

.. _hmis-security:security-public-key_cryptography_in_gnu_health-using_digital_signatures_in_gnu_health:

Using Digital Signatures in GNU Health
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^



GNU Health works along with :wikipedia:`GNU Privacy Guard` for **digitally signing and verifying documents**. Please refer to the :ref:`plugins-gnuhealthplugins:gnu_health_plugins` section for the installation

.. _hmis-security:security-reporting_a_security_vulnerability:

Reporting a security vulnerability
----------------------------------
We take security very seriously, and we appreciate your help on this !

If you believe you have found a vulnerability in GNU Health, please send an email to security@gnuhealth.org
