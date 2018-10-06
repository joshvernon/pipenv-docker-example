import os
import platform
import sys

import requests

print("Hello from Dockerized Python!")
print(f"Current working directory: {os.getcwd()}")
print(f"Current directory contents: {', '.join(os.listdir())}")
print(f"platform.node(): {platform.node()}")
print(f"sys.version: {sys.version}")
print(f"sys.path: {sys.path}")
print(f"sys.executable: {sys.executable}")
print(f"requests version: {requests.__version__}")

