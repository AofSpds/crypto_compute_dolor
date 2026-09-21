# Codex WORK 인계 — 논지 Git 보존·검증·강화·보완

**현재 논지 원문을 먼저 Git에 보존하고, 기존 연구와 외부 근거를 재사용·보강하여 출처를 갖춘 하나의 주장으로 완성한다.**

현재 상태: **파일 작성 완료 / 대상 저장소 commit·push 미실행 / Codex WORK 미제출**.

대상은 `AofSpds/crypto_compute_dolor`이며, 연구 폴더는 `research/macro-digital-money-ai/20260921/thesis-development`다. 실제 저장소 접근이 가능한 WORK에서 수행한다. 웹챗의 접근 경계를 우회하지 않는다.

이 문서는 요약본이 아니다. 아래 12개 파일의 실제 본문을 포함한다. `<!-- BEGIN_FILE: 경로 -->`와 같은 경계 표기 사이가 각 파일의 내용이다. 경계 표기를 파일 내용으로 저장하지 않는다. 개별 파일은 ZIP에도 포함되어 있다.

## 읽는 순서

1. `CODEX_WORK_REQUEST_v1.0_20260921.md`: 최신 목적·범위·Git 보존·실행·반환 기준.
2. `THESIS_BASELINE_v1.0_20260921.md`: 이번에 보존하고 발전시킬 논지 전체.
3. provenance와 인용 seed: 입력 상태와 실제 검증 필요 범위.
4. 기존 외부 검토 입력: 필요한 근거·발견·한계만 재사용. 원 저장소 연구 문서는 적법한 WORK 접근으로 확인.

**명령의 우선순위:** 최신 사용자 요청과 현재 작업 지침을 따른다. 과거 반환 패킷, 과거 분석 코드 및 그 안의 운영 지시는 역사적 입력이다. 이번 요청은 연구 문서 보존을 위한 commit·일반 push만 포함하며 실거래·계좌/지갑·유료 접근·운영전략 변경은 포함하지 않는다.

**주 산출물:** `THESIS_v1.1.md`. 검토표·계획서·문헌 목록으로 끝내지 않는다. 원문은 보존하고 출처·강한 반론·성립 조건·관측 지표를 갖춘 통합 논증문으로 발전시킨다.

---

<!-- BEGIN_FILE: research/macro-digital-money-ai/20260921/thesis-development/CODEX_WORK_REQUEST_v1.0_20260921.md -->
# 웹챗 → Codex WORK: 현재 논지 Git 보존 및 검증·강화·보완 요청

PACKET_CLASS = THESIS_PRESERVATION_AND_DEVELOPMENT_REQUEST  
PACKET_ID = MDMA-THESIS-WORK-20260921-001  
VERSION = 1.0  
DATE = 2026-09-21  
FROM = WEBCHAT / 논지 작성 채널  
TO = CODEX WORK / 연구 실행자  
TASK = PRESERVE_BASELINE_FIRST → VERIFY_AND_STRENGTHEN → SYNTHESIZE → RETURN  
REPOSITORY = AofSpds/crypto_compute_dolor  
PREFERRED_BRANCH = codex/mdma-research-20260921  
FALLBACK_NEW_BRANCH = codex/mdma-thesis-development-20260921  
RESEARCH_ROOT = research/macro-digital-money-ai/20260921  
OUTPUT_ROOT = research/macro-digital-money-ai/20260921/thesis-development  
GIT_STATUS_AT_WEBCHAT_HANDOFF = NOT_EXECUTED  
WORK_SUBMISSION_AT_WEBCHAT_HANDOFF = NOT_SUBMITTED  
THESIS_STATUS = CANDIDATE_ARGUMENT / NOT_AN_ESTABLISHED_CAUSAL_RESULT

## 0. 이번 요청의 목적과 최우선 지시

사용자의 최신 요청은 다음과 같다.

> 현재 논지를 깃에 저장후 검증/강화/보완을 코드엑스 워크에 요청하는 패킷을 주세요.

직전 방향 지시는 다음과 같다.

> 검토보다는 본론을 발전시켜 하나의 주장으로 만들어주세요.

**이번 업무의 최종 산출물은 출처와 논거를 갖춘 하나의 논증문이다.** 기존 보고서를 다시 평가하는 검토표, 문헌 목록, 계획서만 반환하지 않는다. 현재 논지를 그대로 믿을 필요는 없지만, 반론을 늘어놓는 것만으로도 완료되지 않는다. 근거에 맞추어 더 설명력 있고 반증 가능한 주장으로 개정한다.

**먼저 현재 원문과 이 요청서를 Git에 보존한다. 그 다음 자료 확인·논거 강화·개정을 수행한다.** 원문을 덮어쓰지 않고 개정본을 별도 파일로 만든다. 연구 중 일상적인 단계마다 승인을 다시 요청하지 않는다.

웹챗에서 대상 저장소를 변경한 사실은 없다. ZIP·Markdown 생성은 저장소 commit 또는 원격 push와 다르다. 이 패킷에 기재된 저장소 상태·기존 commit은 사용자 인계 정보이며, 실제 작업 세션에서 확인해야 한다.

## 1. 원문과 기존 연구의 계보

### 1.1 이번에 보존하는 논지

파일: `THESIS_BASELINE_v1.0_20260921.md`

제목: **달러경제의 기계화: AI와 디지털 화폐가 바꾸는 것은 돈의 종류보다 경제활동의 실행 방식이다**

현재 중심 명제:

> AI와 디지털 금융의 결합은 사람이 직접 수행해야 했던 판단·조정·결제·검증의 총비용을 낮추어, 이전에는 경제성이 없던 활동을 실행 가능하게 만들 수 있다. 달러와 스테이블코인은 그 활동의 교환·유동성 기반 중 하나다. 거래 확대, 토큰 잔액, 국채 수요, 자산 수익은 서로 다른 조건에 달려 있으며, 창출 가치와 그 가치의 귀속을 구분해야 한다.

위 문단은 작업용 요약이다. 원문 보존의 대상은 요약이 아니라 별도 baseline 파일 전체다. 원문에 남아 있는 단정·수치·인용·전망도 삭제하지 말고 보존한 뒤 개정본에서 고친다. baseline은 정확성 인증서가 아니다.

### 1.2 기존 연구 위치 — 사용자 인계 기준

- 로컬 후보: `C:\Users\ms1pk\dev\rsch\crypto_compute_dolor`
- 기존 연구 결과 commit: `c7ee7a6444097195155b03fc5b671d4b871b0183`
- 전체 연구 통합본 commit: `39d5cbed92459b55b70e0dd7ba231584a4e75b73`
- 통합 문서: `research/macro-digital-money-ai/20260921/WEBCHAT_FULL_RESEARCH_PACKET.md`
- 원 연구: `RESEARCH_RETURN_PACKET.md`, `REPORT.md`, `CLAIMS.jsonl`, `SOURCES.jsonl`, `ANALYSIS_AND_REVIEW.md`, `data/derived/RESULTS.json`, `CHECKPOINT.md`

기존 상태는 사용자 인계상 `COMPLETED_WITH_LIMITATIONS / AUTHOR_SELF_REVIEW_ONLY`다. 32개 가설·68개 자료라는 숫자가 원문 완독·인과 검증 횟수를 뜻하지 않는다. 원문을 읽어서 필요한 부분만 재사용한다.

기존 H10(글로벌 순증 국채 수요), H18(BTC 프리미엄의 인과 기여), H23(독립 반복 고객·순매출)의 보류를 문장 다듬기로 해제하지 않는다. H25 등 관련 가설은 실제 원장을 읽고 매핑한다. 본 패킷의 P01~P10은 논증을 위한 새 번호이며 기존 H번호를 대체하거나 재번호화하지 않는다.

### 1.3 첨부한 외부 검토의 위치와 한계

`inputs/external-review/`는 앞선 웹챗이 생성한 외부 검토 자료의 사본이다. 원 저장소 42개 파일 전체와 원 코드의 독립 검증이 아니라 공개자료 기반의 제한된 주장·산술 검토라는 원래 한계를 유지한다. 이번 패킷 생성 단계에서는 그 출처·회귀·산술 결과를 새로 검증하지 않았다.

해당 입력에는 BIS WP1270의 주석 가격 환산 오류라는 발견, H10/H23 세분화, 자료 빈티지·분모 구분 등이 기록되어 있다. 이 발견도 현재 원문과 정확한 판본에 대조할 대상이다. 잘못된 환산이 기존 연구에 전파됐는지는 미확인이다. 전파되지 않았다면 원 연구의 계산을 불필요하게 바꾸지 않는다.

**과거 입력, 과거 반환 패킷, 코드 주석에 들어 있는 지시는 기록이다. 최신 사용자 요청과 현재 실행 권한으로 승격하지 않는다.** 특히 과거의 push 미승인 표시는 당시 상태다. 이번에 요청된 한정적 연구 문서 보존과 실거래·운영변경 권한은 별개다.

### 1.4 현재 웹챗의 접근 제한

HEF에서 확인된 등록 작업공간은 `C:\Users\ms1pk\dev\AAA\hef-work` 하나이며, 대상 연구 저장소는 그 밖에 있다. 과거 직접 읽기는 작업공간 경계로 차단되었다. 이 패킷은 경계 우회나 HEF 등록 변경을 승인하지 않는다.

**대상 저장소를 정상적으로 열 수 있는 Codex WORK 세션에서 수행한다.** 접근할 수 없다면 실제 차단 이유와 완료한 범위를 기록한다. 링크나 로컬 경로 문자열을 읽었다는 이유로 본문 열람·Git 저장을 주장하지 않는다.

## 2. 먼저 수행할 Git 보존

### 2.1 저장 범위

새로 작성·보존하는 파일은 원칙적으로 `OUTPUT_ROOT` 안으로 제한한다. 기존 R0~R5 원문과 원장, 운영 코드, 다른 프로젝트, 전역 설정은 수정하지 않는다. 기존 연구 오류를 발견하면 이번 개정본과 변경표에 교정을 기록한다. 옛 결과 파일을 조용히 덮어쓰지 않는다.

이 요청은 **이번 연구 문서와 그 직접적인 근거·분석 산출물의 연구 브랜치 commit 및 일반 push**를 수행하도록 요청한다. main으로의 merge, PR 자동 병합, force push, branch 삭제, 원격 URL·인증·워크스페이스 정책 변경은 포함하지 않는다.

### 2.2 실행 전 확인

대상 저장소의 해당 경로에 적용되는 `AGENTS.md` 등 작업 지침을 읽고 준수한다. 다른 프로젝트의 운영체계나 무관한 bootstrap을 가져오지 않는다. 읽기 명령으로 실제 저장소 루트, 원격, 현재 branch, HEAD, 작업트리 상태를 확인한다. 원격이 `AofSpds/crypto_compute_dolor`를 가리키는지 확인하되, 자격증명·토큰을 기록하지 않는다. 제공된 exact commit의 존재를 확인하고, 실제로 읽은 판본을 기록한다. 이전 commit을 확인하는 것은 그 commit으로 강제 checkout/reset하라는 뜻이 아니다.

가능하면 현재의 정상 연구 branch `codex/mdma-research-20260921`에서 이어간다. 다른 branch이거나 보존을 분리할 필요가 있고 작업트리가 clean하면, 적절한 검증된 연구 기준점에서 `codex/mdma-thesis-development-20260921`을 새로 사용할 수 있다. 이미 같은 이름이 있으면 내용을 확인하고 재사용 여부를 판단한다. 다른 branch를 강제로 덮어쓰지 않는다.

무관한 사용자 변경이 있거나 branch 전환이 충돌하면 stash/reset/clean으로 치우지 않는다. 사용 가능한 기존 clean 연구 worktree가 없다면 충돌을 기록하고 Git 변경을 중단한다. 연구 입력 열람 등 비파괴적으로 가능한 부분은 계속할 수 있지만, 원문 Git 보존이 완료된 것처럼 표현하지 않는다.

필요한 네트워크 접근이 이미 허용된 경우에만 해당 연구 branch를 fetch할 수 있다. 인증이나 접근 정책을 고쳐서 통과시키지 않는다. 원격과 충돌하는 push를 강제하지 않는다.

### 2.3 보존 commit A — 개정 전에 수행

1. 전달 payload의 baseline, 요청서, provenance, 출처 seed, 외부 검토 입력을 `OUTPUT_ROOT` 아래에 보존한다.
2. baseline은 내용과 인용을 고치지 않는다. 같은 이름의 파일이 이미 있고 해시가 같다면 재사용한다. 다르면 기존 파일을 보존하고 충돌을 기록하거나 구별되는 새 버전을 사용한다.
3. 이번에 만든 경로만 명시적으로 stage한다. `git add .`, `git add -A`, `git commit -am`, 무관한 파일 stage를 사용하지 않는다.
4. `git diff --cached` 등으로 실제 변경 범위를 확인한 뒤 원문 보존 commit을 만든다.
5. 해당 연구 branch에 일반 push하고 성공 여부를 실제 응답으로 확인한다. 가능한 경우 원격 branch hash와 로컬 hash를 대조한다.
6. 실제 commit·branch·원격 저장 여부를 중간 보고에 남긴다. 파일 저장, local commit, push, 원격 일치를 서로 다른 상태로 기록한다.

권장 commit 메시지:
`docs(research): preserve machine-mediated dollar economy thesis and work request`

원격 장애로 local commit만 성공했다면 `LOCAL_COMMITTED / PUSH_BLOCKED`를 기록한다. 정상 연구 작업을 계속할 수 있는 범위에서 진행하되 원격 보존 완료를 주장하지 않는다.

## 3. 발전시킬 논증 — 핵심 주장 10개

아래는 정답 목록이 아니라 검증·개정 대상이다. 개정 논증의 본문과 `ARGUMENT_EVIDENCE.md`에서 서로 연결한다.

| ID | 현재 주장 | 보강할 핵심 질문 |
|---|---|---|
| P01 | 실행 총비용 하락은 경제적으로 가능한 작업의 경계를 넓힐 수 있다. | 기존 인간 작업·기존 자동화·LLM 보조·에이전트의 적절한 반사실적 비교가 있는가? 단순한 생성량 증가와 다른가? |
| P02 | 새로 실행되는 작업이 경제적 가치를 만들 수 있다. | 잠재 필요, 유효수요, 민간 편익, 최종 부가가치, 사회적 편익을 구분했는가? 중간거래 증가·기존 지출 대체를 이중 계산하지 않았는가? |
| P03 | 판단·생성 비용이 내려가면 권한·검증·책임이 중요해질 수 있다. | 신뢰 비용이 항상 새 병목이 되는가, 특정 환경에만 해당하는가? 신뢰 비용 자체도 내려가는 반례는 무엇인가? |
| P04 | 달러는 새로운 소프트웨어 경제의 교환 기반으로 확장될 수 있다. | 현재 달러 사용이 미래 지속을 자동 보장하는가? 통화·가격 단위와 은행예금·토큰 청구권을 구분했는가? 국내 현지통화 거래의 반례는? |
| P05 | 에이전트 결제는 여러 수단의 총비용 경쟁이다. | 카드·계좌·사후 청구·선불 크레딧·스테이블코인·토큰화 예금의 비교에 신용·환불·접근·회계 비용까지 포함했는가? |
| P06 | 거래가 늘어도 필요한 잔액이 덜 늘거나 줄 수 있다. | netting, 사전예치, 유동성 buffer, 실제 자금 사용 가능 시점, 저축·담보 잔액을 구분했는가? 체인 속도를 자금 회전속도와 동일시하지 않았는가? |
| P07 | 준비자산 수요와 국채 가격 경로는 존재할 수 있지만 필연적 자산 상승 연쇄는 아니다. | 보유량·자금원·사후 재배분·수요곡선·만기별 가격 효과를 구분했는가? 서로 다른 논문의 충격·식별을 혼합하지 않았는가? |
| P08 | AI의 생산성 효과는 과업·숙련·도구·조직 통합·시점에 조건부다. | 품질·인간시간·실패·재작업·도입비용을 포함했는가? 무작위 실험·관찰연구·설문·업체 발표를 구분했는가? |
| P09 | 가치 창출과 사업자·자산 보유자의 가치 포착은 다르다. | 고객·데이터·권한 등을 '확보한다'는 말만으로 이익을 예측하지 않았는가? 경쟁·진입·전환비용·계약·자본비용·보유자 권리를 확인했는가? |
| P10 | 검증 쉬운 과업·결제 추상화·반복 사용이 초기 확산의 관측 후보다. | 확인된 현상과 전망을 구분했는가? 무엇을 관측하면 현재 주장을 약화·기각하거나 대안 설명을 채택할 것인가? |

## 4. 필요한 이론과 외부 근거의 탐색 방향

아래는 연구를 연결할 검색 방향이며, 미리 검증된 참고문헌 목록이 아니다. 제목·저자·판본·발표일은 실제 원문으로 확인한다. 기존 SOURCES에 해당 자료가 있으면 우선 재사용한다.

- **거래비용과 기업 경계:** 탐색·계약·조정·감독 비용이 거래/내부화의 경계에 주는 영향. Coase·Williamson 계열을 출발점으로 사용하되, 디지털 에이전트에 기계적으로 적용하지 않는다.
- **위임·주인-대리인·불완전계약:** 권한과 책임을 분리하는 이유, 관찰·검증가능성이 자동화와 경제성에 주는 영향. 암호학적 지급 증명이 서비스 품질이나 법적 책임을 모두 보장한다는 식으로 서술하지 않는다.
- **과업 기반 생산성·조직 보완자산:** 기존 연구에서 확인한 작업 개선과 품질·숙련·조직 적응·도입비용·생산성 시차. 기술적 가능성과 상업적 보급, 기업 성과, 거시 효과를 분리한다.
- **거래잔액·운전자본·지급결제:** 현금관리/거래잔액 모형, 사전예치와 신용, 상계·묶음정산·총액정산, 운영상 자금 잠김. Baumol–Tobin 계열 등과 현재의 근사식이 어디서 같은지/다른지 점검한다.
- **통화 네트워크와 경쟁:** 가격 단위·통화 보유·지급수단의 네트워크 효과, 국제 달러의 관성 및 지역별 대안. 기존 은행과 폐쇄형 플랫폼이 새로운 활동을 흡수하는 대안도 검토한다.
- **산업조직과 가치 포착:** 개방형 표준·보완자산·규모의 경제·경쟁·전환비용·계약관계. 필수 인프라와 높은 이익률, 높은 이익률과 자산의 기대수익을 구분한다.

각 연결에서 지지 근거만 찾지 않는다. 가장 강한 반대 설명을 검토하여 범위를 좁히거나 제목·주장을 바꿀 수 있다. 단, 자료가 부족한 하위 연결 하나 때문에 이미 유효한 다른 근거를 전부 보류하는 전역 검증 루프를 만들지 않는다.

## 5. 반드시 해소할 논리적 약점

### 5.1 '경제활동 증가'의 의미

API 요청·온체인 이동·에이전트 간 중간구매 증가를 GDP·사회적 후생 증가로 바로 바꾸지 않는다. 최종 수요와 결제 능력, 기존 활동 대체, 가격 하락, 소비자 편익, 생산자 이익을 나눈다. AI가 사용자의 기존 예산을 다른 곳에 지출한 것인지 새로운 유용한 산출을 만든 것인지 구분한다.

실행 비용만 낮아졌다고 물리적 공급·규제·인력·자본·전력 병목이 사라지지는 않는다. 총비용 관점은 당연한 정의에 머물 위험이 있으므로, 어떤 작업에서 어떤 비용이 줄고 어떤 관측이 대안 이론과 구별되는지 제시한다.

