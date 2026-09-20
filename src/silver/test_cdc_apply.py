from src.silver.cdc_apply import CDCEvent, SilverCDCState

state = SilverCDCState()

assert state.apply(CDCEvent('E001','INSERT',100,'ORDER-001',{'order_id':'ORDER-001','status':'created'})) == 'INSERT'
assert state.get('ORDER-001')['status'] == 'created'

assert state.apply(CDCEvent('E002','UPDATE',110,'ORDER-001',{'order_id':'ORDER-001','status':'delivered'})) == 'UPDATE'
assert state.get('ORDER-001')['status'] == 'delivered'

assert state.apply(CDCEvent('E003','DELETE',120,'ORDER-001',{})) == 'DELETE'
assert not state.contains('ORDER-001')

assert state.apply(CDCEvent('E003','DELETE',120,'ORDER-001',{})) == 'DUPLICATE_IGNORED'

try:
    state.apply(CDCEvent('E004','UPDATE',115,'ORDER-001',{'order_id':'ORDER-001','status':'late'}))
    raise AssertionError('Expected stale event rejection')
except ValueError:
    pass

assert state.applied_event_count() == 3
assert state.record_count() == 0

print('INSERT: PASS')
print('UPDATE: PASS')
print('DELETE: PASS')
print('DUPLICATE IDEMPOTENCY: PASS')
print('STALE EVENT REJECTION: PASS')
print('FINAL STATE: PASS')
print('AREA 21-H: CDC APPLICATION UNIT VALIDATION PASS')
