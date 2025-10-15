# Project Overview

This project is designed to extract structured data from PDF documents and import it into a Neo4j graph database. It utilizes the `unstructured` Python library to partition and chunk the document's content, and then loads the processed data into Neo4j.

The project is set up to be run in a few different ways:
1.  Programmatically via the `main.py` script.
2.  As a one-off command-line ingestion using `unstructured-ingest`, as shown in the `README.md`.
3.  Via a shell script `ingest.sh` that encapsulates the `unstructured-ingest` command.

The Neo4j database itself is managed via Docker, as defined in the `docker-compose.yml` file.

## Building and Running

### 1. Start the Neo4j Database

The `docker-compose.yml` file defines a Neo4j service. To start it, run:

```bash
docker-compose up -d
```

The database will be available at `bolt://localhost:7687` with the username `neo4j` and password `your_strong_password`.

### 2. Install Dependencies

This project uses Python 3.12+ and `uv` for package management. To install the required dependencies from `pyproject.toml`:

```bash
uv pip install -r requirements.txt
```

### 3. Running the Ingestion

There are three ways to ingest the data:

**A. Via the Python Script (Recommended)**

The `main.py` script provides a more controlled way to process the document. It partitions the PDF using the "hi_res" strategy, chunks the elements by title, and then uploads them to Neo4j.

To run it:

```bash
python main.py
```

**B. Via the `ingest.sh` script**

The `ingest.sh` script uses the `unstructured-ingest` command-line tool to perform the ingestion.

To run it:

```bash
./ingest.sh
```

**C. Manually with `unstructured-ingest`**

As shown in the `README.md`, you can also run the `unstructured-ingest` command directly:

```bash
unstructured-ingest \
    local --input-path document.pdf \
    neo4j --username neo4j --password your_strong_password --uri bolt://localhost:7687 --database mydb
```

## Development Conventions

*   **Dependencies**: Project dependencies are managed in `pyproject.toml` and locked in `uv.lock`.
*   **Database**: The Neo4j database is managed via `docker-compose.yml`. The default credentials are `neo4j/your_strong_password`.
*   **Data**: The input data is expected to be a PDF file named `document.pdf`.
*   **Ingestion Logic**: The core ingestion logic is in `main.py`, which provides a more sophisticated partitioning and chunking strategy than the basic `unstructured-ingest` command.
