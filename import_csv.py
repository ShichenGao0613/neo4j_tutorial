from neo4j import GraphDatabase

# Connect to Neo4j
driver = GraphDatabase.driver("neo4j://127.0.0.1:7687", auth=("neo4j", "12345678"))

# Define node CSV files
node_files = [
    {"fileName": "file:///level1.csv", "labels": []},
    {"fileName": "file:///level2.csv", "labels": []},
    {"fileName": "file:///level3.csv", "labels": []},
    {"fileName": "file:///reviews_nodes.csv", "labels": []},
    {"fileName": "file:///user_nodes.csv", "labels": []},
    {"fileName": "file:///business_nodes.csv", "labels": []},
]

# Define relationship CSV files
rel_files = [
    {"fileName": "file:///edges.csv", "type": ""}
]

# Import data using APOC
with driver.session() as s:
    result = s.run("""
      CALL apoc.import.csv($nodes, $rels, {
        delimiter: ",",
        arrayDelimiter: "|",
        stringIds: true,
        batchSize: 20000
      })
    """, {"nodes": node_files, "rels": rel_files})

    stats = result.single()
    print(stats)

# Check counts of nodes and relationships
with driver.session() as s:
    print(s.run("MATCH (n) RETURN count(n) AS c").single()["c"])
    print(s.run("MATCH ()-[r]->() RETURN count(r) AS c").single()["c"])

# Close the driver
driver.close()