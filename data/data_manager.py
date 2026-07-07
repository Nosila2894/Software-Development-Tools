import glob
import importlib
import inspect
import os
import sys


class DataManager():
    def __init__(self, target_package):
        self.target_package = target_package
        self.data = {}
        self._discover_and_build_data()

    #Builds the data by extracting all data class from the Game Data package
    #Then calls the build_data method of each data class to populate the data dictionary
    def _discover_and_build_data(self):
        # Identifies this package by name
        package_module = importlib.import_module(self.target_package)

        # Takes the DataManager Module and extracts the package name and path
        package_path = os.path.dirname(os.path.abspath(package_module.__file__))

        #Creates a search path of all files in the package with a .py extension
        search_path = os.path.join(package_path, '*.py')
        all_files = glob.glob(search_path)

        discovered_modules = []
        for file_path in all_files:
            m_name = os.path.basename(file_path)[:-3]
            if m_name not in ("__init__", "data_manager", "sample_data"):
                discovered_modules.append(m_name)

        # True if your real files (like character.py or config.py) exist in the directory
        has_real_game_data = len(discovered_modules) > 0

        #Searches through the search pathway to extract all data files
        for file_path in glob.glob(search_path):

            #Extracts a file name from the pathway
            module_name = os.path.basename(file_path)[:-3]  # Remove the .py extension

            #Skips the DataManager and __init__ modules to avoid circular imports and redundant processing
            if module_name in ("data_manager", "__init__"):
                continue

            # to skip loading the generic 'sample_data' blueprint file entirely!
            if module_name == "sample_data" and has_real_game_data:
                continue

            #Constructs the full module name for importing, considering the package structure
            full_module_name =(f"{self.target_package}.{module_name}")

            try:
                #Import the module using importlib to dynamically load the data classes
                module = importlib.import_module(full_module_name)

                #Constructs and appends the class stored in the data module.
                for name, obj in inspect.getmembers(module, inspect.isclass):
                    if obj.__module__ == full_module_name:
                    
                        instance = obj()
                        data_key = module_name.lower()

                        self.data[data_key] = instance
                        setattr(self, data_key, instance)

                        #Test print to confirm that the data class has been registered
                        print(f"[DATA SCANNER] Registered: data.{data_key}")
            except Exception as e:
                print(f"[DATA ERROR] Error importing {full_module_name}: {e}")



