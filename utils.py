import os
import logging
from typing import List, Dict

def get_terraform_state_file_path(state_file_name: str = 'terraform.tfstate') -> str:
    return os.path.join(os.getcwd(), state_file_name)

def get_terraform_config_file_path(config_file_name: str = 'main.tf') -> str:
    return os.path.join(os.getcwd(), config_file_name)

def get_environment_variables() -> Dict[str, str]:
    return dict(os.environ)

def get_required_environment_variables(required_variables: List[str]) -> Dict[str, str]:
    environment_variables = get_environment_variables()
    required_variables_dict = {}
    for variable in required_variables:
        if variable in environment_variables:
            required_variables_dict[variable] = environment_variables[variable]
        else:
            raise ValueError(f"Required environment variable {variable} is not set")
    return required_variables_dict

def setup_logging(log_level: str = 'INFO') -> None:
    logging.basicConfig(level=getattr(logging, log_level.upper()), format='%(asctime)s - %(levelname)s - %(message)s')

def get_logger(logger_name: str = 'infra-terraform') -> logging.Logger:
    return logging.getLogger(logger_name)

def main():
    setup_logging()
    logger = get_logger()
    logger.info('Utils module initialized')

if __name__ == '__main__':
    main()