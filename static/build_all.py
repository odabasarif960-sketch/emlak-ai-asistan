import os
import subprocess

def run_script(script_name):
    print(f"Running {script_name}...")
    subprocess.run(["python", script_name], check=True)

if __name__ == "__main__":
    scripts = [
        "build.py",
        "build2.py",
        "build3.py",
        "build3_pricing.py",
        "build4.py",
        "build5.py"
    ]
    
    # Change dir to static
    os.chdir(os.path.dirname(os.path.abspath(__file__)))
    
    for s in scripts:
        run_script(s)
        
    print("All builds completed successfully! index.html generated.")
