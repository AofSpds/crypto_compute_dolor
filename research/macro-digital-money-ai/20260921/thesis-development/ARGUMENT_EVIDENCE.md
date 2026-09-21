# THESIS v1.1 — 근거·변경 기록

작성·접근일: 2026-09-22 KST. `AUTHOR_SELF_REVIEW_ONLY`.
이 문서는 [THESIS_v1.1.md](THESIS_v1.1.md)의 주장 위치, 이번에 실제로 읽은 범위, 기존 연구의 재사용, 계산과 한계를 연결한다. 첨부 외부 검토는 별도 웹챗의 제한된 주장 검토이며 이번 개정본의 독립 검토자가 아니다.

## 1. 보존과 연구 범위

- 원문·요청서·첨부 payload 12개와 받은 첨부 두 개의 사본을 먼저 보존했다. baseline은 별도 첨부의 정확한 바이트를 사용하고 패킷 내 본문과 개행 정규화 후 대조했다. SHA-256: `8f1fa519e496182d5a168926dc879be0909d6eba3af61eed4c472fe610083325`.
- 보존 commit A: `3cb224a839fcb3cd393a463824762fcdf0769eda`, branch `codex/mdma-research-20260921`, remote `https://github.com/AofSpds/crypto_compute_dolor.git`. 일반 push 성공 뒤 `ls-remote`에서 같은 SHA를 확인한 다음 연구했다.
- 재사용한 기존 연구 기준점: `39d5cbed92459b55b70e0dd7ba231584a4e75b73`. 기존 원문·SOURCES·CLAIMS·계산 파일은 수정하지 않았다. 외부 검토의 원저장소 미열람 제한도 바꾸지 않았다.
- 첫 전달일과 폴더 이름은 20260921이며, 실제 추가 연구·작성은 자정을 넘어 2026-09-22 KST에 진행했다. 논문의 출판연도와 실험·통계 관측기간을 구분했다.
- HLOM 및 다른 프로젝트의 과거 절차·권한을 이번 연구의 운영 지시로 가져오지 않았다. 첨부 코드 `verify_arithmetic.py`는 기록으로만 보존하고 실행하지 않았다.

## 2. P01–P10 변경과 반증 연결

### P01 — 실행 가능한 활동의 경계 / 본문 §1

**원 주장 → 개정:** 판단·조정 비용 하락이 새 경제활동을 연다 → 품질·완료율·위험 제약을 만족하는 총비용이 구매자의 편익 아래로 내려가고 반복 수요가 고정비를 회수할 때 활동 경계가 넓어진다.

**이유·근거:** N01 §§II–III의 시장/내부 조정 비교, N02 §§3.1–3.2의 특수 투자·적응, 기존 S23/S25/S43, 이번 N11의 업무별 상반된 효과. A01은 사람/규칙 자동화/LLM 보조/에이전트를 두 업무군에서 비교한 가상 계산, A02는 수요·고정비의 진입 경계 계산이다. 실증 계수로 보정한 모형은 아니다.

**강한 반론·대응:** 기존 프로그램이 더 싸거나 새 수요가 없을 수 있다. 규칙 자동화를 비교군으로 넣고, 기존 업무 대체와 신규 업무를 나눈다. AI가 내부 조정비도 낮추므로 기업 해체·완전한 시장 분산은 주장하지 않는다. 업데이트는 같은 업무·품질 기준의 완료당 비용, 고정비 회수기간과 실제 반복 수요로 한다.

### P02 — 경제적 가치 / 본문 §1 마지막 세 단락

**원 주장 → 개정:** 더 많은 가능한 일이 가치가 된다 → 잠재적 필요·유효수요·개인 편익·매출·최종 부가가치·사회적 순편익을 분리한다.

**종류·근거:** 비용/편익 정의와 자체 논리, A02의 구매자 기대 순편익 예시. 새 GDP 추정이나 사회적 후생 수치는 만들지 않았다. N04는 무형투자 측정이 단순하지 않다는 이론적 배경이며 새 활동의 크기를 입증하지 않는다.

