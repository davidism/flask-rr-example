Flask-RR
========

A Flask subclass that uses a global ``Response`` object, and passes both
the ``Request`` and ``Response`` objects as arguments to each view.

.. danger::

    **Do not use this.** This is an example of how you might start
    implementing this behavior, but there are plenty of corner cases
    that haven't been addressed. It will probably blow up your server.

Install
=======

1.  Clone this repository.
2.  ``cd`` into it.
3.  Create a virtualenv.
4.  Activate it.
5.  Install in editable mode with dev requirements.

.. code-block:: text

    git clone https://github.com/davidism/flask-rr
    cd flask-rr
    python3 -m venv --prompt flask-rr venv
    . venv/bin/activate
    pip install -e ".[dev]"

Example
=======

An example package is included and installed with the library. After
following the install instructions above, run ``flask run``. Try:

-   http://127.0.0.1:5000/
-   http://127.0.0.1:5000/hello?name=Flask
-   http://127.0.0.1:5000/status/418
-   http://127.0.0.1:5000/download

Docs
====

Use the ``FlaskRR`` class instead of the ``Flask`` class.

There is a global ``response`` object, like ``request``. It is a proxy
to a ``Response`` object, is passed to each view (so you don't have to
import it), and is returned as the final response.

Unlike Flask, view functions must take two positional arguments,
``request`` and ``response``. Modifying the ``response`` object is
equivalent to modifying the ``response`` proxy.

View functions do not need to return a response since the passed
argument can be modified instead. If they do return, that overwrites
anything already in the ``response`` proxy.
