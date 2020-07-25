Examples
=============

Ejemplo en mybinder
*********************
Acá hay un ejemplo ejecutable usando `MyBinder <https://mybinder.org/v2/gh/sebastiandres/family_birthdays/master?filepath=tests%2Fjupyter_test.ipynb>`_.
No requiere una cuenta.

Ejemplo en Google colab
************************
Acá hay un ejemplo en `Google Colab <https://colab.research.google.com/drive/1XnruLOcG39i4SrQSSy9rnHIQ3RsQJdJr?usp=sharing>`_. 
Requiere tener una cuenta de gmail (google).


Ejemplo en python
*********************
Para ejecutar el código necesitas haber instalado la librería.
To run it, you need to install the library. 

.. code-block:: python

    from family_birthdays import SimulationInterface

    birthdates = {"Captain America":"04-07-1918",
                    "Ironman":"29-05-1970",
                    "Spiderman":"10-08-2001",
                    "Batman":"17-04-1915",
                    "Hulk":"18-12-1969",
    }

    SI = SimulationInterface()
    SI.new({"birthdates":birthdates})
    SI.simulate()