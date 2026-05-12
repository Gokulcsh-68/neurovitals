
import sys
print("Python version:", sys.version)
try:
    import fastapi
    print("FastAPI installed")
except ImportError:
    print("FastAPI NOT installed")
try:
    import uvicorn
    print("Uvicorn installed")
except ImportError:
    print("Uvicorn NOT installed")
