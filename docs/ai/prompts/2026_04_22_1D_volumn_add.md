Please update the current 1D prototype code for the Shardhana project.

Important rules:
1. Treat the CURRENT code as the main base.
2. Treat the older 1D code only as a reference.
3. Do not rewrite the whole structure from the old version.
4. Do not create duplicated logic or parallel temporary classes if avoidable.
5. Keep the code simple, readable, and easy to extend later toward 2D/3D.

Goal:
Extend the current 1D seed model so that each seed has geometric properties,
especially volume and contact-face information, and make those values interact with neighboring seeds.

Concept direction:
- We are not trying to implement full natural behavior yet.
- For now, use simple default geometric assumptions.
- The purpose is to connect:
  state change -> geometry update -> contact-face update
- Breaking/failure behavior can remain simple or be prepared for the next step.

What I want to add now:
1. Each seed should have geometric variables.
   Minimum suggestion:
   - length
   - area
   - volume

2. Each seed should also be able to represent contact faces with neighbors.
   In 1D, this is simple:
   - left face
   - right face
   - each face can have a contact area value

3. Volume does not need to be a fully independent physical variable yet.
   For now, it can be based on default geometry such as:
   - volume = length * area
   This is enough for the current stage.

4. State change should affect geometry in a simple way.
   For example:
   - when state changes, seed length may change
   - when length changes, volume updates
   - when damage or state gap increases, contact-face area may reduce

5. Neighbor interaction should be linked through contact faces.
   I want the code structure to make it clear that:
   - seeds interact through faces
   - face/contact values can be updated from neighboring state differences

6. Keep the implementation minimal.
   I do NOT want:
   - overcomplicated physics
   - too many new abstractions
   - full 3D logic
   - large refactoring unless truly necessary

Preferred design direction:
- default seed shape concept = cuboid-like
- default contact-face concept = rectangular face
- even in 1D, keep naming/design expandable toward future 2D/3D development

Please do the following:
1. Review the current code structure first
2. Reuse as much of the current structure as possible
3. Add only the minimum necessary classes/fields/methods
4. Show the updated code
5. Briefly explain what changed
6. If needed, suggest one small next step for:
   geometry -> contact -> break progression

Current code is the main base:
[PASTE CURRENT CODE HERE]

Older 1D code is only reference:
[PASTE OLD 1D REFERENCE CODE HERE]