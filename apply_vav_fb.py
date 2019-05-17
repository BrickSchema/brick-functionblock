import rdflib

g = rdflib.Graph()
g.parse('schemas/brick_fb.ttl', format='turtle')
g.parse('graphs/vav_example_without_fb.ttl', format='turtle')

q_prefix = """
prefix brick: <https://brickschema.org/schema/1.0.3/Brick#>
prefix bf: <https://brickschema.org/schema/1.0.3/BrickFrame#>
prefix dcterms: <http://purl.org/dc/terms/>
prefix owl: <http://www.w3.org/2002/07/owl#>
prefix rdf: <http://www.w3.org/1999/02/22-rdf-syntax-ns#>
prefix rdfs: <http://www.w3.org/2000/01/rdf-schema#>
prefix skos: <http://www.w3.org/2004/02/skos/core#>
prefix xml: <http://www.w3.org/XML/1998/namespace>
prefix xsd: <http://www.w3.org/2001/XMLSchema#>
prefix fb: <https://brickschema.org/schema/1.0.3/BrickFunctionalBlock#>
prefix basicfb: <https://brickschema.org/schema/1.0.3/BrickFunctionalBlock#Basic#>
prefix vavfb: <https://brickschema.org/schema/1.0.3/BrickFunctionalBlock#Basic#vav>
prefix : <http://example.com/testbed#>
"""

fb_init_query = q_prefix + """
INSERT {
    ?equip fb:hasFunction ?fb.
    ?fb a ?fb_type.
} WHERE {
    ?fb_type fb:mayBeAssociatedWith ?equip_tagset.
    ?equip a ?equip_tagset.
    FILTER NOT EXISTS {
        ?equip fb:hasFunction ?fb.
        ?fb a ?fb_type.
    }
    BIND ( UUID() AS ?fb) .
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

g.update(fb_init_query)
g.update(port_init_query)
g.serialize('graphs/vav_example_generated_fb.ttl', format='turtle')
