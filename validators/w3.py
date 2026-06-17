import json
from pathlib import Path
from w3_data import FIXTURES

REPORT = Path('reports/w3.json')
FLAGS = ['declared','mapped','scoped']

def classify(r):
    if not isinstance(r.get('ready'), bool):
        return 'BLOCKED'
    if any(not isinstance(r.get(f), bool) for f in FLAGS):
        return 'BLOCKED'
    ok = all(r[f] for f in FLAGS)
    if ok and r.get('status') == 'READY' and r.get('ready'):
        return 'READY'
    if (not ok) and r.get('status') == 'INCOMPLETE' and not r.get('ready'):
        return 'INCOMPLETE'
    return 'BLOCKED'

def main():
    rows = []
    unexpected = 0
    for it in FIXTURES:
        actual = classify(it['record'])
        ok = actual == it['expected']
        rows.append({'id': it['id'], 'expected': it['expected'], 'actual': actual, 'ok': ok})
        if not ok:
            unexpected += 1
    report = {'stage':'w3','unexpected':unexpected,'saturated':unexpected == 0,'rows':rows}
    REPORT.parent.mkdir(exist_ok=True)
    REPORT.write_text(json.dumps(report, indent=2, sort_keys=True) + '\n')
    print(json.dumps(report, indent=2, sort_keys=True))
    return 0 if report['saturated'] else 1

if __name__ == '__main__':
    raise SystemExit(main())
