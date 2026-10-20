# 인지 · 판단 · 제어 공개 예제

[← 프로젝트 소개](../README.md)

각 예제는 2025 팀 자료에서 기본 흐름만 골라 Python으로 축약한 **오프라인 설명용 코드**입니다. 원본 패키지·튜닝·차량 입출력은 포함하지 않습니다. 출처와 생략 범위는 [PUBLICATION.md](../PUBLICATION.md)에 있습니다.

저장소 루트에서 Python 3.10 이상으로 실행합니다. 별도 패키지 설치는 필요하지 않습니다.

```bash
python examples/perception/valid_cones.py
python examples/planning/lookahead.py
python examples/control/command_mux.py
```

| 예제 | 합성 입력 | 결과 |
| --- | --- | --- |
| 인지 | 유효·무효 표시가 있는 중심점 후보 | 유효한 점의 x축 정렬 |
| 판단·추종 | 차량 전방의 예시 경로점 | 목표점과 기하학적 조향각 |
| 제어 | 설명용 명령 값과 모드·정지 상태 | 선택된 값 또는 정지 값 |

좌표·휠베이스·명령 값은 설명용으로 만든 값이며 실제 차량·코스 값과 관계없습니다. 출력은 콘솔에만 표시됩니다.
