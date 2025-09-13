# tests/conftest.py
import os, sys
# tests/에서 한 단계 위(프로젝트 루트)를 sys.path 맨 앞에 추가
ROOT = os.path.abspath(os.path.join(os.path.dirname(__file__), ".."))
if ROOT not in sys.path:
    sys.path.insert(0, ROOT)
