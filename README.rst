=====================
django_localflavor_br
=====================

Country-specific Django helpers for Brazil.

What's in the Brazil localflavor?
=================================

* forms.BRPhoneNumberField: A form field that validates input as a Brazilian
  phone number, with the format XX-XXXX-XXXX.

* forms.BRZipCodeField: A form field that validates input as a Brazilian zip
  code, with the format XXXXX-XXX.

* forms.BRStateSelect: A ``Select`` widget that uses a list of Brazilian
  states/territories as its choices.

* forms.BRCPFField: A form field that validates input as `Brazilian CPF`_.
  Input can either be of the format XXX.XXX.XXX-VD or be a group of 11 digits.

* forms.BRCNPJField: A form field that validates input as `Brazilian CNPJ`_.
  Input can either be of the format XX.XXX.XXX/XXXX-XX or be a group of 14
  digits.

.. _Brazilian CPF: http://en.wikipedia.org/wiki/Cadastro_de_Pessoas_F%C3%ADsicas
.. _Brazilian CNPJ: http://en.wikipedia.org/wiki/National_identification_number#Brazil

See the source code for full details.

About localflavors
==================

Django's "localflavor" packages offer additional functionality for particular
countries or cultures.

For example, these might include form fields for your country's postal codes,
phone number formats or government ID numbers.

This code used to live in Django proper -- in django.contrib.localflavor -- but
was separated into standalone packages in Django 1.5 to keep the framework's
core clean.

For a full list of available localflavors, see https://github.com/django/