**반론·조건:** API 중간거래·재판매·대체만 늘거나 스팸 등 외부 피해가 생길 수 있다. 최종 완료, 품질, 기존 활동 대체와 외부 비용을 측정한다. 사적 거래 증가가 사회적 가치 증가로 이어지지 않는 자료는 이 명제의 범위를 줄이는 근거다.

### P03 — 위임·검증·책임 / 본문 §2

**원 주장 → 개정:** 생성이 싸지면 신뢰가 새 병목 → 검증의 비용 비중·절대 비용·처리 병목을 나누고, 닫힌 조직·반복 공급자·자동 확인이 검증비도 낮출 가능성을 포함한다.

**근거·열람:** N03 인쇄 pp24–29를 스캔 화면으로 읽었다. 다중 과업의 측정/보상 왜곡 이론이지 LLM의 선호나 법적 지위를 설명하는 모형으로 쓰지 않는다. N11의 방법·Table 7·한계를 읽고 해당 표 화면을 확인했다. S18/S56은 기존 문서 열람 재사용이며 실제 지급·서명·conformance 없음.

**반론·조건:** 확인이 거의 자동인 업무에서는 별도 검증업체가 필요하지 않을 수 있다. 권한 증거는 산출 품질·법적 집행·환불 보증과 다르다. 대기시간·개입율·사후 오류·복구비가 확장과 어떻게 연결되는지로 병목 여부를 갱신한다.

### P04 — 달러 / 본문 제목·§4

**원 주장 → 개정:** 달러경제의 기계화 → 검증 가능한 위임이라는 일반 메커니즘 안에서 달러를 중요한 사례로 재배치한다. 청구 통화·지급 수단·장기 보유·기초 청구권을 구별한다.

**근거:** N07의 1990–2023년 132개국 불균형 패널과 통계 정의 한계, N08 시나리오·마찰, N10 회의 정리. N15는 지배 통화 모형의 공식 초록 수준만 확인했으므로 새 실증의 근거로 사용하지 않았다. N07의 세계 사용은 AI 수요로 식별되지 않는다. N08/N10가 S07/S37 등을 소개해도 독립 연구 수를 추가하지 않는다.

**반론·조건:** 국내 소득·세금·지출 통화와 기존 지급망이 달러 경유를 불리하게 만들 수 있다. 지역 통화의 효율·접근성이 개선되는 경우도 포함한다. 회랑별 거래의 표시/정산/보유 통화를 연결한 자료로 달러 접근 확대인지 단순 수단 교체인지 구분한다.

### P05 — 지급수단의 경쟁 / 본문 §3

**원 주장 → 개정:** 디지털 화폐가 에이전트 지급의 기반 → 카드·계좌·청구·선불·스테이블코인·토큰화 예금이 접근·신용·환불·회계·자금 비용을 포함해 경쟁한다.

**근거:** N09 §§3–5의 가정과 대차대조표 메커니즘을 새로 읽었다. 기존 S18/T05의 혼합 지급 예시·가상 비용 분석을 재사용했다. S08을 이번에 최초로 주요 관련 절까지 읽어, 액면 교환과 신용·유동성 측면의 강한 반론을 반영했다. 기존 S08 레코드의 DISCOVERED 상태는 역사적 기록으로 유지하며 이 문서가 새 열람의 추가 기록이다.

**반론·조건:** 묶음 청구가 개별 지급비를 없애거나 은행의 신용 기능이 더 효율적일 수 있다. 비은행 지급도 신용·수탁을 다시 묶어 제공할 수 있으므로 기술 이름만으로 비교하지 않는다. 동일 서비스의 완료까지 들어가는 비용·지연·손실과 독립 반복 이용이 관측 기준이다.

### P06 — 잔액 / 본문 §5

**원 주장 → 개정:** 흐름×잠김 시간+buffer → 정상 상태의 금액가중 평균 잠김액 근사로 범위를 좁힌다. 최대 지급 필요액, 미사용 현금의 최적 재고, 신용·상계, 저축·담보 목적 잔액을 분리한다.