### 5.2 완료 작업당 총비용의 측정

가능하면 다음 비교 틀을 사용하되 새로운 실험을 무리하게 요구하지 않는다.

`기존 인간 절차 / 기존 결정론적 자동화 / AI 보조 / 권한 제한 에이전트`

분자는 인간의 기회비용, 모델·도구비, 도입비용의 명시적 배분, 확인·재작업·실패·분쟁 처리비 등을 포함한다. 분모는 합의된 품질을 충족한 완료 작업 수다. 실패한 시도에 지출한 비용도 분자에 남긴다. 성공 사례만 남겨 성공률을 높이지 않는다.

벽시계 시간·인간 적극 작업시간·병렬처리·최종 납기, 한계비용·평균비용을 구분한다. 금전으로 환산한 오류손실과 실제 처리비를 중복 계산하지 않는다. 외부성·비금전적 품질을 억지로 정확한 숫자로 만들지 않는다.

기존 증거가 이 기준을 충족하지 못하면 무엇이 빠져 있는지 표시하고 그 범위 안에서만 사용한다. 자체 가상 예시로 실제 생산성의 크기를 추정했다고 주장하지 않는다.

### 5.3 신뢰가 '새 병목'이라는 주장

위임이 작은 금액·닫힌 조직·반복 공급자 안에서 일어나 기존 시스템으로 대부분 해결되는 대안과 비교한다. 검증·권한·책임 서비스가 필요하다는 것과 별도 사업자가 높은 이익을 얻는다는 것은 다르다. 공통표준으로 비용이 낮아져 소비자 편익으로 귀속되는 시나리오도 분석한다.

### 5.4 달러 중심 제목의 적절성

달러가 현재 사용된다는 사실을 넘어, 이번 논지가 달러에 특수한 설명인지 보편적인 경제활동 자동화 설명인지 판단한다. 후자라면 제목을 더 일반화하고 달러를 중요한 사례로 재배치할 수 있다. 원문의 제목을 유지하기 위해 증거를 선택하지 않는다.

### 5.5 결제용 잔액의 식

원문의 `잔액 ≈ 일 정산금액 × 평균 잠김 일수 + 예비유동성`은 조건부 운영 예시다. 보편적 통화량 법칙이나 실측 회귀식이 아니다. 시간·통화 단위를 확인한다. 1억×1일과 3억×0.1일 예시는 가상 계산으로 남긴다.

잠김 시간에는 환전·on/off-ramp·상환·재사용 제약·재조달 주기가 포함될 수 있다. 블록 확정 시간만 짧아졌다고 경제적 자금 회전이 같은 폭으로 빨라진다고 가정하지 않는다. 실제 순정산액과 총 거래액, credit와 prefunding을 구분한다. 저축·담보·시장조성·안전 buffer 잔액은 거래잔액과 나누되 중복 계산하지 않는다.

### 5.6 생산성·금리·가치의 전달

실질생산성, 명목성장, 평균 조달금리, 차환, 신규투자 수요, 기간프리미엄을 구분한다. AI 확대가 장기금리 하락으로만 이어진다고 쓰지 않는다. 자산 가치의 상승과 특정 매입가격에서의 투자수익도 구분한다.

비트코인 같은 비현금흐름 자산에 기업 FCF식을 그대로 적용하지 않는다. 반대로 네트워크 사용량·희소성만으로 가격 프리미엄을 인과 분해했다고 주장하지 않는다.

## 6. 출처와 증거를 붙이는 방식

1. baseline 안의 링크와 `BASELINE_CITATION_SEEDS.json`은 **검색 출발점**이다. 이번 작성 단계에서 새로 확인한 출처 목록이 아니다. URL 존재·본문·정확한 수치·주장과의 부합을 확인한다. 확인 실패를 본문 열람으로 바꾸지 않는다.
2. 기술·경제·법제에 대한 근거는 가능한 한 원 논문, 저자 공개본, 공식 통계, 규격, 공시, 법령을 사용한다. 기업 발표는 그 기업의 관측·홍보 지표임을 표시하며 독립 실증과 혼동하지 않는다.
3. 중요한 경험적 수치와 인과 주장에는 본문 가까이에 출처를 붙인다. 논문은 제목·저자·연도·판본·표/쪽/절, 통계는 계열·기간·변환·빈티지, 규격은 버전·구현/배포 상태를 추적할 수 있게 한다.
4. 자료의 발행일·실제 관측기간·접근일을 구분한다. 과거 시점 주장에는 당시 이용 가능 정보를 적용하거나 현재 개정치에 의한 회고 분석임을 표시한다. 법·정책을 다룰 때 성립·제안·최종화·시행·인가를 구분하고 관할·시점을 명시한다. 정치적 평가나 지지/반대는 연구 범위가 아니다.
5. 하나의 연구의 초록·언론 요약·개정판을 독립 증거 여러 건으로 세지 않는다. 초록만 읽은 결과와 방법·표까지 읽은 결과를 구분한다. PDF 표나 그림에 의존하면 해당 페이지를 실제로 확인한다.
6. 회계 항등식·정의·가상 예시·이론적 메커니즘·실증 추정·새로운 전망을 구분한다. 산술상 맞는 예시를 인과 효과의 실증으로 승격하지 않는다.
7. 자료는 넓게 수집할 수 있다. 다만 숫자 할당량을 채우기 위해 주변 문헌을 무한히 늘리지 않는다. 핵심 연결에서 유효 근거·강한 반론·남은 한계가 정리되고 추가 탐색이 결론을 실질적으로 바꾸지 않는 범위에서 종료한다.
8. 합법적으로 접근하지 못한 자료는 제한 상태로 남긴다. 유료 접근·인증 우회·비공개 데이터 제공을 시도하지 않는다.

## 7. 실행 순서 — 계획서 제출에서 멈추지 않는다

### M0. 원문·요청서 Git 보존

섹션 2를 수행한다. 전달 내용을 읽고 baseline·request를 먼저 저장한다. 실제 branch·commit·push 상태를 기록한다.

### M1. 기존 근거를 재사용해 핵심 논증 매핑

RESEARCH_RETURN_PACKET → REPORT의 관련 부분 → CLAIMS/SOURCES의 해당 항목 → 필요한 ANALYSIS/RESULTS → CHECKPOINT 순으로 복구한다. 전 파일 정독을 무조건 선행조건으로 삼지 않는다. 필요한 항목을 읽고 출처 식별자를 재사용한다.

P01~P10 각각에 기존 근거·빠진 연결·가장 강한 반론을 매핑한다. 외부 검토 발견 중 본론에 영향을 주는 부분만 대조한다. 유효 판본과 계산을 정보 없이 재실행하지 않는다.

### M2. 목표 지향적 외부 연구·최소 분석

거래비용/위임, 생산성/조직, 잔액/지급결제, 달러/국채, 가치 포착의 빠진 연결을 우선 보강한다. 명확한 경험적 주장에 근거가 없다면 조건부 명제로 개정하거나 삭제한다.

필요한 경우 총비용 비교, 잔액 민감도, 이해관계자별 가치 귀속 같은 작고 재현 가능한 분석을 수행한다. 모형은 논리 구분을 돕는 수준에서 시작한다. 본론 강화에 필수가 아닌 장기 회귀 재현이나 실제 지급 실험을 새 필수 마일스톤으로 붙이지 않는다.

H10/H23을 완전히 해결하지 못해도 그 한계와 조건을 반영해 본론을 완성한다. H10의 금리 효과와 물량 미식별을, H23의 구현/업체 지표와 독립 반복고객/순매출 미확인을 구분한다.

### M3. 출처를 갖춘 통합 논지 개정

본론을 한 편의 글로 다시 작성한다. 출처를 끝에 몰아붙이는 것만으로 완료하지 않는다. 주장을 실제 근거에 맞추어 고친다. 반론은 부록에 숨기지 말고 가장 적절한 논증 위치에서 대응한다.

추천 흐름은 다음과 같으나 제목·구조는 바꿀 수 있다.

`실행 가능한 활동의 경계 → 위임·품질·책임 → 지급수단 선택 → 거래량/잔액/자금재배분 → 생산성과 금융 전달 → 가치 창출/포착 → 관측·반증`

기존의 "전부 조건부다"라는 결론으로 후퇴하지 않는다. **어떤 조건 아래 어떤 결과를 예상하는지**, 그 조건을 어떻게 관측할지까지 명시한다. 반대로 모든 범위에 적용되는 예언으로 과장하지 않는다.

### M4. 1회 최종 점검·결과 보존·인계

실제로 인용된 핵심 수치, 단위, 인과 표현, 본문과 근거의 일치, baseline 보존을 점검한다. 변경이 필요한 부분만 고치고 해당 부분만 재점검한다. 강한 결론을 만들기 위한 다중 검증 무한 루프를 만들지 않는다.

변경 파일만 stage하여 결과 commit B를 만든 뒤 해당 연구 branch에 일반 push한다. 원격 충돌을 강제로 해결하지 않는다. 최종 응답에 실제 HEAD·branch·push·원격 일치 여부를 구분해 기록한다.

동일 작업자가 작성하고 자기점검한 결과는 `AUTHOR_SELF_REVIEW_ONLY`다. 독립 검토자를 실제로 사용한 경우에만 누가 무엇을 읽었는지 기록하여 그 범위의 독립 검토로 표현한다.

## 8. 필수 결과물 — 3개 문서 중심

### 8.1 `THESIS_v1.1.md` — 주 산출물

한국어로 작성한 출처 포함 통합 논지. 기존 원문을 복사하고 끝에 참고문헌만 늘리는 방식은 불충분하다. 서두에 하나의 중심 주장, 본문에 인과 메커니즘·관련 실증·주요 반론과 대응, 말미에 적용 범위·관측 지표·반증 조건을 제시한다.

확인된 사실/조건부 해석/전망을 읽는 사람이 구분할 수 있게 하되 본문 전체를 체크리스트로 만들지 않는다. 본문 제목과 결론은 증거에 맞추어 개정할 수 있다. 특정 도서·저자에 대한 해설이나 평가로 돌아가지 않는다.

### 8.2 `ARGUMENT_EVIDENCE.md` — 근거와 변경 기록

본문의 P01~P10 및 필요한 신규 명제를 실제 단락과 연결한다. 각 항목에 다음을 간결히 기록한다.

- 원 주장 → 개정 주장 → 변경 이유.
- 근거의 종류, 출처 식별자/정확한 위치, 읽은 범위와 독립성.
- 가장 강한 반론, 그에 대한 대응 또는 남은 제한.
- 성립 조건, 대안 설명, 반증·업데이트 조건.

기존 source_id는 재사용한다. 새 출처는 구별되는 식별자를 부여한다. 정확한 URL·판본·관측기간·접근일을 담은 참고문헌 원장을 이 문서에 포함하거나 기존 형식을 이어 `evidence/SOURCES.jsonl`로 둘 수 있다. 빈 형식 파일이나 불필요한 중복 원장을 양산하지 않는다.

### 8.3 `RESEARCH_RETURN_PACKET.md` — 웹챗 복귀

핵심은 다음과 같다.

1. 최종 중심 주장 1문단과 이전 논지에서 실질적으로 바뀐 내용.
2. 유지·조건부 수정·삭제·추가한 핵심 주장과 이유.
3. 실제로 새로 읽고 계산한 범위, 재사용한 근거, 원문 미열람/미재현 한계.
4. H10/H18/H23 및 핵심 반론의 현재 상태. 근거 없이 보류를 승격하지 않았는지.
5. 산출물 경로와 보존 commit A, 결과 commit 및 push 확인의 실제 상태.
6. 다음에 읽을 위치와 높은 가치의 미해결 질문. 완료한 작업 재실행을 요구하지 않는다.

분석을 실제로 수행한 경우에만 `analysis/`에 코드·입력·가공 결과·실행 명령·단위를 보존한다. 외부 raw 파일이 없으면 같은 빈티지 재현 가능성을 제한해서 기록한다.

자신을 포함한 최종 commit hash를 그 commit 내부 문서에 미리 기록할 수는 없다. 기록 문서에는 확인된 보존/분석 commit을 적고, 최종 commit과 원격 검증 결과는 실행 종료 후 실제 응답에 적는다. 자기참조 해시를 맞추려는 불필요한 commit 루프를 만들지 않는다.

## 9. 완료 기준과 중단 조건

**완료 기준:** 원문 보존 상태가 명확하고, 출처를 갖춘 개정 논증문이 존재하며, 핵심 인과 연결의 근거·반론·조건·한계가 추적 가능해야 한다. 문헌 수, 모든 가설 PASS, 모든 회귀 완전 재현이 완료 기준은 아니다.

단순 실행 성공이나 검사 통과를 의미적 진실의 인증으로 표현하지 않는다. 계산 검증·원문 열람·인과 식별·독립 검토를 구분한다.

접근·도구·실행 시간 제한이 생기면 완성한 파일과 아직 남은 부분을 보존한다. `THESIS_COMPLETED_WITH_LIMITATIONS`, `PARTIAL_WITH_CHECKPOINT`, `GIT_BLOCKED` 등 실제 상태를 기록한다. 계속하지 못하면서 무인 백그라운드 실행을 약속하지 않는다. 동일 접근 실패를 반복 호출하지 않는다.

실거래, 계좌·지갑 접속, 실제 지급·서명, 유료 서비스 구매, 자동매매 입력 승격, 운영전략/운영 코드 변경은 금지한다. HLOM 또는 다른 프로젝트의 과거 권한을 가져오지 않는다.

## 10. 최종 응답 형식

계획표가 아니라 다음을 한국어로 반환한다.

- **완성된 주장:** 가장 중요하게 보강된 통합 설명을 본문으로 제시한다.
- **핵심 변화:** 실제 수정된 논거·반론·불확실성을 짧게 설명한다.
- **실제 보존:** 저장소·branch·원문 보존 commit·최종 commit·push·원격 확인 상태·주 산출물 경로.
- **한계와 다음 시작점:** 현재 결론을 바꿀 가능성이 큰 증거가 무엇인지 명시한다.

모든 진행 보고 말미에 다음 형식으로 현재 위치를 표시한다.

`마일스톤: M0 원문 Git 보존 → M1 근거 매핑 → M2 목표 연구 → M3 통합 논지 → M4 보존·인계 | 현재: 실제 상태`

현재 패킷의 상태: **원문 및 요청서 작성 / 대상 Git 저장 미실행 / WORK 실행 미제출**.

<!-- END_FILE: research/macro-digital-money-ai/20260921/thesis-development/CODEX_WORK_REQUEST_v1.0_20260921.md -->

<!-- BEGIN_FILE: research/macro-digital-money-ai/20260921/thesis-development/THESIS_BASELINE_v1.0_20260921.md -->
# 달러경제의 기계화: AI와 디지털 화폐가 바꾸는 것은 돈의 종류보다 경제활동의 실행 방식이다

**AI와 디지털 화폐가 함께 만드는 핵심 변화는 새로운 돈을 대량으로 발행하는 것이 아니라, 사람이 직접 판단·조정·결제해야 했던 경제활동을 더 낮은 비용으로 실행할 수 있게 되는 것이다.**

이 과정에서 스테이블코인은 달러를 대체하기보다 **달러를 새로운 사용자와 소프트웨어 환경으로 확장하는 수단**이 된다. 그러나 거래가 늘어난다고 통화 잔액·국채 수요·자산 가격이 같은 비율로 증가하지는 않는다. 실제 경제적 가치는 **유용한 일을 신뢰할 수 있게 완료하는 비용이 얼마나 낮아지는가**에서 발생하고, 그 가치의 귀속은 **누가 고객·데이터·권한·유동성·이행 책임을 확보하는가**에 따라 달라진다.

이것이 지금까지의 논의를 연결해 제시하는 중심 주장입니다.

---

## 1. 변화의 출발점은 화폐가 아니라, 경제활동을 실행하는 비용이다

경제활동이 일어나지 않는 이유를 자금 부족으로만 설명할 수는 없습니다. 돈을 지불할 의향과 능력이 있어도, 거래를 찾아내고 수행하는 비용이 이익보다 크면 그 거래는 일어나지 않습니다.

가격을 비교하고, 상대방을 확인하고, 조건을 협의하고, 결과물을 검수하고, 문제가 생겼을 때 대응하는 일에도 비용이 듭니다. 작은 거래일수록 이러한 비용이 거래 자체의 가치보다 커질 수 있습니다.

이해를 위해 가상의 사례를 들어보겠습니다.

한 소규모 사업자가 매일 여러 공급업체의 가격과 납기를 비교하면 평균 3,000원의 이익을 더 얻을 수 있다고 가정합시다. 그런데 사람이 자료를 모으고 비교하는 데 들어가는 시간의 가치가 5,000원이라면 그 작업은 하지 않는 편이 낫습니다.

반면 AI와 기존 소프트웨어를 결합해 자료 수집·비교·검증·실행의 총비용을 1,000원으로 낮춘다면, 이전에는 하지 않았던 작업이 경제적으로 의미를 갖습니다.

여기서 생긴 변화는 돈의 발행이 아닙니다.

**원래 존재하던 필요가, 실행 비용의 하락으로 실제 경제활동이 된 것입니다.**

이 원리를 적용하면 AI의 경제적 의미가 달라집니다. AI가 인간처럼 독립적인 욕망을 가진 소비자로 등장해야 경제가 커지는 것이 아닙니다. 사람들이 원했지만 비용 때문에 포기했던 일을 더 많이 실행할 수 있게 되어도 경제의 범위는 넓어집니다.

