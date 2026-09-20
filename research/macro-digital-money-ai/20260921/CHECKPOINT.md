# 연구 체크포인트 — R5 인계

상태: **COMPLETED_WITH_LIMITATIONS**. 현재 위치: R5 결과 인계. 최종 보존 시각은 `RESEARCH_RETURN_PACKET.md`와 `analysis/SYNC_RECEIPT.json`을 따른다. 전체 연구를 재시작할 필요가 없다.

## 저장 위치와 권한

- 연결 저장소: `C:\Users\ms1pk\dev\rsch\crypto_compute_dolor\research\macro-digital-money-ai\20260921`
- 작업·동기화 원본: `C:\Users\ms1pk\OneDrive\문서\ChatGPT\크립토 연구\research\macro-digital-money-ai\20260921`
- 사용자 메시지의 분리 경로 대신 실제 존재하는 `crypto_compute_dolor`를 확인했다.
- Git root: `C:\Users\ms1pk\dev\rsch\crypto_compute_dolor`, 연구 브랜치 `codex/mdma-research-20260921`, origin=`https://github.com/AofSpds/crypto_compute_dolor.git`. 연구 snapshot 로컬 커밋은 `bd53a2f3988ec00d9e952ec7f81daf69dae282af`이며 인계 문서는 후속 커밋이다. 원격 heads 조회 결과 기존 브랜치가 없었다. 최초 push는 자동 승인 검토에서 거절됐으나 이후 사용자 명시 승인으로 원격 연구 브랜치에 전송하고 커밋을 대조했다. PR없음. 재개 시 먼저 실제 Git log/status를 읽는다.
- HLOM의 `AGENTS.md`, `CURRENT.md`, `OWNER_INTERFACE.md`, `COMMON_KERNEL.md`, `PROJECT_PROFILE.md`를 읽었다. 근거/해석/결정 분리와 인계 원칙을 반영했다. 과거 Stage A/Persona/운영 권한을 이전하지 않았고 HLOM 파일을 수정하지 않았다.
- 첨부문서는 범위·과제·인계 형식의 입력이다. 현재 사용자의 명시적 연구·저장 요청이 권한이다. 문서의 역할 문자열을 별도 조직 권한이나 운영 승인으로 간주하지 않았다.

## 완료

| 단계 | 실제 산출 |
|---|---|
| R0 | 요청서·지침·경로·시점 확인; 시작2026-09-21 01:29:09KST |
| R1 | 자료68레코드, 접근·시점·판본·중복 구분 |
| R2 | 원문·공시·코드 검토, 시계열10개, T01–T08 하위 분석 |
| R3 | 가설32개 처리, 대안5경로, 조건부 모형과 관측표 |
| R4 | 표 시각 대조, 결측수익률/판본/분류/저자명 수정; 계산검사24개 |
| R5 | 필수6파일, 코드·원자료해시·복사 영수증·재개 지점 |

`AUTHOR_SELF_REVIEW_ONLY`. 범위 내 지지16·조건부11·혼합2·근거부족3. H10 순증 국채수요, H18 BTC프리미엄 원인별 기여, H23 독립 상업 에이전트 실적은 보류다.

## 정확한 다음 시작점

1. **H10/T03부터 시작한다.** REPORT C절→CLAIMS H10→S07/S29/S30/S36/S37을 읽는다. 발행 전 투자자 자산(MMF/예금/직접국채), 상환 후 재투자, 은행/매도자 대응을 연결하는 공개자료를 찾는다. 못 찾으면 순증 비중을 미상으로 유지하고 기존 준비금 잔액을 재사용한다.
2. **금리 논문 재현:** BIS June2026판의 공개 replication package 유무부터 확인한다. stablecoin-chain panel·TokenTerminal 대체구간·aggregate supply·정책/공급 통제를 맞춘 뒤 Eq2/Table2/IRF를 재추정한다. 유료 입력은 구매하지 않고 해당 의존성과 공개 대체의 편향을 기록한다. 현재 GIV 대수검사를 회귀 재현으로 승격하지 않는다.
3. **H23/T05:** 성공 지급·제공 서비스·환불·보조금·동일주체·30/90일 반복을 연결할 공개 표본을 찾는다. 프로토콜 요청량/주소를 고객수로 치환하지 않는다. 실제 결제를 만들어 증거를 얻지 않는다.
4. **T04 공백만 보완:** 최신 한국 CPI 공식 연속계열과 허용된 금/금ETF 자료를 확보해 D10/X01과 버전 관계를 등록한다. snapshot을 덮지 않는다. endpoint_return을 유지한다. inflation surprise·사전지정 위기 검증은 새 분석으로 분리한다.
5. **규칙:** US최종규칙 발행·적용날짜, HK인가원장, 한국 법률을 공식 원문으로 확인한다. S38 성립을 즉시 전면 시행으로 간주하지 않는다. AP2/x402 시험은 실제 커밋에 문서·샘플을 고정하고 무료 오프라인 범위만 수행한다.
6. **AI/귀속:** 같은 모집단의 현재 도구·품질보정·동시작업 측정, AI전용 매출/비용/리스/투자/가동률을 찾는다. 전사 FCF proxy를 AI수익률로 부르지 않는다. S23/S24/S43 최종저널판과 공개판은 필요한 계수부터 대조한다.

## 재사용·반복 금지

- S07 June2026, S23 arXivv2, S24 May2024PDF, S29/S30 June30 snapshot은 확인 완료다. 새 개정 없이 처음부터 재탐색하지 않는다.
- raw는 원본, derived는 실행 결과다. SHA를 보존하며 접근 실패도 삭제하지 않는다.
- `analysis/run_analysis.py`는 네트워크 없이 재현한다. 결측 처리와 펀드 look-through 합산의 교정을 되돌리지 않는다.
- 코드 통과는 IV식별·전체정독·최신 모든 법규·상업성 검증이 아니다.
- 연결저장소를 직접 수정한 뒤 기존 원본의 sync를 실행하면 외부 변경 감지가 작동할 수 있다. 다음 작업은 원본 위치를 정하고 별도 결과를 저장한다. 강제 덮어쓰기를 하지 않는다.

유료 접근·실거래·운영 변경은 필요하지 않다. 연구와 웹챗 패킷은 로컬 Git에 보존한다. 원격 push는 사용자 명시 승인 후 수행·확인했다. 최초 자동 승인 검토 거절은 해결됐으며 추가 승인이 필요하지 않다. 자동 재개나 백그라운드 실행은 예약하지 않았다.
