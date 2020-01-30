FROM allennlp/allennlp:v0.7.0

# Install Python dependencies
COPY requirements.txt .
RUN pip install -r requirements.txt

# Copy code
COPY build_dataset.py .
COPY convert_multiqa_to_squad_format.py .
COPY multiqa.py .
COPY predict.py .
COPY common/ common/
COPY datasets/ datasets/
COPY models/ models/

ENTRYPOINT []
CMD ["/bin/bash"]