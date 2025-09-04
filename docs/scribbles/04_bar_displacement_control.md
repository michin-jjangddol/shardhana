# Example 4 — Displacement Control (P vs Delta) for a 1D Bar

This example increases displacement at a constant rate and observes the load P.
The bar is: L = 2.0 m, A = 0.0001 m^2 (10x10 mm^2), E = 200 GPa.
The conceptual response has four phases: elastic -> hardening -> softening -> failure.

Note on units:
A = 0.0001 m^2, so at sigma_u = 450 MPa the peak load is
Pu = sigma_u * A = 450e6 * 1e-4 = 45,000 N = 45 kN.

---

## Inputs (concept model)

- E = 200 GPa
- A = 0.0001 m^2 (10x10 mm^2)
- L = 2.0 m
- sigma_y = 250 MPa
- sigma_u = 450 MPa
- displacement rate = 1.0 mm/s (displacement control)

---

## Results summary (numbers you can quote)

| Point                  | Delta [mm] | Time [s] (rate 1 mm/s) | sigma [MPa] | P [kN]  |
|-----------------------|-----------:|------------------------:|------------:|-------:|
| Yield start (Delta_y) | 2.50       | 2.50                    | ~250        | ~25    |
| Peak (Delta_u)        | 6.00       | 6.00                    | ~450        | ~45    |
| Failure (Delta_f)     | 12.00      | 12.00                   | -> 0        | -> 0   |

- P-Delta curve: straight in elastic, then rises slowly in hardening,
  reaches a peak around 45 kN, then decreases in softening until failure.
- Displacement control keeps the solution stable even after the peak.

---

## Diagram

Schematic (SVG):