**근거:** N13의 실시간/이연 정산과 위험·유동성 구조, S08의 신용·선지급 반론. A03은 5개 가상 유동성 조건, A04는 2개 자금 보충비 가정의 재고 모형, RESULTS.json의 일중 두 지급 예시다. A04는 가정을 명시한 자체 미분·최적화 예시다. Baumol/Tobin 원논문을 읽었다고 쓰지 않는다.

**반론·조건:** 지급이 몰리거나 상환·입출금이 느려지면 평균 잠김액이 줄어도 buffer가 커질 수 있다. 가상 3배 흐름/0.1배 시간의 잔액 감소는 시장 전망이 아니다. 순정산액·금액가중 체류 시간·buffer·보유 목적 자료가 있으면 업데이트한다. 목적별 잔액과 발행사 준비금을 중복 합산하지 않는다.

### P07 — 국채 전달 / 본문 §6

**원 주장 → 개정:** 준비금이 국채 수요와 연결된다 → 보유 주체·담보·자금 원천·반사실 수요곡선·만기별 가격 효과를 따로 정의한다. 기존 MMF 대체라도 수요 탄력성·딜러 제약 변화의 가격 효과는 가능하다.

**근거:** 기존 S07 June2026·S37 March2026 방법/표 검토 및 T01/T03, S36, 이번 N09 §5. S07은 이번에 보존 PDF 인쇄 p34 주38을 화면 확인하고 N12 할인채 공식으로 A05를 계산했다. 4–5bp를 0.0100–0.0125달러로 환산하는 예시와 원 주석 달러 표기의 차이를 확인했다. bp 회귀 오류를 확인한 것은 아니다.

**반론·조건:** “모든 매수에는 매도가 있으니 가격 효과도 없다”는 반론은 수요곡선·중개 마찰을 놓친다. 반대로 가격 반응만으로 전 세계 순증 자금 비율도 알 수 없다. H10은 **금리 효과 부분 근거 존재 / 글로벌 순증 규모 미식별**로 보류 유지한다. 이전 자산·발행/상환·은행/매도자 재투자·만기별 대체를 연결한 자료가 우선 필요하다.

### P08 — 생산성·거시금융 / 본문 §§2·7

**원 주장 → 개정:** AI 생산성 확대가 경제활동·부채 여건을 개선 → 과업 효과와 조직 보완투자, 수요, 실질·명목 성장, 투자금리·차환을 연결하되 단일 방향은 가정하지 않는다.

**근거:** H25 실제 원장과 S23/S25/S42/S43, 새 N11, N04, 기존 S34/T02. H25는 MIXED/REFINED였으며 “평균 0” 판정이 아니다. S23의 15%는 해결건수/시간·도입시차 분석; S43의 26.08%는 February2025 저자본의 사용 IV; S25의 +19%는 작업시간 증가. N11의 −19는 정답률 퍼센트포인트다. 도구·모집단·분모가 달라 기계적으로 합산하지 않았다.

**반론·조건:** 신기술·새 과업이 기존 추정의 범위를 넘을 수 있고 선택·학습·평행 작업 측정이 바뀔 수 있다. 무형투자를 주장만으로 생산성 부진의 해명에 쓰지 않는다. 동일 과업·도구·품질 비교와 기업의 유효 산출·투자 비용, 명목세원·차환 자료가 업데이트 조건이다.

### P09 — 가치 창출과 포착 / 본문 §8

**원 주장 → 개정:** 고객·데이터·권한·신뢰 보유자가 가치를 포착 → 모방·경쟁·진입·전환과 보완 자산의 희소성, 권리·계약이 귀속을 결정한다. 필요 기능이라는 사실만으로 별도 사업자의 초과이윤은 입증되지 않는다.

**근거:** N06 §§3–4, 기존 S31/S46 및 T08 산술. A06의 거래량·가격·원가·고정비 세 가상 경로는 거래 확대와 이익이 분리될 수 있음을 보이는 계산이다. 회사 공시는 독립적 AI ROIC 자료가 아니다. 비현금흐름 자산은 FCF식으로 평가하지 않았다.

**반론·조건:** 개방 표준과 경쟁은 소비자 편익을 키우지만 기존 대규모 유통망에 유리할 수도 있다. 고객 유지·교체·멀티호밍·진입·마진·권리별 현금 흐름을 관측한다. H18 인과 프리미엄 분해는 보류 유지하며 본론 비중을 축소했다.

