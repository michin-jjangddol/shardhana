# Add side-by-side comparison: localization vs smoothing

We already have a working 1D HEM GUI with matplotlib visualization.

Now I want to extend it to compare two update rules in the same window.

Goal:
Show how different rules produce different behavior under identical conditions.

Requirements:

1. Keep the existing GUI layout and input fields (N, dt, k, steps).

2. Use the same initial condition for both simulations:

   * all zeros
   * center element has a small perturbation (0.1)

3. Implement two simulation modes:

   (A) Localization mode:
   diff = state[i] - neighbor_avg

   (B) Smoothing mode:
   diff = neighbor_avg - state[i]

4. Run both simulations with identical parameters.

5. Display results in the same window:

   * Two plots side by side (left/right)
   * Left: Localization
   * Right: Smoothing

6. For each plot:

   * show Step 0, middle step, and final step
   * x-axis = element index
   * y-axis = state value

7. Keep the code simple and readable.

8. Do not introduce unnecessary complexity.

9. Reuse as much of the existing code as possible.

Goal:
Visually demonstrate that changing only the rule changes the entire behavior
(localization vs diffusion-like smoothing).
