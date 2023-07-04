import os
from dotenv import load_dotenv


load_dotenv()


def get_env_var(env_var_name, base_value, can_be_empty):
    """Essaie de trouvé la variable d'environnement.\
    Si ne trouve pas, renvois valeur défault"""
    env_var = os.getenv(env_var_name)
    validation = (
        env_var is not None if can_be_empty else env_var is not None and env_var
    )
    if not (validation):
        env_var = base_value

    return env_var


def get_env_var_strict(env_var_name, can_be_empty):
    """Essaie de trouvé la variable d'environnement.\
    Si ne trouve pas, lance une exception"""
    env_var = get_env_var(env_var_name, None, can_be_empty)
    if env_var is None:
        raise Exception(
            "La variable '"
            + env_var_name
            + "' doit être définie comme variable d'environnement."
        )

    return env_var
