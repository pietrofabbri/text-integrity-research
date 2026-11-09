# Text Integrity Research

A research project on AI-generated text detection and text watermarking.

The repository currently contains project documentation, one audit tool and three `EXPERIMENTAL` capabilities that compare the structure of Markdown texts, measure how much a text changed, and compare digit-written numbers. No detection or watermarking capability is implemented, and nothing here should be read as a claim of validated performance.

Start with [`docs/00-project/START-HERE.md`](docs/00-project/START-HERE.md).

Run the audit with `python3 tools/verify_docs.py .`
Run the tests with `python3 -m unittest discover -s tests`
