.. _hmis-patches:patches_and_patchsets:

Patches and Patchsets
=====================
.. _hmis-patches:patches_and_patchsets-about_gnu_health_patchsets:

About GNU Health Patchsets
--------------------------

Since version 2.2.1, patchsets will be released for the GNU Health stable versions (those with even minor number, e.g. 1. **2** .3 ).

Suppose the following scenario: The health center GNU SOLIDARIO HOSPITAL installs version 2.2.0. After some weeks of running the server in the production environment, a bug is discovered that affects the :code:`health_service` module. It's not a critical bug but it should be addressed shortly.

In the meantime, the bug has been reported and it has been fixed and documented. The system administrator at GNU SOLIDARIO HOSPITAL has two options:

#. Download and apply the individual patch using the patch tool.
#. Wait and apply the latest patchset.

It will be the context that will determine which method to use, but a general rule,Mercurial **unless you are in the context of a critical bug, you should use the patchset approach.**

Some general ideas:

* The patches and patchsets don't require to do the whole installation again. The scripts are usually small and the installation time is very short in general.
* The patchsets are valid for minor numbers (e.g. 2.0.x, 2.2.x).

Whenever a patchset is generated, a new GNU Health version is released, with the patchlevel number of the patchset.

.. _hmis-patches:patches_and_patchsets-patches_vs_patchsets:

Patches vs Patchsets
--------------------

This section discusses the general concepts behind a patch and a patchset, and when to use one or the other.

.. _hmis-patches:patches_and_patchsets-patches_vs_patchsets-patches:

Patches
^^^^^^^
 
Generally speaking, a patch is a portion of code that fixes a program or its components. In GNU Health, a patch is a "patch file" generated in a :wikipedia:`Mercurial <Mercurial>` specific :wikipedia:`Changeset <Changeset>` .The patch file (diff) modifies specific sections of code, not replacing the whole file. It is applied with the :wikipedia:`Patch <(Patch_(Unix)>` command. As stated before, the patch is associated to a specific changeset, but not necesarily to the latest patch-level number (third component of the version number, e.g. 1.2. **3**).

Pros of patches:

* They are available immediately: If it's a critical bug, you can patch it immediately, no need to wait for the patchset.
* Very specific: Because of this high specificity, many times you could apply a patch in GNU Health with a running system, not affecting the availability.

Cons of patches:

* Requires more technical knowledge
* Very specific 
* More cumbersome when dealing with binary files, like LibreOffice Reports 
* Need to keep track of other un-applied patches

The high specificity of the patch makes it both a pro and a con. So it's quite operator dependent. **We recommend avoid using patches unless is a critical bug that must be applied immediately.**

.. _hmis-patches:patches_and_patchsets-patches_vs_patchsets-patchsets:

Patchsets
^^^^^^^^^

Patchsets act at a higher level than patches, dealing with entire files and not chunks of code. They are packaged in the form of a compressed :wikipedia:`ŧar <Tar_(computing)>` file.

Applying a patchset is also a selective operation, in the sense that only part of the GNU Health kernel is modified. 

Pros of patchsets:

* Specific
* Can be re-applied after a patch
* Applies all patches in that time-frame, including non-critical patches that were collected over time
* Easier periodic installation / updates process
* Linked to a specific GNU Health version (the patchlevel number)

Cons of patchsets:

* Not as immediate as patches. Although the time for critical patches should not exceed 24 hours.

.. _hmis-patches:patches_and_patchsets-criteria_for_a_new_patchset_release:

Criteria for a New Patchset Release
-----------------------------------
 
#. Bugs marked as critical / blockers 
#. Important security issues
#. The number of non-critical bugs

.. _hmis-patches:patches_and_patchsets-applying_patchsets:

Applying Patchsets
------------------
|version3.0|

Since GNU Health 3.0, we have a new tool, the GNU Health Control Center. GNU Health control center facilitates common administration tasks, such as backups or system updates.
To check the status of your Tryton and GNU Health kernel and modules, as well as to keep your system uptodate, please visit the section :ref:`hmis-controlcenter:the_gnu_health_control_center`

Go to :ref:`hmis-controlcenter:the_gnu_health_control_center` for the documentation on how to install the patchsets.

.. _hmis-patches:patches_and_patchsets-applying_patchsets_manually_(unsupported):

Applying Patchsets manually (Unsupported)
-----------------------------------------

The following method allows you to apply the patchset into a standard GNU Health installation, without using the official tool (gnuhealth-control). The manual installation does not check for the latest Tryton updates, is more complicated and should not be used. Please use :ref:`hmis-controlcenter:the_gnu_health_control_center` unless you know what you're doing.

.. warning::
        GNU Health does not support this method

* Read the instructions related to the patchset in Savannah. Depending on the patch you might need to update the module(s).  
* Stop the GNU Health instance. 
* Backup your kernel and database (always, no matter how small is the patch).
* Log in using the **gnuhealth** account.
* **Don't change directories.** Stay at your $HOME. Verify that you are in the :code:`/home/gnuhealth`.
* Download the latest patchset for your Major.minor number. For example, if you are in version 3.0.x:

.. code-block:: shell
        :linenos:


        wget http://ftp.gnu.org/gnu/health/gnuhealth_patchset-3.0.latest.tar.gz

* Uncompress the patchset:

.. code-block:: shell
        :linenos:


        tar -xzvf gnuhealth_patchset-3.0.latest.tar.gz
        
* Restart the server.
