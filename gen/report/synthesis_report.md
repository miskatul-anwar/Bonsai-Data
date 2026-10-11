# Universal Knowledge Base Synthesis Report

- **Generated on**: 2026-10-11 16:12:24 UTC
- **Total Raw Turtle Files Processed**: 95
- **Total Deduplicated Triples**: 119,373
- **Universal TBox Triples**: 272
- **Universal ABox Triples**: 119,101
- **Reconciliation**: `count(TBox) + count(ABox) == 119,373` (100% triple preservation, 0% loss)

## Universal TBox Summary

- **Ontologies (1)**:
  - `http://ontology.bonsai.uno/core`
- **Classes (12)**:
  - `http://exiobase/source/Activity`
  - `http://exiobase/source/Flowobject`
  - `http://exiobase/source/Inputflow`
  - `http://exiobase/source/Outputflow`
  - `http://ontology.bonsai.uno/core#Activity`
  - `http://ontology.bonsai.uno/core#ActivityType`
  - `http://ontology.bonsai.uno/core#Agent`
  - `http://ontology.bonsai.uno/core#BalanceableProperty`
  - `http://ontology.bonsai.uno/core#BalanceablePropertyType`
  - `http://ontology.bonsai.uno/core#Flow`
  - `http://ontology.bonsai.uno/core#FlowObject`
  - `http://ontology.bonsai.uno/core#ReferenceUnit`
- **Object Properties (22)**:
  - `http://ontology.bonsai.uno/core#activityType`
  - `http://ontology.bonsai.uno/core#determiningFlow`
  - `http://ontology.bonsai.uno/core#hasActivityType`
  - `http://ontology.bonsai.uno/core#hasBalanceableProperty`
  - `http://ontology.bonsai.uno/core#hasDeterminingFlow`
  - `http://ontology.bonsai.uno/core#hasLocation`
  - `http://ontology.bonsai.uno/core#hasObjectType`
  - `http://ontology.bonsai.uno/core#hasPropertyType`
  - `http://ontology.bonsai.uno/core#hasReferenceFlowObject`
  - `http://ontology.bonsai.uno/core#hasTemporalExtent`
  - `http://ontology.bonsai.uno/core#inputOf`
  - `http://ontology.bonsai.uno/core#isInputOf`
  - `http://ontology.bonsai.uno/core#isOutputOf`
  - `http://ontology.bonsai.uno/core#isProportionalTo`
  - `http://ontology.bonsai.uno/core#location`
  - `http://ontology.bonsai.uno/core#objectType`
  - `http://ontology.bonsai.uno/core#outputOf`
  - `http://ontology.bonsai.uno/core#performs`
  - `http://ontology.bonsai.uno/core#proportionalTo`
  - `http://ontology.bonsai.uno/core#referenceFlowObject`
  - `http://ontology.bonsai.uno/core#temporalExtent`
  - `http://www.ontology-of-units-of-measure.org/resource/om-2/hasUnit`
- **Datatype Properties (13)**:
  - `http://exiobase/source/Code`
  - `http://exiobase/source/Name`
  - `http://exiobase/source/activityId`
  - `http://exiobase/source/hasActivityType`
  - `http://exiobase/source/hasLocation`
  - `http://exiobase/source/hasNumericalValue`
  - `http://exiobase/source/hasObjectType`
  - `http://exiobase/source/hasTemporalExtent`
  - `http://exiobase/source/hasUnit`
  - `http://exiobase/source/isInputOf`
  - `http://exiobase/source/isOutputOf`
  - `http://www.ontology-of-units-of-measure.org/resource/om-2/hasNumericalValue`
  - `http://www.w3.org/2000/01/rdf-schema#label`

## Canonical Prefix Registry

