import pdb

import rdflib
from rdflib import Graph

from common import q_prefix

print('\n')



g = Graph()
g.parse('brick_fb.ttl', format='turtle')
g.parse('vav_example.ttl', format='turtle')

def print_all_res(g, qstr):
    print('------------------------------------')
    qstr = q_prefix + qstr
    res = g.query(qstr)
    for row in res:
        print(row)
    print('\n')


# Query input/output template from a FunctionalBlock class.
# Outputs can be retreived in a similar way.
print('Get all input/output templates of the basic VAV FB, `basicfb:vav`.')
qstr = """
select ?input ?point_type where {
vavfb: rdfs:subClassOf ?restriction.
#basicfb:vav rdfs:subClassOf ?restriction.
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
print('Get actual inputs/outputs of `vavfb1``')
qstr = """
select ?port ?port_type where {
{:vavfb1 fb:hasInput ?port.}
UNION
{:vavfb1 fb:hasOutput ?port.}
?port a ?port_class.
?port_class rdfs:subClassOf ?port_type.
?port_type rdfs:subClassOf fb:Port.
}
"""
print_all_res(g, qstr)

print('Get actual inputs/outputs of `vavfb1``')
qstr = """
select ?port ?port_type where {
{:vavfb1 fb:hasInput ?port.}
UNION
{:vavfb1 fb:hasOutput ?port.}
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