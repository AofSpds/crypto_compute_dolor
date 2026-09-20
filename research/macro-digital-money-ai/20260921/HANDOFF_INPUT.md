# 화폐·달러·스테이블코인·AI 경제 — 독립 연구 실행·인계 패킷

```text
PACKET_ID = MDMA-CODEX-WORK-RESEARCH-20260921-001
PACKET_CLASS = INDEPENDENT_RESEARCH_EXECUTION_REQUEST
VERSION = 1.0
PREPARATION_DATE_KST = 2026-09-21
OWNER = 한알
EXECUTION_SURFACE = CODEX_WORK
TASK_ROLE = RESEARCH_LEAD
PERSONA = INHERIT_EXISTING_AUTHORIZED_PERSONA
DISPATCH_STATUS = PREPARED_NOT_DISPATCHED
RESEARCH_STATUS = NOT_STARTED
SEED_DISCOVERY_STATUS = INITIAL_PUBLIC_SOURCE_DISCOVERY_COMPLETED
RETURN_PACKET_REQUIRED = TRUE
OPERATIONAL_STRATEGY_CHANGE = NOT_AUTHORIZED
REPOSITORY = RESOLVE_FROM_ACTIVE_WORKSPACE_NOT_PREASSIGNED
PROPOSED_OUTPUT_ROOT = research/macro-digital-money-ai/20260921/
LANGUAGE = KOREAN
```

**이 문서는 연구 결과가 아니라 실행 요청서다.** 이전 대화 없이 이 문서만으로 연구를 시작할 수 있다. 공개 자료의 초기 접근 확인과 연구 설계는 준비되어 있지만, 체계적 본문 검토·실증 분석·결론 확정은 아직 수행하지 않았다. 아래 가설은 입증해야 할 정답이 아니라 수정·기각할 수 있는 출발점이다.

## 1. 위임 목표와 최종 질문

화폐·국채·달러 유동성·스테이블코인·블록체인·AI 에이전트 경제의 관계를 외부 자료로 폭넓게 연구하고, 처음의 설명보다 정확하고 검증 가능한 통합 모형을 만든다. 단순 요약, 찬성 근거 모음, 링크 수집으로 끝내지 않는다.

최종적으로 다음 질문에 답한다.

> 디지털 결제와 AI 자동화가 확대될 때 화폐의 신뢰, 달러와 안전자산 수요, 거래·계약의 실행 방식, 생산성, 기업·네트워크·자산의 가치 귀속은 어떤 조건에서 어떻게 달라지는가? 서로 다른 경로 중 무엇이 관측 자료로 뒷받침되고, 무엇은 아직 기대나 가정에 머물러 있는가?

결과는 **현재까지 확인된 사실 / 조건부로 지지되는 설명 / 반대 증거가 있는 설명 / 아직 모르는 것**을 분리해야 한다. 처음의 가설을 일부 또는 전부 버리는 결론도 허용한다. 더 좋은 결론이란 더 낙관적인 결론이 아니라, 근거의 범위·반례·성립 조건·반증 조건이 더 명확한 결론이다.

## 2. 승인 범위와 실행 경계

### 수행할 일

공개 웹·논문·중앙은행/국제기구 자료·공식 통계·공시·프로토콜 문서를 실제로 읽는다. 필요하고 이용이 허용되는 공개 데이터를 확보하여 로컬 계산·작은 재현 분석을 수행한다. 근거·반론·누락을 구조화하고 보고서, 재현 가능한 분석, 후속 연구 인계 패킷을 작성한다.

연구 질문의 세분화, 일반적인 검색·자료 정리·공개 데이터의 소규모 가공은 반복 승인을 받지 않고 진행한다. 중간에 계획서만 제출하고 멈추지 않는다. 가용한 실행 환경 안에서 결과 산출과 인계까지 진행한다.

### 하지 않을 일

실거래, 계좌·지갑 접속, 자산 이전, 결제, 유료 데이터/API 신규 결제, 외부 서비스 가입, 비밀값 수집·출력, 운영 배포는 하지 않는다. 실제 결제 프로토콜을 조사하더라도 유료 API 호출이나 지갑 서명·송금으로 시험하지 않는다. 증거를 얻으려고 금융 거래를 만들지 않는다.

이 연구를 M1TOP3·M3TOP3의 점수 규칙·유니버스·가중치·입력 릴리스·전략 실행 승인으로 해석하지 않는다. 기존 워크스트림 결과를 재계산하거나 덮어쓰지 않는다. 조직·페르소나·공통 정책·운영 Current를 변경하지 않는다. 새로운 데이터 플랫폼·DB·워크플로 엔진을 구축하는 과제로 확대하지 않는다.

특정 정책·법률은 관할·시점·문구·적용 범위·경제적 경로를 사실적으로 비교한다. 정치인의 동기·능력이나 정당·정책의 우열을 결론으로 만들지 않는다. 시장 시나리오를 선거 전망으로 확장하지 않는다.

### 저장소 처리

현재 작업 폴더, Git remote, 관련 `AGENTS.md`, 해당 경로의 실제 쓰기 규칙을 먼저 확인한다. 과거 대화의 경로나 다른 연구 요청서의 권한을 가져오지 않는다. 필요한 지침만 한 번 복구하고 실작업으로 진입한다.

승인된 연구 경로가 있으면 그 경로를 우선한다. 위 `PROPOSED_OUTPUT_ROOT`는 제안 경로이지 이미 존재하는 경로가 아니다. 저장소가 지정되지 않았거나 Git 쓰기 권한이 불명확해도 공개 자료 조사·로컬 산출물 작성은 진행할 수 있다. 이 경우 `LOCAL_ONLY`와 실제 경로를 남긴다.

기존 규칙상 Git 기록이 허용된 경우에만 별도 연구 브랜치 또는 격리된 worktree에서 **이번 연구 산출물만** 커밋한다. 기존 dirty worktree, 타 작업, main을 건드리지 않는다. 강제 reset/clean/stash, 자동 merge, 원격 push나 PR 생성 권한을 이 요청서로 새로 부여하지 않는다. 실제 커밋·원격 기록 여부를 구분한다.

## 3. 검증 전 출발 논리

아래는 연구할 관계를 정리한 것이며, 모든 문장을 이미 확인된 사실로 채택하라는 뜻이 아니다.

| 출발 관점 | 연구에서 반드시 분리할 질문 |
|---|---|
| 화폐는 수용 가능성과 지급 약속에 대한 신뢰에 의존한다 | 어떤 기능의 신뢰인가? 발행·보관·이전·검증·상환·법적 청구권이 어떻게 나뉘는가? |
| 금융은 가치저장과 거래의 편의를 연결한다 | 신용 창출의 이점과 만기변환·유동성·손실 부담은 누구에게 귀속되는가? |
| 금태환과 현재의 달러 질서는 서로 다른 제도적 기반을 가진다 | 하나의 필연적인 발전 단계가 아니라 복수의 역사적 경로로 설명할 수 있는가? |
| 달러 구매력, 환율, 국제적 사용은 다를 수 있다 | 각 지표를 따로 측정했을 때 동행·역행·시차는 무엇인가? |
| 미국 부채는 총액뿐 아니라 성장·이자·기초재정수지·만기구조에 좌우된다 | 조건부 회계 관계를 무제한 차입 능력이나 자동 위기 예측으로 잘못 확대하지 않았는가? |
| 스테이블코인은 달러 접근과 이전 방식을 바꿀 수 있다 | 신규 달러 수요인가, 예금·MMF·직접 국채·다른 토큰의 대체인가? |
| 준비자산 보유는 국채 수요와 연결될 수 있다 | 순증 수요, 만기별 효과, 이자 비용, 상환 시 매도 압력을 어떻게 구분하는가? |
| 비트코인과 스마트계약 네트워크의 경제적 역할은 다를 수 있다 | 설계 특성과 실제 사용·수익률 사이의 간극은 무엇인가? |
| AI 에이전트는 위임된 범위에서 유료 거래를 실행할 수 있다 | 실제 상업적 필요, 권한 증명, 책임, 환불, 비용, 반복 사용은 확인되는가? |
| AI의 비용 하락은 이용량 증가를 유도할 수 있다 | 총자원 수요와 생산성이 실제로 늘어나는 조건은 무엇인가? |
| 디지털 경제의 확대는 여러 인프라 수요를 만들 수 있다 | 그 이익이 이용자·발행사·중개사·기업 주주·토큰 보유자 중 어디로 가는가? |
| 기술 채택과 투자 수익은 다른 변수다 | 수요→매출→이익→현금흐름/토큰 귀속→현재 가격의 각 연결이 성립하는가? |

