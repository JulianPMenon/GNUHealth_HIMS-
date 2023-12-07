.. _modulesindetail-imaging:imaging:

Imaging
=======

.. _modulesindetail-imaging:imaging-default_imaging_module:

Default imaging module
----------------------

The default GNU Health imaging module (health_imaging) provides basic imaging support and workflow. Only basic, non-DICOM images are supported. **No DICOM viewer is provided**.

.. _modulesindetail-imaging:imaging-default_imaging_module-creating_a_request:

Creating a request
^^^^^^^^^^^^^^^^^^

#. Create draft request

        * Wizard under Imaging → Dx Imaging - New''  
        * Fill in: 

                * Patient
	        * Urgent or not
	        * Specific test(s)
	        * Requesting doctor
        * Click *Request*
#. Generate order 
        * Find draft requests under *Imaging → Dx Imaging - New → Draft*
        * Click *Request* button on the draft request in the detailed view
        
        	* Request will now be under the *Requested* tab

.. _modulesindetail-imaging:imaging-default_imaging_module-generating_results:

Generating results
^^^^^^^^^^^^^^^^^^

#. Click *Generate Results* button on the form (under *Dx Imaging Requests*)
#. Fill in data (available under the *Dx Imaging - Results* menu item)

        * Add images under the *Images* tab
        * Add comments under the *Comment* tab

.. _modulesindetail-imaging:imaging-default_imaging_module-view_results:

View results
^^^^^^^^^^^^

Results are found under the *Imaging → Dx Imaging - Results* menu item. 

.. _modulesindetail-imaging:imaging-default_imaging_module-configuring_available_tests:

Configuring available tests
^^^^^^^^^^^^^^^^^^^^^^^^^^^

Available tests can be configured under the *Configuration → Dx Imaging* menu item.

There are two sub-sections:

* Dx Imaging Test Types (MRI, Ultrasound, etc)
* Dx Imaging Tests (available tests)

.. _modulesindetail-imaging:imaging-orthanc_integration:

Orthanc Integration
-------------------

.. _modulesindetail-imaging:imaging-orthanc_integration-introduction:

Introduction
^^^^^^^^^^^^

This module (health_orthanc) provides a light integration between Orthanc DICOM servers and GNU Health. The module uses the robust REST API provided by Orthanc to synchronize patient and study information in GNU Health. Put simply, the code asks the Orthanc REST API what studies and patients it has and then saves that information locally in GNU Health. **No image files are saved. No DICOM viewer provided.**

.. _modulesindetail-imaging:imaging-orthanc_integration-usage:

Usage
^^^^^

A new dropdown menu titled *Orthanc* is available under *Health → Imaging*.


The menu has 2 sub-sections:

* Patients
* Studies

These sub-sections provide the list of studies and patients on the known Orthanc servers. You can filter and search normally. The views are generally read-only. On the list of Orthanc patients, however, some patients will be linked to local patients if the remote and local MRN/PUID match. Otherwise, Orthanc patients can be manually linked to a local patient by updating their patient field.

.. note:: 
        
        When an imaging request is completed, the result can be directly linked to Orthanc studies through the new *Studies* tab under the *Imaging → Dx Imaging - Results* entry.

.. _modulesindetail-imaging:imaging-orthanc_integration-administration:

Administration
^^^^^^^^^^^^^^

.. _modulesindetail-imaging:imaging-orthanc_integration-administration-server_configuration:

Server configuration
""""""""""""""""""""

A new dropdown menu titled *Orthanc* is available under *Health → Configuration*


The menu has 2 sub-sections:

* Add Orthanc Server
* Servers

To add a new remote server click *Add Orthanc Server*. This will open a wizard that guides the user through adding a server:


* Fill in the label (must be unique), full domain, username, and password.
* Click *Begin*

After a short time, a success message should appear.


In case of invalid domains or credentials, there will be an error page instead of a success page.


The *Servers* page lists the current servers. Clicking on a specific server will show its credentials, validated status, and other important information. Of note, updating the domain, username, or password will trigger a background, remote check to validate the newly updated information.


.. _modulesindetail-imaging:imaging-orthanc_integration-administration-synchronization:

Synchronization
"""""""""""""""

The module provides a trytond-cron job which by default synchronizes all validated servers every 15 minutes. This can be changed through the *Scheduled Actions* configuration under *Administration → Scheduler*.



Servers can by manually synchronized by clicking the *Sync* button on their individual view.


.. _modulesindetail-imaging:imaging-orthanc_integration-troubleshooting:

Troubleshooting
^^^^^^^^^^^^^^^

.. _modulesindetail-imaging:imaging-orthanc_integration-troubleshooting-server(s)_not_automatically_synchronizing:

Server(s) not automatically synchronizing
"""""""""""""""""""""""""""""""""""""""""

Make sure trytond-cron is running.