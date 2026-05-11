import os
import subprocess

scripts = [
    "static/build.py",
    "static/build2.py",
    "static/build3.py",
    "static/build3_pricing.py",
    "static/build4.py",
    "static/build_valuation.py",
    "static/build5.py",
]

for script in scripts:
    print(f"Running {script}...")
    subprocess.run(["python", script], check=True)

print("Tüm build işlemleri tamamlandı. static/index.html oluşturuldu!")