**연결을 미리 확정하지 말 것:** `AI 확대 → 온체인 결제 확대 → 스테이블코인 잔액 확대 → 국채 금리 하락 → 위험자산 가격 상승`은 검증해야 할 여러 개의 가설이다. 하나의 필연적인 연쇄로 전제하지 않는다.

## 4. 연구 모듈과 초기 가설 원장

8개 모듈의 질문을 먼저 넓게 조사한다. 아래 32개 항목은 수집 범위를 닫는 목록이 아니다. 새로 발견한 설명·반례는 추가하고, 중복은 병합하며 변경 이유만 기록한다. 초기 상태는 모두 `UNASSESSED`다.

### A. 화폐 기능·신뢰·역사적 제도

| ID | 검증할 질문 |
|---|---|
| H01 | 화폐의 수용은 희소성, 청구권, 법적 제도, 네트워크 효과, 세금·채무 결제와 각각 어떤 관계가 있는가? |
| H02 | 화폐사를 물물교환→금속→국가→코드라는 단일 단계로 설명하는 데 반례가 있는가? 다른 시대·지역의 병존과 단절은 무엇인가? |
| H03 | 가치저장·계산단위·교환·최종결제가 다른 수단에 분리될 때 어떤 편익과 마찰이 발생하는가? |
| H04 | 신뢰가 사라지는 대신 구성요소로 나뉜다는 설명은 무엇을 설명하고 무엇을 놓치는가? 중앙집중·분산의 실제 통제권을 어떻게 측정할 것인가? |

일반적인 중앙은행 설명만으로 모든 역사적 기원을 결론 내리지 않는다. 화폐사·경제사 연구와 1차 기록에 연결된 논문을 보완한다. 역사적 비유는 설명 도구이며 현대 제도의 동등성을 증명하지 않는다.

### B. 미국 부채·달러·국채시장·유동성

| ID | 검증할 질문 |
|---|---|
| H05 | 달러의 구매력·대외환율·국제적 사용은 언제 서로 다른 방향으로 움직이며 어떤 지표로 구분되는가? |
| H06 | 부채 지속가능성에서 평균 조달금리, 명목성장률, 기초재정수지, 만기, 차환, 발행통화, 보유 주체는 어떻게 작용하는가? |
| H07 | 재무부 바이백·발행 만기 변경·TGA 변화·연준 QE/QT·ON RRP·레포는 회계상, 시장미시구조상 어떻게 다른가? |
| H08 | 단기국채 수요 변화는 장기금리·기간 프리미엄·담보 수급·위험자산에 어떤 조건에서 전달되며 어디에서 끊기는가? |

부채 총액과 공공 보유 부채, 중앙은행 준비금과 시중 예금, 시장 유동성과 자금조달 유동성, 총발행과 순발행, 정책금리와 시장수익률을 구분한다. `연준 자산−TGA−ON RRP` 같은 단순 지표를 보편적인 위험자산 가격 공식으로 채택하지 않는다.

### C. 스테이블코인 수요·준비자산·순증 효과

| ID | 검증할 질문 |
|---|---|
| H09 | 스테이블코인 사용은 달러 접근을 새로 확장하는가, 기존 달러 상품을 다른 방식으로 보유하게 하는가? 사용자·지역·용도별 차이는 무엇인가? |
| H10 | 발행사 국채 매입 중 직접·간접 보유와 기존 수요 대체를 제거한 순증 수요는 얼마까지 식별 가능한가? |
| H11 | 발행·상환이 예금·준비금·MMF·국채·역외 달러와 연결되는 대차대조표 경로는 무엇인가? 어떤 정의에서 통화량이 달라지는가? |
| H12 | 결제액·거래횟수·평균 보유잔액·회전율·저축 목적 보유는 어떤 관계이며, 거래 증가가 잔액 증가로 이어지지 않는 경우는 무엇인가? |

유통 시가총액을 실제 국채 매입액, 온체인 전송량을 소비, 주소 수를 사람 수로 치환하지 않는다. USDC·USDT 외 상품과 담보형·알고리즘형·합성형의 차이를 포함하되 각 구조를 원문으로 확인한다.

### D. 상환·법적 권리·금융안정·경쟁 제도

| ID | 검증할 질문 |
|---|---|
| H13 | 준비자산의 신용도·듀레이션·유동성·수탁 구조와 이용자의 상환 접근성이 페그 유지에 각각 어떤 영향을 주는가? |
| H14 | 은행 실패·알고리즘형 붕괴·거래소 수탁 문제·브리지/스마트계약 실패를 구분하면 공통 위험과 별개 위험은 무엇인가? |
| H15 | 토큰화 예금·MMF·CBDC·실시간 계좌이체·기존 카드망은 스테이블코인의 대체재 또는 보완재가 될 수 있는가? |
| H16 | 국가별 법적 청구권·준비자산·공시·감사·상환·예금보호·유동성 접근 규칙은 어떤 제약과 효과를 가지는가? |

법률안·통과된 법률·발효·최종 시행규칙·제안/협의안·실제 인가를 별도 상태로 표시한다. 보고서 발행일, 사건일, 판결일, 현재 상태를 구분한다. 규제기관 문서는 그 기관의 입장과 확인 가능한 제도를 보여주지만 모든 경제적 효과를 증명하지는 않는다.

### E. 비트코인·스마트계약·네트워크 가치

| ID | 검증할 질문 |
|---|---|
| H17 | 비트코인의 공급 규칙과 인플레이션 헤지·위기 헤지·장기 구매력 보존·분산투자 성과는 각각 어떤 증거를 요구하는가? |
| H18 | 비트코인의 화폐적 프리미엄·접근성·보안 예산·수탁·시장 유동성은 수요와 가치에 어떤 조건부 영향을 주는가? |
| H19 | 스마트계약 이용 확대에서 발생하는 수수료·소각·검증자 보상·MEV·L2 수익이 어디에 귀속되며 토큰 보유자와 어떻게 연결되는가? |
| H20 | 멀티체인·L2·대체 데이터 가용성·허가형 시스템·기존 DB와의 경쟁 속에서 네트워크 사용 증가와 특정 토큰 가치가 분리되는가? |

분석 대상 체인을 미리 최종 승자로 정하지 않는다. 원화와 달러 표시 수익률, 기간과 시장 국면, 분산투자와 헤지를 구분한다. 프로토콜 규칙은 현행 공식 규격·코드로, 수익률 가설은 별도의 데이터와 연구로 확인한다.

### F. AI 에이전트의 결제·권한·실제 경제활동

| ID | 검증할 질문 |
|---|---|
| H21 | 에이전트가 거래를 수행할 때 권한·예산·사용자 의도·거래 증거·책임·취소/환불을 어떤 구조로 처리하는가? |
| H22 | AP2·x402 등은 기존 카드·은행 결제와 어떤 관계이며, 스테이블코인 또는 퍼블릭체인이 반드시 필요한 사용 사례는 있는가? |
| H23 | 발표·데모·파일럿·실제 유료 사용·반복 고객·감사 가능한 상업 실적을 분리했을 때 시장의 증거는 무엇인가? |
| H24 | 동일 업무에서 수수료뿐 아니라 온/오프램프, FX, 가스, 사전예치, 사기·실패·재시도·사람 검토까지 포함한 총비용은 어떠한가? |

