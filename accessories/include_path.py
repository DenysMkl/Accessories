import os
import sys
from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent.parent
storage_dir = os.path.join(BASE_DIR, 'storage')

sys.path.append(storage_dir)
