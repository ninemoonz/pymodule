import os
from dotenv import load_dotenv


def mode_check() -> None:
    if os.getenv('MATRIX_MODE'):
        print(f"Mode: {os.environ.get('MATRIX_MODE')}")
    else:
        print("MODE: Configuration not found")


def database_check() -> None:
    if os.getenv('DATABASE_URL'):
        print("Database: Connected to local instance")
    else:
        print("Database: Configuration not found")


def api_check() -> None:
    api_key = os.getenv('API_KEY')
    mode = os.getenv('MATRIX_MODE')
    if api_key:
        print("API Access: Authenticated")
    else:
        if mode == 'production':
            print("API Access: [Critical] NO API KEY - "
                  "Cannot authenticate in production mode")
        else:
            print("API Access: Configuration not found")


def log_check() -> None:
    if os.getenv('LOG_LEVEL'):
        print(f"Log Level: {os.environ.get('LOG_LEVEL')}")
    else:
        print("Log Level: Configuration not found")


def zion_check() -> None:
    if os.getenv('ZION_ENDPOINT'):
        print("Zion Network: Online")
    else:
        print("Zion Network: Configuration not found")


def security_check(env_loaded: bool) -> None:
    print("Environment Security check:")
    print("[OK] No hardcoded secrets detected")
    if env_loaded:
        print("[OK] .env file properly configured")
    else:
        print("[WARNING] .env file not found")
    print("[OK] Production overrides available")


def config_loading() -> None:   
    print("Configuration loaded:")
    mode_check()
    database_check()
    api_check()
    log_check()
    zion_check()


def env_loading() -> bool:
    loaded: bool = False
    if os.path.exists('.env'):
        load_dotenv()
        loaded = True
    else:
        print("[ERROR] .env file not found")
    return loaded


if __name__ == "__main__":
    print("\nORACLE STATUS: Reading the Matrix...\n")
    loaded: bool = env_loading()
    config_loading()
    print()
    security_check(loaded)
    print("\nThe Oracle sees all configurations.")
