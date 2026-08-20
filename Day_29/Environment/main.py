import platform
import requests
import sys


def get_python_version():
    return platform.python_version()


def get_requests_version():
    return requests.__version__


def get_environment_name():
    if hasattr(sys, "real_prefix") or (hasattr(sys, "base_prefix") and sys.base_prefix != sys.prefix):
        return sys.prefix.split("\\")[-1]
    return "Global Python"


def is_virtual_environment_active():
    return sys.prefix != getattr(sys, "base_prefix", sys.prefix)


def display_environment_info():
    print("=" * 50)
    print("Environment Information")
    print("=" * 50)

    print(f"Python Version     : {get_python_version()}")
    print(f"Requests Version   : {get_requests_version()}")
    print(f"Environment Name   : {get_environment_name()}")
    print(
        f"Environment Active : {'Yes ✅' if is_virtual_environment_active() else 'No ❌'}"
    )

    if is_virtual_environment_active():
        print("\n🎉 Virtual environment is working correctly!")
    else:
        print("\n⚠️ Running on global Python installation.")


def main():
    display_environment_info()


if __name__ == "__main__":
    main()