무인 실행을 사용자 승인과 무관한 무제한 자율성으로 표현하지 않는다. 명세 존재와 실제 채택을 분리한다. 프로토콜 요청 수·봇 거래·테스트 전송·동일 주체 반복 이동을 순수 상업 수요와 구분한다. 코드와 샘플 검토는 허용되지만 실제 지급·지갑 연결 시험은 범위 밖이다.

### G. AI 생산성·수요 반응·설비투자·실물 제약

| ID | 검증할 질문 |
|---|---|
| H25 | AI의 과업별 효과가 사용자 숙련도·도구·시점·도입 방식에 따라 어떻게 다르며 기업·산업·거시 생산성으로 어떻게 연결되는가? |
| H26 | 효율 상승 후 이용량이 증가하는 크기는 어느 정도이며 제번스 효과·부분 반등·총사용 감소를 가르는 조건은 무엇인가? |
| H27 | 데이터센터·반도체·전력·네트워크 투자 증가는 생산성 개선, 공급 제약, 과잉설비, 기술 대체 중 무엇을 보여주는가? |
| H28 | AI 효과가 GDP·가격·임금·기업이익·세수·정부 이자 부담으로 전달되는 과정에서 시차와 분배는 어떤 역할을 하는가? |

벤치마크 점수·토큰 사용량·투자금·GPU 출하를 생산성으로 바로 바꾸지 않는다. 서비스 품질이 다른 토큰 가격은 직접 비교하지 않는다. 직무 실험 결과를 전 경제의 성장률로 확장하지 않고 일반화 조건을 검토한다.

### H. 경제적 가치 귀속·통합 설명·관측 지표

| ID | 검증할 질문 |
|---|---|
| H29 | 채택→거래량→매출→순이익/현금흐름→주주 또는 토큰 보유자 귀속의 각 단계에서 누가 이익을 얻거나 잃는가? |
| H30 | 준비자산 잔액 증가와 금리 하락, 네트워크 사용 증가와 단가 하락, 설비투자와 감가상각이 동시에 일어나면 결과는 어떻게 달라지는가? |
| H31 | 달러 확장·화폐 형태의 병존·은행 중심 토큰화·제한적 상용화 등 대안 경로를 어떤 관측으로 구분할 수 있는가? |
| H32 | 후속 시장 연구에 사용할 수 있는 관측 변수·사건·빈도·공개 시점·한계는 무엇이며 어떤 근거가 나오면 현재 결론을 바꿀 것인가? |

연구 결과를 매수 목록·목표가격·자동매매 신호로 바꾸지 않는다. 경제적 노출과 수익 귀속 구조를 정리하고 현재 가격에서의 투자 매력은 별도 분석 과제로 남길 수 있다. 현금흐름 권리가 없는 토큰에 주식의 FCF 모형을 근거 없이 적용하지 않는다.

## 5. 외부 자료 수집 — 넓게 찾고, 사용 단계에서 구분

### 5.1 수집 원칙

먼저 자료를 수집하고 이후에 용도를 정한다. 부분 공개·잠정 자료·반론·부정적 결과·측정 방식이 다른 자료도 보존한다. 완전한 데이터나 동일한 형식을 갖추지 못했다는 이유로 후보 목록에서 삭제하지 않는다.

대신 **발견한 자료의 수**와 **결론을 지지하는 독립 근거의 수**를 구분한다. 같은 논문의 초고·개정판·학술지판·해설·보도자료를 독립 연구 여러 개로 세지 않는다. 동일 데이터 공급자의 대시보드 여러 개 역시 중복 관계를 기록한다.

공식 통계·법규·공시·실제 기술 규격·저자 논문을 우선 읽는다. 중앙은행·국제기구의 해석, 발행사·플랫폼의 이해관계, 관측 연구의 한계도 함께 표시한다. 2차 자료는 발견과 해석 비교에 활용하되 핵심 기술·제도 주장과 수치는 가능한 원출처로 연결한다.

자료 수를 채우기 위한 무관한 링크 수집이나 인위적인 합격 정원을 만들지 않는다. 깊이는 모듈별 **메커니즘 / 실증 / 반론 / 최신 상태 / 측정 한계**의 커버리지로 판단한다. 관련 문헌의 참고문헌과 후속 인용을 양방향으로 추적한다. 특정 기관·기업·낙관론·비관론만 반복 인용하지 않는다.

### 5.2 탐색 순서

1. A~H 전체에서 자료가 어떤 종류로 존재하는지 넓게 지도를 만든다. 자료 가용성이 적은 주제도 원장에서 보존한다.
2. 핵심 인과 연결에 영향을 주는 자료부터 본문을 읽고 연구 방법·데이터·반론을 추출한다.
3. 각 핵심 가설을 지지하는 검색과 그 가설이 틀리거나 효과가 작다는 검색을 모두 수행한다.
4. 최신 버전·후속 연구·철회·정정·법률/명세 변경을 확인한다.
5. 비슷한 자료가 반복되고 추가 발견이 결론을 바꾸지 않으면 그 모듈은 정리 단계로 옮긴다. 실질적인 공백은 남겨 둔다.

최신 자료는 중요하지만 오래된 자료를 버리는 기준이 아니다. 역사적 제도·장기 표본과 현재 상태는 역할이 다르다. 영어를 중심으로 국제기구·학술 자료를 확보하고 한국은행 등 국내 자료를 보조한다. 지역별 주장은 해당 지역 원문으로 확인한다.

### 5.3 재현 가능한 검색 묶음

다음은 검색어의 출발점이며 고정된 검색 목록이 아니다. 검색엔진의 무관한 결과나 오래된 캐시를 확인 없이 채택하지 않는다.

| 모듈 | 검색어 묶음 예시 |
|---|---|
| A | money hierarchy; credit theories of money empirical history; unit of account settlement finality; tokenisation monetary singleness |
| B | debt sustainability interest growth primary balance maturity; Treasury buyback funding liquidity versus QE; TGA reserves ON RRP; dollar invoicing safe assets |
| C | stablecoin flows Treasury yields identification; stablecoin deposit substitution net demand; stablecoin reserve look-through; stablecoin payment velocity |
| D | stablecoin redemption run risk legal claim; tokenised deposits versus stablecoins; reserve attestations audit; cross-border payment total cost |
| E | Bitcoin inflation hedge safe haven out of sample; cryptocurrency risk factors; Ethereum L2 fee value capture; token revenue holder rights |
| F | agent payment authorization AP2 x402 cards; agentic payments real usage methodology; machine-to-machine payments recurring customers; agent fraud refunds |
| G | generative AI productivity randomized field experiment; AI macro productivity adoption lag; AI rebound elasticity energy; datacenter capex utilisation depreciation |
| H | stablecoin issuer reserve income distribution costs; network adoption token value accrual; AI infrastructure returns on invested capital; digital money competing scenarios |

### 5.4 확보 수준과 자료 상태

`DISCOVERED`는 발견, `ABSTRACT_ONLY`는 초록 확인, `FULLTEXT_READ`는 필요한 본문 확인, `DATA_ACQUIRED`는 실제 자료 확보, `REPRODUCED`는 명시한 계산 재현이다. 서로 다른 상태를 동의어로 쓰지 않는다. 단순히 HTML 페이지를 열었다고 전체 보고서의 본문을 읽은 것이 아니다.

