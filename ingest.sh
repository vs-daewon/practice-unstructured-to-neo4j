TESSDATA_PREFIX=/opt/homebrew/share/tessdata unstructured-ingest \
    local \
        --input-path document.pdf \
        --ocr-languages kor \
    neo4j --username neo4j --password your_strong_password --uri bolt://localhost:7687 --database neo4j
