import platform
import requests


def get_python_version():
    """Return the installed Python version."""
    return platform.python_version()


def get_requests_version():
    """Return the installed requests library version."""
    return requests.__version__


def check_environment():
    """Check whether Python and requests are available."""
    try:
        python_version = get_python_version()
        requests_version = get_requests_version()
        return True, python_version, requests_version
    except Exception as e:
        return False, str(e), None


def display_environment_info():
    """Display environment information."""
    status, python_version, requests_version = check_environment()

    print("=" * 40)
    print("Environment Information")
    print("=" * 40)

    if status:
        print(f"✅ Python Version   : {python_version}")
        print(f"✅ Requests Version : {requests_version}")
        print("\n🎉 Environment is working correctly!")
    else:
        print(f"❌ Environment Error: {python_version}")


def main():
    """Main entry point."""
    display_environment_info()


if __name__ == "__main__":
    main()