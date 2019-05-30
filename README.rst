.. image:: https://img.shields.io/pypi/v/yason.svg
        :target: https://pypi.python.org/pypi/yason

.. image:: https://img.shields.io/travis/com/ktaletsk/yason.svg
        :target: https://travis-ci.com/ktaletsk/yason

.. image:: https://readthedocs.org/projects/yason/badge/?version=latest
        :target: https://yason.readthedocs.io/en/latest/?badge=latest
        :alt: Documentation Status


.. image:: https://pyup.io/repos/github/ktaletsk/yason/shield.svg
     :target: https://pyup.io/repos/github/ktaletsk/yason/
     :alt: Updates

==========================================
yason: Jupyter Notebook Scheduler for Argo
==========================================

.. image:: logo.png
    :height: 50px
    :align: center
    :alt: logo


JupyterHub deployed on Kubernetes allows teams to do data analysis in the browser and efficiently share computational resources. But when it comes to Jupyter Notebooks, it is not easy to run them remotely and non-interactively or schedule them. Fortunately, with Papermill and Argo Workflows it is now possible to do just that. Yason is Python package and CLI for scheduling the remote execution of Jupyter Notebooks.


* Free software: MIT license
* Documentation: https://yason.readthedocs.io.


Features
--------

* Check the status of all scheduled notebook jobs
* Schedule a notebook for execution
* Get resulting notebook after execution
* Delete scheduled notebook job

Coming soon
-----------

* Including multiple files/folders together with Notebook for execution
* Integration with Argo events for scheduling

Prerequisites
-------------

Yason is intended to run on JupyterLab pods spawned by JupyterHub deployed on Kubernetes. Yason also requires Argo Workflows to be deployed on the same cluster in the namespace `argo`. S3 bucket is required for intermediate storage of Notebooks before and after their execution.

See more details and instructions in the full documentation https://yason.readthedocs.io

Usage
-----

To use Yason in Python project::

    from yason import yason


CLI Tool
--------

To use Yason as CLI tool, type::

    yason COMMAND [ARGS]

To see the list of all scheduled Notebooks for your JupyterHub username, type::

    yason list

To schedule and execute Notebook immediately, type::

    yason run <Notebook Name>.ipynb

To get the resulting Notebook after execution, type::

    yason get <Workflow ID> <Destination>
    
i.e.::

    yason get 25fe9753bc854148aac26ff7d97ba128 My_Notebook_result.ipynb

To delete the scheduled Notebook from your list, type::

    yason delete <Workflow ID>
    
i.e.::

    yason delete 25fe9753bc854148aac26ff7d97ba128

Name
----

Yason (or Jason) in Greek mythology is the leader of Argonauts. Yason brings your Jupyter Notebooks on board of Argo (Workflows).


Credits
-------

This package was created with Cookiecutter_ and the `audreyr/cookiecutter-pypackage`_ project template.

.. _Cookiecutter: https://github.com/audreyr/cookiecutter
.. _`audreyr/cookiecutter-pypackage`: https://github.com/audreyr/cookiecutter-pypackage
