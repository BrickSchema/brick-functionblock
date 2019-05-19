import rdflib

from common import q_prefix

g = rdflib.Graph()
g.parse('schemas/brick_fb.ttl', format='turtle')
g.parse('schemas/standard_fbs.ttl', format='turtle')
g.parse('example_graphs/vav_without_fb.ttl', format='turtle')

fb_init_query = q_prefix + """
INSERT {
    ?equip fb:hasFunction ?fb.
    ?fb a ?fb_type.
} WHERE {
    ?equip a ?equip_tagset.
    ?equip_tagset fb:mayHaveFunction ?fb_type.
    FILTER NOT EXISTS {
        ?equip fb:hasFunction ?fb.
        ?fb a ?fb_type.
    }
    BIND ( UUID() AS ?fb) . # assign a UUID so that it can be dereferenced easily in the future.
}
"""

port_init_query = q_prefix + """
INSERT {
    ?point a ?port_type.
} WHERE {
    ?equip fb:hasFunction ?fb.
    ?fb a ?fb_type.
    ?fb_type rdfs:subClassOf ?restriction.
    ?restriction a owl:Restriction.
    {?restriction owl:onProperty fb:hasInput.
     ?restriction owl:allValuesFrom ?port_type.
    }
    UNION
    {?restriction owl:onProperty fb:hasOutput.
     ?restriction owl:allValuesFrom ?port_type.
    }
    ?port_type rdfs:subClassOf ?port_restriction.
    ?port_restriction owl:onProperty rdf:type.
    ?port_restriction owl:allValuesFrom ?point_type.

    ?equip bf:hasPoint ?point.
    ?point a ?point_type.

}
"""

port_init_query = q_prefix + """
INSERT {
    ?point a ?port_type.
    ?fb ?port_rel ?point.
} WHERE {
    ?equip fb:hasFunction ?fb.
    ?fb a ?fb_type.
    ?fb_type rdfs:subClassOf ?restriction.
    ?restriction a owl:Restriction.
    ?port_rel rdfs:subPropertyOf* fb:hasPort.
    ?restriction owl:onProperty ?port_rel.
    ?restriction owl:allValuesFrom ?port_type.
    ?port_type rdfs:subClassOf ?port_restriction.
    ?port_restriction owl:onProperty rdf:type.
    ?port_restriction owl:allValuesFrom ?point_type.

    ?equip bf:hasPoint ?point.
    ?point a ?point_type.

}
"""

g.update(fb_init_query)
g.update(port_init_query)
g.serialize('example_graphs/vav_generated_fb.ttl', format='turtle')
