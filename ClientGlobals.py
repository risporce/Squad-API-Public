import jwt
import os
import json
from Utils.Configuration import client_configs_from_dict
from Utils.Configuration import client_configs_to_dict


class Configs:
    _instance = None

    def __new__(cls):
        if cls._instance is None:
            cls._instance = super(Configs, cls).__new__(cls)
            cls._instance.load_configuration()
        return cls._instance
    
    def load_configuration(self):
        """Load configuration from config.json."""
        config_file_path = os.path.join(os.path.dirname(__file__), "config.json")
        try:
            with open(config_file_path, "r") as file:
                self.global_data = client_configs_from_dict(json.load(file))
        except FileNotFoundError:
            raise Exception(f"Configuration file not found: {config_file_path}")
        except json.JSONDecodeError as e:
            raise Exception(f"Error parsing JSON: {str(e)}")

    def get_dict(self):
        return client_configs_to_dict(self.global_data)
    
    def update_config(self, new_configs):
        pass

        # Save the modified configuration back to the config.json file
        self.save_configuration()

    def save_configuration(self, new_configs: dict = None):
        """Save the current configuration to config.json."""
        config_file_path = os.path.join(os.path.dirname(__file__), "config.json")
        try:
            if new_configs:
                self.global_data = client_configs_from_dict(new_configs)
            updated_config_dict = client_configs_to_dict(self.global_data)
            with open(config_file_path, "w") as file:
                json.dump(updated_config_dict, file, indent=4)
                file.close()
        except Exception as e:
            raise Exception(f"Error saving configuration: {str(e)}")