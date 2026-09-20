"""Offline reproduction. Python 3.12 + pandas/numpy. No network, wallets or paid calls.
All invented inputs carry SYNTHETIC; market calculations are DESCRIPTIVE_NOT_CAUSAL.
"""
from pathlib import Path
import json, hashlib, datetime, itertools, math
import pandas as pd
import numpy as np
ROOT=Path(__file__).resolve().parents[1]; RAW=ROOT/'data/raw'; OUT=ROOT/'data/derived'
OUT.mkdir(exist_ok=True,parents=True)
results={}; checks=[]
def save(name,rows):
    df=rows if isinstance(rows,pd.DataFrame) else pd.DataFrame(rows)
    df.to_csv(OUT/(name+'.csv'),index=False,encoding='utf-8-sig')
    return df
def check(name,condition):
    checks.append({'check':name,'passed':bool(condition)})
    if not condition: raise AssertionError(name)
def fred(s):
    df=pd.read_csv(RAW/f'fred_{s}.csv',parse_dates=[0],na_values=['.'])
    v=pd.to_numeric(df.iloc[:,1],errors='coerce'); v.index=df.iloc[:,0]
    v=v.sort_index(); check(s+'_no_duplicate_dates',not v.index.duplicated().any())
    return v
data={s:fred(s) for s in ['CBBTCUSD','SP500','NASDAQCOM','CPIAUCSL','DEXKOUS','DTWEXBGS','DGS3MO','DGS10','DFF','KORCPIALLMINMEI']}
save('data_inventory',[{'series':s,'first_valid':v.first_valid_index(),'last_valid':v.last_valid_index(),'nonmissing':int(v.notna().sum()),'missing':int(v.isna().sum()),'sha256':hashlib.sha256((RAW/f'fred_{s}.csv').read_bytes()).hexdigest()} for s,v in data.items()])

# T01. Every participant balances separately. Consolidated domestic banking system.
ledger=[]
def case(name,rows):
    for entity,account,side,delta in rows: ledger.append({'case':name,'entity':entity,'account':account,'side':side,'delta_usd':delta,'kind':'SYNTHETIC_ACCOUNTING_EXAMPLE'})
case('deposit_to_token_cash_reserve',[('User','deposit','asset',-100),('User','token','asset',100),('Issuer','deposit','asset',100),('Issuer','token','liability',100),('Banks','user_deposit','liability',-100),('Banks','issuer_deposit','liability',100)])
case('issuer_buys_existing_bill_from_nonbank',[('Issuer','deposit','asset',-100),('Issuer','bill','asset',100),('Seller','bill','asset',-100),('Seller','deposit','asset',100),('Banks','issuer_deposit','liability',-100),('Banks','seller_deposit','liability',100)])
case('MMF_to_token_end_state',[('User','MMF_share','asset',-100),('User','token','asset',100),('MMF','bill','asset',-100),('MMF','shares','liability',-100),('Issuer','bill','asset',100),('Issuer','token','liability',100)])
case('direct_bill_to_token_end_state',[('User','bill','asset',-100),('User','token','asset',100),('Issuer','bill','asset',100),('Issuer','token','liability',100)])
case('foreign_user_FX_to_token',[('Foreign_user','local_asset_USD_equivalent','asset',-100),('Foreign_user','token','asset',100),('FX_dealer','local_asset_USD_equivalent','asset',100),('FX_dealer','USD_deposit','asset',-100),('Issuer','USD_deposit','asset',100),('Issuer','token','liability',100),('Banks','dealer_deposit','liability',-100),('Banks','issuer_deposit','liability',100)])
case('cash_redemption',[('User','deposit','asset',100),('User','token','asset',-100),('Issuer','deposit','asset',-100),('Issuer','token','liability',-100),('Banks','user_deposit','liability',100),('Banks','issuer_deposit','liability',-100)])
case('treasury_buyback_existing_TGA',[('Treasury','TGA','asset',-100),('Treasury','debt','liability',-100),('Fed','TGA','liability',-100),('Fed','reserves','liability',100),('Banks','reserves','asset',100),('Banks','seller_deposit','liability',100),('Seller','bill','asset',-100),('Seller','deposit','asset',100)])
case('treasury_new_issue_before_buyback',[('Treasury','TGA','asset',100),('Treasury','debt','liability',100),('Fed','TGA','liability',100),('Fed','reserves','liability',-100),('Banks','reserves','asset',-100),('Banks','buyer_deposit','liability',-100),('Buyer','bill','asset',100),('Buyer','deposit','asset',-100)])
case('Fed_QE_from_nonbank',[('Fed','bill','asset',100),('Fed','reserves','liability',100),('Banks','reserves','asset',100),('Banks','seller_deposit','liability',100),('Seller','bill','asset',-100),('Seller','deposit','asset',100)])
l=save('T01_ledger',ledger);l['balance_delta']=np.where(l.side=='asset',l.delta_usd,-l.delta_usd)
check('T01_each_entity_balances',l.groupby(['case','entity']).balance_delta.sum().eq(0).all())
results['T01']={'status':'EXECUTED_SYNTHETIC','cases':l['case'].nunique(),'qualification':'Consolidated banks; internal reserves redistribute; foreign FX source not identified; no valuation/profit.'}

