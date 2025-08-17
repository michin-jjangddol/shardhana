# tests/test_hello.py

import sys
import os

# 현재 파일의 상위 디렉토리(루트)를 sys.path에 추가
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

import hello_shardhana

print("✅ Test started!")
print("✅ Test finished!")

import hello_shardhana  # 루트의 hello_shardhana.py 불러오기

print("✅ Test started!")

# hello_shardhana 안에 print만 있으니까, import하면 자동 실행됨.
# 나중에 함수/클래스로 바뀌면 여기서 함수 호출하면서 테스트 가능.

print("✅ Test finished!")