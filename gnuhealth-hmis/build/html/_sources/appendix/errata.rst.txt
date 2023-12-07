.. _appendix-errata:errata:

Errata
======
In GNU Health we strive to have a system free of bugs and issues, but we know that is not possible :)

This chapter addresses those issues that may impair the installation or upgrade process.

.. _appendix-errata:errata-3.6:

3.6
---
**Context**: Installation (gnuhealth-setup)

**Issue** : GNU Health installer needs to be updated due to incompatibility of Werkzeug 1.0 with Trytond Kernel 5.0<br>

**Solution**:<br>

 Make sure you complete the step of downloading and installing the latest gnuhealth-setup as described in the installation documentation.
 The gnuhealth-setup version must be 3.6.2 or later.

 .. code-block:: shell
        :linenos:


        $ gnuhealth-setup version

.. _appendix-errata:errata-3.4:

3.4
---
**Context**: Upgrade process

**Issue:** Error when migrating the product templates and/or categories.

**Solution**: 

#. Run the script :code:`upgrade_34.sql` as documented in the upgrade process for 3.4
#. Execute the following SQL commands, as indicated in the Tryton migration

.. code-block:: shell
        :linenos:

     
        delete from ir_property where res like 'product.category,%' and SUBSTRING(res, POSITION(',' IN res) + 1)::integer not in (select id from product_category);

.. code-block:: shell
        :linenos:

     
        delete from ir_property where res like 'product.template,%' and SUBSTRING(res, POSITION(',' IN res) + 1)::integer not in (select id from product_template);