# T02. Ratios of current nominal GDP; d>0 is primary deficit; SFA explicitly zero.
rows=[]
for i,g,d in itertools.product([.025,.04,.055],[.025,.04,.055],[0,.02,.04]):
    b=1.0
    for year in range(1,11):
        b=(1+i)/(1+g)*b+d
        rows.append(dict(i=i,g=g,d=d,sfa=0,b0=1,year=year,b=b,kind='SYNTHETIC_SENSITIVITY_NOT_FORECAST'))
save('T02_debt_grid',rows)
roll=[]
for refi in [.1,.25,1.0]:
    b=1.;i=.04
    for year in range(1,11):
        i=(1-refi)*i+refi*.03; b=(1+i)/1.04*b+.02
        roll.append(dict(refinancing_fraction=refi,year=year,average_rate=i,debt_ratio=b,sfa=0))
save('T02_refinancing',roll)
check('T02_equal_rate_growth_identity',abs([r for r in rows if r['i']==.04 and r['g']==.04 and r['d']==.02][-1]['b']-1.2)<1e-12)
results['T02']={'status':'EXECUTED_SYNTHETIC','scenarios':27,'base_i4_g4_d2_b10':1.2,'low_i25_g55_d2_b10':[r['b'] for r in rows if r['i']==.025 and r['g']==.055 and r['d']==.02 and r['year']==10][0],'high_i55_g25_d2_b10':[r['b'] for r in rows if r['i']==.055 and r['g']==.025 and r['d']==.02 and r['year']==10][0]}

# T03. Manual transcription verified against rendered original pages; mutually exclusive assets.
reserves=[('Circle','fund_Treasury_securities',8524064231),('Circle','fund_overnight_Treasury_repo',52527000000),('Circle','fund_cash',1003971544),('Circle','fund_settlement_net',-137687880),('Circle','bank_cash',11382256398),('Circle','other_settlement_net',45304883),('Tether','US_Treasury_bills',114960963604),('Tether','overnight_reverse_repo',18625552412),('Tether','term_reverse_repo',6993428950),('Tether','non_US_Treasury_bills',22374689),('Tether','cash_bank_deposits',40307440),('Tether','corporate_bonds',8711171),('Tether','gold',18838357171),('Tether','bitcoin',5801630681),('Tether','public_equities',3761438892),('Tether','other_investments',5244911675),('Tether','secured_loans',13453749726)]
rv=save('T03_reserves',[dict(issuer=i,category=c,usd=v,as_of='2026-06-30',source_id='S29' if i=='Circle' else 'S30') for i,c,v in reserves])
check('T03_Circle_sum',rv[rv.issuer=='Circle'].usd.sum()==73344909176)
check('T03_Tether_sum',rv[rv.issuer=='Tether'].usd.sum()==187751426411)
net=[]
for stock,rho,sub in itertools.product([100e9],[.5,.9],[0,.5,1]):
    net.append(dict(token_growth_usd=stock,Treasury_allocation=rho,prior_Treasury_exposure_share=sub,net_under_assumptions=stock*(rho-sub),kind='SYNTHETIC_COUNTERFACTUAL_NOT_ESTIMATE'))
save('T03_net_demand_scenarios',net)
# Algebraic check of the reported GIV construction is NOT an econometric replication.
s=np.array([.6,.3,.1]);growth=np.array([.03,.01,-.02]);weighted=s@growth;eps=growth-weighted
giv=(s-1/3)@eps
check('T03_GIV_algebra',abs(giv-(weighted-growth.mean()))<1e-12)
results['T03']={'status':'EXECUTED_RESERVE_RECONCILIATION_AND_SENSITIVITY','Circle_assets':73344909176,'Circle_tokens':73268560097,'Circle_securities_share':8524064231/73344909176,'Circle_repo_share':52527000000/73344909176,'Tether_assets':187751426411,'Tether_US_bills_share':114960963604/187751426411,'Tether_excess_assets':4109529196,'GIV_replication':'NOT_EXECUTED; identifying panel/control data not reconstructed','GIV_algebra_identity':float(giv)}

