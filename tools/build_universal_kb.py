#!/usr/bin/env python3
import os
import glob
import time
from rdflib import Graph, Namespace, URIRef, RDF, RDFS, OWL

BASE_DIR = os.path.abspath(os.path.join(os.path.dirname(__file__), ".."))
RAW_DIR = os.path.join(BASE_DIR, "raw")
GEN_DIR = os.path.join(BASE_DIR, "gen")
TBOX_DIR = os.path.join(GEN_DIR, "tbox")
ABOX_DIR = os.path.join(GEN_DIR, "abox")
REPORT_DIR = os.path.join(GEN_DIR, "report")

CANONICAL_PREFIXES = {
    "rdf": "http://www.w3.org/1999/02/22-rdf-syntax-ns#",
    "rdfs": "http://www.w3.org/2000/01/rdf-schema#",
    "owl": "http://www.w3.org/2002/07/owl#",
    "xsd": "http://www.w3.org/2001/XMLSchema#",
    "skos": "http://www.w3.org/2004/02/skos/core#",
    "foaf": "http://xmlns.com/foaf/0.1/",
    "dc": "http://purl.org/dc/elements/1.1/",
    "dcterms": "http://purl.org/dc/terms/",
    "dcmitype": "http://purl.org/dc/dcmitype/",
    "prov": "http://www.w3.org/ns/prov#",
    "time": "http://www.w3.org/2006/time#",
    "vann": "http://purl.org/vocab/vann/",
    "schema": "http://schema.org/",
    "om2": "http://www.ontology-of-units-of-measure.org/resource/om-2/",
    "qb4o": "http://purl.org/qb4olap/cubes#",
    "org": "https://www.w3.org/TR/vocab-org/",
    "w3c_org": "http://www.w3.org/ns/org#",
    "cc": "http://creativecommons.org/ns#",
    "bont": "http://ontology.bonsai.uno/core#",
    "bont_core": "http://ontology.bonsai.uno/core/",
    "bont_base": "http://ontology.bonsai.uno/",
    "exio": "http://exiobase/source/",
    "onto": "http://www.onto.org/schema#",
    "map": "http://www.map.org/example#",
    "bont_agent": "http://bonsai.uno/foaf/bonsai.rdf#",
    "brdf_foaf": "http://rdf.bonsai.uno/foaf#",
    "brdf_foaf_bonsai": "http://rdf.bonsai.uno/foaf/bonsai#",
    "brdf_foaf_ystafdb": "http://rdf.bonsai.uno/foaf/ystafdb#",
    "brdf_prov": "http://rdf.bonsai.uno/prov#",
    "brdf_prov_ystafdb": "http://rdf.bonsai.uno/prov/ystafdb#",
    "brdf_time": "http://rdf.bonsai.uno/time#",
    "brdf_unit": "http://rdf.bonsai.uno/unit#",
    "brdfat_core": "http://rdf.bonsai.uno/activitytype/core/electricity_grid#",
    "brdfat_entsoe": "http://rdf.bonsai.uno/activitytype/entsoe#",
    "brdfat_exio": "http://rdf.bonsai.uno/activitytype/exiobase3_3_17#",
    "brdfat_lcia": "http://rdf.bonsai.uno/activitytype/lcia/climate_change#",
    "brdfat_ystafdb": "http://rdf.bonsai.uno/activitytype/ystafdb#",
    "brdffo_core": "http://rdf.bonsai.uno/flowobject/core/electricity_grid#",
    "brdffo_exio": "http://rdf.bonsai.uno/flowobject/exiobase3_3_17#",
    "brdffo_lcia": "http://rdf.bonsai.uno/flowobject/lcia/climate_change#",
    "brdffo_epa": "http://rdf.bonsai.uno/flowobject/us_epa_elem#",
    "brdffo_ystafdb": "http://rdf.bonsai.uno/flowobject/ystafdb#",
    "brdffo_us_epa": "http://rdf.bonsai.uno/flowobject/us_epa/",
    "brdfloc_exio": "http://rdf.bonsai.uno/location/exiobase3_3_17#",
    "brdfloc_ystafdb": "http://rdf.bonsai.uno/location/ystafdb#",
    "brdfdata_hsup": "http://rdf.bonsai.uno/data/exiobase3_3_17/hsup#",
    "brdfdata_huse": "http://rdf.bonsai.uno/data/exiobase3_3_17/huse/",
    "brdfdata_ystafdb": "http://rdf.bonsai.uno/data/ystafdb/huse/",
    "wikidata": "https://www.wikidata.org/wiki/",
    "chemspider": "http://www.chemspider.com/",
}