### P10 — 보급·검증 / 본문 §§2·9

**원 주장 → 개정:** 검증 쉬운 업무·지급 추상화가 먼저 보급 → 업무 비교에서 검증비·반복·가역성·외부 지급 마찰이 채택 이익을 가른다는 **전망**으로 명시하고 다섯 관측/반증 조건을 제시한다.

**근거:** N01–N04/N11의 이론·과업 실증을 연결한 저자의 추론이며, 시장 보급 순서 자체를 추정한 논문은 없다. 기존 S21/S22/S31/S56의 업체·프로토콜 지표는 구현/발표 층위로만 쓴다. H23 보류는 통계 미확보이지 세계의 실제 상업활동 부재 판정이 아니다.

**반론·조건:** 열린 시장의 새 서비스도 품질 확인이 싸면 먼저 확대될 수 있다. 접근성·품질·도구·보조금을 맞춘 비교에서 예상 패턴이 반복해 반대로 나오면 설명을 고친다. 새 증거가 없는데 보류를 문장만으로 승격하지 않는다.

## 3. 신규 탐색 원장 — URL·시점·열람·독립성

아래 목록은 **새로운 독립 실증 연구 15건**이라는 뜻이 아니다. 이론 원문, 정책 분석, 실험, 초록 및 실패 후보가 섞여 있다. 발행사 발표·BIS·Fed 문서의 상호 인용도 중복 독립 증거로 세지 않는다. 접근은 모두 2026-09-22 KST. 확보된 로컬 원자료의 정확한 UTC·해시·경로는 [DOWNLOAD_MANIFEST.json](evidence/DOWNLOAD_MANIFEST.json)에 있다. 다운로드 성공은 본문 열람의 자동 표시가 아니며 아래 범위를 따른다.

