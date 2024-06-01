import subprocess

def install_requirements():
    try:
        subprocess.run(["pip", "install", "--no-cache-dir", "-r", "requirements.txt"], check=True)
        print("Requirements installation successful!")
    except subprocess.CalledProcessError as e:
        print(f"Error occurred: {e}")

if __name__ == "__main__":
    install_requirements()
