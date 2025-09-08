# tests/test_env_basic.py
import matplotlib.pyplot as plt
import os

def test_matplotlib_plot(tmp_path):
    # 간단한 그래프 생성
    fig, ax = plt.subplots()
    ax.plot([0, 1, 2], [0, 1, 4])
    ax.set_title("Matplotlib Test")

    # 임시 경로에 저장
    file_path = tmp_path / "test_plot.png"
    fig.savefig(file_path)

    # 저장된 파일이 존재하는지 확인
    assert os.path.exists(file_path)
