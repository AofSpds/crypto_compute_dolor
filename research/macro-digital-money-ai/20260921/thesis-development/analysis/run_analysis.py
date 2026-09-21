"""Offline synthetic mechanisms and a bill-price unit check. Standard library only."""
from pathlib import Path
import csv, json, math, hashlib
ROOT=Path(__file__).resolve().parent
data=json.loads((ROOT/'inputs.json').read_text(encoding='utf-8'))
out=ROOT/'results'; out.mkdir(exist_ok=True)
checks=[]
def check(name, condition):
    checks.append({'name':name,'passed':bool(condition)})
    assert condition, name
def save(name, rows):
    with (out/name).open('w',encoding='utf-8',newline='') as f:
        w=csv.DictWriter(f,fieldnames=list(rows[0]));w.writeheader();w.writerows(rows)

cost=[]
for values in data['cost_cases']:
    r=dict(zip(data['cost_columns'],values)); total=sum(values[4:])
    r.update(total_KRW=total,KRW_per_accepted=total/r['accepted'],completion_fraction=r['accepted']/r['attempted'],meets_floor=r['accepted']/r['attempted']>=data['minimum_completion_fraction'])
    cost.append(r)
save('A01_completed_work_cost.csv',cost)
check('open_agent_can_cost_more_than_human_per_accepted',cost[7]['KRW_per_accepted']>cost[4]['KRW_per_accepted'])
check('deterministic_wins_structured_example',cost[1]['KRW_per_accepted']==min(r['KRW_per_accepted'] for r in cost[:4]))
check('cheap_but_incomplete_is_ineligible',not cost[5]['meets_floor'])
x=data['entry_example']; entry=[]
for n in x['attempts']:
    accepted=n*x['pass_fraction']; total=x['fixed_KRW']+n*x['variable_KRW_per_attempt']
    entry.append({'attempts':n,'expected_accepted':accepted,'cost_KRW':total,'KRW_per_expected_accepted':total/accepted,'expected_private_net_benefit_KRW':accepted*x['buyer_value_KRW_per_accepted']-total})
save('A02_entry_threshold.csv',entry)
minimum=math.floor(x['fixed_KRW']/(x['pass_fraction']*x['buyer_value_KRW_per_accepted']-x['variable_KRW_per_attempt']))+1
check('positive_private_entry_at_12_not_10',minimum==12 and entry[1]['expected_private_net_benefit_KRW']<0<entry[2]['expected_private_net_benefit_KRW'])
balances=[]
for name,flow,fraction,days,buffer in data['balance_cases']:
    balances.append({'case':name,'gross_flow_KRW_per_day':flow,'prefunded_settlement_share':fraction,'reuse_days':days,'buffer_KRW':buffer,'average_locked_KRW':flow*fraction*days,'locked_plus_buffer_KRW':flow*fraction*days+buffer})
save('A03_balance_conditions.csv',balances)
check('flow_tripling_can_coexist_with_balance_falling',balances[1]['locked_plus_buffer_KRW']==30000000 and balances[0]['locked_plus_buffer_KRW']==100000000)
check('buffer_can_reverse_result',balances[2]['locked_plus_buffer_KRW']>balances[0]['locked_plus_buffer_KRW'])
inv=data['cash_inventory']; inventory=[]
for fee in inv['refill_cost_KRW']:
    withdrawal=math.sqrt(2*fee*inv['annual_flow_KRW']/inv['annual_opportunity_rate'])
    def objective(c): return fee*inv['annual_flow_KRW']/c+inv['annual_opportunity_rate']*c/2
    inventory.append({'refill_cost_KRW':fee,'annual_flow_KRW':inv['annual_flow_KRW'],'rate':inv['annual_opportunity_rate'],'optimal_withdrawal_KRW':withdrawal,'average_idle_cash_KRW':withdrawal/2,'annual_refill_plus_holding_cost_KRW':objective(withdrawal)})
    check(f'inventory_minimum_fee_{fee}',objective(withdrawal)<objective(withdrawal*.9) and objective(withdrawal)<objective(withdrawal*1.1))
save('A04_inventory_model.csv',inventory)
cum={'A':0,'B':0}; trough=dict(cum); gross=0
for hour,sender,receiver,amount in data['intraday_events']:
    cum[sender]-=amount;cum[receiver]+=amount;gross+=amount
    for a in cum:trough[a]=min(trough[a],cum[a])
intraday={'gross_units':gross,'net_end_positions':cum,'initial_cash_needed_in_fixed_gross_order':{a:-v for a,v in trough.items()},'deferred_end_net_cash':sum(max(-v,0) for v in cum.values()),'unsecured_exposure_possible_before_netting':90}
check('gross_net_liquidity_not_equivalent',gross==180 and -min(trough.values())==90 and intraday['deferred_end_net_cash']==0)
b=data['bill_check']; bills=[]
for bp in b['discount_rate_decrease_bp']:
    change=b['face_USD']*bp/10000*b['days']/b['day_count']
    p0=b['face_USD']*(1-b['baseline_discount_rate']*b['days']/b['day_count'])
    p1=b['face_USD']*(1-(b['baseline_discount_rate']-bp/10000)*b['days']/b['day_count'])
    check(f'bill_difference_{bp}bp',math.isclose(p1-p0,change,abs_tol=1e-12))
    bills.append({'decrease_bp':bp,'face_USD':b['face_USD'],'remaining_days':b['days'],'price_increase_USD':change,'price_increase_cents':change*100})
save('A05_bill_price_units.csv',bills)
check('footnote_dollar_conversion_factor_100',math.isclose(1/bills[1]['price_increase_USD'],100))
capture=[]
for values in data['value_capture_cases']:
    r=dict(zip(data['value_capture_columns'],values)); r['operating_profit']=r['completed_units']*(r['price']-r['variable_cost'])-r['fixed_cost'];capture.append(r)
save('A06_value_capture.csv',capture)
check('volume_triples_profit_can_fall',capture[1]['completed_units']==3*capture[0]['completed_units'] and capture[1]['operating_profit']<capture[0]['operating_profit'])
summary={'classification':data['classification'],'input_sha256':hashlib.sha256((ROOT/'inputs.json').read_bytes()).hexdigest(),'minimum_attempts_for_positive_private_entry':minimum,'intraday':intraday,'checks':checks,'passed':sum(x['passed'] for x in checks),'causal_regression_replications':0,'live_payments':0}
(out/'RESULTS.json').write_text(json.dumps(summary,indent=2,ensure_ascii=False)+'\n',encoding='utf-8',newline='\n')
print(json.dumps(summary,ensure_ascii=False))