실증 연구는 이 가능성의 출발점을 일부 뒷받침합니다. 고객지원 직원 5,172명을 분석한 연구에서는 AI 보조 도입 후 시간당 해결 건수가 평균 15% 증가했고, 효과는 숙련도에 따라 달랐습니다. 이것은 완전자율 에이전트 경제의 증거는 아니지만, **특정 업무에서 인간의 지식 접근과 수행 비용을 낮출 수 있다는 근거**입니다. ([arxiv.org](https://arxiv.org/abs/2304.11771))

따라서 AI 경제를 판단하는 첫 번째 질문은 “에이전트가 몇 개인가?”가 아닙니다.

> **이전에는 비용 때문에 하지 못했던 유용한 일을, 이제는 얼마의 총비용으로 완료할 수 있는가?**

물론 디지털 작업을 더 많이 수행했다는 사실만으로 사회 전체의 부가가치가 같은 만큼 증가하지는 않습니다. 기존 작업을 대체했는지, 새로운 서비스를 만들었는지, 품질이 개선됐는지, 절약한 시간이 다른 생산적 활동으로 이어졌는지를 봐야 합니다. 연준 연구진도 과업 단위의 개선과 기업·산업·경제 전체의 생산성을 구분하며, 조직의 조정 비용과 다른 생산 병목이 개별 과업의 개선을 상쇄할 수 있다고 설명합니다. ([federalreserve.gov](https://www.federalreserve.gov/econres/notes/feds-notes/the-ai-buildout-and-the-economy-publicly-available-data-to-assess-ais-impact-20260717.html))

**그러므로 이 주장의 출발점은 ‘AI가 모든 것을 자동화한다’가 아니라, ‘AI가 경제적으로 실행 가능한 활동의 경계를 바꾼다’입니다.**

## 2. 실행 비용이 낮아질수록, 결제와 권한이 새로운 제약으로 드러난다

AI가 필요한 서비스를 찾아내고 가격을 비교할 수 있다고 해도, 실제로 돈을 쓰는 순간에는 다른 문제가 등장합니다.

어떤 서비스까지 구매해도 되는가? 얼마까지 지출할 수 있는가? 같은 주문을 중복해서 실행하지 않았는가? 약속한 결과를 받지 못하면 누가 대응하는가?

예를 들어 리서치 에이전트가 외부 데이터를 구매했다고 합시다. 결제가 성공했다는 사실은 확인할 수 있어도, 그것만으로 데이터가 최신인지, 필요한 사용권을 포함하는지, 내용이 정확한지까지 확인되지는 않습니다.

**송금의 성공과 경제활동의 성공은 다릅니다.**

이 구분 때문에 AI 경제의 기반은 결제 API 하나로 완성되지 않습니다. 사용자의 의도, 에이전트의 권한, 예산, 주문, 결제, 서비스 제공, 오류 처리까지 연결되어야 합니다.

AP2가 권한 부여·사용자 의도의 확인·책임 소재를 핵심 문제로 다루고, 서명된 거래·지급 위임을 연결하는 구조를 제시하는 이유도 여기에 있습니다. 이는 단순한 송금 규격보다 **사람이 직접 버튼을 누르지 않는 거래를 어떻게 신뢰할 것인가**에 가까운 문제입니다. ([ap2-protocol.org](https://ap2-protocol.org/))

여기서 한 단계 더 나아갈 수 있습니다.

**AI가 판단과 실행의 비용을 낮출수록, 남아 있는 검증·권한·책임 비용의 중요성이 상대적으로 커집니다.**

자료를 생성하는 비용이 크게 낮아졌는데 사람이 모든 결과를 처음부터 다시 검사해야 한다면, 전체 비용은 충분히 낮아지지 않습니다. 결제는 자동화했지만 오류 한 건을 해결하는 데 며칠이 걸린다면, 작은 거래를 대규모로 수행하기 어렵습니다.

따라서 경쟁력의 기준도 바뀝니다.

가장 많은 답변을 생성하는 시스템보다, **정해진 권한 안에서 유용한 결과를 만들고, 그 결과를 확인하고, 문제가 생겼을 때 복구하는 총비용이 낮은 시스템**이 더 높은 경제적 가치를 만들 수 있습니다.

이것은 검증을 무한히 늘리자는 이야기가 아닙니다. 오히려 반대입니다. 거래의 위험과 금액에 맞추어 검증을 표준화하고 자동화해, 사람이 매번 처음부터 확인해야 하는 비용을 줄여야 한다는 뜻입니다.

**AI 경제가 확장되려면 지능뿐 아니라, 신뢰를 확보하는 과정도 저렴해져야 합니다.**

## 3. 이 경제는 새로운 화폐보다, 기존 화폐를 더 쉽게 사용하는 방식을 먼저 요구한다

여기서 달러와 스테이블코인이 연결됩니다.

국경을 넘는 서비스 거래를 자동화하려는 사업자에게 당장의 문제는 반드시 새로운 가치 단위를 만드는 것이 아닙니다. 이미 사용하는 가격·회계·자금조달 체계 안에서 더 편하게 거래하는 것이 중요할 수 있습니다.

달러는 국제 결제와 자금조달에서 광범위하게 사용되고 있습니다. 2026년 7월 연준의 국제 달러 회의 정리도 스테이블코인을 별개의 독립 경제라기보다, 기존 달러 수요를 새로운 접근·이전·보유 경로로 연결하는 현상으로 설명합니다. ([federalreserve.gov](https://www.federalreserve.gov/econres/notes/feds-notes/fifth-conference-on-the-international-roles-of-the-u-s-dollar-stablecoins-digital-payments-and-the-ir-of-the-usd-20260716.html))

여기서 도출되는 해석은 다음과 같습니다.

> **달러를 사용하는 이유는 유지하면서, 달러에 접근하고 이전하고 조건부로 집행하는 방식만 바꿀 수 있다.**

달러 스테이블코인은 이 분리를 보여주는 한 가지 형태입니다. 가격의 기준은 달러지만, 보유·이전 방식은 블록체인 기반일 수 있습니다. 다만 같은 달러 표시라고 해서 은행예금과 특정 발행사의 토큰이 동일한 청구권이나 위험을 갖는 것은 아닙니다. BIS 역시 화폐의 가치 표시 단위와 실제로 보유하는 발행사별 청구권을 구분합니다. ([bis.org](https://www.bis.org/publications/aer-2025/next-generation-monetary-financial-system))

이렇게 보면 “블록체인이 성장하면 달러가 쇠퇴한다”는 설명보다, **“블록체인이 달러를 유통하는 새로운 기반이 될 수 있다”**는 설명이 더 자연스러워집니다. BIS의 2026년 연구도 달러 표시 스테이블코인의 비중과 사용 구조를 근거로, 초기에는 기존 통화 질서를 강화하는 방향이 나타날 수 있다고 분석합니다. ([bis.org](https://www.bis.org/publications/paper-170-impact-stablecoins-international-monetary-and-financial-system))

그렇다고 모든 경제활동이 달러로 바뀐다는 뜻은 아닙니다. 원화로 수입과 지출을 하는 국내 거래에서 달러를 거치는 것은 불필요한 환전과 환위험을 추가할 수 있습니다.

따라서 이 주장의 적용 범위는 특히 **국경 간 디지털 서비스, 달러 접근성이 중요한 사용자, 서로 다른 금융·소프트웨어 환경을 연결하는 거래**입니다.

스테이블코인이 맡을 수 있는 역할은 “세상의 돈을 모두 교체하는 것”보다 구체적입니다.

**기존 달러 체계를 사용하기 어려웠던 사람과 프로그램이, 달러로 거래할 수 있는 범위를 넓히는 것입니다.**

## 4. 그러나 달러경제의 기계화가 반드시 온체인 경제를 뜻하지는 않는다

이 주장을 스테이블코인 중심의 낙관론으로 오해해서는 안 됩니다.

경제주체가 원하는 것은 특정 결제 기술의 사용 자체가 아니라, 필요한 거래를 적절한 비용과 위험으로 완료하는 것입니다. 카드, 은행이체, 기업 간 월말 정산, 스테이블코인 중 무엇을 선택할지는 그 목적에 따라 달라집니다.

실제로 AP2에는 사람이 실시간으로 개입하지 않는 카드 결제와 x402 결제 예제가 모두 존재합니다. **자동화된 구매와 블록체인 결제는 분리 가능한 선택**입니다. ([ap2-protocol.org](https://ap2-protocol.org/))

가상의 기업이 매일 같은 데이터 제공자의 API를 수만 번 사용한다고 생각해보겠습니다. 호출마다 외부 결제를 실행하는 것보다 사용량을 기록했다가 월말에 한 번 정산하는 편이 간단할 수 있습니다.

반대로 거래 관계가 없던 여러 해외 서비스에서 작은 금액의 데이터를 그때그때 구매한다면, 계정 개설과 계약 체결을 반복하지 않는 결제 방식이 유리할 수 있습니다.

따라서 경쟁은 “카드인가 코인인가”라는 이름 사이에서 벌어지는 것이 아닙니다.

**접근·환전·자금 보유·수수료·오류·환불·회계까지 포함한 총비용 사이에서 벌어집니다.**

연준의 국경 간 스테이블코인 분석도 온체인 전송 비용만으로 전체 효율을 판단하지 않습니다. 법정화폐와의 전환 비용, 외환 처리, 기존 중개기관의 규모의 경제가 결과를 바꿀 수 있다고 설명합니다. ([federalreserve.gov](https://www.federalreserve.gov/econres/notes/feds-notes/payment-stablecoins-and-cross-border-payments-benefits-and-implications-for-monetary-policy-20260330.html))

이로부터 중요한 결론이 나옵니다.

**새로운 결제 기술은 기존 금융기관을 모두 없애기보다, 기존에 한 기관이 묶어서 제공하던 기능을 분리하고 재조합할 가능성이 있습니다.**

어떤 기관은 고객 접점을 유지하고, 다른 기관은 유동성을 공급하고, 또 다른 사업자는 권한 관리와 정산을 담당할 수 있습니다. 반대로 이 기능을 통합한 대형 플랫폼이 규모의 경제를 확보할 수도 있습니다.

그러므로 탈중앙화든 재집중이든 기술만으로 결과가 결정되지 않습니다. **어떤 구조가 더 낮은 총비용으로 신뢰할 수 있는 거래를 제공하느냐**가 결정적인 질문입니다.

## 5. 가장 중요한 역설: 경제활동이 늘어도 필요한 화폐 잔액은 덜 늘 수 있다

이 지점이 기존의 단순한 상승 서사와 가장 크게 갈라지는 부분입니다.

AI가 처리하는 유료 작업이 늘고 결제가 빨라지면, 경제활동이 늘어날 수 있습니다. 그러나 그것을 처리하기 위해 같은 비율의 스테이블코인을 계속 보유해야 하는 것은 아닙니다.

사전예치 기반의 단순한 운영모형을 생각하면 다음과 같이 표현할 수 있습니다.

\[
\text{필요한 결제용 잔액}
\approx
\text{하루 실제 정산금액}
\times
\text{자금이 묶이는 평균 일수}
+
\text{예비유동성}
\]

이는 전체 통화 수요를 설명하는 법칙이 아니라, 결제용 자금의 필요량을 이해하기 위한 근사식입니다. 저축·투자·담보 목적으로 보유하는 잔액은 별도입니다.

가령 예비유동성을 제외하고 하루 1억 원을 처리하는 데 자금이 평균 하루 묶인다면, 필요한 운영 잔액은 약 1억 원입니다.

기술 개선 후 하루 거래가 3억 원으로 늘어도 자금이 묶이는 시간이 0.1일로 줄면, 같은 모형에서 필요한 운영 잔액은 약 3,000만 원입니다.

**거래는 세 배가 되었지만, 필요한 잔액은 줄었습니다.**

이것은 기술의 실패가 아닙니다. 오히려 더 적은 자금으로 더 많은 거래를 처리하는 자본 효율의 개선입니다.

물론 실제 스테이블코인 잔액은 결제 외에 저축과 달러 보유 수요 때문에 증가할 수 있습니다. BIS 연구도 스테이블코인의 교환수단 역할과 가치저장 역할을 구분합니다. 중요한 것은 이 수요들을 하나로 합쳐 거래량에서 곧바로 잔액을 추정하지 않는 것입니다. ([bis.org](https://www.bis.org/publications/paper-170-impact-stablecoins-international-monetary-and-financial-system))

따라서 다음 세 가지는 서로 다른 성공 지표입니다.

**경제활동의 증가, 결제 서비스의 확산, 결제용 자산의 보유 잔액 증가.**

이 구분을 받아들이면 투자 해석도 달라집니다. 결제 기술이 성공했는데 발행사 준비금이 기대만큼 늘지 않을 수 있습니다. 네트워크 사용량이 늘었는데 거래당 수수료가 낮아져 총수익은 덜 늘 수도 있습니다.

**좋은 기술이 반드시 그 기술과 관련된 모든 자산에 좋은 투자 결과를 주는 것은 아닙니다.**

## 6. 미국 국채와의 연결은 존재하지만, 이 변화의 본체는 아니다

스테이블코인 발행사가 준비자산으로 단기국채를 보유하면, 결제와 달러 보유 수요가 국채시장에 연결됩니다. 이 경로는 실제로 중요합니다.

하지만 여기에는 두 개의 구분이 필요합니다.

먼저 **자산의 형태를 바꾸는 것과 신용을 새로 공급하는 것은 다릅니다.** 영란은행이 설명하는 상업은행의 대출·예금 생성과, 기존 자금을 받아 준비자산을 매입하는 발행 구조는 같은 과정이 아닙니다. ([bankofengland.co.uk](https://www.bankofengland.co.uk/quarterly-bulletin/2014/q1/money-creation-in-the-modern-economy))

또한 **발행사의 국채 보유 증가와 경제 전체의 추가 수요는 다릅니다.** 사용자가 기존 MMF나 직접 보유 국채를 줄이고 토큰으로 이동했다면 상당 부분은 보유 주체의 교체일 수 있습니다. 발행사에 국채를 판 투자자가 무엇을 다시 매입하는지도 중요합니다. 연준의 대차대조표 분석은 이러한 다른 투자자와 은행의 조정이 초기 효과를 일부 상쇄할 수 있다고 설명합니다. ([federalreserve.gov](https://www.federalreserve.gov/econres/notes/feds-notes/payment-stablecoins-and-cross-border-payments-benefits-and-implications-for-monetary-policy-20260330.html))

그렇다고 가격 효과가 없다는 뜻은 아닙니다. 보유 주체의 가격 민감도와 선호 만기가 달라지면, 총량의 큰 변화 없이도 가격이 움직일 수 있습니다. BIS 연구는 특정 식별 가정 아래 스테이블코인 유입의 단기국채 금리 효과를 보고하지만, 긴 만기로의 파급은 제한적이라고 설명합니다. ([bis.org](https://www.bis.org/publications/working-paper-1270-stablecoins-and-safe-asset-prices))

따라서 이 연구의 본론은 다음처럼 정리하는 것이 맞습니다.

**스테이블코인은 달러 자산을 보유하고 거래하는 기반을 넓힐 수 있다. 그러나 국가부채를 감당하는 능력은 금융자산의 유통 방식만으로 만들어지지 않는다.**

AI가 국가경제에 더 근본적으로 기여하는 경로는 실제 생산성과 소득의 증가입니다. 같은 노동과 자본으로 더 많은 유용한 결과를 만든다면 경제의 부채 부담을 감당할 기반이 커질 수 있습니다. 반면 결제만 빨라지고 최종 생산이나 소득이 늘지 않는다면 그 효과는 다릅니다.

여기서 AI와 스테이블코인은 같은 역할을 하지 않습니다.

**AI는 생산과 조정의 비용을 낮추는 쪽이고, 디지털 결제는 교환과 자금 운용의 비용을 낮추는 쪽입니다.**

둘이 결합하면 효율을 높일 수 있지만, 그 결과가 장기금리 하락으로만 나타나지는 않습니다. 생산성과 투자 기회가 커지면서 자금 수요가 늘 수도 있기 때문입니다. 자산 가격은 이익 증가와 할인율 변화가 함께 작용한 결과입니다.

그러므로 “AI가 발전하니 스테이블코인이 늘고, 미국의 부채 부담이 줄고, 모든 위험자산이 오른다”는 설명보다 다음 설명이 더 일관됩니다.

> **AI와 디지털 금융은 경제의 생산·거래 효율을 바꾼다. 국채 수요와 자산 가격은 그 변화가 금융시장에 전달되는 여러 결과 중 하나다.**

## 7. 비트코인과 투자 가치도 이 구조 안에서 역할을 분리해야 한다

이 설명에서 비트코인이 사라지는 것은 아닙니다. 다만 비트코인을 모든 변화의 필수적인 기반으로 놓을 필요가 없어집니다.

비트코인의 공급 규칙과 발행 주체에 대한 의존 구조는 달러 스테이블코인과 다릅니다. 동시에 공급 규칙이 제한되어 있다는 사실이 가격 안정이나 수익을 보장하지는 않습니다. 비트코인 설명 문서도 가격이 수요·공급에 따라 움직이며 구매력이 보장되지 않는다고 명시합니다. ([bitcoin.org](https://bitcoin.org/en/faq))

비트코인에 관한 경제적 질문은 다음에 가깝습니다.

**사람들은 국가나 특정 발행사의 채무가 아닌 디지털 자산을 보유하는 데 얼마의 가치를 부여하는가?**

스테이블코인에 관한 질문은 다릅니다.

**사람들은 달러를 더 쉽게 보유하고 이전하는 기능에 얼마의 가치를 부여하는가?**

한 사람이 일상적인 거래에는 달러 기반 결제를 사용하면서, 자산 배분의 일부로 비트코인을 보유하는 것은 논리적으로 모순되지 않습니다. 반대로 달러 기반 디지털 거래가 커진다는 사실만으로 비트코인 수요 증가를 설명할 수도 없습니다.

블록체인 네트워크와 기업의 투자 가치는 다시 나누어야 합니다.

사업이 유용하다는 사실과 그 사업자가 높은 이익을 남긴다는 사실은 다릅니다. 경쟁이 치열해지면 효율 개선의 대부분이 더 낮은 가격으로 고객에게 돌아갈 수 있습니다. 개방형 표준이 널리 쓰이더라도 특정 사업자가 그 표준을 독점적으로 수익화하지 못할 수 있습니다.

따라서 **“인프라가 중요하니 인프라 관련 자산을 사면 된다”**는 결론도 충분하지 않습니다.

어떤 인프라는 필수적이지만 대체가 쉽고, 어떤 인프라는 사용량이 적어도 대체가 어렵습니다. 어떤 기업은 고객과 유통망을 확보하고, 어떤 기업은 동일한 서비스를 제공하기 위해 계속 비용을 지불해야 합니다.

이 주장에서 투자 가치의 분석 기준은 다음입니다.

> **경제활동을 완료하는 총비용을 실제로 낮추는가? 그리고 그 과정에서 만들어진 이익의 일부를 경쟁 이후에도 지속적으로 확보할 수 있는가?**

기업과 현금흐름형 자산에는 이 질문이 직접 적용됩니다. 비트코인과 같은 비현금흐름 자산은 별도로 화폐적 편익·희소성·유동성에 대한 수요를 분석해야 합니다. 모든 자산을 한 가지 평가 방식으로 처리해서는 안 됩니다.

## 8. 이 주장이 맞다면, 가장 먼저 나타날 변화는 무엇인가

이 설명은 막연한 미래 서사가 아니라 몇 가지 구체적인 예상을 만들어냅니다.

**먼저, 결과를 확인하기 쉬운 업무에서 위임이 확산될 것입니다.** 무엇을 완료했는지 명확하고, 오류의 비용을 제한할 수 있으며, 기존 시스템과 연결하기 쉬운 작업이 유리합니다. 어려운 판단을 모두 자동화하는 것보다, 완료 기준이 분명한 작업의 총비용을 낮추는 곳에서 경제성이 먼저 나타날 것이라는 예측입니다.

**다음으로, 결제수단은 사용자에게 덜 중요하게 보일 수 있습니다.** 사용자가 “어느 체인을 쓸까”를 고르는 대신, 시스템이 허용된 수단 중 비용·접근성·실패 위험을 비교해 선택하는 방향입니다. 이 경우 실제 사용량은 늘어도 사용자의 코인에 대한 관심이나 직접 보유는 같은 속도로 늘지 않을 수 있습니다.

**마지막으로, 가치의 중심은 생성량보다 완료율과 반복 사용으로 이동할 것입니다.** 많은 요청을 처리하는 서비스보다, 고객이 실제 결과를 얻고 다시 비용을 지불하는 서비스가 경제적 지속성을 보여줄 것입니다. 필요한 지표도 에이전트 수나 주소 수보다, 품질을 충족한 완료 작업당 총비용과 고객의 반복 구매에 가까워집니다.

반대로 에이전트가 더 많은 오류와 검토 부담을 만들고, 결제·분쟁 처리까지 포함한 총비용이 줄지 않는다면 이 주장은 약해집니다. **주장의 중심 변수가 통화량이나 기술 시연이 아니라 ‘유효한 완료의 비용’이기 때문입니다.**

---

## 결론: 새로운 돈보다 중요한 것은, 돈으로 실행할 수 있는 일의 범위다

이 연구에서 발전시킬 수 있는 가장 일관된 주장은 **달러의 붕괴나 코인의 일괄적인 상승**이 아닙니다.

**AI는 사람이 직접 처리해야 했던 판단과 조정을 일부 위임할 수 있게 하고, 디지털 금융은 그 결과를 결제와 계약 실행으로 연결한다. 이 결합이 충분히 저렴하고 신뢰할 수 있게 되면, 기존에는 비용 때문에 실행되지 않았던 경제활동이 가능해진다.**

달러는 이 변화 속에서 사라져야 하는 대상이 아닙니다. 기존의 가격·유동성·자금조달 기반을 제공하면서 새로운 방식으로 사용될 수 있습니다. 스테이블코인은 그 확장 수단 중 하나이며, 기존 은행·카드·토큰화 예금과 경쟁하거나 결합할 수 있습니다.

그러나 경제활동의 확대와 자산 가격 상승은 같은 문장이 아닙니다. 더 빠른 결제는 오히려 필요한 잔액을 줄일 수 있고, 더 좋은 기술은 경쟁을 통해 사업자의 이익을 낮추면서 소비자에게 더 큰 편익을 줄 수도 있습니다.

따라서 앞으로 추적해야 할 것은 단순히 **돈이 얼마나 발행되는가**가 아닙니다.

**어떤 일을 새롭게 실행할 수 있게 되었는가, 그 일을 끝내는 총비용은 얼마나 낮아졌는가, 그리고 그 과정에서 만들어진 가치는 누구에게 돌아가는가**입니다.

> **AI 시대 금융의 핵심은 ‘어떤 코인이 돈이 되는가’보다, ‘누구의 의도를 어떤 권한과 비용으로 신뢰할 수 있게 실행하는가’에 있다. 달러의 디지털화, 에이전트 결제, 국채 수요, 인프라의 가치는 이 변화 안에서 각각의 역할을 갖는다.**

<!-- END_FILE: research/macro-digital-money-ai/20260921/thesis-development/THESIS_BASELINE_v1.0_20260921.md -->

<!-- BEGIN_FILE: research/macro-digital-money-ai/20260921/thesis-development/INPUT_PROVENANCE.json -->
{
  "packet_id": "MDMA-THESIS-WORK-20260921-001",
  "date_label": "2026-09-21",
  "user_intent": "Preserve the current thesis in Git, then ask Codex WORK to verify, strengthen and supplement it into one sourced argument.",
  "baseline": {
    "file": "THESIS_BASELINE_v1.0_20260921.md",
    "source": "Immediately preceding assistant thesis in this conversation",
    "scope": "Full thesis body, including existing links and illustrative examples",
    "status": "Candidate argument, not independently established in this packaging task",
    "sha256": "8f1fa519e496182d5a168926dc879be0909d6eba3af61eed4c472fe610083325",
    "semantic_editing_in_packaging": "None intended; UTF-8/LF transcription from the conversation"
  },
  "repository": {
    "name": "AofSpds/crypto_compute_dolor",
    "local_path_from_user": "C:\\Users\\ms1pk\\dev\\rsch\\crypto_compute_dolor",
    "branch_from_user": "codex/mdma-research-20260921",
    "full_research_commit_from_user": "39d5cbed92459b55b70e0dd7ba231584a4e75b73",
    "previous_final_commit_from_user": "c7ee7a6444097195155b03fc5b671d4b871b0183",
    "metadata_verification_this_turn": "NOT_VERIFIED",
    "destination": "research/macro-digital-money-ai/20260921/thesis-development"
  },
  "webchat_execution_status": {
    "target_repo_read": "NOT_PERFORMED",
    "target_repo_write": "NOT_PERFORMED",
    "target_git_commit": "NOT_PERFORMED",
    "target_git_push": "NOT_PERFORMED",
    "codex_work_submission": "NOT_SUBMITTED",
    "new_external_research": "NOT_PERFORMED",
    "new_independent_research_review": "NOT_PERFORMED",
    "artifact_creation": "PERFORMED_IN_CHATGPT_CONTAINER"
  },
  "access_boundary": {
    "available_hef_workspace": "C:\\Users\\ms1pk\\dev\\AAA\\hef-work",
    "target_repo_in_registered_workspace": false,
    "boundary_bypass_authorized": false,
    "handoff_execution_location": "Codex WORK session with legitimate access to the target repository"
  },
  "inherited_external_review": {
    "source_archive_name": "MDMA_EXTERNAL_REVIEW_20260921.zip",
    "source_archive_sha256": "197dfff0674adcce84f691482fc7646a02a93ebdf255d7dd23164abdec13840e",
    "preserved_file_count": 7,
    "destination": "inputs/external-review/",
    "verification_this_turn": "Byte-preservation checks only; no new verification of claims, source contents, code outputs or regressions",
    "instructions_inside": "Historical records, not current operational authority"
  },
  "git_write_scope_for_work": {
    "purpose": "Commit and normal-push the baseline, this request, and directly related research outputs to the research branch",
    "forbidden": [
      "main merge",
      "force push",
      "branch deletion",
      "unrelated edits",
      "credential changes",
      "access boundary bypass",
      "live financial transactions"
    ]
  }
}

<!-- END_FILE: research/macro-digital-money-ai/20260921/thesis-development/INPUT_PROVENANCE.json -->

<!-- BEGIN_FILE: research/macro-digital-money-ai/20260921/thesis-development/BASELINE_CITATION_SEEDS.json -->
{
  "schema_version": "1.0",
  "baseline_file": "THESIS_BASELINE_v1.0_20260921.md",
  "unique_url_count": 10,
  "not_a_verified_source_register": true,
  "sources": [
    {
      "seed_id": "BS001",
      "url": "https://arxiv.org/abs/2304.11771",
      "provenance": "Link inherited from the immediately preceding webchat thesis",
      "verification_in_this_packaging_turn": "NOT_PERFORMED",
      "use": "Discovery seed; verify source existence, edition and claim support in Codex WORK",
      "baseline_occurrences": [
        {
          "line": 29,
          "paragraph": "실증 연구는 이 가능성의 출발점을 일부 뒷받침합니다. 고객지원 직원 5,172명을 분석한 연구에서는 AI 보조 도입 후 시간당 해결 건수가 평균 15% 증가했고, 효과는 숙련도에 따라 달랐습니다. 이것은 완전자율 에이전트 경제의 증거는 아니지만, **특정 업무에서 인간의 지식 접근과 수행 비용을 낮출 수 있다는 근거**입니다. ([arxiv.org](https://arxiv.org/abs/2304.11771))"
        }
      ]
    },
    {
      "seed_id": "BS002",
      "url": "https://www.federalreserve.gov/econres/notes/feds-notes/the-ai-buildout-and-the-economy-publicly-available-data-to-assess-ais-impact-20260717.html",
      "provenance": "Link inherited from the immediately preceding webchat thesis",
      "verification_in_this_packaging_turn": "NOT_PERFORMED",
      "use": "Discovery seed; verify source existence, edition and claim support in Codex WORK",
      "baseline_occurrences": [
        {
          "line": 35,
          "paragraph": "물론 디지털 작업을 더 많이 수행했다는 사실만으로 사회 전체의 부가가치가 같은 만큼 증가하지는 않습니다. 기존 작업을 대체했는지, 새로운 서비스를 만들었는지, 품질이 개선됐는지, 절약한 시간이 다른 생산적 활동으로 이어졌는지를 봐야 합니다. 연준 연구진도 과업 단위의 개선과 기업·산업·경제 전체의 생산성을 구분하며, 조직의 조정 비용과 다른 생산 병목이 개별 과업의 개선을 상쇄할 수 있다고 설명합니다. ([federalreserve.gov](https://www.federalreserve.gov/econres/notes/feds-notes/the-ai-buildout-and-the-economy-publicly-available-data-to-assess-ais-impact-20260717.html))"
        }
      ]
    },
    {
      "seed_id": "BS003",
      "url": "https://ap2-protocol.org/",
      "provenance": "Link inherited from the immediately preceding webchat thesis",
      "verification_in_this_packaging_turn": "NOT_PERFORMED",
      "use": "Discovery seed; verify source existence, edition and claim support in Codex WORK",
      "baseline_occurrences": [
        {
          "line": 51,
          "paragraph": "AP2가 권한 부여·사용자 의도의 확인·책임 소재를 핵심 문제로 다루고, 서명된 거래·지급 위임을 연결하는 구조를 제시하는 이유도 여기에 있습니다. 이는 단순한 송금 규격보다 **사람이 직접 버튼을 누르지 않는 거래를 어떻게 신뢰할 것인가**에 가까운 문제입니다. ([ap2-protocol.org](https://ap2-protocol.org/))"
        },
        {
          "line": 97,
          "paragraph": "실제로 AP2에는 사람이 실시간으로 개입하지 않는 카드 결제와 x402 결제 예제가 모두 존재합니다. **자동화된 구매와 블록체인 결제는 분리 가능한 선택**입니다. ([ap2-protocol.org](https://ap2-protocol.org/))"
        }
      ]
    },
    {
      "seed_id": "BS004",
      "url": "https://www.federalreserve.gov/econres/notes/feds-notes/fifth-conference-on-the-international-roles-of-the-u-s-dollar-stablecoins-digital-payments-and-the-ir-of-the-usd-20260716.html",
      "provenance": "Link inherited from the immediately preceding webchat thesis",
      "verification_in_this_packaging_turn": "NOT_PERFORMED",
      "use": "Discovery seed; verify source existence, edition and claim support in Codex WORK",
      "baseline_occurrences": [
        {
          "line": 73,
          "paragraph": "달러는 국제 결제와 자금조달에서 광범위하게 사용되고 있습니다. 2026년 7월 연준의 국제 달러 회의 정리도 스테이블코인을 별개의 독립 경제라기보다, 기존 달러 수요를 새로운 접근·이전·보유 경로로 연결하는 현상으로 설명합니다. ([federalreserve.gov](https://www.federalreserve.gov/econres/notes/feds-notes/fifth-conference-on-the-international-roles-of-the-u-s-dollar-stablecoins-digital-payments-and-the-ir-of-the-usd-20260716.html))"
        }
      ]
    },
    {
      "seed_id": "BS005",
      "url": "https://www.bis.org/publications/aer-2025/next-generation-monetary-financial-system",
      "provenance": "Link inherited from the immediately preceding webchat thesis",
      "verification_in_this_packaging_turn": "NOT_PERFORMED",
      "use": "Discovery seed; verify source existence, edition and claim support in Codex WORK",
      "baseline_occurrences": [
        {
          "line": 79,
          "paragraph": "달러 스테이블코인은 이 분리를 보여주는 한 가지 형태입니다. 가격의 기준은 달러지만, 보유·이전 방식은 블록체인 기반일 수 있습니다. 다만 같은 달러 표시라고 해서 은행예금과 특정 발행사의 토큰이 동일한 청구권이나 위험을 갖는 것은 아닙니다. BIS 역시 화폐의 가치 표시 단위와 실제로 보유하는 발행사별 청구권을 구분합니다. ([bis.org](https://www.bis.org/publications/aer-2025/next-generation-monetary-financial-system))"
        }
      ]
    },
    {
      "seed_id": "BS006",
      "url": "https://www.bis.org/publications/paper-170-impact-stablecoins-international-monetary-and-financial-system",
      "provenance": "Link inherited from the immediately preceding webchat thesis",
      "verification_in_this_packaging_turn": "NOT_PERFORMED",
      "use": "Discovery seed; verify source existence, edition and claim support in Codex WORK",
      "baseline_occurrences": [
        {
          "line": 81,
          "paragraph": "이렇게 보면 “블록체인이 성장하면 달러가 쇠퇴한다”는 설명보다, **“블록체인이 달러를 유통하는 새로운 기반이 될 수 있다”**는 설명이 더 자연스러워집니다. BIS의 2026년 연구도 달러 표시 스테이블코인의 비중과 사용 구조를 근거로, 초기에는 기존 통화 질서를 강화하는 방향이 나타날 수 있다고 분석합니다. ([bis.org](https://www.bis.org/publications/paper-170-impact-stablecoins-international-monetary-and-financial-system))"
        },
        {
          "line": 145,
          "paragraph": "물론 실제 스테이블코인 잔액은 결제 외에 저축과 달러 보유 수요 때문에 증가할 수 있습니다. BIS 연구도 스테이블코인의 교환수단 역할과 가치저장 역할을 구분합니다. 중요한 것은 이 수요들을 하나로 합쳐 거래량에서 곧바로 잔액을 추정하지 않는 것입니다. ([bis.org](https://www.bis.org/publications/paper-170-impact-stablecoins-international-monetary-and-financial-system))"
        }
      ]
    },
    {
      "seed_id": "BS007",
      "url": "https://www.federalreserve.gov/econres/notes/feds-notes/payment-stablecoins-and-cross-border-payments-benefits-and-implications-for-monetary-policy-20260330.html",
      "provenance": "Link inherited from the immediately preceding webchat thesis",
      "verification_in_this_packaging_turn": "NOT_PERFORMED",
      "use": "Discovery seed; verify source existence, edition and claim support in Codex WORK",
      "baseline_occurrences": [
        {
          "line": 107,
          "paragraph": "연준의 국경 간 스테이블코인 분석도 온체인 전송 비용만으로 전체 효율을 판단하지 않습니다. 법정화폐와의 전환 비용, 외환 처리, 기존 중개기관의 규모의 경제가 결과를 바꿀 수 있다고 설명합니다. ([federalreserve.gov](https://www.federalreserve.gov/econres/notes/feds-notes/payment-stablecoins-and-cross-border-payments-benefits-and-implications-for-monetary-policy-20260330.html))"
        },
        {
          "line": 163,
          "paragraph": "또한 **발행사의 국채 보유 증가와 경제 전체의 추가 수요는 다릅니다.** 사용자가 기존 MMF나 직접 보유 국채를 줄이고 토큰으로 이동했다면 상당 부분은 보유 주체의 교체일 수 있습니다. 발행사에 국채를 판 투자자가 무엇을 다시 매입하는지도 중요합니다. 연준의 대차대조표 분석은 이러한 다른 투자자와 은행의 조정이 초기 효과를 일부 상쇄할 수 있다고 설명합니다. ([federalreserve.gov](https://www.federalreserve.gov/econres/notes/feds-notes/payment-stablecoins-and-cross-border-payments-benefits-and-implications-for-monetary-policy-20260330.html))"
        }
      ]
    },
    {
      "seed_id": "BS008",
      "url": "https://www.bankofengland.co.uk/quarterly-bulletin/2014/q1/money-creation-in-the-modern-economy",
      "provenance": "Link inherited from the immediately preceding webchat thesis",
      "verification_in_this_packaging_turn": "NOT_PERFORMED",
      "use": "Discovery seed; verify source existence, edition and claim support in Codex WORK",
      "baseline_occurrences": [
        {
          "line": 161,
          "paragraph": "먼저 **자산의 형태를 바꾸는 것과 신용을 새로 공급하는 것은 다릅니다.** 영란은행이 설명하는 상업은행의 대출·예금 생성과, 기존 자금을 받아 준비자산을 매입하는 발행 구조는 같은 과정이 아닙니다. ([bankofengland.co.uk](https://www.bankofengland.co.uk/quarterly-bulletin/2014/q1/money-creation-in-the-modern-economy))"
        }
      ]
    },
    {
      "seed_id": "BS009",
      "url": "https://www.bis.org/publications/working-paper-1270-stablecoins-and-safe-asset-prices",
      "provenance": "Link inherited from the immediately preceding webchat thesis",
      "verification_in_this_packaging_turn": "NOT_PERFORMED",
      "use": "Discovery seed; verify source existence, edition and claim support in Codex WORK",
      "baseline_occurrences": [
        {
          "line": 165,
          "paragraph": "그렇다고 가격 효과가 없다는 뜻은 아닙니다. 보유 주체의 가격 민감도와 선호 만기가 달라지면, 총량의 큰 변화 없이도 가격이 움직일 수 있습니다. BIS 연구는 특정 식별 가정 아래 스테이블코인 유입의 단기국채 금리 효과를 보고하지만, 긴 만기로의 파급은 제한적이라고 설명합니다. ([bis.org](https://www.bis.org/publications/working-paper-1270-stablecoins-and-safe-asset-prices))"
        }
      ]
    },
    {
      "seed_id": "BS010",
      "url": "https://bitcoin.org/en/faq",
      "provenance": "Link inherited from the immediately preceding webchat thesis",
      "verification_in_this_packaging_turn": "NOT_PERFORMED",
      "use": "Discovery seed; verify source existence, edition and claim support in Codex WORK",
      "baseline_occurrences": [
        {
          "line": 187,
          "paragraph": "비트코인의 공급 규칙과 발행 주체에 대한 의존 구조는 달러 스테이블코인과 다릅니다. 동시에 공급 규칙이 제한되어 있다는 사실이 가격 안정이나 수익을 보장하지는 않습니다. 비트코인 설명 문서도 가격이 수요·공급에 따라 움직이며 구매력이 보장되지 않는다고 명시합니다. ([bitcoin.org](https://bitcoin.org/en/faq))"
        }
      ]
    }
  ]
}

<!-- END_FILE: research/macro-digital-money-ai/20260921/thesis-development/BASELINE_CITATION_SEEDS.json -->

<!-- BEGIN_FILE: research/macro-digital-money-ai/20260921/thesis-development/START_CODEX.txt -->
첨부한 MDMA_THESIS_CODEX_WORK_HANDOFF_v1.0_20260921.md 또는 ZIP을 읽고 실행하세요.

대상 저장소: AofSpds/crypto_compute_dolor
기존 연구 branch: codex/mdma-research-20260921
출력 경로: research/macro-digital-money-ai/20260921/thesis-development

먼저 THESIS_BASELINE_v1.0_20260921.md와 CODEX_WORK_REQUEST_v1.0_20260921.md,
동봉한 입력 자료를 원문 그대로 연구 branch에 commit·일반 push하세요.
이후 기존 연구를 재사용하면서 출처를 확인하고 반대 증거·이론·실증을 보완하여
THESIS_v1.1.md를 하나의 통합 논증문으로 완성하세요.

원문을 옹호하는 결론에 맞추지 마세요. 증거에 따라 주장·범위·제목을 바꿀 수 있습니다.
검토표나 계획서만 반환하지 말고, 출처를 갖춘 완성된 주장과 근거·변경 기록을 반환하세요.
본문의 출처 링크와 과거 검토 결과를 이번 실행에서 이미 검증한 것으로 취급하지 마세요.
기존 H10/H18/H23의 보류를 근거 없이 해제하지 마세요.

접근 경계를 우회하지 말고, 원문을 덮어쓰거나 main에 병합하지 마세요.
실거래·계좌/지갑 접속·유료 접근·운영전략 변경은 하지 마세요.
일상적인 연구 단계마다 승인을 다시 요청하지 마세요.

최종적으로 THESIS_v1.1.md, ARGUMENT_EVIDENCE.md, RESEARCH_RETURN_PACKET.md와
실제 branch·원문 보존 commit·결과 commit·push 상태를 보고하세요.
진행 보고 말미에는 M0~M4의 마일스톤과 현재 위치를 표시하세요.

<!-- END_FILE: research/macro-digital-money-ai/20260921/thesis-development/START_CODEX.txt -->

<!-- BEGIN_FILE: research/macro-digital-money-ai/20260921/thesis-development/inputs/external-review/RESEARCH_RETURN_PACKET.md -->
# 웹챗 → 연구 실행자: 독립 외부 검토 인계

PACKET_CLASS = EXTERNAL_RESEARCH_REVIEW_RETURN  
DATE = 2026-09-21  
REVIEW_STATUS = EXTERNAL_CLAIM_REVIEW_COMPLETED_WITH_LIMITATIONS  
FULL_ORIGINAL_ARTIFACT_REVIEW = NOT_PERFORMED

## 입력과 실제 접근

사용자 인계 메시지와 그 안의 핵심 주장·수치를 검토했다. 지정된 통합 원문, 42개 파일, CLAIMS/SOURCES 원장 및 원 분석 코드는 읽지 못했다. 대상 커밋 39d5cbed92459b55b70e0dd7ba231584a4e75b73의 존재·내용·로컬/원격 일치는 이번에 독립 확인하지 않았다.

HEF run `mdma-fullpacket-read-39d5cbe-01`은 완료 상태이나 실제 결과는 작업공간 경계에 따른 읽기 제한이었다. 명령 실행 0, 파일 변경 0. 완료 상태를 연구 파일 읽기 성공으로 해석하지 않는다.

## 이번 반환물

- INDEPENDENT_EXTERNAL_REVIEW.md: 외부 1차 자료를 이용한 핵심 명제 검토와 수정 결론.
- SOURCES_REVIEWED.json: 이번 검토의 24개 출처 레코드와 실제 열람 깊이. 원 68개 원장이 아니다.
- verify_arithmetic.py / ARITHMETIC_RESULTS.json: 공개 표에서 전사한 입력으로 수행한 산술검사 12개, 결과17행. BTC 실질수익 항목은 사용자 제공 명목수익률을 조건부 입력으로 사용했다.
- FINDINGS.json: 영향 범위를 명시한 발견 및 보완 사항.

## 반드시 반영할 사항

### F01 — BIS 원문 설명 주석의 가격 환산 오류

BIS WP1270 June2026개정판, PDF페이지인덱스35(36번째 페이지), 인쇄34쪽, footnote38.
90일 할인채 액면100달러의 금리1bp변화에 대한 가격 변화는 약0.0025달러다. 4~5bp에1~1.25달러,10bp에2.5달러라는 주석의 달러 환산은 약100배 크다. 원문 PDF 화면으로 확인했다. 이는 가격 환산 설명 오류이며 bp회귀 추정치 자체의 오류를 입증하지 않는다.

원 연구에 해당 환산이 전파됐는지 검색한 뒤 전파된 부분만 수정한다. 원 연구에 전파됐다고 전제하지 않는다. 원 출처 전체를 폐기하지 않는다.

### F02 — H10 추정 대상 분리

원의 순증비중은 미상 유지. 직접보유량, 발행 전 자금원과 반사실적 배분, 매도자·은행 사후 조정, 특정 가격에서의 수요 이동, 만기별 가격 효과를 분리한다. 대체 비중이 높더라도 보유자의 가격 민감도가 바뀌면 가격 효과가 있을 수 있다. 물량 미식별과 가격 효과 부재를 동치로 만들지 않는다.

### F03 — H23 증거 수준 분리

독립 반복고객·환불/보조금 차감 순매출은 미확인 유지. CircleQ2의 유료서비스900개 이상 및 x402내USDC99.3%는 회사 발표 지표로 따로 보존한다. 서비스 목록=고객, 프로토콜내점유율=전체시장점유율,주소=독립고객,거래액=순매출로 승격하지 않는다.

### F04 — 단기 가격 효과와 전체 연쇄

BIS와IMF는 단기국채 가격 경로의 조건부 증거다. 충격 단위·기간·식별이 달라 계수를 평균하지 않는다. IMF의 동적 위험자산 반응을 삭제하지 않는다. 이로부터 AI로 시작하는 전체 연쇄의 인과 식별이 성립하는 것은 아니다.

### F05 — 정의·빈티지·분모

2022CPI6.40%는 현재 계절조정 자료의12월/12월변화율로 재현된다. 당시 BLS비계절조정6.5%와 구분한다. Circle준비금과Tether총자산이라는 분모를 보존한다. 현금PPE차감전사CFO는AI전용ROI가 아니다.

### F06 — AI 증거의 시간·방법 분리

METR2025지연결과를현재모든도구에고정하지 않는다. 2026후속측정은선택·시간문제가있고,5월자기보고조사는실험적효과가아니다. 개선방향의증거를함께보존하되,품질보정완료작업당인간시간·모델비·검토·재작업을측정한다.

## 재개 순서

1. 실제 통합 원문을 접근 가능한 첨부로 제공받거나 적법한 등록 작업공간에서 읽는다. 기존 읽기 제한을 우회하지 않는다.
2. F01의 원 연구 전파 여부만 확인한다. F02/F03/F05/F06을 정확한 원 가설·출처ID에 매핑한다.
3. H10 자금원과 사후 조정, H23 주문-결제-서비스-환불-보조금-반복 코호트 연결 가능성을 탐색한다.
4. 데이터/코드가 실제 공개된 BIS 또는 IMF 한 편부터 정확한 판본으로 재현한다.

일반 연구 단계를 위한 반복 승인, 원 연구 전면 재수집, 원 자기검토 상태의 소급 독립 PASS 승격을 하지 않는다. 실거래·계좌/지갑·유료 접근·운영전략 변경·Git push는 이 패킷이 승인하지 않는다.

## 다음 대화 시작 문구

“외부 검토 패킷의 F01~F06을 실제 통합 원문에 대조하세요. 원 파일을 먼저 읽고, BIS footnote38의 가격 환산 오류가 전파됐는지 확인한 뒤 해당 부분만 수정하세요. H10과H23의 보류를 임의 해제하지 말고 증거 층을 분리하세요. 기존 성공한 산술·출처 확인을 불필요하게 반복하지 마세요.”

현재 위치: 외부 공개자료 기반 명제·산술 검토 완료 / 원 통합 본문·코드·원장 검토 미수행.

<!-- END_FILE: research/macro-digital-money-ai/20260921/thesis-development/inputs/external-review/RESEARCH_RETURN_PACKET.md -->

<!-- BEGIN_FILE: research/macro-digital-money-ai/20260921/thesis-development/inputs/external-review/INDEPENDENT_EXTERNAL_REVIEW.md -->
# 화폐·달러·스테이블코인·AI 경제 — 독립 외부 검토

검토 기준일: 2026-09-21  
대상: 대화에 제공된 Codex 연구 인계 메시지의 핵심 명제·수치·보류 사항  
상태: EXTERNAL_CLAIM_REVIEW_COMPLETED / ORIGINAL_ARTIFACT_REVIEW_NOT_PERFORMED

## 0. 실제 수행 범위

최신 통합 파일 `WEBCHAT_FULL_RESEARCH_PACKET.md`의 실제 본문은 확보하지 못했다. 파일 검색과 런타임에서는 연구 요청서만 확인됐다. HEF 읽기 요청은 접수·종료됐으나 등록 작업공간 밖의 저장소 읽기가 허용되지 않아 원문을 반환하지 않았다. 따라서 commit `39d5cbed92459b55b70e0dd7ba231584a4e75b73`, 42개 파일, CLAIMS/SOURCES 원장, 원 분석 코드 및 원시 데이터 빈티지는 검증하지 않았다. 원 연구의 32개 평가 집계·68개 자료 집계·24개 계산검사·14개 파일검사는 사용자 인계에 기록된 상태이며, 이번에 독립 확인한 실적이 아니다.

대신 공개 1차 자료의 관련 본문·표·수식·공시를 직접 확인하고, 공개 자료에서 전사한 입력값으로 별도의 계산을 수행했다. 24개 출처 레코드의 열람 깊이를 `SOURCES_REVIEWED.json`에 기록했다. 24편의 논문을 전면 정독했다거나 독립 실증 24건을 재현했다는 뜻은 아니다. BIS/IMF의 방법·주요 결과·한계와 관련 PDF 표를 검토했지만 회귀 완전 재현은 0건이다. 다른 생산성 논문 일부는 초록·판본 확인에 한정된다.

별도 산술 프로그램은 12개 검사·17개 결과 행을 생성한다. 이는 이번에 작성한 작은 계산기의 검사이며, 원 연구의 검사나 인과 식별 검증을 대신하지 않는다. 원시 PDF와 전체 가격 시계열은 이 패키지에 재배포하지 않는다. 링크는 후일 변경될 수 있으며 원 자료의 해시를 확보했다고 주장하지 않는다.

## 1. 종합 판단

인계 메시지의 핵심 결론, 즉 다음 연쇄를 필연으로 채택하지 않는 판단은 유지할 근거가 있다.

> AI 확대 → 온체인 지급 확대 → 스테이블코인 잔액 증가 → 순증 국채 수요 → 장기금리 하락 → 위험자산 상승

다만 ‘전체 연쇄가 미입증’과 ‘개별 경로에 관한 실증이 없음’은 다르다. 단기국채 가격 경로에는 조건부 실증이 있고, 에이전트 결제에는 구현과 기업 발표 지표가 있다. 반면 전체 자금 원천, 독립 반복 고객, 환불·보조금을 제거한 매출, AI에 귀속되는 투자수익은 별도 확인이 필요하다. [R01,R02,R05,R14,R15,R22]

이번 검토에서 추가한 핵심 수정은 다음과 같다.

- BIS 원문 주석의 금리-가격 환산에 약 100배 단위 오류가 있다. 회귀 추정치 자체의 오류와 구분해야 한다.
- H10은 단순 자료 부족 외에 추정 대상의 정의가 필요하다. 보유 주체 교체와 수요곡선 이동, 잔액과 가격 효과를 분리해야 한다.
- H23은 ‘상업 증거가 전혀 없음’이 아니다. 기업이 발표한 공급·결제 지표는 있으나 고객·서비스 이행·환불·보조금·반복을 연결한 독립 증거가 부족하다.
- AI 생산성의 혼합 결과는 도구·숙련·작업·시점·측정법의 이질성을 뜻한다. 혼합을 평균 효과 0으로 해석해서는 안 된다.

이것은 원 파일에 대한 전체 독립 PASS가 아니라, 실제 공개 자료로 확인한 명제에 한정한 외부 검토 결과다.

## 2. 주요 수치의 독립 재계산

| 항목 | 확인한 원 입력과 산식 | 이번 계산 | 판단 |
|---|---|---:|---|
| 미국 CPI, 2022년 12월/2021년 12월 | 298.832 / 280.845 − 1 | +6.405% | 인계의 +6.40%와 반올림 일치. 현재 개정 계절조정 계열이다. [R07] |
| 명목 광의 달러지수, 각 연도 마지막 관측 | 121.4256 / 115.2830 − 1 | +5.328% | +5.33%와 일치. 관측일은 각각 2022-12-30, 2021-12-30. [R08] |
| Circle 2026-06-30 직접 국채 | 8,524,064,231 / 73,344,909,176 | 11.622% | 총 USDC 준비금 분모. [R03] |
| Circle 같은 날 익일물 Treasury repo | 52,527,000,000 / 73,344,909,176 | 71.616% | 총 USDC 준비금 분모. [R03] |
| Tether 2026-06-30 직접 미국 bills | 114,960,963,604 / 187,751,426,411 | 61.230% | 보고된 총자산 분모. 현금성 자산 소계가 아니다. [R04] |
| Circle 2026Q2 RLDC | 701.315 − 412.470 | $288.845M | 영업비용 차감 전 지표. [R05] |
| Circle 같은 분기 영업이익 | 288.845 − 254.486 | $34.359M | RLDC와 순이익도 각각 다르다. [R05] |
| Microsoft FY2026 CFO−현금 PPE | 182.935 − 115.948 | $66.987B | 전사 수치. [R06] |
| Microsoft 위 지표 전년 대비 | 66.987 / 71.611 − 1 | −6.457% | 인계의 −6.46%와 일치. [R06] |

### 수치가 맞아도 정의를 보존해야 한다

CPI +6.405%는 ‘2022년 평균 물가상승률’이라는 의미가 아니다. 현재 계절조정 계열의 12월 대 12월 변화율이다. 당시 BLS 보도자료의 비계절조정 전년동월비는 6.5%였다. 서로 다른 빈티지·조정 방식의 통계를 오류로 오인하지 말아야 한다. [R07,R09]

또한 구매력 하락률은 CPI 상승률에 단순히 음수를 붙인 값이 아니다. 같은 물가 바스켓을 기준으로 이번 입력에서 달러 구매력 변화는 280.845/298.832−1, 약 −6.019%다. 이 차이는 비율 계산의 역수 관계다.

Circle과 Tether의 준비자산 구성은 분모와 자산 범위를 맞춘 뒤 비교해야 한다. 위 표는 인계에 사용된 각 비율의 산술을 검증한 것이지, 두 회사의 전체 재무 건전성을 평가하거나 감사를 수행한 것이 아니다.

BTC의 인계된 명목 수익률 −64.25%를 입력으로 받아 CPI로 조정하면 −66.402%가 나온다. 다만 명목 가격 원자료와 −83.80% 최대낙폭은 이번에 독립 재현하지 않았다. 이 항목은 `CONDITIONAL_ON_UNVERIFIED_NOMINAL_RETURN`으로 표시했다.

## 3. 새 발견: BIS 주석의 단위 오류

BIS Working Paper 1270의 2026년 6월 개정 PDF에서, PDF 36번째 페이지(인쇄 쪽수 34), 주석 38은 3개월 국채의 금리 변화와 달러 가격 변화를 환산한다. 해당 주석의 일부 달러 금액은 같은 주석의 센트 설명 및 가격 공식과 불일치한다. PDF 화면에서도 확인했으므로 단순 텍스트 추출 오류로 볼 근거는 없다. [R01]

TreasuryDirect의 할인채 가격식은 다음과 같다. d는 소수로 쓴 할인율, n은 잔존 일수다. [R10]

P = F × (1 − d × n / 360)

액면 $100, 잔존 90일을 가정하면 1bp 하락에 대한 가격 증가는 다음과 같다.

ΔP = 100 × 0.0001 × 90/360 = $0.0025

| 할인율 하락 | $100 액면·90일 예시의 가격 증가 |
|---:|---:|
| 1bp | $0.0025 = 0.25센트 |
| 4bp | $0.0100 = 1센트 |
| 5bp | $0.0125 = 1.25센트 |
| 10bp | $0.0250 = 2.5센트 |

주석의 4–5bp 가격 환산 $1–1.25와 10bp 환산 $2.5는 위 예시보다 약 100배 크다. 투자수익률 방식, 실제 잔존일, 할인율 방식의 작은 차이는 이 정도 단위 차이를 설명하지 못한다.

**영향 범위:** 달러 가격을 설명하는 주석의 오류다. 이것만으로 논문의 bp 단위 회귀 결과가 틀렸다고 결론 내릴 수 없다. 원 Codex 연구가 이 주석을 인용했는지는 통합 파일 미확보로 확인하지 못했다. 후속 작업은 주석 환산의 전파 여부만 검색하고, 전파된 계산만 수정하는 것으로 충분하다. 원 수익률 회귀를 무조건 폐기하거나 연구 전체를 처음부터 다시 수행할 사유는 아니다.

## 4. 단기국채 효과: 일부 지지와 인과 한계를 함께 보존

BIS 개정판의 주요 설정은 발행사·체인별 흐름을 이용한 도구변수와 동적 반응 추정이다. 약 $3.5B의 5일 유입 충격에 대해 3개월 금리가 영향 시점 약 0.7bp, 이후 약 4bp 낮아지는 결과를 보고하며 긴 만기로의 효과는 제한적이다. 미래 규모 확대 계산에는 다른 국채 투자자를 대체하지 않는다는 상한 가정이 들어간다. [R01]

IMF WP26/44는 별도의 사건·변동성 식별을 사용한다. 시가총액 1% 충격에 대해 당일 단기금리 반응을 찾지만, 장기금리의 같은 시점 효과는 유의하지 않다. 일부 위험자산에는 지연 반응이 있으며 저자들은 주가 효과의 경제적 크기가 작다는 점도 설명한다. 따라서 ‘전파가 전혀 없다’는 결론도 지지되지 않는다. [R02]

두 논문의 숫자는 충격 단위, 표본, 시간축, 식별 방식이 달라 단순 평균할 수 없다. 강한 1단계 도구변수 통계는 배제제약의 진실성을 증명하지 않는다. 발행사·체인 또는 제도 관련 사건이 다른 경로로 위험선호를 움직일 가능성은 별도로 평가해야 한다. 반대로 저자들이 통제·제외일·대안 사건표본을 이미 검토했다는 점을 무시하고 ‘아무 통제도 하지 않았다’고 비판해서도 안 된다.

현재 유지할 문장은 ‘관측된 표본과 식별 가정 아래에서 스테이블코인 충격이 단기국채 가격에 영향을 미칠 수 있다는 실증이 있다’이다. ‘AI가 장기금리를 낮추고 자산시장 전체를 올린다는 인과사슬이 입증됐다’는 문장으로 확대할 수 없다.

## 5. H10: 미상 비중을 보존하되, 질문을 더 정확히 바꿔야 한다

### 5.1 무엇의 순증인가

‘글로벌 순증 국채 수요’는 그대로는 모호하다. 발행된 국채는 사후적으로 누군가 보유한다. 연구할 대상은 특정 가격에서의 수요곡선 이동, 기존 투자자 대체, 보유자의 만기와 가격 민감도, 결과적인 균형금리 또는 추가 발행 흡수 능력이다.

다음 네 측정 대상을 분리할 것을 제안한다.

1. 발행사 직접 보유량과 변화: 준비자산 보고로 일부 측정 가능.
2. 토큰을 취득하기 전 사용자의 자산과 그 반사실적 배분: 현재 미식별.
3. 재배분 후 국채 가격·금리 반응: 제한적 실증이 있으나 식별 조건 필요.
4. 장기 만기·전체 재정비용·위험자산으로의 전파: 별도 추정 필요.

발행사가 국채를 매입했다는 사실 하나로 2~4가 모두 해결되지는 않는다.

### 5.2 발행 전의 투자자뿐 아니라 매도자 이후도 봐야 한다

다음은 가상의 회계 예다. 사용자가 예금 $100을 토큰으로 교환하고, 발행사가 그 자금으로 비은행 투자자의 기존 국채를 산다고 하자. 국채 매도자는 예금 $100을 받는다. 이 경우 사용자의 예금 감소만 추적하고 멈추면, 매도자의 예금 증가를 누락한다.

반대로 은행이 자기 보유 국채를 발행사에 팔거나, 신규 국채 발행으로 자금이 TGA에 들어가거나, 재정지출로 다시 은행권에 나오는 경우는 경로가 달라진다. 연준의 2026년 3월 연구도 준비자산 종류와 다른 보유자·은행의 조정에 따라 결과가 달라짐을 모형으로 보여준다. 이는 실제 순증 비율의 추정치가 아니다. [R12]

따라서 ‘MMF에서 온 자금은 전부 대체, 예금에서 온 자금은 전부 신규’라는 이분법도 충분하지 않다. 발행 전 투자와 매도 후 자산 배분, 시간축을 함께 봐야 한다.

### 5.3 순증 물량이 작아도 가격 효과는 있을 수 있다

총 보유량이 같아도 가격에 민감한 보유자를 덜 민감한 보유자가 대체하면 균형가격은 바뀔 수 있다. 특정 만기의 선호, 딜러 재고 부담, 담보·repo 자금조달 제약이 중요한 이유다. 이 논리는 ‘순증 물량 미상’과 ‘조건부 단기 가격 효과’가 양립함을 보여준다.

repo를 직접 국채 소유로 합산하는 것은 잘못이지만, repo의 경제적 효과를 0으로 처리하는 것도 잘못일 수 있다. 익일물 자금 제공과 담보 국채의 만기·소유권을 각각 기록해야 한다.

**H10 권고 상태:** 원의 순증 비중 추정은 보류 유지. 다만 연구 단위를 위 네 질문으로 분리하고, 물량 미식별을 가격 효과 부재와 혼동하지 않도록 설명을 보완한다.

## 6. H23: 상업적 단서와 실제 수익 증거를 구분

AP2에는 카드 및 x402를 사용하는 비대면 에이전트 결제 예제가 함께 있다. 따라서 에이전트 결제 기술과 블록체인 결제 기술은 동일한 개념이 아니다. 서명된 위임은 권한과 의도의 검증을 돕지만 서비스 품질, 환불, 분쟁 해결을 자동 입증하지 않는다. [R14,R16]

### 6.1 이번에 확인한 기업 발표 지표

Circle은 2026Q2 발표에서 Agent Stack의 유료 서비스 900개 이상, x402 에이전트 결제액 중 USDC 비중 99.3%를 제시했다. 이는 사업자 발표로 확인되는 상업적 단서다. 독립적으로 검증한 고객·매출 자료와 동등하지는 않다. [R05]

900개 서비스는 결제한 고객 900명을 뜻하지 않는다. x402 내부 점유율은 전체 에이전트 상거래의 점유율이 아니다. 결제액은 환불·보조금·자기거래를 차감한 순매출과도 다르다.

Visa의 에이전트 대시보드는 구매자·판매자를 주소 수로 정의하고 조정 거래액을 제공한다. 출발 자료로 유용하지만 주소와 고객의 일대일 대응, 제공 완료된 서비스, 환불·반복 구매를 보증하지 않는다. 이번에는 동적 차트의 수치 자체를 추출하지 않았다. [R15]

### 6.2 보류를 해제하는 데 필요한 증거

연결 단위는 ‘온체인 거래 해시 하나’가 아니라 경제적 주문이어야 한다.

order_id → 고객/동일 지배자 식별 → 권한 → 결제 성공 → 서비스 제공 완료 → 환불·취소 → 보조금 차감 → 30/90일 반복 → 매출 인식

주소 연결이 불완전하면 독립 고객 수를 범위로 보고해야 한다. 관찰 기간이 90일에 못 미친 신규 고객을 90일 재구매 실패로 세지 않도록 코호트 우측 절단을 처리해야 한다. 실제 사용자는 그대로인데 지갑을 바꾸는 경우와 하나의 주체가 여러 주소를 만드는 경우도 구분해야 한다.

고객이 실제로 부담한 금액에 기초한 경제적 순거래액과 회계상 매출은 별도 지표로 설계한다. 보조금 차감 분석을 한다고 해서 모든 보조금을 회계상 매출 차감 항목으로 처리한다는 뜻은 아니다.

가상 비용 비교에는 카드의 묶음 청구, 선불 계정, 월별 정산 등 대안을 동일한 주문 묶음으로 비교해야 한다. 온체인 비용만이 아니라 환전·입출금·보관·보안·규정 준수·환불·운전자금까지 포함한 서비스 완료당 비용이 측정 대상이다.

**H23 권고 상태:** 독립 반복 고객·순매출의 보류 유지. 기술 구현과 공급자 발표 지표는 별도 하위 주장으로 기록한다. 측정할 수 없다는 이유로 0을 대입하지 않는다.

## 7. AI 생산성: 부정·긍정 증거를 같은 질문에 대한 답으로 섞지 않는다

고객지원 연구의 현재 공개 초록은 5,172명과 해결 건수/시간 기준 약 15% 개선을 보고한다. 이는 단계적 도입을 분석한 연구다. 개발자 대상 세 현장 실험의 발표 논문 초록은 4,867명, 완료 과업 약 26.08% 증가를 보고한다. 표본·결과 변수·설계가 다르므로 같은 생산성 계수로 합산하면 안 된다. 이번에 이 두 논문의 전체 원자료·방법을 재현한 것은 아니다. [R17,R18]

METR의 2025년 숙련 오픈소스 개발자 실험은 해당 환경에서 19% 지연을 보고했다. 그러나 2026년 2월 후속 설명에서는 AI 없이 작업하기를 꺼리는 참가자와 과업 선택, 병렬 에이전트 환경의 시간 측정 문제가 드러난다. 더 빨라진 방향의 후속 추정이 있어도 정확한 효과 크기의 근거로 취급하기 어렵다는 것이 연구팀의 설명이다. [R19,R20]

2026년 5월 METR 조사에는 349명 기술 종사자의 높은 자기보고 효용·속도 개선이 있다. 이는 2026년 사용 경험에 관한 추가 단서지만, 무작위 실험과 동일한 인과 증거가 아니며 같은 기관의 자료를 독립 재현 여러 건으로 세지 않는다. [R21]

**더 나은 결론:** 특정 직무·작업에서의 개선을 지지하는 근거는 존재한다. 그러나 효과 크기는 숙련, 코드베이스, 도구, 작업 선택, 통합, 검증·재작업, 시점에 따라 달라진다. ‘상반된 연구가 있으니 효과 0’도, ‘긍정 연구가 있으니 전 산업 동일 개선’도 맞지 않는다.

### 7.1 측정 대상을 작업시간에서 품질보정 비용으로 이동

제안하는 종속변수는 ‘합의된 품질 기준을 충족한 완료 과업 1건당 총비용’이다. 작업자 시간, 모델 사용료, 검토·수정, 지연, 실패·롤백, 사후 결함을 포함한다. 에이전트가 일하는 동안 사람이 다른 일을 할 수 있다면 벽시계 시간과 인간 투입시간을 구분해야 한다.

연준의 2026년 7월 자료는 기술 능력·비용, 기업 도입·투자, 생산성·노동을 분리한다. 설비투자에는 비AI 지출과 수입 장비가 포함되며 리스도 있어 단순 현금 지출로 AI 생산성이나 국내 GDP 기여를 추정하기 어렵다. [R22]

### 7.2 효율 개선은 총수요 증가를 보장하지 않는다

총 연산량 = 작업 1건당 연산량 × 작업 건수.

작업당 연산량이 절반이 되고 작업 수가 세 배이면 총연산량은 1.5배다. 작업 수가 1.2배라면 총량은 0.6배다. 제번스형 반등을 주장하려면 수요 반응을 실제로 측정해야 한다. 같은 이유로 결제 거래량 증가가 결제 잔액의 같은 배수 증가를 보장하지 않는다. 선불 잔액·정산 주기·회전율·유동성 여유가 함께 결정한다.

또한 생산성 개선은 물가를 낮추는 경로와 투자·실질 자금 수요를 높이는 경로를 동시에 가질 수 있다. 따라서 AI 확산으로 장기 명목금리가 반드시 내려간다는 결론은 논리적으로 나오지 않는다.

## 8. 화폐·달러·부채와 가치 귀속

### 8.1 ‘코드가 모든 신뢰를 대체’하는 대신 기능별로 분해

현대 은행의 대출·예금 생성은 단순한 기존 저축 재분배와 다르다. 반면 준비자산형 토큰의 교환·이전 기록은 신용창조의 동일한 증거가 아니다. 영란은행의 설명은 이 구분을 뒷받침한다. [R23]

원장 기록이 검증돼도 준비자산의 보관·상환·외부정보·법적 집행·서비스 이행은 별개다. 안전한 준비자산만으로 중개·운영·연결 위험이 모두 없어지지는 않는다. [R13]

이 검토에서는 화폐 역사 전체를 새로 조사하지 않았다. 따라서 보편적 역사 단계가 틀렸다는 포괄 역사 판정을 독립 재검증한 것으로 표시하지 않는다. 기능별 신뢰 분석은 현재 금융 구조를 설명하는 데 재사용할 수 있다.

### 8.2 달러의 세 의미와 재무부 바이백

미국 물가, 외환시장에서의 달러, 국제 결제·저축에서의 사용은 서로 다른 측정 대상이다. 위 2022년 재계산은 첫 두 변수의 방향이 동시에 달라질 수 있음을 보여준다. 국제적 사용 증가의 크기까지 이 계산으로 입증하지는 않는다.

TreasuryDirect의 현재 FAQ는 바이백을 현금관리와 시장유동성 지원으로 구분하며, 매입한 국채는 소각한다고 설명한다. 자금 원천에는 신규 차입금과 일반기금이 포함될 수 있다. 중앙은행 자산매입과 재무부의 기존 채무 상환을 같은 행위로 부를 수 없다. [R11,R23]

예를 들어 새 국채 발행으로 현금을 조달해 기존 국채를 사들이는 경우와, 이미 쌓인 현금을 지출하는 경우의 회계 경로는 다르다. 발표된 바이백 한도 전체를 같은 금액의 신규 통화 공급이라고 계산해서는 안 된다. 거래 유동성 개선과 중앙은행 준비금 순증도 구분해야 한다.

### 8.3 부채와 AI

단순 부채비율 항등식은 b_t=[(1+i)/(1+g)]b_(t−1)+d_t다. 평균 조달금리 i, 명목 성장률 g, 기초재정적자 d를 구분한다. 시장의 신규 금리가 바뀌어도 기존 부채의 평균 이자비용이 즉시 같은 폭으로 바뀌는 것은 아니다. 차환 구조와 만기별 금리가 필요하다.

따라서 AI 생산성이 일부 높아졌다는 사실이나 단기금리의 작은 변화만으로 전체 재정 지속가능성이 개선됐다고 단정할 수 없다. 이 문서는 특정 정책에 대한 평가나 재정·금리 예측을 제공하지 않는다.

### 8.4 BTC와 기업·토큰 가치 귀속

BTC의 2022년 인계된 손실은 ‘어느 해에나 구매력을 보존한다’는 강한 주장의 반례가 될 수 있다. 다만 다른 보유기간, 예상 밖 인플레이션 충격, 통화별 실질 성과에 관한 별도 가설까지 동일하게 반증하지는 않는다. H18의 프리미엄 요인별 인과 기여는 보류 유지가 적절하다. 상관·회귀 설명력을 곧바로 인과 기여 비중으로 바꾸지 않는다.

Circle의 RLDC에서 영업이익까지, Microsoft 전사 CFO에서 투자 후 현금까지의 계산은 일치했다. 하지만 RLDC는 순이익이 아니며 전사 현금흐름은 AI 전용 투자수익률이 아니다. [R05,R06]

이번 Microsoft 계산의 하락은 투자 선행·확대와 현금 회수 시점의 차이일 수도 있고 수익성 문제일 수도 있다. 이 수치만으로 어느 해석을 확정할 수 없다. 기술 채택, 사업자 매출, 이익, 특정 자산 보유자의 가치와 매입가격을 순서대로 연결해야 한다.

### 8.5 감사 상태의 시점 주의

Tether의 2026년 8월 13일 회사 발표에는 KPMG US가 2025년 재무제표 감사를 마쳤다는 내용이 있다. 이번에는 서명된 전체 감사보고서 자체를 확보하지 못했다. 그러므로 회사 발표와 독립 확인을 구분한다. 이 사실은 6월 말 준비자산 확인업무를 전체 재무감사라고 부르지 말아야 한다는 원칙과 모순되지 않는다. 동시에 ‘과거에도 현재에도 전체 감사가 전혀 없다’는 무기한 서술은 재확인이 필요하다. [R24]

## 9. 통합 결론: 반드시 같이 성장하는 하나의 시장이 아니다

연구의 다음 설명 모형은 한 줄의 상승 연쇄보다 다음 네 층이 적절하다.

1. 수요 발생: AI가 어떤 유료 작업을 얼마나 발생시키는가.
2. 결제 선택: 카드·예금·토큰 중 무엇으로 얼마의 비용에 완료하는가.
3. 잔액·금융자산: 선불·회전율·자금 원천·준비자산·매도자 조정은 무엇인가.
4. 가치 귀속: 수수료·이자·영업이익·현금흐름이 어떤 보유자에게 얼마만큼 돌아가는가.

이것은 이번 검토자의 분석 틀이지 실증적으로 확정된 미래 예측이 아니다. 다음과 같은 분기가 모두 논리적으로 가능하다.

- AI 사용은 증가하지만 기존 기업 청구·카드·예금으로 대부분 처리되는 경우.
- 온체인 결제는 증가하지만 높은 회전율 때문에 준비자산 잔액은 완만하게 증가하는 경우.
- 토큰 잔액은 크게 증가하지만 기존 MMF·국채 배분을 대체하는 비중이 높은 경우.
- 단기국채 수요·가격은 변하지만 장기금리나 발행사 이익·토큰 보유자 가치로의 연결은 약한 경우.

반드시 ‘아무 효과도 없다’와 ‘모든 관련 자산이 오른다’ 중 하나를 선택할 필요는 없다. 각 단계의 실제 관측과 경쟁·비용·상환 위험을 분리하면 반증 가능한 연구가 된다.

## 10. 후속 우선순위 — 이미 확인한 작업을 반복하지 않는 방식

### P0: 문서 정확성과 재현 범위

통합 원문이 실제 전달되면 RESEARCH_RETURN_PACKET, REPORT, CLAIMS/SOURCES, 분석 코드, RESULTS 순서로 읽는다. 원 출처 레코드에 BIS 주석 오류와 출처 버전, H23의 기업 발표 수준을 반영한다. 기존 유효 계산은 재사용하되 이번 독립 산술 결과와 원 코드 출력이 같은 정의를 쓰는지만 대조한다. 모든 원 논문이나 자료를 처음부터 다시 수집할 필요는 없다.

### P1-A: H10

발행 전 자금원, 발행사 매입, 국채 매도자 및 은행의 사후 조정을 연결한다. 단일 순증 비율을 임의 부여하지 않는다. 직접 보유·MMF 내부자산·repo 원금·담보를 별도 열로 두고 만기와 중복을 식별한다. 공개 자료로 완전 연결이 안 되면 조건별 범위와 확인되지 않은 구간을 보고한다.

### P1-B: H23

공개 수치만 더 모으기보다 서비스 운영자 단위의 결제-이행-환불-보조금-고객 코호트 연결 가능성을 먼저 확인한다. 가능한 표본만 좁게 검증해도 주소 수 수백만 개를 모으는 것보다 판단에 도움이 될 수 있다. 실제 결제·지갑 접근은 현재 승인 범위에 포함하지 않는다.

### P2: 회귀 실제 재현

BIS와 IMF 중 실제 데이터·코드가 확보되는 한 편부터, 논문에서 사용한 정확한 판본·표본·충격 정규화로 재현한다. 첫 작업에서 두 논문의 모든 회귀를 병렬 재현할 필요는 없다. 무정보 재실행을 피한다.

### P3: 남은 비교·시점 갱신

금 및 최신 한국 CPI 비교, 당시 사용 가능했던 빈티지, 법률-제안규칙-최종규칙-적용일-인가 상태, 품질보정 기업 생산성 및 AI 전용 증분 현금흐름을 목적에 맞춰 추가한다. 이번에는 이 항목들을 완결 검증했다고 표시하지 않는다.

## 최종 상태

EXTERNAL_CLAIM_REVIEW = COMPLETED_WITH_LIMITATIONS  
ORIGINAL_FULL_PACKET = NOT_ACCESSED  
ORIGINAL_COMMIT = NOT_VERIFIED  
ORIGINAL_CODE_AND_RAW_VINTAGE = NOT_REPRODUCED  
FULL_PAPER_REGRESSION_REPLICATIONS = 0  
INDEPENDENT_ARITHMETIC_CHECKS = 12  
ARITHMETIC_RESULT_ROWS = 17  
SOURCE_RECORDS_IN_THIS_REVIEW = 24 (not 24 full papers)  
ORIGINAL_32_HYPOTHESIS_AGGREGATE = NOT_RECOUNTED  
TRADING_OR_OPERATIONAL_CHANGES = NONE  
GIT_WRITES_OR_PUSH = NONE

현재 위치: 공개자료 기반 핵심 주장·수치 검토 완료. 원 통합 파일·코드·자료 원장 검토는 미수행. 후속 연구의 직접 시작점은 BIS 환산 주석 전파 확인, H10 추정 대상 분리, H23 고객·순매출 연결 증거다.

---

## 출처 색인

아래 번호는 이번 검토자가 새로 만든 출처 식별자다. 원 연구의 68개 자료 ID와 혼동하지 않는다. 열람 깊이와 한계는 `SOURCES_REVIEWED.json`에 별도 보존했다.

**[R01] Stablecoins and safe asset prices — BIS Working Paper 1270, June 2026 revision**  
https://www.bis.org/publications/working-paper-1270-stablecoins-and-safe-asset-prices.pdf  
열람: `SELECTED_METHODS_RESULTS_LIMITATIONS_AND_TABLES_VISUALLY_CHECKED`  
한계: 54-page PDF; selected methods/results, table 2, projections, limitations. PDF page index35 = printed34, footnote38 visually checked. Not full regression replication. Price-unit error isolated from yield coefficients.

**[R02] Stablecoin Shocks — IMF Working Paper 2026/044, March 2026**  
https://www.imf.org/-/media/files/publications/wp/2026/english/wpiea2026044-source-pdf.pdf  
열람: `SELECTED_METHODS_RESULTS_AND_TABLES_VISUALLY_CHECKED`  
한계: Event selection, heteroskedasticity identification, impact table, dynamic figures, robustness sections. No original regression code/data executed.

**[R03] Circle USDC reserve examination, June 2026**  
https://6778953.fs1.hubspotusercontent-na1.net/hubfs/6778953/USDCAttestationReports/2026/2026%20USDC_Examination%20Report%20June%2026.pdf  
열람: `PDF_RESERVE_TABLE_VISUALLY_CHECKED`  
한계: June30 table, PDF page index3; denominator is total USDC reserves. Point-in-time reserve examination, not full-company audit.

**[R04] BDO report: Tether International Financial Figures, June30 2026**  
https://assets.ctfassets.net/vyse88cgwfbl/2kYf7r64h3tzwiu6F0CbUB/2997abd2f11ecea74a21528048b50707/Opinion___Report_-_Tether_International_Financial_Figure_30-06-2026.pdf  
열람: `PDF_ASSET_TABLE_AND_ASSURANCE_SCOPE_VISUALLY_CHECKED`  
한계: Asset table PDF index8; assurance scope PDF index3. Direct bills divided by total reported assets, not cash-equivalent subtotal.

**[R05] Circle Reports Second Quarter 2026 Results**  
https://www.circle.com/pressroom/circle-reports-second-quarter-2026-results  
열람: `COMPANY_RELEASE_AND_DETAILED_STATEMENTS_READ`  
한계: Full detailed tables accessed also via issuer's BusinessWire distribution. Financial figures and agent metrics are company disclosures, not independent third-party commercial verification.

**[R06] Microsoft FY2026 Q4 earnings release and cash-flow statement**  
https://www.microsoft.com/en-us/Investor/earnings/FY-2026-Q4/press-release-webcast  
열람: `PUBLIC_EARNINGS_CASH_FLOW_TABLE_READ`  
한계: FY endsJune30. Statement presented in USDmillions. CFO minus cash PPE arithmetic only; not AI-specific investment returns; not full10K audit review.

**[R07] FRED CPIAUCSL: seasonally adjusted US CPI**  
https://fred.stlouisfed.org/data/CPIAUCSL  
열람: `TEXT_SERIES_ENDPOINT_OBSERVATIONS_READ`  
한계: Current revised data: Dec2021 280.845; Dec2022 298.832. Not historical real-time vintage.

**[R08] FRED DTWEXBGS: nominal broad US dollar index**  
https://fred.stlouisfed.org/data/DTWEXBGS  
열람: `TEXT_SERIES_ENDPOINT_OBSERVATIONS_READ`  
한계: 2021-12-30 115.2830 and2022-12-30 121.4256; last available observations in respective calendar years. Not CPI-adjusted dollar index.

**[R09] BLS archived December2022 CPI release, Jan12 2023**  
https://www.bls.gov/news.release/archives/cpi_01122023.htm  
열람: `ARCHIVED_RELEASE_HEADLINE_AND_DEFINITIONS_READ`  
한계: 12-month unadjusted headline6.5%; do not mix with revised SA6.4046%.

**[R10] TreasuryDirect: Understanding Pricing and Interest Rates**  
https://www.treasurydirect.gov/marketable-securities/understanding-pricing/  
열람: `BILL_PRICING_FORMULA_READ`  
한계: Discount-price formula Face*(1-discountRate*days/360). Used for own90-day examples, not a regression re-estimate.

**[R11] TreasuryDirect: FAQs about Treasury Securities Buybacks**  
https://www.treasurydirect.gov/help-center/faqs/buyback-faqs/  
열람: `PURPOSE_FUNDING_AND_RETIREMENT_SECTIONS_READ`  
한계: Cash management vs liquidity support, financing authorization and retirement. No transaction-by-transaction liquidity impact estimate.

**[R12] Federal Reserve: Payment Stablecoins and Cross Border Payments, March30 2026**  
https://www.federalreserve.gov/econres/notes/feds-notes/payment-stablecoins-and-cross-border-payments-benefits-and-implications-for-monetary-policy-20260330.html  
열람: `MODEL_ASSUMPTIONS_AND_BALANCE_SHEET_MECHANISMS_READ`  
한계: Stylized balance-sheet cases, including Treasury seller and banks' adjustments. Not an estimate of actual global net-demand share.

**[R13] Federal Reserve: Stablecoins in 2025, April8 2026**  
https://www.federalreserve.gov/econres/notes/feds-notes/stablecoins-in-2025-developments-and-financial-stability-implications-20260408.html  
열람: `PUBLIC_NOTE_RISK_AND_INTERMEDIATION_SECTIONS_READ`  
한계: Reserves do not exhaust risks: layered intermediation, links, operational risks. Not whole-market assurance.

**[R14] Agent Payments Protocol AP2 official documentation**  
https://ap2-protocol.org/  
열람: `SPEC_OVERVIEW_AND_EXAMPLE_INDEX_READ`  
한계: Human-not-present card and x402 examples, authorization/mandates. No sample execution, signatures or payments.

**[R15] Visa Onchain Analytics: Agentic Payments**  
https://visaonchainanalytics.com/agentic-payments  
열람: `PUBLIC_METRIC_DEFINITIONS_READ`  
한계: Buyer and merchant wallets are unique addresses; organic volume adjustedUSD. Dynamic dashboard totals not retrieved. No independent repeat-customer/net-sales panel.

**[R16] Coinbase x402 launch documentation**  
https://www.coinbase.com/developer-platform/discover/launches/x402  
열람: `OFFICIAL_PROTOCOL_DESCRIPTION_READ`  
한계: Protocol functionality not economic adoption measurement; no actual requests or funds transferred.

**[R17] Generative AI at Work, arXiv2304.11771**  
https://arxiv.org/abs/2304.11771  
열람: `ABSTRACT_AND_VERSION_METADATA_READ`  
한계: Current abstract5172 support agents,15% productivity improvement. Staggered adoption, not described here as randomized trial. Whole methods not re-read.

**[R18] The Effects of Generative AI on High-Skilled Work, Management Science**  
https://pubsonline.informs.org/doi/10.1287/mnsc.2025.00535  
열람: `PUBLISHED_ABSTRACT_AND_METADATA_READ`  
한계: Three developer field experiments,4867 participants,26.08% completed-task increase(SE10.3%). No full paper replication.

**[R19] METR early2025 experienced developer randomized study**  
https://metr.org/blog/2025-07-10-early-2025-ai-experienced-os-dev-study/  
열람: `RESEARCH_TEAM_PUBLIC_METHODS_AND_RESULTS_READ`  
한계: 16experienced open-source developers,246tasks;19% slower in study setting. Not universal productivity effect.

**[R20] METR developer productivity measurement update, Feb24 2026**  
https://metr.org/blog/2026-02-24-uplift-update/  
열람: `RESEARCH_TEAM_METHOD_LIMITATIONS_AND_RESULTS_READ`  
한계: Selection and timing measurement problems; imprecise faster estimates cannot be treated as reliable causal industry effect.

**[R21] METR AI usage survey, May11 2026**  
https://metr.org/blog/2026-05-11-ai-usage-survey/  
열람: `RESEARCH_TEAM_SURVEY_METHOD_AND_RESULTS_READ`  
한계: 349technical workers Feb-Apr2026; self-reportedwork-value/speed. Different design from RCT, same organization, not independent replication.

**[R22] Federal Reserve: The AI Buildout and the Economy, July17 2026**  
https://www.federalreserve.gov/econres/notes/feds-notes/the-ai-buildout-and-the-economy-publicly-available-data-to-assess-ais-impact-20260717.html  
열람: `TEXT_METHOD_FRAMEWORK_AND_LIMITATIONS_READ`  
한계: Capabilities/costs, adoption/investment, productivity/labor; gross investment/imports, nonAIcapex and leases. Chart source series not downloaded or recreated.

**[R23] Bank of England: Money creation in the modern economy,2014**  
https://www.bankofengland.co.uk/quarterly-bulletin/2014/q1/money-creation-in-the-modern-economy  
열람: `OFFICIAL_SUMMARY_READ`  
한계: Bank loan/deposit creation and QE conceptual summary; no comprehensive historical anthropology review.

**[R24] Tether company announcement of inaugural financial audit,Aug13 2026**  
https://tether.io/news/tether-completes-the-largest-inaugural-financial-audit-in-history/  
열람: `COMPANY_ANNOUNCEMENT_ONLY`  
한계: Company says KPMGUS completed2025USGAAP audit. Signed full auditor report not obtained. Cannot independently upgrade assurance based on announcement alone.

<!-- END_FILE: research/macro-digital-money-ai/20260921/thesis-development/inputs/external-review/INDEPENDENT_EXTERNAL_REVIEW.md -->

<!-- BEGIN_FILE: research/macro-digital-money-ai/20260921/thesis-development/inputs/external-review/SOURCES_REVIEWED.json -->
{
  "source_record_count": 24,
  "not_equivalent_to_full_papers_read": true,
  "not_the_original_68_record_ledger": true,
  "sources": [
    {
      "id": "R01",
      "title": "Stablecoins and safe asset prices — BIS Working Paper 1270, June 2026 revision",
      "url": "https://www.bis.org/publications/working-paper-1270-stablecoins-and-safe-asset-prices.pdf",
      "accessed_on": "2026-09-21",
      "access_depth": "SELECTED_METHODS_RESULTS_LIMITATIONS_AND_TABLES_VISUALLY_CHECKED",
      "limitations": "54-page PDF; selected methods/results, table 2, projections, limitations. PDF page index35 = printed34, footnote38 visually checked. Not full regression replication. Price-unit error isolated from yield coefficients.",
      "raw_file_preserved_here": false,
      "source_hash": null
    },
    {
      "id": "R02",
      "title": "Stablecoin Shocks — IMF Working Paper 2026/044, March 2026",
      "url": "https://www.imf.org/-/media/files/publications/wp/2026/english/wpiea2026044-source-pdf.pdf",
      "accessed_on": "2026-09-21",
      "access_depth": "SELECTED_METHODS_RESULTS_AND_TABLES_VISUALLY_CHECKED",
      "limitations": "Event selection, heteroskedasticity identification, impact table, dynamic figures, robustness sections. No original regression code/data executed.",
      "raw_file_preserved_here": false,
      "source_hash": null
    },
    {
      "id": "R03",
      "title": "Circle USDC reserve examination, June 2026",
      "url": "https://6778953.fs1.hubspotusercontent-na1.net/hubfs/6778953/USDCAttestationReports/2026/2026%20USDC_Examination%20Report%20June%2026.pdf",
      "accessed_on": "2026-09-21",
      "access_depth": "PDF_RESERVE_TABLE_VISUALLY_CHECKED",
      "limitations": "June30 table, PDF page index3; denominator is total USDC reserves. Point-in-time reserve examination, not full-company audit.",
      "raw_file_preserved_here": false,
      "source_hash": null
    },
    {
      "id": "R04",
      "title": "BDO report: Tether International Financial Figures, June30 2026",
      "url": "https://assets.ctfassets.net/vyse88cgwfbl/2kYf7r64h3tzwiu6F0CbUB/2997abd2f11ecea74a21528048b50707/Opinion___Report_-_Tether_International_Financial_Figure_30-06-2026.pdf",
      "accessed_on": "2026-09-21",
      "access_depth": "PDF_ASSET_TABLE_AND_ASSURANCE_SCOPE_VISUALLY_CHECKED",
      "limitations": "Asset table PDF index8; assurance scope PDF index3. Direct bills divided by total reported assets, not cash-equivalent subtotal.",
      "raw_file_preserved_here": false,
      "source_hash": null
    },
    {
      "id": "R05",
      "title": "Circle Reports Second Quarter 2026 Results",
      "url": "https://www.circle.com/pressroom/circle-reports-second-quarter-2026-results",
      "accessed_on": "2026-09-21",
      "access_depth": "COMPANY_RELEASE_AND_DETAILED_STATEMENTS_READ",
      "limitations": "Full detailed tables accessed also via issuer's BusinessWire distribution. Financial figures and agent metrics are company disclosures, not independent third-party commercial verification.",
      "raw_file_preserved_here": false,
      "source_hash": null,
      "additional_url": "https://www.businesswire.com/news/home/20260805828963/en/Circle-Reports-Second-Quarter-2026-Results",
      "independence_note": "Circle site and BusinessWire copy are ONE issuer release, not two independent sources."
    },
    {
      "id": "R06",
      "title": "Microsoft FY2026 Q4 earnings release and cash-flow statement",
      "url": "https://www.microsoft.com/en-us/Investor/earnings/FY-2026-Q4/press-release-webcast",
      "accessed_on": "2026-09-21",
      "access_depth": "PUBLIC_EARNINGS_CASH_FLOW_TABLE_READ",
      "limitations": "FY endsJune30. Statement presented in USDmillions. CFO minus cash PPE arithmetic only; not AI-specific investment returns; not full10K audit review.",
      "raw_file_preserved_here": false,
      "source_hash": null
    },
    {
      "id": "R07",
      "title": "FRED CPIAUCSL: seasonally adjusted US CPI",
      "url": "https://fred.stlouisfed.org/data/CPIAUCSL",
      "accessed_on": "2026-09-21",
      "access_depth": "TEXT_SERIES_ENDPOINT_OBSERVATIONS_READ",
      "limitations": "Current revised data: Dec2021 280.845; Dec2022 298.832. Not historical real-time vintage.",
      "raw_file_preserved_here": false,
      "source_hash": null
    },
    {
      "id": "R08",
      "title": "FRED DTWEXBGS: nominal broad US dollar index",
      "url": "https://fred.stlouisfed.org/data/DTWEXBGS",
      "accessed_on": "2026-09-21",
      "access_depth": "TEXT_SERIES_ENDPOINT_OBSERVATIONS_READ",
      "limitations": "2021-12-30 115.2830 and2022-12-30 121.4256; last available observations in respective calendar years. Not CPI-adjusted dollar index.",
      "raw_file_preserved_here": false,
      "source_hash": null
    },
    {
      "id": "R09",
      "title": "BLS archived December2022 CPI release, Jan12 2023",
      "url": "https://www.bls.gov/news.release/archives/cpi_01122023.htm",
      "accessed_on": "2026-09-21",
      "access_depth": "ARCHIVED_RELEASE_HEADLINE_AND_DEFINITIONS_READ",
      "limitations": "12-month unadjusted headline6.5%; do not mix with revised SA6.4046%.",
      "raw_file_preserved_here": false,
      "source_hash": null
    },
    {
      "id": "R10",
      "title": "TreasuryDirect: Understanding Pricing and Interest Rates",
      "url": "https://www.treasurydirect.gov/marketable-securities/understanding-pricing/",
      "accessed_on": "2026-09-21",
      "access_depth": "BILL_PRICING_FORMULA_READ",
      "limitations": "Discount-price formula Face*(1-discountRate*days/360). Used for own90-day examples, not a regression re-estimate.",
      "raw_file_preserved_here": false,
      "source_hash": null
    },
    {
      "id": "R11",
      "title": "TreasuryDirect: FAQs about Treasury Securities Buybacks",
      "url": "https://www.treasurydirect.gov/help-center/faqs/buyback-faqs/",
      "accessed_on": "2026-09-21",
      "access_depth": "PURPOSE_FUNDING_AND_RETIREMENT_SECTIONS_READ",
      "limitations": "Cash management vs liquidity support, financing authorization and retirement. No transaction-by-transaction liquidity impact estimate.",
      "raw_file_preserved_here": false,
      "source_hash": null
    },
    {
      "id": "R12",
      "title": "Federal Reserve: Payment Stablecoins and Cross Border Payments, March30 2026",
      "url": "https://www.federalreserve.gov/econres/notes/feds-notes/payment-stablecoins-and-cross-border-payments-benefits-and-implications-for-monetary-policy-20260330.html",
      "accessed_on": "2026-09-21",
      "access_depth": "MODEL_ASSUMPTIONS_AND_BALANCE_SHEET_MECHANISMS_READ",
      "limitations": "Stylized balance-sheet cases, including Treasury seller and banks' adjustments. Not an estimate of actual global net-demand share.",
      "raw_file_preserved_here": false,
      "source_hash": null
    },
    {
      "id": "R13",
      "title": "Federal Reserve: Stablecoins in 2025, April8 2026",
      "url": "https://www.federalreserve.gov/econres/notes/feds-notes/stablecoins-in-2025-developments-and-financial-stability-implications-20260408.html",
      "accessed_on": "2026-09-21",
      "access_depth": "PUBLIC_NOTE_RISK_AND_INTERMEDIATION_SECTIONS_READ",
      "limitations": "Reserves do not exhaust risks: layered intermediation, links, operational risks. Not whole-market assurance.",
      "raw_file_preserved_here": false,
      "source_hash": null
    },
    {
      "id": "R14",
      "title": "Agent Payments Protocol AP2 official documentation",
      "url": "https://ap2-protocol.org/",
      "accessed_on": "2026-09-21",
      "access_depth": "SPEC_OVERVIEW_AND_EXAMPLE_INDEX_READ",
      "limitations": "Human-not-present card and x402 examples, authorization/mandates. No sample execution, signatures or payments.",
      "raw_file_preserved_here": false,
      "source_hash": null
    },
    {
      "id": "R15",
      "title": "Visa Onchain Analytics: Agentic Payments",
      "url": "https://visaonchainanalytics.com/agentic-payments",
      "accessed_on": "2026-09-21",
      "access_depth": "PUBLIC_METRIC_DEFINITIONS_READ",
      "limitations": "Buyer and merchant wallets are unique addresses; organic volume adjustedUSD. Dynamic dashboard totals not retrieved. No independent repeat-customer/net-sales panel.",
      "raw_file_preserved_here": false,
      "source_hash": null
    },
    {
      "id": "R16",
      "title": "Coinbase x402 launch documentation",
      "url": "https://www.coinbase.com/developer-platform/discover/launches/x402",
      "accessed_on": "2026-09-21",
      "access_depth": "OFFICIAL_PROTOCOL_DESCRIPTION_READ",
      "limitations": "Protocol functionality not economic adoption measurement; no actual requests or funds transferred.",
      "raw_file_preserved_here": false,
      "source_hash": null
    },
    {
      "id": "R17",
      "title": "Generative AI at Work, arXiv2304.11771",
      "url": "https://arxiv.org/abs/2304.11771",
      "accessed_on": "2026-09-21",
      "access_depth": "ABSTRACT_AND_VERSION_METADATA_READ",
      "limitations": "Current abstract5172 support agents,15% productivity improvement. Staggered adoption, not described here as randomized trial. Whole methods not re-read.",
      "raw_file_preserved_here": false,
      "source_hash": null
    },
    {
      "id": "R18",
      "title": "The Effects of Generative AI on High-Skilled Work, Management Science",
      "url": "https://pubsonline.informs.org/doi/10.1287/mnsc.2025.00535",
      "accessed_on": "2026-09-21",
      "access_depth": "PUBLISHED_ABSTRACT_AND_METADATA_READ",
      "limitations": "Three developer field experiments,4867 participants,26.08% completed-task increase(SE10.3%). No full paper replication.",
      "raw_file_preserved_here": false,
      "source_hash": null
    },
    {
      "id": "R19",
      "title": "METR early2025 experienced developer randomized study",
      "url": "https://metr.org/blog/2025-07-10-early-2025-ai-experienced-os-dev-study/",
      "accessed_on": "2026-09-21",
      "access_depth": "RESEARCH_TEAM_PUBLIC_METHODS_AND_RESULTS_READ",
      "limitations": "16experienced open-source developers,246tasks;19% slower in study setting. Not universal productivity effect.",
      "raw_file_preserved_here": false,
      "source_hash": null,
      "independence_note": "METR series: same research organization; designs, samples and periods differ; do not count as three independent replications."
    },
    {
      "id": "R20",
      "title": "METR developer productivity measurement update, Feb24 2026",
      "url": "https://metr.org/blog/2026-02-24-uplift-update/",
      "accessed_on": "2026-09-21",
      "access_depth": "RESEARCH_TEAM_METHOD_LIMITATIONS_AND_RESULTS_READ",
      "limitations": "Selection and timing measurement problems; imprecise faster estimates cannot be treated as reliable causal industry effect.",
      "raw_file_preserved_here": false,
      "source_hash": null,
      "independence_note": "METR series: same research organization; designs, samples and periods differ; do not count as three independent replications."
    },
    {
      "id": "R21",
      "title": "METR AI usage survey, May11 2026",
      "url": "https://metr.org/blog/2026-05-11-ai-usage-survey/",
      "accessed_on": "2026-09-21",
      "access_depth": "RESEARCH_TEAM_SURVEY_METHOD_AND_RESULTS_READ",
      "limitations": "349technical workers Feb-Apr2026; self-reportedwork-value/speed. Different design from RCT, same organization, not independent replication.",
      "raw_file_preserved_here": false,
      "source_hash": null,
      "independence_note": "METR series: same research organization; designs, samples and periods differ; do not count as three independent replications."
    },
    {
      "id": "R22",
      "title": "Federal Reserve: The AI Buildout and the Economy, July17 2026",
      "url": "https://www.federalreserve.gov/econres/notes/feds-notes/the-ai-buildout-and-the-economy-publicly-available-data-to-assess-ais-impact-20260717.html",
      "accessed_on": "2026-09-21",
      "access_depth": "TEXT_METHOD_FRAMEWORK_AND_LIMITATIONS_READ",
      "limitations": "Capabilities/costs, adoption/investment, productivity/labor; gross investment/imports, nonAIcapex and leases. Chart source series not downloaded or recreated.",
      "raw_file_preserved_here": false,
      "source_hash": null
    },
    {
      "id": "R23",
      "title": "Bank of England: Money creation in the modern economy,2014",
      "url": "https://www.bankofengland.co.uk/quarterly-bulletin/2014/q1/money-creation-in-the-modern-economy",
      "accessed_on": "2026-09-21",
      "access_depth": "OFFICIAL_SUMMARY_READ",
      "limitations": "Bank loan/deposit creation and QE conceptual summary; no comprehensive historical anthropology review.",
      "raw_file_preserved_here": false,
      "source_hash": null
    },
    {
      "id": "R24",
      "title": "Tether company announcement of inaugural financial audit,Aug13 2026",
      "url": "https://tether.io/news/tether-completes-the-largest-inaugural-financial-audit-in-history/",
      "accessed_on": "2026-09-21",
      "access_depth": "COMPANY_ANNOUNCEMENT_ONLY",
      "limitations": "Company says KPMGUS completed2025USGAAP audit. Signed full auditor report not obtained. Cannot independently upgrade assurance based on announcement alone.",
      "raw_file_preserved_here": false,
      "source_hash": null
    }
  ]
}

<!-- END_FILE: research/macro-digital-money-ai/20260921/thesis-development/inputs/external-review/SOURCES_REVIEWED.json -->

<!-- BEGIN_FILE: research/macro-digital-money-ai/20260921/thesis-development/inputs/external-review/FINDINGS.json -->
[
  {
    "id": "F01",
    "kind": "PRIMARY_SOURCE_UNIT_ERROR",
    "target": "BIS WP1270 June2026 PDF index35, printed34, footnote38",
    "observed": "Dollar price conversion approximately 100x too large",
    "scope": "Explanatory price conversion only; impact on original research unknown",
    "action": "Search original artifacts for propagation and correct only affected quantities",
    "sources": [
      "R01",
      "R10"
    ]
  },
  {
    "id": "F02",
    "kind": "ESTIMAND_REFINEMENT",
    "target": "H10",
    "observed": "Issuer holdings and marginal price effects do not identify global net-additional demand share",
    "scope": "Keep original unidentified share on hold",
    "action": "Separate counterfactual demand, holder substitution, repo/collateral, seller/bank adjustment and tenor-specific prices",
    "sources": [
      "R01",
      "R12"
    ]
  },
  {
    "id": "F03",
    "kind": "EVIDENCE_LAYER_REFINEMENT",
    "target": "H23",
    "observed": "Company commercial indicators exist; independent repeat-customer/refund-net-sales panel not obtained",
    "scope": "No claim that all public evidence worldwide is absent",
    "action": "Retain company metrics with provenance; do not substitute addresses or catalogue entries for customers",
    "sources": [
      "R05",
      "R14",
      "R15"
    ]
  },
  {
    "id": "F04",
    "kind": "CAUSAL_SCOPE",
    "target": "Stablecoin shock to asset prices",
    "observed": "Conditional short-rate evidence and small dynamic spillovers, not an identified AI-to-assets chain",
    "scope": "No regression replication performed",
    "action": "Preserve shock normalization, method, maturity and horizon; do not pool coefficients mechanically",
    "sources": [
      "R01",
      "R02"
    ]
  },
  {
    "id": "F05",
    "kind": "NUMERICAL_DEFINITIONS",
    "target": "Reported CPI, reserves, RLDC, cash flow",
    "observed": "Public-source arithmetic consistent with handoff after rounding",
    "scope": "Not full financial audit, original code review or real-time-vintage reproduction",
    "action": "Retain SA/NSA, denominator, units, company-wide versus AI-specific and conditional BTC input flags",
    "sources": [
      "R03",
      "R04",
      "R05",
      "R06",
      "R07",
      "R08",
      "R09"
    ]
  },
  {
    "id": "F06",
    "kind": "PRODUCTIVITY_MEASUREMENT",
    "target": "H25 and AI macro transmission",
    "observed": "Task/population/design/time heterogeneity; later positive signals differ in evidential quality",
    "scope": "Two papers checked at abstract/metadata level; METR public reports read; no replication",
    "action": "Measure quality-adjusted completed-work cost and separate task, job, firm and economy levels",
    "sources": [
      "R17",
      "R18",
      "R19",
      "R20",
      "R21",
      "R22"
    ]
  }
]

<!-- END_FILE: research/macro-digital-money-ai/20260921/thesis-development/inputs/external-review/FINDINGS.json -->

<!-- BEGIN_FILE: research/macro-digital-money-ai/20260921/thesis-development/inputs/external-review/ARITHMETIC_RESULTS.json -->
{
  "review_date": "2026-09-21",
  "scope": "Manually transcribed public-source inputs and own arithmetic only",
  "original_research_code_executed": false,
  "original_raw_snapshots_accessed": false,
  "paper_regression_replications": 0,
  "checks": {
    "circle_treasury_rounds_to_11_62": true,
    "circle_repo_rounds_to_71_62": true,
    "tether_bills_rounds_to_61_23": true,
    "circle_rldc": true,
    "circle_operating_income": true,
    "microsoft_fcf": true,
    "microsoft_yoy": true,
    "cpi_sa": true,
    "broad_usd": true,
    "conditional_btc_real": true,
    "bill_dv01": true,
    "bis_factor_100": true
  },
  "results": [
    {
      "id": "CIRCLE_DIRECT_TREASURY_SHARE_20260630",
      "value": "11.621889408228012992038339203628",
      "unit": "percent of total USDC reserves",
      "sources": [
        "R03"
      ],
      "formula": "8524064231 / 73344909176 * 100",
      "status": "PUBLIC_INPUT_ARITHMETIC_REPRODUCED"
    },
    {
      "id": "CIRCLE_OVERNIGHT_REPO_SHARE_20260630",
      "value": "71.616422448564352967602344120462",
      "unit": "percent of total USDC reserves",
      "sources": [
        "R03"
      ],
      "formula": "52527000000 / 73344909176 * 100",
      "status": "PUBLIC_INPUT_ARITHMETIC_REPRODUCED"
    },
    {
      "id": "TETHER_DIRECT_BILLS_SHARE_20260630",
      "value": "61.230407566834152780448992207577",
      "unit": "percent of reported total assets",
      "sources": [
        "R04"
      ],
      "formula": "114960963604 / 187751426411 * 100",
      "status": "PUBLIC_INPUT_ARITHMETIC_REPRODUCED"
    },
    {
      "id": "CIRCLE_RLDC_2026Q2",
      "value": "288.845",
      "unit": "USD million",
      "sources": [
        "R05"
      ],
      "formula": "(701315 - 412470) / 1000; source in USD thousand",
      "status": "PUBLIC_INPUT_ARITHMETIC_REPRODUCED"
    },
    {
      "id": "CIRCLE_OPERATING_INCOME_2026Q2",
      "value": "34.359",
      "unit": "USD million",
      "sources": [
        "R05"
      ],
      "formula": "(701315 - 412470 - 254486) / 1000",
      "status": "PUBLIC_INPUT_ARITHMETIC_REPRODUCED"
    },
    {
      "id": "MSFT_CFO_MINUS_CASH_PPE_FY2026",
      "value": "66.987",
      "unit": "USD billion",
      "sources": [
        "R06"
      ],
      "formula": "(182935 - 115948) / 1000",
      "status": "PUBLIC_INPUT_ARITHMETIC_REPRODUCED"
    },
    {
      "id": "MSFT_CFO_MINUS_CASH_PPE_FY2025",
      "value": "71.611",
      "unit": "USD billion",
      "sources": [
        "R06"
      ],
      "formula": "(136162 - 64551) / 1000",
      "status": "PUBLIC_INPUT_ARITHMETIC_REPRODUCED"
    },
    {
      "id": "MSFT_CFO_MINUS_CASH_PPE_YOY",
      "value": "-6.4571085447766404602644845065700",
      "unit": "percent",
      "sources": [
        "R06"
      ],
      "formula": "(66987 / 71611 - 1) * 100",
      "status": "PUBLIC_INPUT_ARITHMETIC_REPRODUCED"
    },
    {
      "id": "US_CPI_SA_DEC2022_VS_DEC2021",
      "value": "6.4046004023571721056098559703800",
      "unit": "percent",
      "sources": [
        "R07"
      ],
      "formula": "(298.832 / 280.845 - 1) * 100",
      "status": "PUBLIC_INPUT_ARITHMETIC_REPRODUCED"
    },
    {
      "id": "USD_DOMESTIC_PURCHASING_POWER_CHANGE",
      "value": "-6.0191010333565347753921936071150",
      "unit": "percent",
      "sources": [
        "R07"
      ],
      "formula": "(280.845 / 298.832 - 1) * 100",
      "status": "PUBLIC_INPUT_ARITHMETIC_REPRODUCED"
    },
    {
      "id": "BROAD_USD_LAST_2022_VS_LAST_2021",
      "value": "5.32827910446466521516615632834",
      "unit": "percent",
      "sources": [
        "R08"
      ],
      "formula": "(2022-12-30 level 121.4256 / 2021-12-30 level 115.2830 - 1) * 100",
      "status": "PUBLIC_INPUT_ARITHMETIC_REPRODUCED"
    },
    {
      "id": "BTC_REAL_2022_CONDITIONAL",
      "value": "-66.401828619424961182202709214543",
      "unit": "percent",
      "sources": [
        "USER_HANDOFF",
        "R07"
      ],
      "formula": "((1 - 0.6425) / (298.832 / 280.845) - 1) * 100",
      "status": "CONDITIONAL_ON_UNVERIFIED_NOMINAL_RETURN"
    },
    {
      "id": "BILL_PRICE_PER100_DROP_1BP",
      "value": "0.0025",
      "unit": "USD per USD100 face",
      "sources": [
        "R10"
      ],
      "formula": "100 * (1 / 10000) * 90 / 360; 90-day bill discount-rate example",
      "status": "OWN_FORMULA_CALCULATION"
    },
    {
      "id": "BILL_PRICE_PER100_DROP_4BP",
      "value": "0.01",
      "unit": "USD per USD100 face",
      "sources": [
        "R10"
      ],
      "formula": "100 * (4 / 10000) * 90 / 360; 90-day bill discount-rate example",
      "status": "OWN_FORMULA_CALCULATION"
    },
    {
      "id": "BILL_PRICE_PER100_DROP_5BP",
      "value": "0.0125",
      "unit": "USD per USD100 face",
      "sources": [
        "R10"
      ],
      "formula": "100 * (5 / 10000) * 90 / 360; 90-day bill discount-rate example",
      "status": "OWN_FORMULA_CALCULATION"
    },
    {
      "id": "BILL_PRICE_PER100_DROP_10BP",
      "value": "0.025",
      "unit": "USD per USD100 face",
      "sources": [
        "R10"
      ],
      "formula": "100 * (10 / 10000) * 90 / 360; 90-day bill discount-rate example",
      "status": "OWN_FORMULA_CALCULATION"
    },
    {
      "id": "BIS_FOOTNOTE38_PRICE_SCALE_RATIO_4BP",
      "value": "1E+2",
      "unit": "multiple",
      "sources": [
        "R01",
        "R10"
      ],
      "formula": "Footnote's USD1 / independently computed USD0.01",
      "status": "SOURCE_EXPLANATORY_UNIT_ERROR_NOT_REGRESSION_REPLICATION"
    }
  ]
}

<!-- END_FILE: research/macro-digital-money-ai/20260921/thesis-development/inputs/external-review/ARITHMETIC_RESULTS.json -->

<!-- BEGIN_FILE: research/macro-digital-money-ai/20260921/thesis-development/inputs/external-review/verify_arithmetic.py -->
"""Independent arithmetic checks, not replication of the original research.

Python 3.10+, standard library only. Run in this directory:
    python verify_arithmetic.py
Inputs were manually transcribed from public primary sources identified in
SOURCES_REVIEWED.json. This script neither downloads data nor establishes
source authenticity, original data vintage, economic causality or audit assurance.
BTC nominal return is an UNVERIFIED input supplied in the user's handoff.
"""
from decimal import Decimal, getcontext
from pathlib import Path
import json

getcontext().prec = 32
D = Decimal

def pct_ratio(numerator: str, denominator: str) -> Decimal:
    den = D(denominator)
    if den == 0:
        raise ValueError("Denominator must not be zero")
    return D(numerator) / den * 100


def pct_change(new: str, old: str) -> Decimal:
    return pct_ratio(new, old) - 100


def main() -> None:
    rows = []
    def add(name, value, unit, sources, formula, status="PUBLIC_INPUT_ARITHMETIC_REPRODUCED"):
        rows.append({"id": name, "value": str(value), "unit": unit,
                     "sources": sources, "formula": formula, "status": status})

    add("CIRCLE_DIRECT_TREASURY_SHARE_20260630", pct_ratio("8524064231", "73344909176"),
        "percent of total USDC reserves", ["R03"], "8524064231 / 73344909176 * 100")
    add("CIRCLE_OVERNIGHT_REPO_SHARE_20260630", pct_ratio("52527000000", "73344909176"),
        "percent of total USDC reserves", ["R03"], "52527000000 / 73344909176 * 100")
    add("TETHER_DIRECT_BILLS_SHARE_20260630", pct_ratio("114960963604", "187751426411"),
        "percent of reported total assets", ["R04"], "114960963604 / 187751426411 * 100")
    add("CIRCLE_RLDC_2026Q2", (D("701315") - D("412470"))/1000,
        "USD million", ["R05"], "(701315 - 412470) / 1000; source in USD thousand")
    add("CIRCLE_OPERATING_INCOME_2026Q2", (D("701315")-D("412470")-D("254486"))/1000,
        "USD million", ["R05"], "(701315 - 412470 - 254486) / 1000")
    ms26, ms25 = D("182935")-D("115948"), D("136162")-D("64551")
    add("MSFT_CFO_MINUS_CASH_PPE_FY2026", ms26/1000, "USD billion", ["R06"], "(182935 - 115948) / 1000")
    add("MSFT_CFO_MINUS_CASH_PPE_FY2025", ms25/1000, "USD billion", ["R06"], "(136162 - 64551) / 1000")
    add("MSFT_CFO_MINUS_CASH_PPE_YOY", (ms26/ms25-1)*100, "percent", ["R06"], "(66987 / 71611 - 1) * 100")
    inflation = D("298.832")/D("280.845")
    add("US_CPI_SA_DEC2022_VS_DEC2021", (inflation-1)*100, "percent", ["R07"], "(298.832 / 280.845 - 1) * 100")
    add("USD_DOMESTIC_PURCHASING_POWER_CHANGE", (1/inflation-1)*100, "percent", ["R07"], "(280.845 / 298.832 - 1) * 100")
    add("BROAD_USD_LAST_2022_VS_LAST_2021", pct_change("121.4256", "115.2830"), "percent", ["R08"],
        "(2022-12-30 level 121.4256 / 2021-12-30 level 115.2830 - 1) * 100")
    add("BTC_REAL_2022_CONDITIONAL", ((1-D("0.6425"))/inflation-1)*100, "percent", ["USER_HANDOFF", "R07"],
        "((1 - 0.6425) / (298.832 / 280.845) - 1) * 100", "CONDITIONAL_ON_UNVERIFIED_NOMINAL_RETURN")
    for bp in (1, 4, 5, 10):
        delta = D(100)*D(bp)/D(10000)*D(90)/D(360)
        add(f"BILL_PRICE_PER100_DROP_{bp}BP", delta, "USD per USD100 face", ["R10"],
            f"100 * ({bp} / 10000) * 90 / 360; 90-day bill discount-rate example", "OWN_FORMULA_CALCULATION")
    add("BIS_FOOTNOTE38_PRICE_SCALE_RATIO_4BP", D("1")/D("0.01"), "multiple", ["R01", "R10"],
        "Footnote's USD1 / independently computed USD0.01", "SOURCE_EXPLANATORY_UNIT_ERROR_NOT_REGRESSION_REPLICATION")

    # These checks test only this small, independent arithmetic program.
    byid = {r["id"]: D(r["value"]) for r in rows}
    checks = {
        "circle_treasury_rounds_to_11_62": byid["CIRCLE_DIRECT_TREASURY_SHARE_20260630"].quantize(D(".01")) == D("11.62"),
        "circle_repo_rounds_to_71_62": byid["CIRCLE_OVERNIGHT_REPO_SHARE_20260630"].quantize(D(".01")) == D("71.62"),
        "tether_bills_rounds_to_61_23": byid["TETHER_DIRECT_BILLS_SHARE_20260630"].quantize(D(".01")) == D("61.23"),
        "circle_rldc": byid["CIRCLE_RLDC_2026Q2"] == D("288.845"),
        "circle_operating_income": byid["CIRCLE_OPERATING_INCOME_2026Q2"] == D("34.359"),
        "microsoft_fcf": byid["MSFT_CFO_MINUS_CASH_PPE_FY2026"] == D("66.987"),
        "microsoft_yoy": byid["MSFT_CFO_MINUS_CASH_PPE_YOY"].quantize(D(".01")) == D("-6.46"),
        "cpi_sa": byid["US_CPI_SA_DEC2022_VS_DEC2021"].quantize(D(".01")) == D("6.40"),
        "broad_usd": byid["BROAD_USD_LAST_2022_VS_LAST_2021"].quantize(D(".01")) == D("5.33"),
        "conditional_btc_real": byid["BTC_REAL_2022_CONDITIONAL"].quantize(D(".01")) == D("-66.40"),
        "bill_dv01": byid["BILL_PRICE_PER100_DROP_1BP"] == D(".0025"),
        "bis_factor_100": byid["BIS_FOOTNOTE38_PRICE_SCALE_RATIO_4BP"] == D("100"),
    }
    if not all(checks.values()):
        raise AssertionError(f"Arithmetic check failure: {checks}")
    result = {
        "review_date": "2026-09-21",
        "scope": "Manually transcribed public-source inputs and own arithmetic only",
        "original_research_code_executed": False,
        "original_raw_snapshots_accessed": False,
        "paper_regression_replications": 0,
        "checks": checks,
        "results": rows,
    }
    out = Path(__file__).resolve().parent / "ARITHMETIC_RESULTS.json"
    out.write_text(json.dumps(result, ensure_ascii=False, indent=2)+"\n", encoding="utf-8")
    print(f"{len(checks)} arithmetic checks passed; {len(rows)} result rows written to {out.name}")

if __name__ == "__main__":
    main()

<!-- END_FILE: research/macro-digital-money-ai/20260921/thesis-development/inputs/external-review/verify_arithmetic.py -->

<!-- BEGIN_FILE: research/macro-digital-money-ai/20260921/thesis-development/inputs/external-review/MANIFEST.json -->
{
  "created_on": "2026-09-21",
  "scope": "Only generated review artifacts; hashes are NOT source-PDF hashes or Git hashes",
  "files": [
    {
      "path": "ARITHMETIC_RESULTS.json",
      "bytes": 5557,
      "sha256": "a32a0a4c5312849c9ee0bdcbc424941a4c56e35a2531a13f812acf0c2624fcfb"
    },
    {
      "path": "FINDINGS.json",
      "bytes": 2847,
      "sha256": "80b9eb3ac0bc24d667be15ad29541faab9e7946ec4da783ed7424a654d64a682"
    },
    {
      "path": "INDEPENDENT_EXTERNAL_REVIEW.md",
      "bytes": 35435,
      "sha256": "78cb64be6597850115b8abcec9dad09a18594c0712659627a27caa569d0a18a6"
    },
    {
      "path": "RESEARCH_RETURN_PACKET.md",
      "bytes": 5236,
      "sha256": "899a1cbd35504af1eb23f890183e1da332fcfb6708bf7dfd0248369036961f7e"
    },
    {
      "path": "SOURCES_REVIEWED.json",
      "bytes": 13480,
      "sha256": "570852874c6edd5a37ab41bf166a32d8fa33d2a5867952026b4cf23b74a3d14e"
    },
    {
      "path": "verify_arithmetic.py",
      "bytes": 5533,
      "sha256": "f9b108b83f86e4da04262aa596da160bc64925ebb59304fadd29db5d2d44decb"
    }
  ]
}

<!-- END_FILE: research/macro-digital-money-ai/20260921/thesis-development/inputs/external-review/MANIFEST.json -->