def load_file_triples(file_path):
    g = Graph()
    if file_path.endswith("github_BONSAMURAIS/rdf_separate_lcia/flowobject/us_epa/us_epa.ttl"):
        with open(file_path, "r", encoding="utf-8") as fh:
            lines = fh.readlines()
        fixed = []
        for line in lines:
            if line.startswith("@prefix brdf:"):
                fixed.append("@prefix brdf: <http://rdf.bonsai.uno/flowobject/us_epa/> .\n")
            elif line.startswith("@prefix chemrdf:"):
                fixed.append("@prefix chemrdf: <http://www.chemspider.com/> .\n")
                fixed.append("@prefix dc: <http://purl.org/dc/elements/1.1/> .\n")
                fixed.append("@prefix foaf: <http://xmlns.com/foaf/0.1/> .\n")
                fixed.append("@prefix ns0: <http://purl.org/vocab/vann/> .\n")
                fixed.append("@prefix owl: <http://www.w3.org/2002/07/owl#> .\n")
                fixed.append("@prefix xsd: <http://www.w3.org/2001/XMLSchema#> .\n")
                fixed.append("@prefix cc: <http://creativecommons.org/ns#> .\n")
            elif "rdfs:label:" in line:
                fixed.append(line.replace("rdfs:label:", "rdfs:label"))
            else:
                fixed.append(line)
        g.parse(data="".join(fixed), format="turtle")
    elif file_path.endswith("github_BONSAMURAIS/rdf_separate_lcia/foaf/bonsai.ttl"):
        with open(file_path, "r", encoding="utf-8") as fh:
            lines = fh.readlines()
        fixed = [
            "@prefix skos: <http://www.w3.org/2004/02/skos/core#> .\n",
            "@prefix org: <http://www.w3.org/ns/org#> .\n",
            "@prefix foaf: <http://xmlns.com/foaf/0.1/> .\n",
        ]
        for line in lines[1:]:
            if "foaf:interest <https://www.wikidata.org/wiki/Q131201>" in line:
                fixed.append(line.rstrip() + " ;\n")
            elif "foaf:interest <https://www.wikidata.org/wiki/Q2323664>" in line:
                fixed.append(line.rstrip() + " ;\n")
            elif "foaf:interest <https://www.wikidata.org/wiki/Q18692990>" in line:
                fixed.append(line.rstrip() + " .\n")
            else:
                fixed.append(line)
        g.parse(data="".join(fixed), format="turtle")
    else:
        g.parse(file_path, format="turtle")
    return set(g)

