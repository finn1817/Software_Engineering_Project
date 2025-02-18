import subprocess

def install_packages():
    """Installs required dependencies."""
    subprocess.run(["pip", "install", "flask"], check=True)
    print("✅ Flask installed successfully!")

if __name__ == "__main__":
    install_packages()
    print("🚀 Installation complete! Run `python main.py` to start the app.")
