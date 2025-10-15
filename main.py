import os

from unstructured.partition.pdf import partition_pdf
from unstructured.chunking.title import chunk_by_title
from unstructured.staging.neo4j import Neo4jUploader
from unstructured_client.models.shared.ne

# --- 1. CONFIGURATION ---
# Replace with your local Neo4j database credentials
NEO4J_URI = "neo4j://localhost:7687"
NEO4J_USERNAME = "neo4j"
NEO4J_PASSWORD = "your_strong_password"

# Define the path to your local PDF file
FILE_PATH = "document.pdf"


def main():
    # Check if the file exists
    if not os.path.exists(FILE_PATH):
        print(f"Error: The file '{FILE_PATH}' was not found.")
    else:
        print(f"Processing document: {FILE_PATH}")

        # --- 2. PARTITION THE DOCUMENT ---
        # The 'hi_res' strategy uses advanced models to detect layout,
        # including titles and tables.
        elements = partition_pdf(
            filename=FILE_PATH,
            strategy="hi_res",
            infer_table_structure=True,  # This is key for table detection
        )

        # --- 3. CHUNK ELEMENTS BY TITLE ---
        # This groups related elements under their respective titles,
        # creating a more meaningful structure for the graph.
        chunks = chunk_by_title(elements)
        print(
            f"\nSuccessfully partitioned and chunked document into {len(chunks)} sections."
        )

        # --- 4. UPLOAD TO NEO4J ---
        # Initialize the uploader with your database credentials
        uploader = Neo4jUploader(
            uri=NEO4J_URI,
            user=NEO4J_USERNAME,
            password=NEO4J_PASSWORD,
        )

        # Upload the chunks to Neo4j. Each chunk becomes a node.
        # The uploader automatically creates relationships between consecutive chunks.
        print("\nUploading data to Neo4j...")
        uploader.upload_chunks(chunks)
        print("✅ Upload complete!")
        print(
            "\nTo view your graph, open the Neo4j Browser and run the query: MATCH (n) RETURN n"
        )


if __name__ == "__main__":
    main()
