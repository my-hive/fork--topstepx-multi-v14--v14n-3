"""v14n-3: afternoon Nasdaq risk premium."""
import numpy as np

PARAMS = {'entry': 43200, 'flat': 54000,
          'stop_points': 50., 'contracts': 3}


def entry_risk(panel):
    return {s: np.full(len(d), PARAMS['stop_points'] * 2 if s == 'MNQ' else 0.)
            for s, d in panel.items()}


def signals(panel):
    result = {}
    for symbol, df in panel.items():
        out = np.zeros(len(df), dtype=np.int64)
        result[symbol] = out
        if symbol != 'MNQ':
            continue
        c, o, sec = (df[k].to_numpy() for k in ('close', 'open', 'ct_sec'))
        for ix in df.groupby('session', sort=False).indices.values():
            side, used, stop = 0, False, 0.
            for i in ix:
                t = sec[i]
                if side and (t >= PARAMS['flat'] or c[i] <= stop):
                    side = 0
                if not used and t == PARAMS['entry'] :
                    side = 1
                    stop = c[i] - PARAMS['stop_points']
                    used = True
                out[i] = side * PARAMS['contracts']
    return result


