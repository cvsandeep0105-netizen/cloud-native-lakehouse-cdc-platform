from dataclasses import dataclass
from typing import Dict

@dataclass(frozen=True)
class DQEvidence:
    rule_id: str
    dataset: str
    layer: str
    check_status: str
    observed_value: str
    expected_value: str
    discrepancy_type: str
    lineage_context: str

@dataclass(frozen=True)
class AIInsight:
    finding: str
    evidence_reference: str
    affected_dataset: str
    affected_layer: str
    lineage_impact: str
    suggested_investigation: str
    confidence_statement: str
    human_review_required: bool

class AIInsightEngine:
    def analyze(self, evidence: DQEvidence) -> AIInsight:
        if evidence.check_status == 'PASS':
            finding = 'No deterministic data-quality failure was identified in the supplied evidence.'
            investigation = 'No corrective action required; retain the deterministic validation result.'
        else:
            finding = 'A deterministic data-quality discrepancy requires engineering investigation.'
            investigation = 'Inspect the authoritative source, transformation boundary, and downstream lineage before taking corrective action.'

        return AIInsight(
            finding=finding,
            evidence_reference=evidence.rule_id,
            affected_dataset=evidence.dataset,
            affected_layer=evidence.layer,
            lineage_impact=evidence.lineage_context,
            suggested_investigation=investigation,
            confidence_statement='Advisory interpretation based only on supplied deterministic evidence; not an independent validation.',
            human_review_required=True
        )

def insight_to_dict(insight: AIInsight) -> Dict:
    return {
        'finding': insight.finding,
        'evidence_reference': insight.evidence_reference,
        'affected_dataset': insight.affected_dataset,
        'affected_layer': insight.affected_layer,
        'lineage_impact': insight.lineage_impact,
        'suggested_investigation': insight.suggested_investigation,
        'confidence_statement': insight.confidence_statement,
        'human_review_required': insight.human_review_required
    }
