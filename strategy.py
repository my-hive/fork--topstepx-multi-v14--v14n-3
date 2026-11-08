"""v14n-3: Russell afternoon risk premium, fixed causal close stop."""
import numpy as np

PARAMS = {'entry': 43200, 'flat': 54000, 'stop_points': 6., 'contracts': 1}


def entry_risk(panel):
    return {s: np.full(len(d), PARAMS['stop_points'] * 50 if s == 'RTY' else 0.)
            for s, d in panel.items()}


def signals(panel):
    result = {}
    for symbol, df in panel.items():
        out = np.zeros(len(df), dtype=np.int64)
        result[symbol] = out
        if symbol != 'RTY':
            continue
        c, sec = (df[k].to_numpy() for k in ('close', 'ct_sec'))
        for ix in df.groupby('session', sort=False).indices.values():
            side, used, stop = 0, False, 0.
            for i in ix:
                if side and (sec[i] >= PARAMS['flat'] or c[i] <= stop):
                    side = 0
                if not used and sec[i] == PARAMS['entry']:
                    side = 1
                    stop = c[i] - PARAMS['stop_points']
                    used = True
                out[i] = side * PARAMS['contracts']
    return result
