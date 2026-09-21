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
