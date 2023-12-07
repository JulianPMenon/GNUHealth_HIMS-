.. _demo_test-demodb:the_demo_database:

The Demo database
=================

.. _demo_test-demodb:the_demo_database-introduction_to_the_demo_database:

Introduction to the Demo Database
---------------------------------

GNU Health default installation comes with no data. It's interesting, for academic and training purposes to have some demo data that exemplifies concepts and improves the learning curve.

The demo database is an ongoing project and it will be adapting to the each new GNU Health version. The clinical history will also grow with time.

For consistency sake, it's important to have the main characters information constant (family members name, birth dates and place, health centers, family doctors etc.). The information and characters are fictitious and we should try to make it valid for different cultures.

.. _demo_test-demodb:the_demo_database-the_zenon-betz_family:

The Zenon-Betz Family
---------------------

The story goes around the Betz family, and the main character, Ana Betz, a primary school teacher. 

* Health Center: GNU Solidario Hospital in Las Palmas, Spain 
* Family Doctor: Cameron Cordara

	* ID: 765870
	* Speciality: Family Medicine
	* Institution: GNU Solidario Hospital
* Family: Zenon-Betz family

	* John Zenon (SSN: 40556644)
	* **Ana Betz (Fed ID: ESPGNU777ORG)** born October 4th, 1985, the main character
	* Matt (SSN: 97234436), born March 15th 2010, their son

.. _demo_test-demodb:the_demo_database-the_zenon-betz_family-demographics_information:

Demographics Information
^^^^^^^^^^^^^^^^^^^^^^^^

* Sex: Female
* Marital Status: Married
* Profession: School teacher
* Education Level: University
* Domiciliary Unit  

	* Housing Conditions: Comfortable and good sanitary conditions

.. _demo_test-demodb:the_demo_database-the_zenon-betz_family-patient_information:

Patient Information
^^^^^^^^^^^^^^^^^^^

* Socio-Economic Status: Middle class
* Allergies: β-lactam hypersensitivity
* Diseases: Type 1 Diabetes diagnosed on November 10th 1993
* Medication: Insulin since November 10th 1993
* Genetic Information

	* Family history  
	* Maternal Grandfather: Marfan's Syndrome (Q87.4)
	* Father: Essential (primary) hypertension (I10)
	* Disease Genes 
	* BRCA1: breast cancer 1, early onset

* Obstetric Information: G1P1A0

	* Newborn: Matt, epidural, vaginal birth 

* Lifestyle  

	* Ex-smoker
	* Addictions: No recreational drugs 
	* Sexuality: Heterosexual, monogamous, practices safe sex
	* Safety: Motorcycle rider, uses helmet

.. _demo_test-demodb:the_demo_database-the_zenon-betz_family-other_information:

Other Information
^^^^^^^^^^^^^^^^^

* Family information (Family functionality level, members, operational sectors...)
* Medical Imaging (X-rays, CTs, MRIs...)
* Genetic info / risks
* Lab orders and results
* Clinical history of the family

.. _demo_test-demodb:the_demo_database-online_community_servers:

Online Community Servers
------------------------

We have two main community servers available in the Internet so you can connect and try the latest GNU Health. This is probably the simplest way to check out GNU Health for the first time.

#. **federation.gnuhealth.org**: The GNU Health Federation community hub. Contains the latest stable version
#. **health.gnusolidario.org** : This server holds the **previous** stable version of GNU Health HMIS and LIMS servers (3.2)

.. _demo_test-demodb:the_demo_database-online_community_servers-gnu_health_federation_community_hub:

GNU Health Federation Community Hub
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

**federation.gnuhealth.org**: The GNU Health Federation community hub. Contains the latest stable version of the following components :

* Thalamus message server
* Health Information System and Person Master Index
* GNU Health HMIS and LIMS nodes
* GNU Health WebDAV server and calendaring system


The community Hospital Management demo server runs behind a web server (NGINX) and a WSGI server (UWSGI).

.. _demo_test-demodb:the_demo_database-online_community_servers-gnu_health_federation_community_hub-connection_to_the_gnu_health_hmis_and_lims:

Connection to the GNU Health HMIS and LIMS
""""""""""""""""""""""""""""""""""""""""""

#. Install the GNU Health client (GNU/Linux, FreeBSD or other *NIX*) Proceed as explained in the :ref:`GNU Health Client Installation section <hmis-installation-vanilla:vanilla_installation-installation_of_the_gnu_health_client>`
#. Use the following server and credentials . Please note that the Database name can change. You can use the "profile" to select the DB from the list 

.. hint::
        * **Server**: federation.gnuhealth.org</br> 
        * **Database**: health42rc2</br> 
        * **User name**: admin</br> 
        * **Password**: gnusolidario
	
        The community server uses the standard port 8000

.. note::
         The community server database resets itself everyday at 00:30 UTC , so we have clean demo data. That means that you can also play and experiment with it without fear of "breaking" the DB : .

.. note::
         Please **do not** change the language of the admin account! Instead, copy the admin account to a new account, e.g. admin_fr, and set this accounts language to the desired language!

.. _demo_test-demodb:the_demo_database-online_community_servers-gnu_health_federation_community_hub-connection_to_the_health_information_system_via_browser:

Connection to the Health Information System via Browser
"""""""""""""""""""""""""""""""""""""""""""""""""""""""
You can connect to the community hub using the web interface.
Please note that this is alpha and not intended for production systems yet.

https://federation.gnuhealth.org:8900

.. _demo_test-demodb:the_demo_database-online_community_servers-development_server:

Development server
^^^^^^^^^^^^^^^^^^

**For developers** : There is a developer database that runs on the latest development version. To connect to the developer community server, use port 9555, with the same credentials. Needless to say, the developer version is highly unstable, and is just for developers.

The Webdav server is at port 9080

.. _demo_test-demodb:the_demo_database-local_demo_database:

Local Demo Database
-------------------

This method should give the most up-to-date demo database.

As the gnuhealth user, use the GHealth demo DB installer script. You can download the latest version from GNUHealth at Savannah mercurial repository

( https://hg.savannah.gnu.org/hgweb/health/file/tip/tryton/scripts/demodb )

.. code-block:: shell
        :linenos:


        $ ./install_demo_database.sh 40

This will download the demo database of version 4.0.x . It will also create the database locally.

Now enter the database through the GNU Health client. For example, for 4.0.x releases:

* **Database:** ghdemo40
* **Username:** admin
* **Password:** gnusolidario

There is a user "admin_es" that uses the Spanish language.

You can browse the current demo databases, from our GH site download area:

https://www.gnuhealth.org/downloads/postgres_dumps/

.. hint::

        Remember that **databases with odd minor numbers (eg, 41) are unstable**. They are the development version of the upcoming release, and for dev / testing purposes.
