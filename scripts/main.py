import subprocess


def run_script(script_name):
    result = subprocess.run(["python", script_name], capture_output=True, text=True)
    if result.returncode != 0:
        print(f"Error running {script_name}: {result.stderr}")
    else:
        print(f"Output of {script_name}: {result.stdout}")


if __name__ == "__main__":
    run_script("scraper.py")
    run_script("data_cleaner.py")