| ID | 정확한 자료·판본·URL | 실제 범위 / 성격 / 제한 |
|---|---|---|
| N01 | Coase, *The Nature of the Firm*, Economica 1937, 4(16):386–405, [DOI](https://onlinelibrary.wiley.com/doi/10.1111/j.1468-0335.1937.tb00002.x) | 공식 HTML §§I–III, 특히 II–III 읽음. 이론. 웹 열람 성공, 로컬 다운로드403. AI 실증 아님. |
| N02 | Williamson, *Transaction Cost Economics: The Natural Progression*, Nobel lecture 2009, [PDF](https://www.nobelprize.org/uploads/2018/06/williamson_lecture.pdf) | PDF pp8–10, §§3.1–3.2의 가정·적응·특수 투자. 저자의 이론 정리. 전체22쪽 완독 아님. 첫 웹 PDF 처리 실패 뒤 공식 공개 PDF 정상 다운로드. |
| N03 | Holmström & Milgrom, *Multitask Principal–Agent Analyses*, JLEO 7 special issue, 1991:24–52, [저자 보관 PDF](https://web.stanford.edu/~milgrom/publishedarticles/Multitask%20Principal%20Agent.pdf) | 스캔 PDF pp1–3(인쇄24–29) 직접 화면 확인. 서론·선형 모형 설정. 전체 증명 검증 없음. 모델의 계약 가정을 불완전계약 이론과 동일시하지 않음. 다른 잘못된 후보 URL은 열람 실패. |
| N04 | Brynjolfsson, Rock & Syverson, *The Productivity J-Curve*, NBER25148, Oct2018/Jan2020개정, [NBER 공식 공개본](https://conference.nber.org/confer/2020/YSAIf20/EB2.pdf), [서지](https://www.nber.org/papers/w25148) | 표지·초록·서론 PDF pp1–5의 보완투자/측정 메커니즘. 2021 AEJ판 출판은 메타데이터만 확인. 과거 소프트웨어·자본 측정 연구이며 2026 AI 계수로 인용 안 함. S23과 저자 일부 중복, 다른 분석. |
| N05 | Baumol1952 원문 후보: [OUP](https://academic.oup.com/qje/article-abstract/66/4/545/1938624), [찾은 PDF](https://karlshell.com/wp-content/uploads/2016/02/The-Transactions-Demand-for-Cash-An-Inventory-Theoretic-Approach.pdf) | **원문 미열람.** OUP 최소 페이지/직접 PDF 실패. 받은 17쪽 PDF는 1952 논문이 아니라 강의 슬라이드여서 1차 근거에서 제외. 파일명·검색결과를 원문 확인으로 승격하지 않음. A04는 자체 명시 모형. |
| N06 | Teece, *Profiting from technological innovation*, Research Policy15(6),1986:285–305, [원논문 공개 사본](https://www.edegan.com/pdfs/Teece%20%281986%29%20-%20Profiting%20From%20Technological%20Innovation%20Implications%20For%20Integration%20Collaboration%20Licensing%20And%20Public%20Policy.pdf), DOI10.1016/0048-7333(86)90027-2 | PDF p1·pp5–7(인쇄285·289–291), §§3–4. 원논문 본문을 읽었으나 호스트는 저자/출판사가 아닌 학술 사본. 출판사 열람 실패·SSRN 초록은 다운로드 불가; 사본과 서지 대조. 미래 AI 승자 실증 아님. |
| N07 | Boz, Brüggen, Casas, Georgiadis, Gopinath, Mehl, *Patterns of Invoicing Currency in Global Trade in a Fragmenting World Economy*, IMF WP25/178, Sep5 2025, [PDF](https://www.imf.org/-/media/files/publications/wp/2025/english/wpiea2025178-source-pdf.pdf) | 웹 PDF 서론·§2.1–2.4·§4 관련 제한 주16 읽음. 132개국1990–2023 불균형 패널, 통계 정의/표본 제약. 별도 회귀·자료 재현 없음, 수치 표 추출 안 함. 로컬403로 고정 PDF 미보존. |
| N08 | Aldasoro, Frost & Ito, *The impact of stablecoins on the international monetary and financial system*, BIS Paper170, May5 2026, [본문·PDF](https://www.bis.org/publications/paper-170-impact-stablecoins-international-monetary-and-financial-system) | PDF pp3–6·19–20(인쇄1–4·17–18), 개요·역할·세 시나리오·마찰. 시나리오 확률 추정 아님. S07 등 인용 연구와 독립 중복 계산 금지. 일부 본문 지역/법제 서술은 최신 법 확인 없이 인용하지 않음. |
| N09 | Kim, Ruprecht & Styczynski, *Payment Stablecoins and Cross Border Payments: Benefits and Implications for Monetary Policy Implementation*, FEDS Notes Mar30 2026, [HTML](https://www.federalreserve.gov/econres/notes/feds-notes/payment-stablecoins-and-cross-border-payments-benefits-and-implications-for-monetary-policy-20260330.html) | §§3–5, 가상 접근비·대차대조표·자금 재배분·on/off-ramp 제한 읽음. 실제 평균 비용 효과를 추정한 실증이 아님. S36과 연준 기관 중복, 메커니즘 보완. 법 시행 여부의 새 확인으로 쓰지 않음. |
| N10 | Correa, Goldberg, Keerati, Londono, Ravazzolo, *Fifth Conference on the International Roles of the U.S. Dollar…*, FEDS Notes Jul16 2026, [HTML](https://www.federalreserve.gov/econres/notes/feds-notes/fifth-conference-on-the-international-roles-of-the-u-s-dollar-stablecoins-digital-payments-and-the-ir-of-the-usd-20260716.html) | June22–23 2026 회의의 주요 논의·결론 읽음. 발언과 논문을 소개한 회의 정리. S37 발표 소개를 새 독립 인과 연구로 세지 않음. |
| N11 | Dell’Acqua, McFowland III, Mollick, Lifshitz-Assaf, Kellogg, Rajendran, Krayer, Candelon, Lakhani, *Navigating the Jagged Technological Frontier*, Organization Science, online Mar11 2026, DOI10.1287/orsc.2025.21838, [HBS PDF](https://www.hbs.edu/ris/Publication%20Files/dell-acqua-et-al-2026-navigating-the-jagged-technological-frontier_5c589c8c-fbb5-458f-b285-c944746cd717.pdf) | 표지·초록·방법 PDF5–6·주요 결과12·한계17, Table7/Fig5 화면 확인. 사전 등록 RCT758명,385/373명 과업군, 모델Apr2023 GPT-4·실험Jun2023 설명. BCG와 협력·저자 이해관계 맥락. 유효한 새 반례이나 현재 모델 외삽·전국 생산성 추정 안 함. 미시자료 재현0. |
| N12 | US TreasuryDirect, *Understanding Pricing and Interest Rates*, [Bills 가격식](https://www.treasurydirect.gov/marketable-securities/understanding-pricing/) | 공식 할인채 가격식·단위·예시. 문서 발행일 미표시, 접근일만 확정. 시장수익률·기간구조 추정 아님. A05에서90일·100달러를 명시. |
| N13 | Bech, Shimizu & Wong, *The quest for speed in payments*, BIS Quarterly Review2017, [HTML](https://www.bis.org/publications/quest-speed-payments) | real-time/deferred inter-PSP settlement·prefunding·liquidity 단락. 당시 나라별 이용 통계는 현재 자료로 안 씀. 지급 구조의 공식 연구자 분석. |
| N14 | Baumol/Tobin 관련 저자 보관 후보 [CommunicationTheOptimalCash.pdf](https://pages.stern.nyu.edu/~wbaumol/CommunicationTheOptimalCash.pdf) | 검색상 JEL1989 관련 서지·웹 PDF 객체만 확인; 텍스트0/스크린샷 실패, 직접404. **내용 미열람·인용 근거 미사용**. 같은 실패 재시도하지 않음. |
| N15 | Casas, Diez, Gopinath & Gourinchas, *Dominant Currency Paradigm: A New Model for Small Open Economies*, IMF WP17/264, Nov22 2017, [공식 페이지](https://www.imf.org/en/publications/wp/issues/2017/11/22/dominant-currency-paradigm-a-new-model-for-small-open-economies-45431) | 초록·메타데이터만 확인. 가격 보완성·수입중간재 모형의 탐색 자료. 콜롬비아 분석의 방법·표 미열람, 본론의 수치·인과 근거로 미사용. |

**S08의 신규 열람 추가:** BIS Annual Economic Report2025 III장 [공식 HTML](https://www.bis.org/publications/aer-2025/next-generation-monetary-financial-system)의 요점, Money and trust, stablecoins/singleness/elasticity, tokenised central-bank/commercial-bank money 관련 절을 확인했다. 정책·제도 분석이며 토큰화 예금의 보편적 성능 우위를 실험한 결과는 아니다. 본론은 은행 중심 해석이라는 성격과 함께 사용한다.

## 4. 재사용 근거의 위치와 제한

기존 원장의 정확한 서지·원자료 해시는 [../SOURCES.jsonl](../SOURCES.jsonl), 계산 입력/변환은 [../ANALYSIS_AND_REVIEW.md](../ANALYSIS_AND_REVIEW.md)에 있다. 아래는 이번 사용의 위치이며 새 독립 재현을 주장하지 않는다.

| 기존 ID | 이번 본문 사용 / 유지할 제한 |
|---|---|
| S02/S36, T01 | 은행화폐·준비금 발행·예금 재배분. 메커니즘/가상 회계, 세계 순효과 추정 아님. |
| S07 | June2026, 2021-01–2026-03·7stablecoin/117chains, GIV/LP, Eq2·Table2·반응함수 관련 기존 검토 재사용. 이번 추가는 PDF36/인쇄34/주38 화면·산술뿐. PDF SHA `f98543e21976dace3fc50c02e872cd0a41cd0ae5af8c6b52d42f5c7ff524506a`. |
| S37 | IMF WP26/44,2019-01–2025-06, USDT/USDC 사건·이분산성 식별. Table1·동적 반응의 기존 검토. N10 회의 소개와 중복. 회귀 미재현. |
| S18/S56 | AP2·x402 문서 관련 절/예시. moving docs; 기존 repo SHA는 문서의 동일 commit을 보증하지 않음. 실제 구현 적합성·지급 미시험. 새 추측 URL `/specification/`는 실패하여 새 열람으로 세지 않음. |
| S21/S22/S31 | Visa/Allium 정의, Circle 업체 실적 지표. 프로토콜/업체 발표와 독립 반복고객·환불차감 순매출 구별. |
| S23 | arXiv2304.11771v2,Nov6 2024,5,172명·15%, 도입시차 분석. QJE2025 최종판과 구판 수치 혼합 금지. |
| S25/S42 | METR 초기 실험/후속 같은 연구 계열. 초기16명246과업·조정시간+19%, 후속 선택·보상·병렬작업 측정 한계. 최신 도구 전체의 평균 추정 아님. |
| S43 | Feb2025 저자 PDF,2022–24 세 회사 실험4,867명,26.08% 사용 IV. 2026 최종판 본문 미대조. |
| S34/T02 | Blanchard2019의 이론·제약과 가상 부채·차환 민감도. i,g 명목, 기초수지와 차환 구별. |
| S31/S46/T08 | Circle2026Q2·MicrosoftFY2026 공개 재무표에서 기존에 계산한 숫자. SEC 호스팅은 승인·독립 검증 아님. Microsoft 전사 CFO−현금PPE는 비현금 리스 추가를 포함한 전체 투자수익률이 아님. |
| H18/T04 | BTC 요인별 인과 기여 보류·비현금흐름 자산 구분. 본문에는 이전 수익률 표를 다시 넣지 않았고 새 금융수익 전망도 없음. |

원문의 S27 연준 AI buildout, Bitcoin FAQ 및 기타 일부 링크는 기존 검토/검색 출발점으로 남겼지만 개정 본문의 실증 근거를 채우기 위해 불필요하게 재인용하지 않았다. 모든 seed를 새로 완독했다고 주장하지 않는다.

## 5. 실행한 최소 분석과 발견

실행 명령(저장소 루트, Python 표준 라이브러리만 필요):

```powershell
python research/macro-digital-money-ai/20260921/thesis-development/analysis/run_analysis.py
```

입력: [analysis/inputs.json](analysis/inputs.json). 코드: [run_analysis.py](analysis/run_analysis.py). 결과: [RESULTS.json](analysis/results/RESULTS.json) 및 A01–A06 CSV. **15개 계산 검사 통과는 수학·단위·예시 구현 확인이며 인과 식별·논문의 진실·독립 검토 인증이 아니다.**

| 분석 | 실제 계산 / 단위 / 결과 의미 |
|---|---|
| A01 | 2업무군·9개 가상 방식. KRW/품질충족 완료건수, 실패 비용 포함,90%완료율 제약 별도. 규칙 자동화·AI 실패·검토 비용의 대안 결과를 모두 남김. |
| A02 | 고정비30,000KRW·변동1,000KRW/시도·완료확률0.9·편익4,000KRW/완료. 기대 순편익 양수 시작12시도. 분모의 기대 완료 건수는 관측치 아님. |
| A03 | 흐름KRW/일×외부 선지급 비중×경제적 재사용 일수. 평균 잠김+buffer5조건. 별도 A/B의90+90지급 원장: 총180,순0,정해진 총액 순서 최초현금90. 이연 상계의 신용 노출은 비용0으로 처리하지 않음. |
| A04 | fT/C+rC/2의 내부해·주변 비용 비교. T=연1억원,r=연5%, f=100/10,000원. 평균미사용현금 약316,227.77/3,162,277.66원. 선지급 처리중 잔액과 별개. 실제 금리·지출 보정 없음. |
| A05 | F=100USD,n=90일,360일 관행,1/4/5/10bp 할인율 감소. 가격 상승0.0025/0.0100/0.0125/0.0250USD. 가격 수준 차분으로 단위 교차 확인. 투자수익률 기준 정확한 가격 민감도와 완전 동일하다고 주장하지 않음. |
| A06 | 가상 완료량100→300,가격·변동비·고정비3조건의 이익200/50/950. 가치 포착 방향이 계약·경쟁에 따라 다름을 보이는 산술. 금액 단위는 일관된 임의 단위. |

### BIS 주석 오류와 기존 결과 전파 점검

첨부 외부 검토 F01은 현재 검토한 **보존된 June2026 판본**에서 확인됐다. 주38의 달러 표기와 센트 설명이 서로 맞지 않고 할인채 근사와100배 차이가 난다. 화면 확인 파일은 로컬 `evidence/raw/inspection/bis1270_june2026_p36.png`다. 외부 검토의 예비 주장을 실제 원문에서 대조한 것이며 회귀 원자료를 검증한 것은 아니다.

기존 연구의 텍스트·코드·가공 CSV/JSON 41개 파일에서 이 달러 환산의 다섯 표현을 검색했고 일치0건이었다. 결과와 검색 패턴·범위는 `analysis/results/ARTIFACT_CHECKS.json`에 기록했다. 원문 PDF/추출문에는 당연히 주석이 있으므로 산출물 전파와 구별했다. 기존 계산·보고서에서 전파를 찾지 못하여 옛 파일은 고치지 않고 이번 교정만 보존했다. 제한된 패턴 검색이 모든 가능한 의미 변형의 부재를 증명하지는 않는다.

### 데이터 보존과 재현 수준

신규 원자료 PDF/HTML·추출문·화면은 로컬 `evidence/raw/`에 보존하고 Git에서는 제외했다. Git에는 URL·해시·열람 원장과 자체 작성한 입력·코드·가공 결과가 있다. **A01–A06은 새 clone에서 네트워크 없이 재현 가능하다.** 문헌 화면 재검토는 로컬 원자료 또는 동일 해시의 합법적 공개본이 필요하다. 로컬 실패한 N01/N07는 웹 도구로 해당 범위를 읽었지만 고정 원자료 보존·같은 빈티지 재현은 보장하지 못한다. 새 다운로드는 기존 스냅샷과 달라질 수 있다.

## 6. 삭제·유지·추가의 실질적 차이

- **유지:** AI가 실행비용을 낮춰 일부 활동의 경계를 넓힐 수 있다는 중심 생각. 다만 비교 단위를 완료 업무로 구체화했다.
- **조건부 수정:** 달러 중심 설명, 검증이 새 병목이라는 표현, 초기 보급 순서, 지급 추상화, 잔액 근사와 금융 전달. 각 부분에 대안 경로·관측·반증을 붙였다.
- **중심 주장에서는 삭제/축소:** 달러가 일반 메커니즘의 필수 조건인 듯한 제목, 생성비 하락에서 검증사업자의 이익으로 뛰는 연결, BTC를 본론과 동일 비중으로 다루는 구성. 고정비·수요·기존 자동화 비교가 없는 단순 사례는 더 명확한 모형으로 대체했다.
- **추가:** Coase/Williamson의 내부·외부 조정 양방향, 다중 과업 측정 문제, BCG의 빠르지만 부정확한 과업 반례, 지급 유동성의 신용/상계 반론, 생산성 보완투자, 경쟁과 권리별 귀속, BIS 주석 단위 교정.
- **보류 유지:** H10(순증수요 규모), H18(BTC 프리미엄 요인 기여), H23(독립 반복고객·순매출). H25는 이질성 설명을 강화했으며 기존 MIXED를 전면 지지로 승격하지 않았다.

## 7. 종료 판단

최종 원본·manifest·Git blob·링크·매핑·가공 결과 검사는9/9 통과했다. 작성 중 N13의 저자 표기를 공식 페이지와 대조해 Bech·Shimizu·Wong으로 바로잡았다. 검사 보고서의 자기 링크가 최초 생성 전에 없어 실패했던 항목은 보고서 생성 후 재검사해 해소했다. 문헌의 진실을 기계 검사로 인증했다는 의미는 아니다.

주요 연결마다 지지 근거·강한 반론·적용 조건을 본문에 통합했다. 추가 문헌 숫자를 채우기 위한 확장은 중단한다. 더 높은 가치는 이미 실행한 회계·가상 산술의 반복이 아니라 **실제 완료 업무 비용과 반복 유료 이용을 함께 기록한 패널**, 그 지급에서 토큰 잔액·자금 원천으로 이어지는 연결 자료에 있다. 단일 연구자가 작성·점검했으며 독립 검토를 수행했다는 주장은 하지 않는다.
