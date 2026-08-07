# ECAT/ICAT Mathematical Notation

This notation describes the bounded repository model. It does not assign universal psychological or relational truth.

Let an experiential standing profile be

`E = (id, c, x, k, r, b, v, l, q)`

where `id` is the entity identifier, `c` declared context, `x` declared experience, `k` coherence status, `r` recoverability status, `b` boundary relevance, `v` validity window, `l` limitations, and `q` receipt/evidence reference.

Let an interaction standing profile be

`I = (P, c, d, s, t, r, b, v, l, q)`

where `P` is the declared entity set, `c` interaction context, `d` declared relationship context, `s` shared-understanding status, `t` trust relevance, and the remaining terms have the analogous bounded meanings above.

Define structural profile validity as predicates:

`V_E(E) in {0,1}`

`V_I(I) in {0,1}`

computed only from declared repository schema requirements and validation rules.

For the RC1 fixture set `F`, deterministic validation yields

`R(F) = (n, n_valid, n_invalid)`

with the committed expected condition currently

`R(F) = (4, 2, 2)`.

A downstream carriage relation is written

`E or I -> B -> G`

where `B` is later boundary analysis and `G` later governance analysis. The arrow denotes dependency/carriage only:

`authority(E) = authority(I) = 0`

within this repository.

Reconstruction is separated from present standing:

`reconstructable(q) != authority_now(q)`.

Likewise, an observed or replayed valid historical profile does not imply a current admissibility decision.

These expressions are formal bookkeeping for the repository contract, not clinical measures, calibrated probabilities, or universal existence scores.
