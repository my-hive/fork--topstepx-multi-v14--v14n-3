"""v14n-3: buy morning equity weakness after liquidity-driven selling."""
import numpy as np

PARAMS = {'reference': 30600, 'entry': 36000, 'flat': 54000,
          'stop_points': 6., 'contracts': 1}


def entry_risk(panel):
    return {s: np.full(len(d), PARAMS['stop_points'] * 50 if s == 'ES' else 0.)
            for s, d in panel.items()}


def signals(panel):
    result = {}
    for symbol, df in panel.items():
        out = np.zeros(len(df), dtype=np.int64)
        result[symbol] = out
        if symbol != 'ES':
            continue
        c, o, sec = (df[k].to_numpy() for k in ('close', 'open', 'ct_sec'))
        for ix in df.groupby('session', sort=False).indices.values():
            reference, side, used, stop = np.nan, 0, False, 0.
            for i in ix:
                t = sec[i]
                if t == PARAMS['reference']:
                    reference = o[i]
                if side and (t >= PARAMS['flat'] or c[i] <= stop):
                    side = 0
                if not used and t == PARAMS['entry'] and c[i] < reference:
                    side = 1
                    stop = c[i] - PARAMS['stop_points']
                    used = True
                out[i] = side * PARAMS['contracts']
    return result


if __name__ == '__main__':
    import pandas as pd
    p = PARAMS
    d = pd.DataFrame({'session': ['s'] * 4,
                      'ct_sec': [p['reference'], p['entry'], p['entry'] + 60, p['flat']],
                      'open': [100., 99., 98., 101.], 'close': [100., 99., 98., 101.]})
    assert signals({'ES': d})['ES'].tolist() == [0, p['contracts'], p['contracts'], 0]
    assert np.array_equal(signals({'ES': d.iloc[:2]})['ES'], signals({'ES': d})['ES'][:2])