유료 장벽·403·동적 페이지·미공개는 `ACCESS_LIMITED`로 남기고 공개 저자판·공식 대체 자료를 탐색한다. 접근 실패는 반대 증거가 아니며, 초록만 읽고 방법론을 확인했다고 쓰지 않는다. PDF 분석 시 페이지와 표·그림을 직접 확인하고 사용 가능한 시각 도구로 필요한 페이지만 대조한다. OCR은 최후 수단이다.

인용은 실제 URL/DOI/문서 ID와 페이지·절·표 또는 데이터 항목으로 연결한다. 긴 원문 복제 대신 필요한 범위의 요약과 짧은 인용을 사용한다. 원문 재배포 권한이 없으면 전체 파일을 저장소에 복제하지 않는다. 허용된 로컬 분석용 보관과 원격 재배포는 별개로 처리한다.

## 6. 자료 원장과 판단 규칙

### SOURCES.jsonl — 자료별 최소 필드

```text
source_id, title, authors_or_publisher, canonical_url, alternate_urls,
publication_date, revision_date, accessed_at, observation_period,
source_type, read_depth, source_family_id, independence_note,
relevant_claim_ids, exact_locator, access_limit, conflict_of_interest_note
```

실제 확보한 파일·데이터에만 `local_path`, `sha256`, `data_version`을 추가한다. 알 수 없는 필드는 `null`과 이유를 사용한다. 초기에 완전한 메타데이터를 강제하지 말고 읽는 과정에서 채운다.

### CLAIMS.jsonl — 주장별 최소 필드

```text
claim_id, initial_statement, refined_statement, claim_type,
scope_and_horizon, mechanism, supporting_source_ids,
challenging_source_ids, alternative_explanations, data_or_test_ids,
assessment, uncertainty, falsification_condition, decision_delta
```

`claim_type`은 회계관계·제도/규칙·역사·실증·인과·모형·시나리오를 구분한다. `assessment`는 `SUPPORTED_IN_SCOPE`, `CONDITIONAL`, `MIXED`, `NOT_SUPPORTED_BY_AVAILABLE_EVIDENCE`, `INSUFFICIENT_EVIDENCE`, `UNASSESSED` 등을 사용할 수 있다. **근거 부족은 거짓이라는 뜻이 아니다.** 인과가 확인되지 않았다는 이유만으로 유용한 관측 상관을 삭제하지 않는다.

숫자 하나의 종합 점수나 출처 수만으로 결론을 정하지 않는다. 표본·지역·시기·효과 크기·식별 방법·외적 타당성이 더 중요하다. 동일한 결론을 반복하는 여러 2차 글은 원연구 하나를 압도하는 증거가 아니다.

## 7. 분석·재현 과제

문헌만 정리하지 말고 실제 수행 가능한 계산을 한다. 아래 과제는 분석 묶음이며, 각각의 자료 상태와 실행 결과를 구분한다. 공개 자료로 가능한 부분부터 진행하고 필요한 자료가 없으면 대체 분석과 한계를 남긴다. 미실행 과제를 실행한 것처럼 보고하지 않는다.

### T01. 대차대조표 경로 비교

은행예금→스테이블코인, MMF/직접 국채→스테이블코인, 역외 사용자→달러 스테이블코인, 스테이블코인 상환을 비교한다. 사용자·발행사·은행·중앙은행·기존 자산 매도자의 자산/부채를 그린다. 준비금과 예금은 별도로 표시한다.

재무부 바이백은 자금 원천을 분기하여 다룬다. 기존 현금 사용과 신규 국채 발행을 구분하고, TGA 지출·차입의 시점 차이를 보존한다. 연준의 자산 매입과 비교하되 동일한 효과라고 가정하지 않는다. 산술 예제는 `SYNTHETIC_ACCOUNTING_EXAMPLE`로 표시한다.

### T02. 부채비율 민감도

정의가 명확한 공공 데이터 또는 명시적 가상 입력으로 다음 관계를 계산한다.

`b_t = ((1+i_t)/(1+g_t)) * b_(t-1) + d_t + sfa_t`

`b`는 명목 GDP 대비 부채, `i`는 해당 기간의 평균 명목 조달금리, `g`는 명목 GDP 성장률, `d`는 GDP 대비 기초재정적자, `sfa`는 부채 평가·분류 등 stock-flow adjustment다. `sfa=0`은 생략이 아니라 가정으로 표시한다.

기존 부채의 만기와 차환 때문에 정책금리 변화가 평균 조달금리에 즉시 1:1로 반영된다고 가정하지 않는다. 단기 시장금리 효과를 전체 이자비용 절감으로 바로 확대하지 않는다. AI의 실질 생산성·물가·세수 효과는 별도 조건으로 둔다. 결과는 예측이 아니라 민감도다.

### T03. 준비자산·순증 수요와 금리 효과

공시 가능한 발행사의 동일 기준일 자료로 준비자산의 직접 국채·MMF·레포·현금을 구분한다. 경제적 노출을 look-through 하되 같은 국채를 직접 보유와 펀드 내부 보유 양쪽에 중복 계산하지 않는다. 불명확한 간접 노출은 범위 또는 미상으로 남긴다.

발행사 매입액과 신규 글로벌 수요를 분리한다. BIS Working Paper 1270 등 핵심 실증 논문의 표본·충격 정의·규모·식별·시차·만기별 결과를 비교한다. 최신 개정판과 과거 계수를 혼합하지 않는다.

실제 시계열 확보 시 금리 수준과 변화, 정책금리/단기 기준금리 대비 스프레드, 시기별 국면을 구분한다. 국채 공급·세금 납부·위험선호·가상자산 가격·정책 기대에 따른 역인과와 누락 변수를 점검한다. 단순 상관/회귀만 수행했으면 `DESCRIPTIVE_NOT_CAUSAL`로 명시한다. IV·국소투영법도 식별 가정을 확인하기 전 자동으로 인과 증명으로 채택하지 않는다.

### T04. 비트코인 역할의 기간·국면 검증

가격 수준이 함께 올랐다는 비교를 넘어 수익률, 실질 수익률, 상관, 하방 국면, 최대 낙폭, 기간별 결과를 구분한다. 달러/원화 표시, 금·현금성 자산·주식 등 비교 기준, 표본 시작·종료일을 명시한다.

인플레이션 수준과 예상 밖 인플레이션, 단기 위기 헤지와 장기 구매력, 분산효과와 안전자산 성격을 각각 다른 질문으로 검증한다. 결과를 본 뒤 정한 구간은 탐색적이라고 기록한다. 가능하면 단순한 보유 기간·국면 민감도를 확인하되 본격적 전략 백테스트로 확장하지 않는다.

### T05. 에이전트 결제의 채택·비용·제약 비교

동일한 사용 사례를 두고 카드/계좌 결제, 토큰화된 은행 수단, 스테이블코인 결제를 비교한다. 발표·프로토콜 명세·샘플·실제 상업 실적을 별도 증거로 기록한다. 자동으로 특정 수단에 최고점·승자 지위를 주지 않는다.

메트릭을 `요청 수 / 성공한 지급 수 / 지급액 / 독립 이용자·사업자 / 반복 이용 / 순매출`로 분리한다. 조정 전·후 온체인 자료의 필터와 커버리지를 추적하고 데이터 공급자 간 중복을 확인한다.

총비용에는 결제수수료, FX/스프레드, 온·오프램프, 가스, 대기·사전예치 자금비용, 오류·사기·재시도·분쟁·사람 검토를 포함한다. 견적·가정·관측 비용을 구분한다. 필요한 공개 자료가 없으면 계산 가능한 하위 항목과 미상을 제시한다.

### T06. AI 생산성 문헌의 비교

긍정적·부정적·효과가 작은 연구를 연구 설계·도구 버전·직무·숙련도·기간·품질 지표에 따라 대조한다. 서로 다른 모집단의 효과 크기를 단순 평균하지 않는다. 일반화 가능한 조건과 일반화할 수 없는 조건을 적는다.

