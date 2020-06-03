"""Make all files in the current directory executable"""
import os

dir = os.path.dirname(os.path.abspath(__file__))

for _, _, files in os.walk(dir):
    for file in files:
        if file != 'cron-setup':
            os.system(f"chmod ugo+x {os.path.join(dir, file)}")
