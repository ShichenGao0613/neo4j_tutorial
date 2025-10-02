# Knowledge Graph Project

## Project Structure

- **dataset/**
  - Contains CSV files used for building the knowledge graph.
  - Each CSV file defines nodes or relationships according to Neo4j’s CSV import format.

- **import_csv.py**
  - Python script responsible for loading the CSV files into Neo4j.
  - It handles connections to the Neo4j database, reads the CSVs, and executes Cypher queries for importing nodes and relationships.
