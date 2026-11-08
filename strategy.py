"""v14n-3: completed morning range breakout; one attempt per session."""
import numpy as np

PARAMS = dict(range_start=30600, range_end=36000, entry_end=43200,
              flat=50400, stop_points=75., contracts=2)


def entry_risk(panel):
    # Exchange point value is a contract specification, not a fitted choice.
    return {s: np.full(len(d), PARAMS['stop_points'] * 2 if s == 'MNQ' else 0.)
            for s, d in panel.items()}


def signals(panel):
    result = {}
    for symbol, df in panel.items():
        out = np.zeros(len(df), dtype=np.int64)
        result[symbol] = out
        if symbol != 'MNQ':
            continue
        c, h, l, sec = (df[k].to_numpy() for k in ('close', 'high', 'low', 'ct_sec'))
        for ix in df.groupby('session', sort=False).indices.values():
            hi, lo, side, used, stop = -np.inf, np.inf, 0, False, 0.
            for i in ix:
                t = sec[i]
                if PARAMS['range_start'] <= t < PARAMS['range_end']:
                    hi, lo = max(hi, h[i]), min(lo, l[i])
                if side and (t >= PARAMS['flat'] or side * (c[i] - stop) <= 0):
                    side = 0
                if (not used and PARAMS['range_end'] <= t < PARAMS['entry_end']
                        and np.isfinite(hi) and (c[i] > hi or c[i] < lo)):
                    side = 1 if c[i] > hi else -1
                    stop = c[i] - side * PARAMS['stop_points']
                    used = True
                out[i] = side * PARAMS['contracts']
    return result


if __name__ == '__main__':
    import pandas as pd
    d = pd.DataFrame(dict(session=['s'] * 5, ct_sec=[30600, 35940, 36000, 36060, 50400],
                          close=[100., 100., 102., 20., 20.],
                          high=[101., 101., 103., 21., 21.], low=[99., 99., 101., 19., 19.]))
    assert signals({'MNQ': d})['MNQ'].tolist() == [0, 0, 2, 0, 0]
    assert np.array_equal(signals({'MNQ': d.iloc[:3]})['MNQ'], signals({'MNQ': d})['MNQ'][:3])