S23·S24·S25는 서로 같은 질문을 같은 방법으로 시험한 자료가 아니다. 현장 관측/도입 연구, 거시 모형, 특정 과업 실험의 차이를 유지한다. 최신 후속 연구와 실제 기업 도입 데이터를 추가한다.

### T07. 효율·수요·잔액의 민감도

다음의 단순 모형을 입력 가정과 함께 계산한다.

`총연산량 = 유효 작업 수 × 작업당 연산량`

`결제 목적 평균잔액 ≈ 기간 중 결제액 / 같은 기간 잔액 회전횟수`

두 번째 식은 회계적 사고 도구이지 식별된 화폐수요 모형이 아니다. 저축·담보·대기자금·예방적 보유와 네팅·외상 결제 등을 구분한다. 데이터 정의가 맞지 않으면 관측 회전율을 정밀 추정하지 않는다.

효율 개선으로 비용이 낮아지는 정도, 가격 전가, 수요 탄력성, 품질 변화, 공급 제약을 분기한다. 총연산량·총전력·매출·이익은 별개다. 총전력은 자원당 에너지 효율까지 별도로 반영한다. 가상 숫자는 실제 시장 수치와 같은 표에 섞지 않는다.

### T08. 가치 귀속 사례와 대안 시나리오

발행사, 결제/수탁/유통사, 네트워크·L2, AI 인프라/응용 서비스처럼 서로 다른 수익 구조를 대표하는 사례를 공개 공시 범위에서 선택한다. 먼저 넓게 탐색한 뒤 선택 이유를 기록하고 특정 기업 목록을 미리 고정하지 않는다.

예를 들어 발행사의 준비자산 이자수익은 평균 잔액·운용수익률과 관계가 있지만 유통 파트너 지급·운영비·손실·기타 수익을 반영해야 한다. 네트워크 소각은 회사 매출이나 이용자의 현금 배당과 다르다. AI 인프라는 감가상각·유지/확장 투자·가격 경쟁·고객 집중·가동률을 분리한다. 실제 제도와 회계는 원문으로 확인한다.

대안 시나리오를 최소한 다음 유형까지 검토하되, 증거에 따라 병합·수정한다: `디지털 달러 접근 확대`, `은행/기존 결제망 중심 토큰화`, `퍼블릭체인 성장과 토큰 가치 귀속 약화`, `상용화 지연 또는 특정 용도에 집중`, `생산성 확대와 공급 제약/마진 압박의 병존`.

모든 시나리오에 성립 조건·관측 지표·반증 조건·주요 불확실성을 붙인다. 지지 근거가 약한 시나리오에 동등한 확률을 임의 부여하지 않는다. 데이터로 뒷받침되지 않는 정밀 확률·가격 전망은 만들지 않는다.

## 8. 데이터·통계의 공통 품질 규칙

- 단위·빈도·통화·명목/실질·계절조정·기준일·표본·정의 변경을 기록한다. 차트의 관측기간을 생략하지 않는다.
- 원자료와 가공 자료를 분리하고, 코드·계산식·실제 실행 명령을 남긴다. 결측을 0으로 채우거나 출처 없는 보간·추정을 사실로 쓰지 않는다.
- 시계열의 발표일과 관측일을 구분한다. 현재 개정 데이터를 사용한 과거 설명을 당시 이용 가능한 예측으로 표현하지 않는다. 처음부터 결과를 알고 수행하는 탐색은 탐색으로 기록한다.
- 통계적 유의성과 경제적 크기, 상관과 인과, 표본 내 적합과 외부 예측, 구조 변화와 일시적 사건을 구분한다. 표본이 작아도 자료를 삭제하지 말고 적절히 해석한다.
- 수집 규모·빈도는 서비스 이용 조건과 rate limit을 따른다. 무제한 크롤링·유료 조회를 하지 않는다. 동일 실패가 반복되면 다른 공식 경로나 분석으로 전환하고 영향만 기록한다.

## 9. 실행 순서와 자율 진행

| 마일스톤 | 수행 내용 | 종료 시 남길 증거 |
|---|---|---|
| R0 | 로컬 지침·범위·기존 결과·시점 확인, 초기 원장 생성 | 실제 출력 경로, 시점 기준, 최초 가설, 가용 도구/제약 |
| R1 | A~H 전체의 넓은 자료 탐색과 반론 수집 | 자료 원장, 중복/독립성, 접근 상태, 커버리지와 빈칸 |
| R2 | 핵심 본문 분석과 T01~T08의 실행 가능한 분석 | 주장별 근거, 계산/코드/결과, 미실행 이유, 잠정 수정 |
| R3 | 대안 설명과 통합 결론 구성 | 초기 주장→수정→이유, 성립·반증 조건, 관측 지표 |
| R4 | 핵심 결론·인용·산술에 대한 제한된 검토 | 발견 사항, 수정, 남은 불확실성, 검토 독립성 여부 |
| R5 | 결과·근거·재현 방법·다음 시작점 인계 | 완성 보고서와 `RESEARCH_RETURN_PACKET.md`, 실제 파일/Git 영수증 |

각 단계는 승인 대기 게이트가 아니다. 자료 수집과 본문 분석은 필요한 범위에서 겹쳐 진행할 수 있다. R0를 반복하거나 모듈 하나의 미확인으로 전체 연구를 멈추지 않는다. 이미 유효한 증거는 재사용하고 새 정보·버전 변경이 있을 때 영향받는 부분만 갱신한다.

실제 독립 작업자 기능이 제공되고 기존 권한·비용 안에서 가능하면 A/B, C/D, E/F, G/H를 나눌 수 있다. 최종 원장은 한 명이 통합하여 중복과 상충을 관리한다. 사용할 수 없는 에이전트나 모델을 호출했다고 표현하지 않는다. 단일 작업자가 수행해도 된다.

R4는 전면 재연구가 아니다. 중요 수치·범주 혼동·주요 반론 누락·결론 과장을 한 번 점검하고 수정 부분만 재확인한다. 독립 검토가 실제로 없으면 `AUTHOR_SELF_REVIEW_ONLY`로 표시한다. 자기 검토를 독립 PASS로 바꾸지 않으며, 독립 검토의 부재만으로 유용한 연구 결과를 숨기지 않는다.

진행 보고는 단계 전환이나 실질적 발견 시 짧게 한다. `현재 단계 / 완료한 것 / 바뀐 판단 / 다음 작업`을 알리고 말미에 마일스톤과 현재 위치를 표시한다. 근거 없는 진행률·시간·토큰 수를 만들지 않는다.

실행 환경 제한이나 중단이 발생하면 가능한 결과를 보존하고 `CHECKPOINT.md`에 **완료 / 미완료 / 새로 확인된 것 / 정확한 다음 행동 / 재사용할 근거**를 기록한다. 백그라운드 실행·자동 재개·나중 통지를 실제 기능 없이 약속하지 않는다.

## 10. 최종 산출물 — 파일 수는 적게, 근거는 연결되게

필수 산출물은 다음 6개다. 이름은 저장소 규칙에 맞게 조정할 수 있지만 역할은 유지한다.

| 파일 | 반드시 포함할 내용 |
|---|---|
| `REPORT.md` | 쉬운 설명의 요약, 모듈별 판단, 주요 수치·조건, 반론, 대안 설명, 통합 결론, 관측 지표 |
| `SOURCES.jsonl` | 실제 읽은 범위, 원출처, 버전·시점, 중복/독립 관계, 확보·접근 제한 |
| `CLAIMS.jsonl` | 초기 주장, 수정된 주장, 지지/반대 근거, 판단과 불확실성, 반증 조건 |
| `ANALYSIS_AND_REVIEW.md` | T01~T08의 수행/미수행, 계산 재현 방법, 검토와 교정, 증거의 한계 |
| `CHECKPOINT.md` | 현재 단계·완료·미해결·다음 행동·실제 저장 위치 |
| `RESEARCH_RETURN_PACKET.md` | 다음 채널이 이전 대화 없이 결과를 이해하고 이어갈 수 있는 인계 패킷 |

