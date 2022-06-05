__all__ = ("__version__", "info")


__version__ = "0.4.13.3"


def info():
    print(
        f"Version {__version__} of EpikCord.py, written by EpikHost. "
        f"This is an unstable build and will contain bugs. "
        f"Please report any bugs to https://github.com/EpikCord/EpikCord.py/issues."
    )


if __name__ == "__main__":
    info()
