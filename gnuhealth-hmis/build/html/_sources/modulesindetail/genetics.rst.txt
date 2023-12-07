.. _modulesindetail-genetics:genetics:

Genetics
========

.. _modulesindetail-genetics:genetics-overview:

Overview
--------


One goal of genetic research is to identify genes related to human health and disease, and understand how these genes are influenced by a person's environment and lifestyle. 

GNU Health genetic related packages integrate hereditary risks, family history and individual relevant genetic information. GNU Health aims to improve people's health by using the best approach to an individual including, combining and adjusting his / her lifestyle, nutrition, and other external factors with the person's unique genetic information.  We also want to build the bridge between the clinician and the research community. 

GNU Health genetic functionality brings together both the molecular and environmental bases of many health conditions, foundation for precision medicine.

GNU Health incorporates information from **The National Center for Biotechnology Information** :wikipedia:`NCBI` as well as from **the** :wikipedia:`UniProt` **Consortium** protein-related human health conditions and natural variants.

.. _modulesindetail-genetics:genetics-genetic_information:

Genetic Information
-------------------

For each individual, GNU Health stores the details on each of the genes / proteins that might be involved on a person health condition. 
This information can be accessed from the "Genetics" tab on the patient main form.

* **Gene / Protein involved** : Information about the gene. The gene code, official long name, chromosome and locus. It also provides information about the protein encoded and the link to UniProt protein code. On this example, the BRCA1 gene is associated to the protein code P38398, which can be reached directly from GNU Health clicking on the Protein URI.
* **Natural Variant** : The specific change at amino acid level that might make the person susceptible to a health condition. In the example above, the natural variant code is :code:`VAR_007766`, with a change of Tyrosine by Aspartic acid, at position 465 on the protein encoded by the BRCA1 gene.
* **Phenotype** : This field is used **only** if the person shows clinical signs associated to the expression of that gene / protein variant. 
* **Onset** : Age (expressed in years) when the first clinical signs where reported
* **Notes** : Comments contextualized to the individual.

Most of the time, single natural variants do not result in disease. The health professional must take in consideration other factors of the individual (annotated in GNU health) that have an impact on her or his health, such as living conditions, nutrition or lifestyle. Biology plays a role on our health, but even more important to one's health are the environmental, external factors. The combination of biology and environment is the right way to approach personalized medicine.

.. _modulesindetail-genetics:genetics-family_history:

Family History
--------------
Gathering a complete and accurate family medical history is becoming more important as genetic medicine explains more diseases. As genes are passed down from generation to generation, medical conditions and diseases, or the increased risk for disease, tend to run in families due to gene abnormalities. Researchers and Health professionals now better understand how irregular genes are passed from one generation to the next and have an increased ability to test for hundreds of inherited illnesses.

GNU Health shows extra info related to diseases including the name, code and main disease category, genetic data and a free text box for adding relevant extra info.

.. _modulesindetail-genetics:genetics-protein_related_diseases:

Protein Related Diseases
------------------------

GNU Health helps you searching the disease gene through a very useful searching filter with different categories such as affected chromosome, dominance, official long name and official symbol.

.. _modulesindetail-genetics:genetics-protein_related_diseases-natural_variants:

Natural Variants
^^^^^^^^^^^^^^^^

GNU Health has selected the relevant mutations that might be involved in health conditions. These natural variants are mapped to UniProt list of protein related diseases. Some of the fields on each Protein natural variant are :

* Gene involved
* Change in amino acid 
* Phenotypes / susceptibility to health conditions related to this particular variant

In GNU Health we firmly believe that knowing the details at molecular level is key for personalized / precision medicine, that will help provide the best medical and therapeutical approach.
 