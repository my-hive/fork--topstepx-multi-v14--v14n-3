"""v14n-3: natural gas producer hedging pressure in US day."""
import numpy as np

PARAMS = {'reference': 30600, 'entry': 36000, 'flat': 54000,
          'stop_points': .03, 'contracts': 1}


def entry_risk(panel):
    return {s: np.full(len(d), PARAMS['stop_points'] * 10000 if s == 'NG' else 0.)
            for s, d in panel.items()}


def signals(panel):
    result = {}
    for symbol, df in panel.items():
        out = np.zeros(len(df), dtype=np.int64)
        result[symbol] = out
        if symbol != 'NG':
            continue
        c, o, sec = (df[k].to_numpy() for k in ('close', 'open', 'ct_sec'))
        for ix in df.groupby('session', sort=False).indices.values():
            reference, side, used, stop = np.nan, 0, False, 0.
            for i in ix:
                t = sec[i]
                if t == PARAMS['reference']:
                    reference = o[i]
                if side and (t >= PARAMS['flat'] or c[i] >= stop):
                    side = 0
                if not used and t == PARAMS['entry'] :
                    side = -1
                    stop = c[i] + PARAMS['stop_points']
                    used = True
                out[i] = side * PARAMS['contracts']
    return result


