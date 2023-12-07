.. _hmis-contributing:contributing:

Contributing
============
.. _hmis-contributing:contributing-contributors_wanted!:

Contributors Wanted!
--------------------

GNU Health is a :abbr:`FLOSS (Free/Libre/Open-Source Software)` project, you are very welcome to contribute to it. There are several ways to do so, most of which not requiring you to know how to code!

.. _hmis-contributing:contributing-translating_the_software:

Translating the Software
------------------------

Providing GNU Health in a user's native language is a big part of the success. You can help by improving existing translations, or creating a new translation in your own language. Translating GNU Health is easy, it does not require technical knowledge, and is all done via a web interface. Have a look at the :ref:`hmis-administration-localization:localization` page for more details on the process.

.. _hmis-contributing:contributing-writing_and_translating_the_documentation:

Writing and Translating the Documentation
-----------------------------------------

The GNU Health documentation on Wikibooks (which you are reading right now) is not complete, and it needs adjustments or additions with every GNU Health upgrade.

And if you don't want to write documentation, you can still contribute by translating it into your language to make it easier for health professionals to work with GNU Health.

.. _hmis-contributing:contributing-reporting_bugs:

Reporting Bugs
--------------

Unfortunately almost any software contains bugs. While we are actively working on fixing them so you don't have to struggle, please do report any bug or anomaly that you encounter.

Reporting a bug does not take much time. It is done via `Savannah <https://savannah.gnu.org/bugs/?group=health>`__.

Tip: For faster resolution, please include a description of the steps you performed to get to the bug, and if possible include screenshots of the issue. But be careful: '''Don't include patient information in the screenshots or your description!'''

.. _hmis-contributing:contributing-coding:

Coding
------

GNU Health is mostly a set of `Tryton <http://www.tryton.org/>`__ modules, the programming language used is `Python <http://python.org/>`__. The code is hosted on `Savannah <https://savannah.gnu.org/hg/?group=health>`__ and versioned under `Mercurial <http://mercurial.selenic.com/>`__.

.. _hmis-contributing:contributing-coding-obtaining_your_copy_of_the_code:

Obtaining Your Copy of the Code
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

You can get your copy of the latest code by doing an anonymous checkout:

.. code-block:: shell
        :linenos:


        hg clone http://hg.savannah.gnu.org/hgweb/health/

You can also `browse the code online <http://hg.savannah.gnu.org/hgweb/health/>`__.

.. _hmis-contributing:contributing-coding-coding_style:

Coding style
^^^^^^^^^^^^

The coding style should follow the Tryton `guidelines <https://code.google.com/p/tryton/wiki/CodingGuidelines>`__ or else Python best `practices <https://www.python.org/dev/peps/pep-0008/>`__.

.. _hmis-contributing:contributing-coding-customizing_and_creating_your_own_modules:

Customizing and Creating Your Own Modules
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Chances are that if you are installing GNU Health for your center, you will be customizing it to meet your specific needs. Reports, access control rules and views are just some of the objects that are normally customized. The main concept is to **not edit the standard code or modules**, since it will be overwritten in the next update and most probably will end up in a broken system.

The recommended steps to customize GNU Health to your center are:

#. **Create your module**: It's recommended that you use the following naming convention for your local modules: :code:`z_health_<modulename>`. For example, if your project is called *catalina*, your local module name would be :code:`z_health_catalina`. This way makes is easy to detect and differentiate your modules from the base code. You can also easily make backup of them following the pattern.
#. **Inherit the objects.**
#. **Modify or create new models.**

If you create a new custom field, you should also use the :code:`z_<fieldname>` naming convention. This avoids collision with future field names of the official releases. We will not use any module, class, or model name starting with :code:`z_`.

.. _hmis-contributing:contributing-coding-customizing_and_creating_your_own_modules-the_"local"_modules_directory:

The "local" modules directory
"""""""""""""""""""""""""""""

There is a directory called **local** under :code:`~/gnuhealth/tryton/server/modules`. Please put your local modules that contain the customizations for your project under this directory. When using this approach, it makes sure that the update procedure does not overwrite your packages.

Also, sometimes you might want to include another existing package from Tryton or the community. This local modules directory is the place to place them.

Please note that can only support those packages that are included on each GNU Health HMIS distribution.

.. _hmis-contributing:contributing-coding-submitting_patches:

Submitting Patches
^^^^^^^^^^^^^^^^^^

Regular contributors have write access to the code repository. However, if you're just starting out, we want to make sure that your changes get reviewed. The way to do this is to `open a bug <https://savannah.gnu.org/bugs/?group=health>`_ describing the issue you've fixed or the feature you've added, and to attach a patch to that bug report. One of the developers will review your patch and commit it to the main development branch if approved.
