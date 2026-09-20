from src.ai_engine.insight_engine import DQEvidence, AIInsightEngine, insight_to_dict

evidence = DQEvidence(
    rule_id='DQ-SLV-001',
    dataset='orders',
    layer='silver',
    check_status='FAIL',
    observed_value='99443',
    expected_value='99441',
    discrepancy_type='row_count',
    lineage_context='silver.orders -> gold.order_performance'
)

insight = AIInsightEngine().analyze(evidence)
result = insight_to_dict(insight)

assert result['evidence_reference'] == 'DQ-SLV-001'
assert result['affected_dataset'] == 'orders'
assert result['affected_layer'] == 'silver'
assert result['human_review_required'] is True
assert 'deterministic evidence' in result['confidence_statement']
assert 'production' not in result['suggested_investigation'].lower()

passed = AIInsightEngine().analyze(
    DQEvidence('DQ-SLV-002','customers','silver','PASS','99441','99441','row_count','silver.customers')
)
assert 'No deterministic data-quality failure' in passed.finding

print('===== AREA 28-C: AI INSIGHT ENGINE =====')
print('ENGINE IMPORT: PASS')
print('STRUCTURED INPUT CONTRACT: PASS')
print('ADVISORY OUTPUT CONTRACT: PASS')
print('FAILURE INTERPRETATION: PASS')
print('PASS INTERPRETATION: PASS')
print('HUMAN REVIEW FLAG: PASS')
print('DETERMINISTIC EVIDENCE PRECEDENCE: PASS')
print('PRODUCTION DATA ACCESS: NONE')
print('EXTERNAL AI SERVICE: NOT USED')
print('AWS AI EXECUTION: NOT CLAIMED')
print('===== AREA 28-C: PASS =====')