# T04. Last nonmissing monthly observation, no filling missing prices/CPI.
monthly=pd.concat({s:v.resample('ME').last() for s,v in data.items()},axis=1)
monthly=monthly.loc[:'2026-08-31'] # September incomplete, not used as a full month.
monthly['BTC_KRW']=monthly.CBBTCUSD*monthly.DEXKOUS
monthly['BTC_real_USD']=monthly.CBBTCUSD/monthly.CPIAUCSL
monthly['BTC_real_KRW']=monthly.BTC_KRW/monthly.KORCPIALLMINMEI
ret=monthly.pct_change(fill_method=None)
ret['cash_quote_proxy']=monthly.DGS3MO.shift(1)/1200
save('T04_monthly_values',monthly.reset_index());save('T04_monthly_returns',ret.reset_index())
def endpoint_return(column,start,end):
    first=pd.Timestamp(start)-pd.offsets.MonthEnd(1); last=pd.Timestamp(end)+pd.offsets.MonthEnd(0)
    if first not in monthly.index or last not in monthly.index:return None
    a,b=monthly.loc[first,column],monthly.loc[last,column]
    return float(b/a-1) if pd.notna(a) and pd.notna(b) else None
def cash_return(q):
    return float((1+q.cash_quote_proxy).prod()-1) if q.cash_quote_proxy.notna().all() else None
windows=[('2017_2019','2017-01-01','2019-12-31'),('2020_2022','2020-01-01','2022-12-31'),('2023_2025','2023-01-01','2025-12-31'),('2017_2025','2017-01-01','2025-12-31'),('2026_YTD_Aug','2026-01-01','2026-08-31')]
stats=[]
for name,start,end in windows:
    q=ret.loc[start:end,['CBBTCUSD','SP500','NASDAQCOM','CPIAUCSL','DTWEXBGS','BTC_KRW','BTC_real_USD','BTC_real_KRW','cash_quote_proxy']]
    pair=q[['CBBTCUSD','SP500']].dropna();down=pair[pair.SP500<0]
    daily=data['CBBTCUSD'].loc[start:end].dropna();mdd=(daily/daily.cummax()-1).min()
    stats.append(dict(window=name,start=start,end=end,n_pair=len(pair),n_btc_cpi=len(q[['CBBTCUSD','CPIAUCSL']].dropna()),btc_sp500_corr=pair.corr().iloc[0,1],btc_monthly_CPI_change_corr=q[['CBBTCUSD','CPIAUCSL']].corr().iloc[0,1],btc_daily_mdd_within_window=mdd,sp_down_months=len(down),btc_mean_when_sp_down=down.CBBTCUSD.mean(),btc_positive_share_when_sp_down=(down.CBBTCUSD>0).mean(),btc_nominal_usd=endpoint_return('CBBTCUSD',start,end),btc_real_usd=endpoint_return('BTC_real_USD',start,end),btc_nominal_krw=endpoint_return('BTC_KRW',start,end),btc_real_krw=endpoint_return('BTC_real_KRW',start,end),sp500_price_return=endpoint_return('SP500',start,end),cash_quote_proxy=cash_return(q)))
save('T04_window_statistics',stats)
annual=[]
for year in range(2017,2027):
    q=ret.loc[str(year)] if str(year) in ret.index.strftime('%Y') else pd.DataFrame()
    if q.empty: continue
    start=f'{year}-01-01';end=str(q.index[-1].date())
    annual.append(dict(year=year,n_months=len(q),BTC_USD=endpoint_return('CBBTCUSD',start,end),BTC_real_USD=endpoint_return('BTC_real_USD',start,end),BTC_KRW=endpoint_return('BTC_KRW',start,end),BTC_real_KRW=endpoint_return('BTC_real_KRW',start,end),SP500_price=endpoint_return('SP500',start,end),CPI=endpoint_return('CPIAUCSL',start,end),USD_broad=endpoint_return('DTWEXBGS',start,end),cash_quote_proxy=cash_return(q)))
save('T04_annual',annual)
check('T04_missing_Korean_CPI_not_zero',next(x for x in annual if x['year']==2024)['BTC_real_KRW'] is None)
a25=next(x for x in annual if x['year']==2025)
check('T04_real_return_endpoint_identity',abs((1+a25['BTC_USD'])/(1+a25['CPI'])-1-a25['BTC_real_USD'])<1e-12)
horizons=[]
for h in [12,36,60]:
    q=monthly['BTC_real_USD'].pct_change(h,fill_method=None).loc['2017-01-01':'2025-12-31'].dropna()
    horizons.append(dict(months=h,n_overlapping_windows=len(q),loss_share=(q<0).mean(),min_return=q.min(),median_return=q.median(),max_return=q.max()))
