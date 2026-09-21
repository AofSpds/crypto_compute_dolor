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
