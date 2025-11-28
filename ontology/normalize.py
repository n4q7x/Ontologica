def normalize_json_data(raw):
    if not isinstance(raw, dict):
        raise ValueError("JSON ontology must be a dictionary")

    # required keys
    if "nodes" not in raw:
        raise ValueError("JSON ontology missing 'nodes' field")

    if "triples" not in raw:
        raise ValueError("JSON ontology missing 'triples' field")

    nodes = raw["nodes"]
    triples = raw["triples"]

    # Validate nodes list
    if not isinstance(nodes, list):
        raise ValueError("'nodes' must be a list")

    for node in nodes:
        if not isinstance(node, dict):
            raise ValueError("Each node must be a dict")
        if "id" not in node:
            raise ValueError("Node missing 'id'")
        if "kind" not in node:
            raise ValueError("Node missing 'kind'")

    # Validate triples list
    if not isinstance(triples, list):
        raise ValueError("'triples' must be a list")

    for t in triples:
        if not isinstance(t, dict):
            raise ValueError("Each triple must be a dict")
        for field in ("subject", "predicate", "object"):
            if field not in t:
                raise ValueError(f"Triple missing '{field}'")

    return nodes, triples