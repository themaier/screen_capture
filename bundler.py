import subprocess


def create_executable(script_name):
    try:
        # Building the executable with PyInstaller
        subprocess.run(["pyinstaller", "--onefile", script_name], check=True)
        print(f"Executable for {script_name} created successfully.")
    except subprocess.CalledProcessError as e:
        print(f"Failed to create executable: {e}")


if __name__ == "__main__":
    # Name of the Python script you want to convert into an executable
    script_name = "your_script.py"
    create_executable(script_name)
