import pdb

import rdflib
from rdflib import Graph

from common import q_prefix

print('\n')



g = Graph()
g.parse('schemas/brick_fb.ttl', format='turtle')
g.parse('schemas/brick_fb.ttl', format='turtle')
g.parse('schemas/standard_fbs.ttl', format='turtle')
g.parse('example_graphs/vav_with_fb.ttl', format='turtle')

def print_all_res(g, qstr):
    print('------------------------------------')
    qstr = q_prefix + qstr
    res = g.query(qstr)
    for row in res:
        print(row)
    print('\n')


# Query input/output template from a FunctionalBlock class.
# Outputs can be retreived in a similar way.
print('Get all input/output templates of the basic VAV FB, `basicfb:VAV_FB`.')
qstr = """
select ?input ?point_type where {
basicfb:VAV_FB rdfs:subClassOf ?restriction.
?restriction a owl:Restriction.
?restriction owl:onProperty fb:hasInput.
?restriction owl:allValuesFrom ?input.

?input rdfs:subClassOf ?input_restriction.
?input_restriction owl:onProperty rdf:type.
?input_restriction owl:allValuesFrom ?point_type.
}
"""

print_all_res(g, qstr)

print('Get all FB instances.')
qstr = """
select ?fb where {
?fb a/rdfs:subClassOf* fb:FunctionalBlock.
}
"""
print_all_res(g, qstr)

# Query actual input output of a functional block
print('Get actual inputs/outputs of `vav_fb1``')
qstr = """
select ?port ?port_type where {
{:vav_fb1 fb:hasInput ?port.}
UNION
{:vav_fb1 fb:hasOutput ?port.}
?port a ?port_class.
?port_class rdfs:subClassOf ?port_type.
?port_type rdfs:subClassOf fb:Port.
}
"""
print_all_res(g, qstr)

print('Get actual inputs/outputs of `vav_fb1``')
qstr = """
select ?port ?port_type where {
{:vav_fb1 fb:hasInput ?port.}
UNION
{:vav_fb1 fb:hasOutput ?port.}
?port a ?port_class.
?port_class rdfs:subClassOf ?port_type.
?port_type rdfs:subClassOf fb:Port.
}
"""
print_all_res(g, qstr)

print("Return inputs to change this room's temperature.")
qstr = """
select ?input ?fb where {
?znt bf:hasLocation :room1.
?fb fb:hasOutput ?znt.
?fb fb:hasInput ?input.
}
"""
print_all_res(g, qstr)
