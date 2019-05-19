Brick FunctionBlocks
====================

Brick FunctionBlocks (FB) abstract a bunch of Points and their complex relationships with input/output interface and its descriptions. This 1) provides a more high-level view of a set of Points and Equipment, 2) explicitly represents what to control for affecting a target, and 3) enables modular composition of components for a higher level view.

# Design Goals
- Input/Output per FB.
- Instantiate existing Point instances as Input and Ouput.
- Each FB class may have functional description as annotations.
- Control dependencies across Points.

# RDF Model
TODO

# Repository Structure
- `schemas/brick_fb.ttl`: It has meta structure for FBs.
- `schemas/standard_fbs.ttl`: It has standard FBs. One may directly instantiate or extend it.
- `graphs/*.ttl`: Example graphs.
- `apply_vav_fb.ttl`: A single Python script to automatically instantiate FBs for possible entities (e.g., if there is a VAV, you can instantiate `vavfb` automatically and associate the VAV's Points with the FB.
- `example_queries.py`: Example queries over FBs.


# Examples
## VAV and Damper
TODO

## Heat Exchanger
TODO

### Possible future extentions
- Map to OpenBuildings/Modelical model to make exact control sequences queriable.


### Notes
- I wanted to implement a namespace itself as a FunctionBlock class, but it is not allowed in SPARQL. E.g., `vavfb: rdfs:subClassOf fb:FunctionBlock` may be defined in Turtle, but not allowed in SPARQL.