| Prefix | Namespace URI |
| :--- | :--- |
| `bont:` | `http://ontology.bonsai.uno/core#` |
| `bont_agent:` | `http://bonsai.uno/foaf/bonsai.rdf#` |
| `bont_base:` | `http://ontology.bonsai.uno/` |
| `bont_core:` | `http://ontology.bonsai.uno/core/` |
| `brdf_foaf:` | `http://rdf.bonsai.uno/foaf#` |
| `brdf_foaf_bonsai:` | `http://rdf.bonsai.uno/foaf/bonsai#` |
| `brdf_foaf_ystafdb:` | `http://rdf.bonsai.uno/foaf/ystafdb#` |
| `brdf_prov:` | `http://rdf.bonsai.uno/prov#` |
| `brdf_prov_ystafdb:` | `http://rdf.bonsai.uno/prov/ystafdb#` |
| `brdf_time:` | `http://rdf.bonsai.uno/time#` |
| `brdf_unit:` | `http://rdf.bonsai.uno/unit#` |
| `brdfat_core:` | `http://rdf.bonsai.uno/activitytype/core/electricity_grid#` |
| `brdfat_entsoe:` | `http://rdf.bonsai.uno/activitytype/entsoe#` |
| `brdfat_exio:` | `http://rdf.bonsai.uno/activitytype/exiobase3_3_17#` |
| `brdfat_lcia:` | `http://rdf.bonsai.uno/activitytype/lcia/climate_change#` |
| `brdfat_ystafdb:` | `http://rdf.bonsai.uno/activitytype/ystafdb#` |
| `brdfdata_hsup:` | `http://rdf.bonsai.uno/data/exiobase3_3_17/hsup#` |
| `brdfdata_huse:` | `http://rdf.bonsai.uno/data/exiobase3_3_17/huse/` |
| `brdfdata_ystafdb:` | `http://rdf.bonsai.uno/data/ystafdb/huse/` |
| `brdffo_core:` | `http://rdf.bonsai.uno/flowobject/core/electricity_grid#` |
| `brdffo_epa:` | `http://rdf.bonsai.uno/flowobject/us_epa_elem#` |
| `brdffo_exio:` | `http://rdf.bonsai.uno/flowobject/exiobase3_3_17#` |
| `brdffo_lcia:` | `http://rdf.bonsai.uno/flowobject/lcia/climate_change#` |
| `brdffo_us_epa:` | `http://rdf.bonsai.uno/flowobject/us_epa/` |
| `brdffo_ystafdb:` | `http://rdf.bonsai.uno/flowobject/ystafdb#` |
| `brdfloc_exio:` | `http://rdf.bonsai.uno/location/exiobase3_3_17#` |
| `brdfloc_ystafdb:` | `http://rdf.bonsai.uno/location/ystafdb#` |
| `cc:` | `http://creativecommons.org/ns#` |
| `chemspider:` | `http://www.chemspider.com/` |
| `dc:` | `http://purl.org/dc/elements/1.1/` |
| `dcmitype:` | `http://purl.org/dc/dcmitype/` |
| `dcterms:` | `http://purl.org/dc/terms/` |
| `exio:` | `http://exiobase/source/` |
| `foaf:` | `http://xmlns.com/foaf/0.1/` |
| `map:` | `http://www.map.org/example#` |
| `om2:` | `http://www.ontology-of-units-of-measure.org/resource/om-2/` |
| `onto:` | `http://www.onto.org/schema#` |
| `org:` | `https://www.w3.org/TR/vocab-org/` |
| `owl:` | `http://www.w3.org/2002/07/owl#` |
| `prov:` | `http://www.w3.org/ns/prov#` |
| `qb4o:` | `http://purl.org/qb4olap/cubes#` |
| `rdf:` | `http://www.w3.org/1999/02/22-rdf-syntax-ns#` |
| `rdfs:` | `http://www.w3.org/2000/01/rdf-schema#` |
| `schema:` | `http://schema.org/` |
| `skos:` | `http://www.w3.org/2004/02/skos/core#` |
| `time:` | `http://www.w3.org/2006/time#` |
| `vann:` | `http://purl.org/vocab/vann/` |
| `w3c_org:` | `http://www.w3.org/ns/org#` |
| `wikidata:` | `https://www.wikidata.org/wiki/` |
| `xsd:` | `http://www.w3.org/2001/XMLSchema#` |

## Output File Locations

- **Universal TBox (Turtle)**: `gen/tbox/universal_tbox.ttl`
- **Universal TBox (N-Triples)**: `gen/tbox/universal_tbox.nt`
- **Universal ABox (Turtle)**: `gen/abox/universal_abox.ttl`
- **Universal ABox (N-Triples)**: `gen/abox/universal_abox.nt`