save('T04_holding_horizons',horizons)
results['T04']={'status':'EXECUTED_DESCRIPTIVE_NOT_CAUSAL','windows':stats,'annual_2022':next(x for x in annual if x['year']==2022),'holding_horizons':horizons,'limits':['SP500 price excludes dividends','cash is accrued previous-month annualized quote/12, not investable total return','month-end FX and BTC closing times differ','realized CPI change is not inflation surprise','revised vintage; not a real-time forecast','gold comparison unavailable','overlapping holdings are not independent samples']}

# T05. Synthetic identical service: 1,000 API requests x $0.01; no actual payment.
cost=[]
for name,fixed,rate,batches,gas,ramp,funds,days,fail,review in [
('card_per_request',.30,.029,1000,0,0,0,0,0,0),
('card_monthly_batch',.30,.029,1,0,0,0,0,0,0),
('bank_token_batch_assumed',.10,0,1,0,0,10,1,.01,.02),
('stablecoin_prefunded',0,0,1000,.001,0,10,30,.01,.02),
('stablecoin_new_on_off_ramp',0,0,1000,.001,1,10,30,.01,.02)]:
    fees=fixed*batches+rate*10+gas*batches+ramp+funds*.05*days/365+fail+review
    cost.append(dict(rail=name,payment_value=10,requests=1000,fee_fixed=fixed,fee_rate=rate,settlement_batches=batches,network_fee_each=gas,on_off_ramp_total=ramp,prefunding_cost=funds*.05*days/365,expected_failure_cost=fail,human_review_cost=review,total_incremental_cost=fees,kind='SYNTHETIC_ASSUMPTIONS_NOT_PRICE_QUOTE'))
save('T05_cost',cost)
budget=10.;paid=set()
def authorize(req):
    global budget
    if req['nonce'] in paid:return 'DUPLICATE'
    if req['merchant']!='weather' or req['currency']!='USD' or req['expired'] or req['price']>budget:return 'DENY'
    budget-=req['price'];paid.add(req['nonce']);return 'AUTHORIZED_MOCK_ONLY'
q={'nonce':'n1','merchant':'weather','currency':'USD','expired':False,'price':.01}
check('T05_mock_valid',authorize(q)=='AUTHORIZED_MOCK_ONLY')
check('T05_mock_replay',authorize(q)=='DUPLICATE')
check('T05_mock_budget',authorize({**q,'nonce':'n2','price':11})=='DENY')
check('T05_mock_expiry',authorize({**q,'nonce':'n3','expired':True})=='DENY')
check('T05_mock_merchant',authorize({**q,'nonce':'n4','merchant':'other'})=='DENY')
results['T05']={'status':'EXECUTED_SYNTHETIC_COST_AND_OFFLINE_AUTHORIZATION_MODEL','implementation_ceiling':'Not AP2/x402 conformance, no signature verification, no chain settlement, no refund guarantee','cost':cost}

# T06. Keep distinct estimands. Normal interval illustrative only, no meta-analytic mean.
save('T06_literature_comparison',[
dict(study='Brynjolfsson_Li_Raymond_v2_2024_QJE2025',n=5172,design='staggered_rollout_not_RCT',estimand='issues_resolved_per_hour',effect=.15,source_id='S23',limitation='one_customer_support_context'),
dict(study='METR_early2025',n=16,design='task_randomized_246_tasks',estimand='task_completion_time',effect=.19,source_id='S25',limitation='experienced_OSS_early2025_tools'),
dict(study='Cui_et_al_Feb2025',n=4867,design='three_randomized_field_experiments',estimand='completed_tasks_tool_users_IV',effect=.2608,source_id='S43',limitation='noisy_heterogeneous_trials_tool_compliance'),
dict(study='METR_late2025_original_subsample',n=10,design='randomized_tasks_selected_participation',estimand='task_completion_time',effect=-.18,source_id='S42',limitation='selection_and_concurrency_measurement'),
dict(study='METR_late2025_new_subsample',n=47,design='randomized_tasks_selected_participation',estimand='task_completion_time',effect=-.04,source_id='S42',limitation='selection_and_concurrency_measurement')])
results['T06']={'status':'EXECUTED_STRUCTURED_COMPARISON_NOT_MICRODATA_REPLICATION','Cui_normal_95pct_interval':[.2608-1.96*.103,.2608+1.96*.103],'METR_time_plus19_equivalent_throughput_if_fixed_quality':1/1.19-1,'prohibited_interpretation':'No average across different populations/estimands; no aggregate GDP estimate.'}

