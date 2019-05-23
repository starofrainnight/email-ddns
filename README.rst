==========
email-ddns
==========


.. image:: https://img.shields.io/pypi/v/email-ddns.svg
    :target: https://pypi.python.org/pypi/email-ddns

.. image:: https://travis-ci.org/starofrainnight/email-ddns.svg?branch=master
    :target: https://travis-ci.org/starofrainnight/email-ddns

.. image:: https://ci.appveyor.com/api/projects/status/github/starofrainnight/email-ddns?svg=true
    :target: https://ci.appveyor.com/project/starofrainnight/email-ddns

A DDNS server/client that only rely on free services (email, outer ip getter)

* License: AGPL-3.0

Usage
--------

This library provied a script you could just run under console

Server:

::

    $ email-ddns -i imap.qq.com -s smtp.qq.com -a xxxx@qq.com -p password server

Client:

::

    $ email-ddns -i imap.qq.com -s smtp.qq.com -a xxxx@qq.com -p password client

Credits
---------

This package was created with Cookiecutter_ and the `PyPackageTemplate`_ project template.

.. _Cookiecutter: https://github.com/audreyr/cookiecutter
.. _`PyPackageTemplate`: https://github.com/starofrainnight/rtpl-pypackage

