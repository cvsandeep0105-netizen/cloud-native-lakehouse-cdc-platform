from .engine import evaluate_all

results = evaluate_all()
failed = [r for r in results if r['status'] != 'PASS']
print('RULE COUNT:', len(results))
print('PASSED:', len(results) - len(failed))
print('FAILED:', len(failed))

if failed:
    print('DQ FRAMEWORK: FAIL')
    raise SystemExit(1)

print('DQ FRAMEWORK: PASS')