# T07. Cost compression e, pass-through theta, constant-elasticity demand; energy/compute k.
sens=[]
for e,theta,eta,k in itertools.product([.5],[.5,1.0],[.5,1.0,1.5,2.0],[1,.8]):
    price=1-theta*(1-e);q=price**(-eta);compute=q*e;energy=compute*k;revenue=q*price
    sens.append(dict(compute_per_task=e,price_pass_through=theta,elasticity=eta,energy_per_compute=k,price_ratio=price,task_ratio=q,total_compute_ratio=compute,total_energy_ratio=energy,revenue_ratio=revenue,kind='SYNTHETIC_SENSITIVITY'))
save('T07_rebound',sens)
balances=[]
for payments,velocity,saving in itertools.product([1e9,2e9],[12,24,120],[0,500e6]):
    balances.append(dict(annual_payment_USD=payments,annual_turnover=velocity,saving_collateral_buffer=saving,payment_balance=payments/velocity,total_balance=payments/velocity+saving,kind='SYNTHETIC_SENSITIVITY'))
save('T07_balances',balances)
results['T07']={'status':'EXECUTED_SYNTHETIC','compute_rebound_threshold_full_pass_through':'eta>1 at e<1, unchanged quality; energy threshold depends on k','payment_balance_base':1e9/12,'payment_double_turnover_double':2e9/24}

# T08. Circle Q2 financial statement transcription; 8-K exhibit, unaudited quarterly.
circle={'reserve_income':667733000,'other_revenue':33582000,'distribution_transaction_other_costs':412470000}
circle['revenue_reserve_total']=circle['reserve_income']+circle['other_revenue']
circle['after_distribution_before_opex']=circle['revenue_reserve_total']-circle['distribution_transaction_other_costs']
circle['reserve_fraction']=circle['reserve_income']/circle['revenue_reserve_total']
circle['operating_expenses']=254486000
circle['operating_income']=circle['after_distribution_before_opex']-circle['operating_expenses']
circle['other_income']=17947000
circle['income_tax']=4092000
circle['net_income_continuing']=circle['operating_income']+circle['other_income']-circle['income_tax']
check('T08_Circle_operating_and_net_bridge',circle['operating_income']==34359000 and circle['net_income_continuing']==48214000)
save('T08_circle',[dict(metric=k,value=v,source_id='S31',period='2026Q2') for k,v in circle.items()])
margin=[]
for balance,yield_,dist in itertools.product([100e9,125e9],[.04,.03],[.5,.7]):
    income=balance*yield_;after=income*(1-dist)
    margin.append(dict(average_reserve=balance,yield_rate=yield_,distribution_share=dist,gross_reserve_income=income,after_distribution_before_opex=after,kind='SYNTHETIC_ANNUAL_NOT_FORECAST'))
save('T08_margin_sensitivity',margin)
msft=[dict(fiscal_year=y,net_income=ni,operating_cash_flow=cfo,cash_PPE_additions=capex,CFO_less_cash_PPE=cfo-capex,depreciation_amortization_and_other=da,source_id='S46',unit='USD_millions',scope='whole_company_not_AI_segment') for y,ni,cfo,capex,da in [(2025,101832,136162,64551,29433),(2026,133749,182935,115948,38534)]]
save('T08_msft',msft)
check('T08_MSFT_FCF_proxy',msft[0]['CFO_less_cash_PPE']==71611 and msft[1]['CFO_less_cash_PPE']==66987)
results['T08']={'status':'EXECUTED_ISSUER_COMPANY_ARITHMETIC_AND_SCENARIOS','circle':circle,'MSFT':msft,'MSFT_CFO_less_cash_PPE_growth':66987/71611-1,'balance_up25_yield4_to3_income_change':1.25*.03/.04-1}

# Record results and real execution environment. Re-run emits same analytic CSVs.
(OUT/'RESULTS.json').write_text(json.dumps(results,ensure_ascii=False,indent=2,allow_nan=False),encoding='utf-8')
(OUT/'CHECKS.json').write_text(json.dumps({'executed_at':datetime.datetime.now(datetime.timezone.utc).isoformat(),'pandas':pd.__version__,'numpy':np.__version__,'checks':checks},ensure_ascii=False,indent=2),encoding='utf-8')
print(json.dumps({'executed_tests':list(results),'checks_passed':len(checks),'T02':results['T02'],'T04_2022':results['T04']['annual_2022'],'T03':results['T03'],'T08':results['T08']},ensure_ascii=False,indent=2))
