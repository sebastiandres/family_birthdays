import pickle
import sys

class SimulationInterface():
    """family_birthdays is a package computes the family birthdays 
    The framework can be personalized and extended for a specific simulation need.
    Link: https://family_birthdays.readthedocs.io/
    """

    def __init__(self):
        """Initializes the class, with no inputs. 
        Will assume that if you have the colab library installed, 
        you're running on google colab(oratory). 

        :return: Nothing
        :rtype: Nothing
        """
        self.configuration = self.__get_configuration()
        self.inputs = {}
        self.plot_options = {}
        self.outputs = {}
        return

    def __get_configuration(self):
        """Carefully tries to import required libraries,
        storing the python and library version.

        :return: Nothing
        :rtype: Nothing
        """
        # Gets the library version
        from .version_file import version_number as GSL_version
        # Gets the python environmnet
        try:
            import colab
            pyenv = "google_colab"
        except:
            try:
                aux = __file__
                pyenv = "python"
            except:
                print("Not in python")
                pyenv = "jupyter_notebook"
        # Check the version for python
        try:
            import platform
            python_version = platform.python_version()
        except:
            python_version = ""
        # Pack and return
        configuration = {
                         "environment":pyenv,
                         "python_version":python_version,
                         "family_birthdays_version":GSL_version,
                         }
        return configuration

    def status(self):
        """Prints out the detected configuration: environment, python and library versions.
        """
        # Configuration
        print("System configuration:")
        for key in self.configuration:
            library = "    " + key.replace("_", " ") + ":"
            if self.configuration[key]:
                print(library, self.configuration[key])
            else:
                print(library, "Not installed")
        # Inputs
        print("Inputs:")
        if self.inputs:
            for key in self.inputs:
                print("    "+key, self.inputs[key])
        else:
            print("    No inputs")
        return  

    def new(self, inputs, plot_options=None):
        """Associates inputs and plot options to the simulation. 

        :param inputs: The inputs that will be used in the simulation. 
            This can be completely personalized. 
        :type inputs: dict
        :param plot_options: The plot options, defaults to None
        :type plot_options: dict, optional
        """
        self.inputs = inputs
        self.plot_options = plot_options

    def save(self, filename):
        """Saves the current state of the simulation, with all
        the provided information. The created file can be
        used with the `load` method to restore the simulation. 

        :param filename: Name for the simulation file.
        :type filename: string
        """
        # Pickle and return
        my_dict = {
                   "configuration":self.configuration,
                   "inputs":self.inputs, 
                   "outputs":self.outputs,
                   "plot_options":self.plot_options,
                  }
        with open(filename, "wb") as fh:
            pickle.dump(my_dict, fh)
            print("Saving simulation into file ", filename)         
        self.download(filename)  #Offer to download the file 
        return

    def load(self, filename):
        """Loads a simulation from a simulation file generated
        with the `save` method to restore the simulation. 

        :param filename: Name for the simulation file.
        :type filename: string
        """
        # Unpack and assign
        with open(filename, "rb") as f:
            my_dict=pickle.load(f)
        self.configuration=my_dict["configuration"]
        self.inputs=my_dict["inputs"] 
        self.outputs=my_dict["outputs"] 
        self.plot_options=my_dict["plot_options"]
        return

    def simulate(self):
        """Conditionally imports the numpy library.
        """
        # Unpack required values
        x_min = self.inputs["x_min"]
        x_max = self.inputs["x_max"]
        N_points = self.inputs["N_points"]
        m = self.inputs["m"]
        b = self.inputs["b"]
        # Run the delegated simulation
        outputs = execute_simulation(self.inputs)
        # Store simulation
        self.outputs = outputs
        return
        
    def download(self, filename):
        """Utility to download file, using colab
        """
        if self.configuration["environment"]=="google_colab":
            from google.colab import files
            files.download(filename)
        returns