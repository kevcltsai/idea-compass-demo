# Idea Compass — Product Definition & Evaluation v1.0
Date: 2026-11-12

## Fixed WHY
Help people move beyond familiar knowledge and cognitive boundaries by discovering, understanding, and recombining cross-domain knowledge into creative possibilities they would not otherwise consider.

## WHAT (revisable)
An open-ended, evidence-aware knowledge exploration environment that begins with a problem, discovers potentially transferable relations or structures across domains, and enables users to develop and challenge novel combinations.

**Semantic bridges are a candidate technique, not a required product object.** The product must not presume a fixed number, taxonomy, or granularity of intermediary points. No fixed 12-node ceiling, and no requirement to display all discovered points at once.

### Non-negotiable demo constraints
- Exactly three evaluation problems: (1) useful long-term AI memory, (2) reducing extreme polarization on social media, (3) making cities less flood-prone during extreme rain.
- Every numerical score, ranking, embedding, and displayed computed relation must be computed from real inputs with a named method/model and reproducible provenance. Never invent scores, vectors, evidence, experiments, or sources.
- Existing 36 authored mechanism descriptions are seed *hypotheses*, not verified literature evidence, and not the limit of the knowledge universe.
- Clearly distinguish retrieved factual claims, model-inferred analogies, user hypotheses, and validated interventions.

## Candidate WHATs evaluated conceptually
1. Semantic abstraction: extract goals/functions/relations and retrieve analogous knowledge. Strong explainability; risks tautological restatement.
2. Semantic-distance exploration: search beyond nearest-neighbor knowledge. Strong breadth; distance alone is not creative utility.
3. Structural analogy: identify comparable causal or functional relationships in otherwise distant domains. Strongest hypothesized transfer; structural mapping needs scrutiny.
4. Complementary combination: discover mechanisms with complementary strengths and failure conditions. Potentially actionable; premature solution bias.
5. Open relation traversal: discover additional relations from retrieved knowledge without a fixed bridge list. High breadth; drift and evidence quality risks.

**Current preferred WHAT hypothesis:** combine structural analogy, relation traversal, and complementarity. This is a product hypothesis, not a measured winner. Semantic embeddings are a retrieval signal, not an efficacy or creativity score.

## Evaluation design — no invented results
For each of the three fixed problems, compare the same knowledge corpus and retrieval budget:
- Baseline 1: nearest-neighbor semantic retrieval.
- Baseline 2: broad/distant semantic retrieval.
- Candidate: explainable structural/relational retrieval followed by complementarity analysis.
Collect each retrieved source's title, URL/identifier, retrieval timestamp, source excerpt or verified structured claim, and method. Record the intermediary relation and why it is hypothesized to transfer.
Blind-review outputs on: (a) novelty relative to obvious domain solutions, (b) intelligible transfer rationale, (c) falsifiability and practical applicability, (d) traceable evidence, (e) diversity without redundancy. Use human ratings or explicit rubrics; do not represent embedding scores as these outcomes.
Reject a method if it produces plausible-sounding but unsupported cross-domain claims or fails to outperform simple retrieval on the same evaluation protocol.

## Phase gates
**Phase 1 WHY↔WHAT:** iterate candidate product capabilities and evaluation rubrics until the intended benefit is specific and testable. Do not mistake conceptual comparison for empirical validation.
**Phase 2 WHAT↔HOW:** only then iterate architecture, algorithm, UI and interaction using real data. UI presentation limits must never become ontology limits.
**Phase 3 WHY→WHAT→HOW:** evaluate end-to-end user value and return to either prior phase when needed.

## Observed implementation gaps (as inspected)
- The current static data source has 3 problems and 12 manually authored mechanisms each. The descriptions are hypotheses and contain no verified primary-source references.
- Embedding similarity represents textual proximity, not causal transfer, novelty, or verified solution quality.
- A radial map's arbitrary angle and relative min-max radius can imply unsupported geometric relationships; changing visible nodes can change displayed positions.
- Existing composition primarily exports an instruction prompt rather than demonstrating validated combinations.
- Cross-topic reuse of the 36 seed mechanisms, where implemented, is not open-world discovery.

## Release criteria
Do not label a release as evidence-grounded open-world discovery unless sources are actually retrieved and traceable. Do not claim browser visual QA without opening the deployed site. Keep separate labels for implementation complete, automated checks passed, deployed, and user-observed behavior.

## Iteration summary
- WHY retained unchanged.
- WHAT moved from a fixed semantic-bridge pipeline to open-ended cross-domain relation discovery, with structural transfer and complementarity as candidate capabilities.
- Bridge count and type are not capped; knowledge breadth is constrained only by actual accessible evidence and computational resources, not UI or arbitrary ontology constants.
- Established a falsifiable comparison against simpler retrieval baselines; empirical outcome remains **not yet measured**.
