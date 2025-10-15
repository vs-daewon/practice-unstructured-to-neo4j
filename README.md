# practice unstrucutured to neo4j

## prerequisites

```bash
brew install poppler tesseract

# add kor
mkdir -p /opt/homebrew/share/tessdata
cd /opt/homebrew/share/tessdata
curl -L -O https://github.com/tesseract-ocr/tessdata_best/raw/main/kor.traineddata
# validation kor
tesseract --list-langs
```

## dev

```bash
unstructured-ingest \
    local --input-path document.pdf \
    neo4j --username neo4j --password your_strong_password --uri bolt://localhost:7687 --database mydb
```