실제로 사용한 경우에만 `data/`, `analysis/`, 그림·소형 결과표를 추가한다. 빈 디렉터리·빈 템플릿을 완료물처럼 양산하지 않는다. 원문 재배포가 허용되지 않으면 URL·메타데이터·발췌 위치·분석 결과만 기록한다.

`REPORT.md`는 첫 부분에서 답을 제시하고 상세 근거를 뒤에 둔다. 한국어로 작성하고 필요한 전문용어는 처음에 설명한다. 분량을 고정하기보다 8개 모듈의 연결, 중요한 반론, 재현 가능한 판단을 빠뜨리지 않는 데 집중한다. 출처와 모형의 설명을 여러 문서에 무의미하게 반복하지 않는다.

결론에는 다음을 반드시 구분한다: **유지된 주장 / 수정된 주장 / 근거가 약해 보류한 주장 / 새로 도출한 설명 / 아직 해결되지 않은 질문**. 출발 가설을 유지한 항목도 왜 유지하는지 근거를 적는다.

## 11. 연구 완료 기준과 보류 처리

완료란 모든 명제가 참으로 판명되거나 자료가 완벽하게 채워졌다는 뜻이 아니다. 각 모듈의 핵심 질문을 실제로 조사하고, 결론과 그 한계가 추적 가능하며, 다음 작업자가 재개할 수 있다는 뜻이다.

검토 시 다음을 확인한다.

1. A~H와 H01~H32의 처리 상태가 모두 보인다. 미해결은 미해결로 남아 있고 조용히 삭제되지 않았다.
2. 핵심 결론은 실제 열람한 원출처와 적용 범위에 연결된다. 접근 확인·초록·정독·재현 상태가 섞이지 않는다.
3. 중요한 대안 설명과 반례가 다뤄졌고 특정 결론에 유리한 표본·시점만 고르지 않았다.
4. T01~T08의 수행 여부와 산출물이 구분되며 실제 가능한 계산을 불필요한 엄격성 때문에 전부 뒤로 미루지 않았다.
5. 초기 가설보다 어떤 설명이 어떻게 개선됐는지 명확하다. 데이터 부족이 전체 결과의 폐기를 뜻하지 않는다.
6. 인계 패킷·체크포인트·실제 파일 경로가 있고, Git을 사용했다면 실제 identity와 원격 상태를 확인했다.

최종 상태는 `COMPLETED_WITH_LIMITATIONS` 또는 `PARTIAL_CHECKPOINTED` 등으로 표시할 수 있다. 별도의 `EVIDENCE_ASSESSMENT`에 주요 지지·조건부·혼합·미확인 항목을 기록한다. 연구 완료와 개별 주장 입증을 같은 PASS로 합치지 않는다.

## 12. 연구 결과 인계 패킷 형식

연구가 끝나거나 실행 환경상 중단해야 할 때 실제 결과로 아래 형식을 채운다. 빈 템플릿이나 예상 결론을 결과물로 제출하지 않는다.

```text
PACKET_CLASS = RESEARCH_RESULT_HANDOFF
FROM = 실제 수행 역할/환경
TO = OWNER / NEXT_RESEARCH_CHANNEL
PARENT_PACKET_ID = MDMA-CODEX-WORK-RESEARCH-20260921-001
RESEARCH_TITLE = 화폐·달러·스테이블코인·AI 경제
RESEARCH_STATUS = 실제 완료 또는 부분 완료 상태
EXECUTION_STARTED_AT = 실제 확인값 또는 UNKNOWN
COMPLETED_OR_CHECKPOINTED_AT = 실제 확인값
INFORMATION_CUTOFF = 마지막 검색과 데이터 기준의 실제 값
MILESTONE = 실제 위치
OUTPUT_ROOT = 실제 존재 경로
GIT_REPOSITORY = 확인한 값 또는 LOCAL_ONLY
GIT_BRANCH = 확인한 값 또는 NOT_CREATED
GIT_COMMIT = 실제 커밋 또는 NOT_CREATED
REMOTE_STATUS = 확인한 상태 또는 NOT_PUSHED / NOT_CHECKED
REVIEW_STATUS = 실제 독립 검토 / AUTHOR_SELF_REVIEW_ONLY / NOT_DONE
```

이어서 다음 내용을 한 패킷 안에 담는다.

- **핵심 결론:** 판단을 바꾸는 5~10개 결과. 각 결과에 근거 ID·대상 기간·조건·불확실성.
- **초기 가설의 변화:** 유지·수정·보류·신규 설명과 이유. 반대 근거를 포함.
- **확보한 근거와 분석:** 자료 수·원연구 수·정독 수·재현 수를 실제 집계 기준과 함께 제시. 목록 수를 독립 증거 수로 포장하지 않음.
- **미해결과 한계:** 현재 결론에 미치는 영향, 확보하지 못한 자료, 미수행 분석.
- **다음 연구의 시작점:** 무엇을 확인하면 결론이 달라지는지와 다음 행동. 이미 완료한 조사·계산의 반복 금지 범위.
- **산출물 위치:** 실제 파일, 실제 Git identity, 원격에 존재하는지 여부. 파일 경로·커밋을 추정해 쓰지 않음.
- **운영 경계:** 실거래·전략 변경·모델 입력 승격이 이루어지지 않았음을 실제 작업 내역과 구분해 기록.

최종 사용자 응답은 결과의 핵심과 이 인계 패킷을 중심으로 한다. 새 승인 질문을 만들어 마무리를 미루지 않는다. 유료 접근·외부 권한 등 사용자가 실제로 결정해야 할 문제가 남은 경우에만 그 영향과 필요한 결정 하나를 명확하게 적는다.

## 13. 준비 단계의 실제 상태

이번 인계 준비에서 공개 자료·문서·데이터 입구 28개에 접근해 시작 자료로 등록했다. **28은 읽은 논문 수·독립 연구 수·전체 본문 정독 수가 아니다.** 준비 단계에서 논문 전체의 체계적 검토, 통계 데이터 수집, 회귀·재현 분석, 독립 검증은 수행하지 않았다.

일부 NBER·Congress.gov·FiscalData와 바이백 자료 경로에는 접근 제한 또는 조회 실패가 있었다. 성공한 다른 원출처와 아직 해결되지 않은 탐색 과제를 분리해 `MDMA_SOURCE_SEEDS_v1.0_20260921.json`에 기록했다. 접근하지 못한 원문의 내용을 확인했다고 간주하지 않는다.

자료 목록은 검색의 시작점이지 최종 문헌 범위가 아니다. 특히 화폐사, 부채 지속가능성, 비트코인의 실증 금융연구, 국가별 현행 제도, 독립적 상업 이용 통계는 추가로 폭넓게 찾아야 한다. 공개 근거가 부족한 경우는 그대로 보고한다.

아래 S01~S28의 접근 상태는 **이 패킷 작성 당시의 상태**다. WORK의 실제 독서·데이터 확보·분석 상태는 별도로 갱신한다.

## 부록 A. 공개 출발 자료 28개

각 항목의 설명은 연구에 사용할 위치를 지정한 것이다. 해당 자료의 주장 전체를 이 패킷의 결론으로 채택한 것이 아니다.


### S01 · Money in the modern economy: an introduction

- 발행/작성: Bank of England
- 관련 모듈: A
- 준비 단계 접근: `PAGE_OPENED_SEED_ONLY`
- 원문/입구: https://www.bankofengland.co.uk/quarterly-bulletin/2014/q1/money-in-the-modern-economy-an-introduction
- 연구 시 유의: 화폐의 기능·청구권·신뢰 설명의 출발점. 다른 제도와 역사 전체에 자동 일반화하지 않는다.


