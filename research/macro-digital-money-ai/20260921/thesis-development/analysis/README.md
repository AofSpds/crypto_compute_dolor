# 실행과 재현

`python analysis/run_analysis.py`를 thesis-development 폴더에서 실행한다. Python 표준 라이브러리만 필요하며 네트워크·API·계좌·지갑을 사용하지 않는다. 입력 `inputs.json`, 결과 `results/A01_*.csv`–`A06_*.csv` 및 `RESULTS.json`이 고정돼 있다. 모든 비용·잔액·가치귀속 입력은 가상이며, A05만 공개 할인채 공식과 원문 주석을 대조하는 단위 계산이다. 실험·회귀 재현은 아니다.

비용 모형은 총 시도 비용을 유지하고 사전 품질을 만족한 완료 건수를 분모로 쓴다. setup은 해당 배치에 배분된 고정비다. `residual_loss`는 verification/rework에 포함되지 않은 잔여 손실의 가상 금액이며 중복되지 않는다고 가정한다. 시간·외부성·피해 꼬리를 실제로 측정한 자료는 없으므로 이 모형으로 제품을 추천할 수 없다.

`python analysis/validate_artifacts.py`는 원본 해시·첨부 외부 검토 manifest·로컬 링크·계산 결과와 기존 연구의 주석 환산 전파를 점검한다. Git commit A blob 비교는 현재 로컬 저장소 경로를 사용하므로 다른 clone에서는 코드의 `repo` 경로를 지정해야 한다. 이는 계산 재현의 필수조건은 아니다.

`acquire_sources.py`는 공개 문서 다운로드 보조다. **동일 빈티지 계산을 위해 다시 실행할 필요가 없다.** 실행 시 원격 문서가 바뀔 수 있으므로 새 빈티지는 다른 디렉터리에서 받아야 한다. 이번 실행의 성공·실패 URL/해시는 `../evidence/DOWNLOAD_MANIFEST.json`에 있다. 특정 ID만 수집하려면 명령 뒤에 ID를 전달한다. 다운로드 성공과 실제 열람은 다르며 열람 범위는 ARGUMENT_EVIDENCE.md가 기준이다. PDF 추출에는 pypdf가 필요하다.

`inspect_pdf.py PATH text|image 1,2,3`은 1부터 세는 PDF 페이지를 읽거나 렌더한다. pypdf/pypdfium2가 필요하다. 화면 자료와 원논문은 로컬 evidence/raw에만 있고 Git에는 없다.

`ingest_inputs.py`는 최초 첨부 추출 이력이다. 현재의 Download 파일과 기존 파일이 충돌하면 중단한다. 연구를 재개하기 위해 다시 실행할 필요가 없다. 첨부 속 과거 코드는 실행하지 않았다.
