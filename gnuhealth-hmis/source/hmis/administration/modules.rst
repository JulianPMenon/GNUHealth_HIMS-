.. _hmis-administration-modules:modules:

Modules
=======
.. _hmis-administration-modules:modules-installing_extra_modules:

Installing Extra Modules
------------------------

The default modules of GNU Health are just a subset of the modules available and provide basic functionality. Depending on your health institution, you will most likely want to install some of the other modules that come with GNU Health.

.. _hmis-administration-modules:modules-installing_extra_modules-installation_process:

Installation Process
^^^^^^^^^^^^^^^^^^^^

.. todo:: Fill HMIS - Administration - Modules - Installation Process

.. _hmis-administration-modules:modules-installing_extra_modules-dependencies:

Dependencies
^^^^^^^^^^^^

Some modules are depending on other modules: You can not install this module without having installed the other modules as well. You can see these dependencies by double-clicking on a module in the *Administration → Modules → Modules* section.

For example: The module :code:`health_inpatient_calendar` (which adds caldav support to the inpatient management functionality) depends on :code:`health_inpatient` (which privides the basic inpatient management functionality) and :code:`calendar` (which implements the basic caldav functionality).

.. _hmis-administration-modules:modules-available_modules:

Available Modules
-----------------

GNU Health consists of the following modules:

* 	:code:`health`: This is the core module providing the basic functionality of GNU Health. See :ref:`basics-coremodule-index:the_core_module`.
* 	:code:`health_archives`: Functionality to store and track old or paper-based clinical records.
* 	:code:`health_calendar`: Calendar / caldav functionality.
* 	:code:`health_crypto`: Ensures confidentiality, integrity and non-repudiation in GNU Health. Allows digital signatures on prescriptions, patient evaluations, surgeries or lab tests. See :ref:`hmis-security:security`.
* 	:code:`health_genetics`: See :ref:`modulesindetail-genetics:genetics`.
* 	:code:`health_gyneco`: See :ref:`modulesindetail-gynecology:gynecology`.
* 	:code:`health_history`: Generates the patient clinical history reports.
* 	:code:`health_icd10`: WHO International Classification of Diseases.
* 	:code:`health_icd10pcs`: ICD-10 Procedure Coding System.
* 	:code:`health_icpm`: WHO International Classification of Procedures in Medicine.
* 	:code:`health_icu`: Functionality for Intensive Care Units. See :ref:`modulesindetail-icu:intensive_care_unit`.
* 	:code:`health_imaging`: Support for management of Diagnostic Imaging
* 	:code:`health_inpatient`: Functionality to manage inpatients (or hospitalizations). See :ref:`modulesindetail-inpatientmanagement:inpatient_management`.
* 	:code:`health_inpatient_calendar`: Adds caldav support for hospitalizations. See :ref:`modulesindetail-inpatientmanagement:inpatient_management`.
* 	:code:`health_lab`: See :ref:`healthcentermanagement-lims:laboratory_management`.
* 	:code:`health_lifestyle`: See :ref:`modulesindetail-lifestyle:lifestyle`.
* 	:code:`health_mdg6`: :wikipedia:`World Health Organization <WHO_Model_List_of_Essential_Medicines>` Millennium Development Goal 6. Functionality to fight Malaria, Tuberculosis and HIV/AIDS.
* 	:code:`health_ntd`: See :ref:`modulesindetail-neglectedtropicaldiseases:neglected_tropical_diseases`.
* 	:code:`health_ntd_chagas`: Implements functionality for the Chagas disease. See :wikipedia:`Neglected Tropical Diseases <Neglected_Tropical_Diseases>`.
* 	:code:`health_ntd_dengue`: Implements functionality for the denge fever. See :wikipedia:`Neglected Tropical Diseases <Neglected_Tropical_Diseases>`.
* 	:code:`health_nursing`: Procedures, roundings and inpatient / outpatient care. See :ref:`modulesindetail-nursing:nursing`.
* 	:code:`health_pediatrics`: See :ref:`modulesindetail-pediatric:pediatric`.
* 	:code:`health_pediatrics_growth_charts`: Charts and reports to evaluate the child growth.
* 	:code:`health_pediatrics_growth_charts_who`: WHO child development / growth tables.
* 	:code:`health_profile` : Template to load common modules (deprecated).
* 	:code:`health_qrcodes`: Permits identifying the patient and the newborns with 2-dimensional Quick-Recognition codes.
* 	:code:`health_reporting`: Statistics on different indicators (diseases, doctor assignments, .. ). It also creates different charts
* 	:code:`health_services`: Registers all the services done to a patient, in an ambulatory or inpatient scenario. It will also generate invoices on selected services.
* 	:code:`health_socioeconomics`: See :ref:`modulesindetail-socioeconomics:socioeconomics`.
* 	:code:`health_stock`: See :ref:`healthcentermanagement-stockmanagement:stock_management`.
* 	:code:`health_surgery`: See :ref:`modulesindetail-surgery:surgery`.
* 	:code:`health_synchro`: Implements the functionality to exchange data between several GNU Health installations.
* 	:code:`health_who_essential_medicines`: :wikipedia:`WHO essential medicines <WHO_Model_List_of_Essential_Medicines>`.
* 	:code:`health_iss`: Injury Surveillance System. Records and georeferences violent injuries, such as accidents, suicides, sexual assaults or robberies.

.. todo:: Update HMIS - Administration - Modules - Available Modules: health_synchro does not exist, some are missing

.. _hmis-administration-modules:modules-custom_modules:

Custom Modules
--------------

If you are a software developer, you can customize existing modules or develop your own custom modules according to the needs of your health institution. For more information, please refer to the section :ref:`hmis-contributing:contributing-coding-customizing_and_creating_your_own_modules`.

The next chapters will guide you through the customization of GNU Health to meet your health center needs.
