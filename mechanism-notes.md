# v14n-3 research complete

16 recorded experiments. Best dev_score first reached at experiment 8; experiments 9–16 supplied no improvement. Early-stop rule triggered. No sealed-validation submission: no candidate meets development eligibility.

## Frozen ranking

| Experiment | Source commit | dev_score | fold_score | Positive years | Knobs | Fold rates |
|---|---|---:|---:|---:|---:|---|
| 8 / 10 | 6c6d0812 / abb39863 | 0.20157940338430702 | 0 | .4 | 5 | 0, 0, .07720588235294118, 0 |
| 6 | 4a3c4dc9 | 0.17203736543243522 | .009191176470588236 | .6 | 4 | 0, .01838235294117647, .14705882352941177, .0661764705882353 |
| 5 | 809560de | 0.12836721269918516 | 0 | .6 | 5 | 0, 0, 0, 0 |

Best source SHA256: `980908653b4c2848629f7b190cd7fb70b8d93245097ce8f2a6621adcfaed8e4a`. Restored byte-identically to strategy.py, with no parameter change after null.

## Mechanism and causal calculations

Descriptive research read all 14 supplied allowed roots: ES MES NQ MNQ YM MYM RTY M2K NKD CL MCL QM NG MNG. Morning-direction continuation was weak across most roots. Account simulations used one symbol each to control runtime and correlated exposure.

Morning breakout hypothesis: persistent institutional flow should extend completed 08:30–10:00 range. First break entered after 10:00, fixed close-triggered stop, once per session. Opposite-side exhaustion variant also failed stressed costs. ES recovery after morning weakness and NG daytime producer hedging also failed.

Afternoon hypothesis: equity inventory absorption and benchmark flows produce late-session premium. Frozen best buys three MNQ contracts only at 12:00 CT when completed close exceeds 08:30 open; exits on close at/below fixed 50-point stop or at 15:00. Signal fills next open. Risk per contract declared as 50 points × $2/point = $100; three contracts declare $300 total. Close-triggered stops cannot guarantee $300 realized loss under gaps/slippage. Only three independent entry gates: symbol eligibility, entry time, morning-price direction; once-per-session state prevents re-entry. Exit gates are not entry filters.

Best economics are dominated by 2022: yearly stressed PnL 2019 -1482.75, 2020 -2594.25, 2021 -114.75, 2022 +13265.25, 2023 +2082.75. This is not robust directional evidence. Experiment 10 ran frozen best source with 20 null seeds: provisional p=1.0; all-null tie at zero worst-three pass metric is uninformative for small economic gains but definitively does not satisfy required gate. No 200-seed run warranted. No further adjustment of frozen mechanism after seeing null.

Independent energy settlement-pressure and geographic/breadth premium transfers were tested afterward, not modifications of frozen MNQ parameters. CL/NG short, YM/RTY/NKD afternoon long, MCL pre-settlement long all failed economics. Cross-market failures argue against generic inventory-pressure edge after stressed costs.

## Audit caveats

Experiment 1 used dict(...) syntax for PARAMS, which evaluator did not recognize; logged actual 18-knob fallback result. Later experiments use literal mappings. Test fixture numeric constants are synthetic checks, not trading choices. Instrument multipliers are exchange specifications. Some earlier files carried unused reference parameter: counted and penalized, not hidden.

All evaluator attempts retained in experiments.jsonl including raw economics, folds, gates and null. No hidden sweeps, new data purchases, OOS access, live API or validation requests. Baseline prefix self-check passed; evaluator lookahead checks passed all successful screens. Best source preserved unchanged despite no longer containing standalone synthetic check. Validation quota remains unused because eligibility fails.