def main():
    start_time = time.time()
    os.makedirs(TBOX_DIR, exist_ok=True)
    os.makedirs(ABOX_DIR, exist_ok=True)
    os.makedirs(REPORT_DIR, exist_ok=True)

    ttl_files = sorted(glob.glob(os.path.join(RAW_DIR, "**/*.ttl"), recursive=True))
    print(f"Discovered {len(ttl_files)} TTL files under {RAW_DIR}")

    all_triples = set()
    file_stats = {}

    for i, fpath in enumerate(ttl_files, 1):
        rel = os.path.relpath(fpath, RAW_DIR)
        try:
            triples = load_file_triples(fpath)
            file_stats[rel] = len(triples)
            all_triples.update(triples)
            if i % 15 == 0 or i == len(ttl_files):
                print(f"[{i}/{len(ttl_files)}] Processed {rel} - Current unique triples: {len(all_triples)}")
        except Exception as e:
            print(f"Error parsing {rel}: {e}")
            raise e

    print(f"\nTotal unique triples across entire dataset: {len(all_triples)}")

    TBOX_TYPES = {
        OWL.Ontology,
        OWL.Class,
        OWL.ObjectProperty,
        OWL.DatatypeProperty,
        OWL.AnnotationProperty,
        OWL.FunctionalProperty,
        OWL.InverseFunctionalProperty,
        OWL.TransitiveProperty,
        OWL.SymmetricProperty,
        RDFS.Datatype,
        RDF.Property,
    }

    TBOX_PREDICATES = {
        RDFS.subClassOf,
        RDFS.subPropertyOf,
        RDFS.domain,
        RDFS.range,
        OWL.equivalentClass,
        OWL.equivalentProperty,
        OWL.disjointWith,
        OWL.unionOf,
        OWL.intersectionOf,
        OWL.complementOf,
        OWL.inverseOf,
        OWL.propertyChainAxiom,
        OWL.hasValue,
        OWL.someValuesFrom,
        OWL.allValuesFrom,
        OWL.onProperty,
    }

    TBOX_ANNOTATION_PREDICATES = {
        RDFS.label,
        RDFS.comment,
        RDFS.isDefinedBy,
        RDFS.seeAlso,
        OWL.versionInfo,
        URIRef("http://purl.org/dc/elements/1.1/title"),
        URIRef("http://purl.org/dc/elements/1.1/description"),
        URIRef("http://purl.org/dc/elements/1.1/creator"),
        URIRef("http://purl.org/dc/elements/1.1/publisher"),
        URIRef("http://purl.org/dc/elements/1.1/contributor"),
        URIRef("http://purl.org/dc/elements/1.1/modified"),
        URIRef("http://purl.org/dc/terms/title"),
        URIRef("http://purl.org/dc/terms/description"),
        URIRef("http://purl.org/dc/terms/creator"),
        URIRef("http://purl.org/dc/terms/contributor"),
        URIRef("http://purl.org/dc/terms/publisher"),
        URIRef("http://purl.org/dc/terms/modified"),
        URIRef("http://creativecommons.org/ns#license"),
        URIRef("http://xmlns.com/foaf/0.1/homepage"),
        URIRef("http://purl.org/vocab/vann/preferredNamespaceUri"),
        URIRef("http://purl.org/vocab/vann/preferredNamespacePrefix"),
        URIRef("http://www.w3.org/2004/02/skos/core#prefLabel"),
        URIRef("http://www.w3.org/2004/02/skos/core#definition"),
    }

    tbox_entities = set()
    for s, p, o in all_triples:
        if p == RDF.type and o in TBOX_TYPES:
            tbox_entities.add(s)

    tbox_triples = set()
    abox_triples = set()

    for s, p, o in all_triples:
        is_tbox = False
        if p == RDF.type and o in TBOX_TYPES:
            is_tbox = True
        elif p in TBOX_PREDICATES:
            is_tbox = True
        elif s in tbox_entities and p in TBOX_ANNOTATION_PREDICATES:
            is_tbox = True

        if is_tbox:
            tbox_triples.add((s, p, o))
        else:
            abox_triples.add((s, p, o))

    print(f"\nTBox triples: {len(tbox_triples)}")
    print(f"ABox triples: {len(abox_triples)}")
    assert len(tbox_triples) + len(abox_triples) == len(all_triples), "Triple conservation mismatch!"
    assert len(tbox_triples.intersection(abox_triples)) == 0, "Overlap between TBox and ABox!"

    print("\nBuilding clean TBox graph with canonical prefixes...")
    tbox_graph = Graph()
    for pfx, uri in CANONICAL_PREFIXES.items():
        tbox_graph.bind(pfx, Namespace(uri), override=True)
    for t in tbox_triples:
        tbox_graph.add(t)

    tbox_ttl_path = os.path.join(TBOX_DIR, "universal_tbox.ttl")
    tbox_nt_path = os.path.join(TBOX_DIR, "universal_tbox.nt")
    print(f"Writing {tbox_ttl_path}...")
    tbox_graph.serialize(destination=tbox_ttl_path, format="turtle")
    print(f"Writing {tbox_nt_path}...")
    tbox_graph.serialize(destination=tbox_nt_path, format="nt")

    print("\nBuilding clean ABox graph with canonical prefixes...")
    abox_graph = Graph()
    for pfx, uri in CANONICAL_PREFIXES.items():
        abox_graph.bind(pfx, Namespace(uri), override=True)
    for t in abox_triples:
        abox_graph.add(t)

    abox_ttl_path = os.path.join(ABOX_DIR, "universal_abox.ttl")
    abox_nt_path = os.path.join(ABOX_DIR, "universal_abox.nt")
    print(f"Writing {abox_ttl_path}...")
    abox_graph.serialize(destination=abox_ttl_path, format="turtle")
    print(f"Writing {abox_nt_path}...")
    abox_graph.serialize(destination=abox_nt_path, format="nt")

    report_path = os.path.join(REPORT_DIR, "synthesis_report.md")
    print(f"Generating report: {report_path}...")

    classes = sorted(set(tbox_graph.subjects(RDF.type, OWL.Class)))
    obj_props = sorted(set(tbox_graph.subjects(RDF.type, OWL.ObjectProperty)))
    dt_props = sorted(set(tbox_graph.subjects(RDF.type, OWL.DatatypeProperty)))
    ontologies = sorted(set(tbox_graph.subjects(RDF.type, OWL.Ontology)))

    with open(report_path, "w", encoding="utf-8") as rf:
        rf.write("# Universal Knowledge Base Synthesis Report\n\n")
        rf.write(f"- **Generated on**: {time.strftime("%Y-%m-%d %H:%M:%S UTC", time.gmtime())}\n")
        rf.write(f"- **Total Raw Turtle Files Processed**: {len(ttl_files)}\n")
        rf.write(f"- **Total Deduplicated Triples**: {len(all_triples):,}\n")
        rf.write(f"- **Universal TBox Triples**: {len(tbox_triples):,}\n")
        rf.write(f"- **Universal ABox Triples**: {len(abox_triples):,}\n")
        rf.write(f"- **Reconciliation**: `count(TBox) + count(ABox) == {len(all_triples):,}` (100% triple preservation, 0% loss)\n\n")

        rf.write("## Universal TBox Summary\n\n")
        rf.write(f"- **Ontologies ({len(ontologies)})**:\n")
        for o in ontologies:
            rf.write(f"  - `{o}`\n")
        rf.write(f"- **Classes ({len(classes)})**:\n")
        for c in classes:
            rf.write(f"  - `{c}`\n")
        rf.write(f"- **Object Properties ({len(obj_props)})**:\n")
        for p in obj_props:
            rf.write(f"  - `{p}`\n")
        rf.write(f"- **Datatype Properties ({len(dt_props)})**:\n")
        for p in dt_props:
            rf.write(f"  - `{p}`\n")

        rf.write("\n## Canonical Prefix Registry\n\n")
        rf.write("| Prefix | Namespace URI |\n")
        rf.write("| :--- | :--- |\n")
        for pfx, uri in sorted(CANONICAL_PREFIXES.items()):
            rf.write(f"| `{pfx}:` | `{uri}` |\n")

        rf.write("\n## Output File Locations\n\n")
        rf.write(f"- **Universal TBox (Turtle)**: `gen/tbox/universal_tbox.ttl`\n")
        rf.write(f"- **Universal TBox (N-Triples)**: `gen/tbox/universal_tbox.nt`\n")
        rf.write(f"- **Universal ABox (Turtle)**: `gen/abox/universal_abox.ttl`\n")
        rf.write(f"- **Universal ABox (N-Triples)**: `gen/abox/universal_abox.nt`\n")

    elapsed = time.time() - start_time
    print(f"\nExecution successfully completed in {elapsed:.2f} seconds.")

if __name__ == "__main__":
    main()