### S02 · Money creation in the modern economy

- 발행/작성: Bank of England
- 관련 모듈: A, B, C
- 준비 단계 접근: `PAGE_OPENED_SEED_ONLY`
- 원문/입구: https://www.bankofengland.co.uk/quarterly-bulletin/2014/q1/money-creation-in-the-modern-economy
- 연구 시 유의: 은행 대출·예금·중앙은행 준비금의 회계 구분을 점검할 출발점.


### S03 · The International Role of the U.S. Dollar – 2025 Edition

- 발행/작성: Federal Reserve
- 관련 모듈: A, B, C
- 준비 단계 접근: `PAGE_OPENED_SEED_ONLY`
- 원문/입구: https://www.federalreserve.gov/econres/notes/feds-notes/the-international-role-of-the-u-s-dollar-2025-edition-20250718.html
- 연구 시 유의: 2025년 판이다. 최신 판과 통계 개정을 확인하고 준비통화·결제·외환거래·부채 표시 통화를 구분한다.


### S04 · Recent balance sheet trends

- 발행/작성: Federal Reserve
- 관련 모듈: B, C
- 준비 단계 접근: `PORTAL_OPENED_DATA_NOT_EXTRACTED`
- 원문/입구: https://www.federalreserve.gov/monetarypolicy/bst_recenttrends.htm
- 연구 시 유의: 연준 자산·부채 자료의 입구. 실제 시계열과 빈티지는 별도 확보해야 한다.


### S05 · Treasury Quarterly Refunding

- 발행/작성: U.S. Department of the Treasury
- 관련 모듈: B
- 준비 단계 접근: `PORTAL_OPENED_DATA_NOT_EXTRACTED`
- 원문/입구: https://home.treasury.gov/policy-issues/financing-the-government/quarterly-refunding
- 연구 시 유의: 국채 발행·현금관리·바이백 관련 최신 원문을 찾을 출발점. 발표와 실제 집행을 분리한다.


### S06 · Interest Rate Statistics

- 발행/작성: U.S. Department of the Treasury
- 관련 모듈: B, C, E
- 준비 단계 접근: `PORTAL_OPENED_DATA_NOT_EXTRACTED`
- 원문/입구: https://home.treasury.gov/policy-issues/financing-the-government/interest-rate-statistics
- 연구 시 유의: 단기·장기·실질 금리 자료의 입구. 할인수익률·투자수익률·만기와 관측일을 확인한다.


### S07 · Stablecoins and safe asset prices — BIS Working Paper 1270

- 발행/작성: BIS; Rashad Ahmed and Iñaki Aldasoro
- 관련 모듈: B, C
- 준비 단계 접근: `ABSTRACT_AND_SUMMARY_OPENED`
- 원문/입구: https://www.bis.org/publications/working-paper-1270-stablecoins-and-safe-asset-prices
- 연구 시 유의: 랜딩 페이지의 최초 발행일은 2025-05-28이지만 현재 초록에는 2026-03까지의 표본이 표시된다. 본문 판본·개정일·표본·계수를 결합해 확인한다. BIS 기관 전체의 견해로 단정하지 않는다.


### S08 · III. The next-generation monetary and financial system

- 발행/작성: BIS Annual Economic Report 2025
- 관련 모듈: A, C, D
- 준비 단계 접근: `PAGE_OPENED_SEED_ONLY`
- 원문/입구: https://www.bis.org/publications/aer-2025/next-generation-monetary-financial-system
- 연구 시 유의: 스테이블코인의 한계와 토큰화된 중앙은행·은행 화폐 경로를 함께 조사한다. 기관의 주장과 실증 결과를 구분한다.


### S09 · Investigating the impact of global stablecoins

- 발행/작성: G7 Working Group / BIS
- 관련 모듈: C, D
- 준비 단계 접근: `LANDING_PAGE_OPENED_REPORT_NOT_READ`
- 원문/입구: https://www.bis.org/publications/investigating-impact-global-stablecoins
- 연구 시 유의: 2019년의 위험·편익 분석 출발점. 현재의 시장규모·규제 상태를 나타내는 자료로 사용하지 않는다.


### S10 · Transparency & Stability

- 발행/작성: Circle
- 관련 모듈: C, D, H
- 준비 단계 접근: `PAGE_OPENED_REPORTS_NOT_AUDITED`
- 원문/입구: https://www.circle.com/transparency
- 연구 시 유의: 준비자산·상환·보고서 원문을 확보한다. 발행사 공시, 외부 확인업무, 전체 재무감사는 서로 구분한다.


### S11 · Transparency

- 발행/작성: Tether
- 관련 모듈: C, D, H
- 준비 단계 접근: `PAGE_OPENED_REPORTS_NOT_AUDITED`
- 원문/입구: https://tether.to/en/transparency/
- 연구 시 유의: 기간별 준비자산 원문과 발행 주체·토큰을 확인한다. 직접 국채·펀드·레포의 look-through 중복을 점검한다.


### S12 · Review of the Federal Reserve’s Supervision and Regulation of Silicon Valley Bank — Key Takeaways

- 발행/작성: Federal Reserve
- 관련 모듈: B, D
- 준비 단계 접근: `KEY_TAKEAWAYS_OPENED`
- 원문/입구: https://www.federalreserve.gov/publications/2023-April-SVB-Key-Takeaways.htm
- 연구 시 유의: 2023년 사례다. 금리위험·유동성·자금조달·감독에 관한 기관의 조사와 본 연구의 해석을 구분한다.


### S13 · Terraform and Kwon to Pay $4.5 Billion Following Fraud Verdict

- 발행/작성: U.S. SEC
- 관련 모듈: D
- 준비 단계 접근: `RELEASE_OPENED`
- 원문/입구: https://www.sec.gov/newsroom/press-releases/2024-73
- 연구 시 유의: 2024-06-13 발표다. 사건 당시 경제적 메커니즘과 현재 법적 상태를 구분하고 필요하면 판결 원문을 확인한다.


### S14 · Frequently Asked Questions

- 발행/작성: Bitcoin.org
- 관련 모듈: A, E
- 준비 단계 접근: `PAGE_OPENED_SEED_ONLY`
- 원문/입구: https://bitcoin.org/en/faq
- 연구 시 유의: 공급 규칙과 가격·수요 설명의 출발점. 실제 프로토콜 규칙은 Bitcoin Core 코드·규격과 대조하고 투자성과 증거로 사용하지 않는다.


### S15 · Ethereum gas and fees: technical overview

- 발행/작성: Ethereum.org
- 관련 모듈: E, H
- 준비 단계 접근: `PAGE_OPENED_SEED_ONLY`
- 원문/입구: https://ethereum.org/developers/docs/gas/
- 연구 시 유의: 수수료 구성·소각·검증자 보상 관련 규칙을 현행 버전으로 확인한다. 가격 상승의 증거가 아니다.


### S16 · Scaling

- 발행/작성: Ethereum.org
- 관련 모듈: E, H
- 준비 단계 접근: `PAGE_OPENED_SEED_ONLY`
- 원문/입구: https://ethereum.org/developers/docs/scaling/
- 연구 시 유의: L1/L2와 확장 방식의 기술적 관계를 확인하고 실제 경제적 귀속은 별도 자료로 검증한다.


### S17 · Oracles

- 발행/작성: Ethereum.org
- 관련 모듈: D, E, F
- 준비 단계 접근: `PAGE_OPENED_SEED_ONLY`
- 원문/입구: https://ethereum.org/developers/docs/oracles/
- 연구 시 유의: 온체인 검증과 외부 사실 확인의 경계, 오라클 신뢰·실패 경로를 조사한다.


### S18 · Agent Payments Protocol (AP2) Documentation

