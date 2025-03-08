import sys
from cx_Freeze import setup, Executable

# Зависимости
build_exe_options = {
    "packages": [
        "flask",
        "torch",
        "transformers",
        "nltk",
        "sqlalchemy",
        "pandas",
        "scikit-learn"
    ],
    "include_files": [
        ("templates", "templates"),
        ("static", "static"),
        ("README.md", "README.md"),
        ("requirements.txt", "requirements.txt")
    ],
    "excludes": [],
    "include_msvcr": True
}

# Создание exe
base = None
if sys.platform == "win32":
    base = "Win32GUI"  # Используем Win32GUI для Windows

setup(
    name="Bunny Hab",
    version="1.0",
    description="Виртуальный помощник для программистов",
    options={"build_exe": build_exe_options},
    executables=[
        Executable(
            "main.py",
            base=base,
            icon="static/img/logo.ico",
            target_name="BunnyHab.exe"
        )
    ]
) 