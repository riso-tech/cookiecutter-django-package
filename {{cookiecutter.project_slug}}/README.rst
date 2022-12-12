{{ cookiecutter.project_name }}
===============

{{ cookiecutter.description }}

Installable App
---------------

This app can be installed and used in your django project by:

.. code-block:: bash

    $ pip install {{ cookiecutter.project_slug }}


Edit your `settings.py` file to include `'{{ cookiecutter.app_slug }}'` in the `INSTALLED_APPS`
listing.

.. code-block:: python

    INSTALLED_APPS = [
        ...

        "{{ cookiecutter.app_slug }}",
    ]


Edit your project `urls.py` file to import the URLs:


.. code-block:: python

    url_patterns = [
        ...

        path('{{ cookiecutter.app_slug }}/', include('{{ cookiecutter.app_slug }}.urls')),
    ]


Finally, add the models to your database:


.. code-block:: bash

    $ ./manage.py makemigrations {{ cookiecutter.app_slug }}


The "project" Branch
--------------------

The `master branch <{{ cookiecutter.repo_url }}/tree/master>`_ contains the final code for the PyPI package.


Docs & Source
-------------

* Source: {{ cookiecutter.repo_url }}
* PyPI: https://pypi.org/project/{{ cookiecutter.project_slug }}/