- 발행/작성: AP2 project
- 관련 모듈: D, F
- 준비 단계 접근: `HOME_AND_SAMPLE_DESCRIPTIONS_OPENED`
- 원문/입구: https://ap2-protocol.org/
- 연구 시 유의: 카드와 x402 예제, 권한 위임·결제 증거 구조의 출발점. 변경되는 명세의 버전·커밋을 다시 고정하며 예제를 상용 채택으로 세지 않는다.


### S19 · Introducing x402: a new standard for internet-native payments

- 발행/작성: Coinbase
- 관련 모듈: F
- 준비 단계 접근: `PAGE_OPENED_SEED_ONLY`
- 원문/입구: https://www.coinbase.com/developer-platform/discover/launches/x402
- 연구 시 유의: 발표 당시 기능 설명이다. 최신 규격·저장소·실제 사용 데이터를 추가 확인하고 사업자의 기대와 관측을 분리한다.


### S20 · Stablecoin Transactions

- 발행/작성: Visa / Allium
- 관련 모듈: C, F
- 준비 단계 접근: `PAGE_AND_METHODOLOGY_LINKS_OPENED_DATA_NOT_EXTRACTED`
- 원문/입구: https://visaonchainanalytics.com/transactions
- 연구 시 유의: 조정 전·후 거래량과 분류 정의를 구분한다. 조정 거래량을 곧바로 실물 상품 결제나 독립 고객 수로 바꾸지 않는다.


### S21 · Agentic Payments

- 발행/작성: Visa / Allium
- 관련 모듈: F
- 준비 단계 접근: `PORTAL_OPENED_DATA_NOT_EXTRACTED`
- 원문/입구: https://visaonchainanalytics.com/agentic-payments
- 연구 시 유의: 에이전트 결제 데이터 탐색 입구. 프로토콜·체인·관측 범위·봇 제거·실제 결제 여부를 검증하기 전 수치를 채택하지 않는다.


### S22 · Stablecoins — Overview

- 발행/작성: Allium
- 관련 모듈: C, F
- 준비 단계 접근: `DOCUMENTATION_OPENED_SEED_ONLY`
- 원문/입구: https://docs.allium.so/historical-data/stablecoins
- 연구 시 유의: 데이터 테이블·분류·필터의 정의를 추적한다. Visa 화면과 같은 원데이터를 독립 증거 두 개로 세지 않는다.


### S23 · Generative AI at Work

- 발행/작성: Erik Brynjolfsson, Danielle Li, Lindsey Raymond
- 관련 모듈: G
- 준비 단계 접근: `ABSTRACT_AND_VERSION_HISTORY_OPENED`
- 원문/입구: https://arxiv.org/abs/2304.11771
- 연구 시 유의: arXiv v2는 2024-11-06 개정이다. 고객지원 현장 연구의 표본·과업·기간을 유지하고 다른 직무나 거시경제에 그대로 일반화하지 않는다. 학술지 최종판도 추가 확인한다.


### S24 · The Simple Macroeconomics of AI

- 발행/작성: Daron Acemoglu / MIT
- 관련 모듈: G
- 준비 단계 접근: `SUMMARY_OPENED_PAPER_NOT_READ`
- 원문/입구: https://shapingwork.mit.edu/research/the-simple-macroeconomics-of-ai/
- 연구 시 유의: 이 페이지는 2024-04 / 2024-05 개정 논문 요약이다. 최신 출판판·입력 가정·민감도를 확인하고 모형 추정을 관측 사실로 취급하지 않는다.


### S25 · Measuring the Impact of Early-2025 AI on Experienced Open-Source Developer Productivity

- 발행/작성: METR
- 관련 모듈: F, G
- 준비 단계 접근: `RESEARCH_PAGE_OPENED_SEED_ONLY`
- 원문/입구: https://metr.org/blog/2025-07-10-early-2025-ai-experienced-os-dev-study/
- 연구 시 유의: 숙련 개발자·특정 환경·2025년 초 도구를 대상으로 한 연구다. 최신 후속 연구와 표본 선택·중단·학습 효과를 확인한다.


### S26 · Energy and AI

- 발행/작성: International Energy Agency
- 관련 모듈: G, H
- 준비 단계 접근: `LANDING_PAGE_OPENED_REPORT_NOT_READ`
- 원문/입구: https://www.iea.org/reports/energy-and-ai
- 연구 시 유의: 전력·데이터센터 제약 연구의 출발점. 실제 사용량·예측·시나리오 가정을 분리하고 최신 판을 추가 확인한다.


### S27 · The AI Buildout and the Economy: Publicly Available Data to Assess AI’s Impact

- 발행/작성: Federal Reserve; Paul E. Soto, Mason Thieu, Jeffrey S. Allen
- 관련 모듈: B, F, G, H
- 준비 단계 접근: `ARTICLE_TEXT_OPENED_DATA_NOT_EXTRACTED`
- 원문/입구: https://www.federalreserve.gov/econres/notes/feds-notes/the-ai-buildout-and-the-economy-publicly-available-data-to-assess-ais-impact-20260717.html
- 연구 시 유의: 2026-07-17 연구다. 능력·비용, 기업 투자·도입, 생산성·노동을 분리한 지표 설계와 연결된 공공 데이터를 확인한다.


### S28 · EDGAR Full Text Search

- 발행/작성: U.S. SEC
- 관련 모듈: C, G, H
- 준비 단계 접근: `PORTAL_OPENED_FILINGS_NOT_EXTRACTED`
- 원문/입구: https://www.sec.gov/edgar/search/
- 연구 시 유의: 기업별 공시를 찾는 입구일 뿐 기업 분석 완료가 아니다. 실제 filing accession·기간·항목을 별도 기록한다.


## 부록 B. 해결해야 할 탐색 공백


**Risks and Returns of Cryptocurrency** — `FETCH_FAILED_403`

제목·저자·판본을 원 출판사 또는 저자 기관에서 확인. 이번 패킷의 사실 근거로 채택하지 않음.


**U.S. Treasury debt buyback FAQs and operation results** — `CORRECT_CURRENT_FAQ_AND_RESULTS_URLS_TO_RESOLVE`

S05와 뉴욕 연은 공식 시장운영 문서에서 현행 FAQ·집행결과를 발견하고 확인. 접근 실패한 추정 경로를 확정 URL로 재사용하지 않음.


**Debt to the Penny / fiscal and debt statistics** — `FETCH_FAILED_IN_PREPARATION`

FiscalData 공식 탐색·대체 공식 자료에서 실제 데이터와 정의 확보.


**U.S. stablecoin legislation and implementing rules** — `FETCH_RESTRICTED_IN_PREPARATION_LEGAL_STATUS_NOT_VERIFIED`

Congress.gov/GovInfo/관할 감독기관의 원문으로 법률 식별자·성립·발효·시행 규칙을 각각 확인. 이 링크 자체로 현행법 내용을 확정하지 않음.


**BIS/IMF/CBO/FSB/CPMI/BOK and academic counter-literature** — `BROAD_SEARCH_REQUIRED`

부채 지속가능성, 외환보유·국제결제, 예금 대체, 역사적 화폐, 디지털자산 수익률, 실물 결제, AI 생산성에 대해 신규 근거와 반례 탐색.


## 부록 C. 최초 실행 지시

이 패킷을 현재 연구 업무의 실행 요청으로 접수하고 R0부터 시작한다. 출발 가설의 입증을 목표로 삼지 말고, 원문·반론·데이터를 통해 수정 가능한 설명을 만든다. 일반적인 단계 전환은 추가 승인 없이 진행한다. 결과를 정리한 뒤 `RESEARCH_RETURN_PACKET.md`를 반환한다. 실행 환경이 중단을 요구하면 완료한 근거와 정확한 재개 지점을 보존하고 실제 상태만 보고한다.

**패킷 준비 위치:** 설계·초기 자료 탐색 완료 / Codex WORK 접수·연구 실행 미수행.
