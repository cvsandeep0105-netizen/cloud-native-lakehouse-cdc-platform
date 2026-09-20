from .rules import RULES

def evaluate(rule_id, violations):
    if rule_id not in RULES:
        raise KeyError(rule_id)
    status = 'PASS' if violations == 0 else 'FAIL'
    return {
        'rule_id': rule_id,
        'status': status,
        'violations': violations,
        'severity': RULES[rule_id]['severity'],
        'scope': RULES[rule_id]['scope'],
        'action': RULES[rule_id]['action']
    }

def evaluate_all():
    return [evaluate(rule_id, 0) for rule_id in RULES]
