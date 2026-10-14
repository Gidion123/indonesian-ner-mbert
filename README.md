# Indonesian Named Entity Recognition with mBERT

Fine-tuning multilingual BERT to identify **people, organizations, locations, and dates** in Indonesian text. This notebook project covers dataset inspection, exploratory analysis, label normalization, subword alignment, model training, evaluation, and error analysis using the NERGrit corpus.

**Recorded test entity F1: 87.03%** on 2,397 test sequences after mapping the corpus to four entity types. Organization recognition is the main remaining weakness, with a rounded per-class F1 of 0.72.

> Results below come from the notebook's saved execution outputs. They have not been independently reproduced for this README. The training output includes a checkpoint reload warning documented under [Limitations](#limitations-and-next-steps).

[Explore the notebook](Gidion%20Depari_Assigment_nlp.ipynb) · [Dataset documentation](data_nergrit18/nergrit-corpus/Readme.md) · [Dataset license](data_nergrit18/nergrit-corpus/LICENSE)

## Project overview

Named Entity Recognition turns unstructured text into labeled spans that can support document search, information extraction, and downstream text analysis. This project implements the modeling workflow for Indonesian NER and examines where the model succeeds and fails.

| Component | Implementation |
|---|---|
| Backbone | `bert-base-multilingual-cased` |
| Task | Supervised token classification |
| Target entities | `PER`, `ORG`, `LOC`, `DAT` |
| Label scheme | Nine BIO labels, including `O` |
| Frameworks | PyTorch, Hugging Face Transformers, Datasets, Evaluate |
| Evaluation | Entity precision, recall, and F1 with `seqeval`; token accuracy; confusion matrix |
| Interface | Executable Jupyter notebook with saved outputs |

The project-specific work is in the root notebook: a corpus parser, exploratory analysis, target-label mapping, word-to-subword alignment, fine-tuning configuration, and evaluation. The bundled NERGrit directory also contains upstream scripts and legacy model files; those are supplied corpus resources, separate from this notebook's mBERT implementation.

## Dataset and task definition

The notebook uses the corrected NERGrit archive distributed through [Cahya Wirawan's Indonesian language models repository](https://github.com/cahya-wirawan/indonesian-language-models/blob/master/data/nergrit-corpus_20190726_corrected.tgz). Only the files under `ner/data/` are used for this experiment.

The original split boundaries are retained:

| Split | Parsed sequences | Purpose |
|---|---:|---|
| Train | 12,514 | Fine-tuning and exploratory analysis |
| Validation | 2,520 | Evaluation after each epoch and checkpoint selection |
| Test | 2,397 | Final recorded evaluation and subsequent error analysis |
| **Total** | **17,431** | |

The parser treats blank lines as sequence boundaries and reads the first field as the token and the last field as its label. “Sequence” is used here because these file-delimited units are not guaranteed to be individual linguistic sentences.

The source corpus covers 18 entity categories. This experiment narrows the task to:

| Entity | Meaning | Mapping |
|---|---|---|
| `PER` | Person | Retain recognized person tags |
| `ORG` | Organization | Retain recognized organization tags |
| `LOC` | Location | Merge recognized `GPE` and `LOC` tags |
| `DAT` | Date | Retain recognized date tags |
| `O` | Outside the target entities | Map other or unrecognized labels to `O` |

The resulting label set is `O`, `B-PER`, `I-PER`, `B-ORG`, `I-ORG`, `B-LOC`, `I-LOC`, `B-DAT`, and `I-DAT`.

## Exploration and modeling decisions

The notebook explores the training data before fine-tuning. The most useful findings and their implications are:

| Finding from saved outputs | Decision or interpretation |
|---|---|
| 309,202 training tokens and 126 distinct raw labels, including malformed annotations | Map raw labels into a consistent nine-label target vocabulary and inspect mapping behavior. |
| Raw `O` labels account for 213,728 tokens, or 69.12% of the training set | Use entity F1 as the checkpoint-selection metric; token accuracy alone can obscure entity errors. This percentage is before target-label mapping. |
| Mean sequence length is 24.71 original tokens; the 95th and 99th percentiles are approximately 50 and 83; maximum is 467 | Set a practical tokenizer limit of 128 and use dynamic batch padding. Original-token lengths do not establish the actual subword truncation rate. |
| Samples include dates written with words, numbers, and separators | Keep `DAT` as an explicit target category and inspect date-related errors. |
| The corpus distinguishes geopolitical entities from other locations | Merge `GPE` into `LOC` to match the four-entity task definition. |

### Label mapping behavior

`map_tag_to_target()` strips surrounding whitespace, uppercases labels, recognizes selected entity-name substrings, and maps other labels to `O`. For example:

| Raw label | Mapped label |
|---|---|
| `B-GPE` | `B-LOC` |
| `I-DaT` | `I-DAT` |
| `B=PER` | `B-PER` |
| `B-L0C` | `O` |
| `B-MON` | `O` |

This is a rule-based vocabulary normalization step. It does not fully repair annotation errors or validate every BIO transition. Some potentially recoverable entity labels are lost when they map to `O`.

### Subword alignment

The tokenizer receives pretokenized sequences with `is_split_into_words=True`. The first subword of each original token receives its label; continuation subwords and special tokens receive `-100` and are excluded from loss and metric calculations. `DataCollatorForTokenClassification` pads batches dynamically.

The 128-token limit applies to the tokenizer output, including special tokens. Long sequences are truncated without sliding windows, so the reported evaluation covers the retained portions of those sequences.

## Training configuration

| Setting | Value in the notebook |
|---|---|
| Learning rate | `2e-5` |
| Training epochs | `3` |
| Per-device train / evaluation batch size | `16` / `16` |
| Weight decay | `0.01` |
| Maximum tokenized length | `128` |
| Evaluation and checkpoint saving | Every epoch |
| Best-checkpoint selection | Validation F1, with `load_best_model_at_end=True` |
| External experiment reporting | Disabled with `report_to="none"` |

The saved run used Apple Silicon MPS and completed 2,349 training steps in approximately 21 minutes 43 seconds. This is a recorded runtime for that environment, not a cross-hardware benchmark.

### Recorded validation progression

| Epoch | Validation loss | Entity precision | Entity recall | Entity F1 |
|---|---:|---:|---:|---:|
| 1 | 0.082402 | 84.01% | 87.04% | 85.50% |
| 2 | 0.077482 | 86.79% | 89.11% | 87.93% |
| 3 | 0.081553 | 87.64% | 88.38% | **88.01%** |

Epoch 3 has the highest recorded validation F1, while epoch 2 has the lowest validation loss. The configuration prioritizes F1. This single run does not establish an optimal epoch count or prove the absence of overfitting.

## Recorded test results

| Metric | Value |
|---|---:|
| Entity precision | 86.70% |
| Entity recall | 87.37% |
| Entity F1 | **87.03%** |
| Token accuracy | 97.49% |
| Loss | 0.0965 |

Entity precision, recall, and F1 use the overall `seqeval` metrics. Accuracy is calculated over retained, unmasked token labels. The code uses default `seqeval` behavior and does not explicitly enable strict IOB2 evaluation.

### Per-entity report

Values below retain the two-decimal precision printed by the notebook; support counts refer to evaluated gold entities after mapping and truncation.

| Entity | Precision | Recall | F1 | Support |
|---|---:|---:|---:|---:|
| Date (`DAT`) | 0.93 | 0.94 | 0.94 | 788 |
| Location (`LOC`) | 0.87 | 0.87 | 0.87 | 1,644 |
| Organization (`ORG`) | 0.70 | 0.74 | 0.72 | 856 |
| Person (`PER`) | 0.94 | 0.92 | 0.93 | 1,448 |
| **Total** | | | | **4,736** |

These results describe this four-entity transformation of NERGrit. They should not be directly compared with results for the original 18-entity task or a different preprocessing and evaluation protocol.

## Error analysis and lessons

The notebook inspects correct predictions, mismatches, and a token-level confusion matrix.

- **Organizations need the most attention.** The confusion matrix records 156 `B-ORG` and 228 `I-ORG` tokens predicted as `O`. These token counts complement the lower entity-level ORG F1.
- **Uppercase news datelines can be ambiguous.** Saved examples include `CIANJUR` and `BANDUNG` labeled as locations but predicted as organizations.
- **Entity boundaries can be missed.** A recorded example labels `Kabupaten Cianjur` as a location, while the model predicts `O` for both tokens.
- **Annotation quality requires review.** Some mismatches may involve ambiguous or inconsistent gold labels; a mismatch alone does not establish which label is semantically correct.
- **Date-to-location confusion was absent in this evaluated output.** The saved confusion matrix contains zero `DAT` tokens predicted as `LOC`. This is specific to this run and evaluation scope.

The strongest next experiment is targeted review of ORG annotations and boundary errors, followed by validation-based comparison against the existing baseline.

## Run the notebook

The saved notebook metadata records Python **3.10.20**. Exact dependency versions were not captured in a lockfile, so the following is a starting environment rather than a verified reproduction of the original run.

```bash
git clone https://github.com/Gidion123/indonesian-ner-mbert.git
cd indonesian-ner-mbert
python3.10 -m venv .venv
source .venv/bin/activate
python -m pip install --upgrade pip
python -m pip install torch transformers datasets evaluate seqeval accelerate numpy pandas scikit-learn ipywidgets jupyterlab ipykernel
python -m ipykernel install --user --name indonesian-ner-mbert --display-name "Indonesian NER mBERT"
jupyter lab
```

On Windows, activate the environment with `.venv\Scripts\activate` instead. Select the **Indonesian NER mBERT** kernel and open `Gidion Depari_Assigment_nlp.ipynb`.

1. Start Jupyter from the repository root so relative dataset paths resolve.
2. Run cells in order. The NER data files are already included; the archive download described in the notebook is not required for a normal clone.
3. Allow network access for the initial pretrained model/tokenizer and metric downloads.
4. Inspect training and checkpoint-loading warnings before interpreting the evaluation.
5. The final cell saves the model and tokenizer into `best_indonesian_ner_model/`.

An accelerator is recommended for fine-tuning. The notebook includes an MPS availability check; Hugging Face Trainer manages its training device. No CUDA-specific runtime benchmark is provided.

**The fine-tuned mBERT weights are not committed.** `best_indonesian_ner_model/`, checkpoint directories, and several weight formats are excluded by `.gitignore`. Re-running training is necessary to create the notebook's model artifact locally. The legacy `.h5` files inside the bundled corpus are not this fine-tuned mBERT model.

## Repository structure

```text
indonesian-ner-mbert/
├── README.md
├── Gidion Depari_Assigment_nlp.ipynb
├── .gitignore
└── data_nergrit18/
    ├── nergrit.tgz
    └── nergrit-corpus/
        ├── LICENSE
        ├── Readme.md
        ├── README.md.pdf
        ├── ner/
        │   ├── data/
        │   │   ├── train.txt
        │   │   ├── valid.txt
        │   │   └── test.txt
        │   └── ... upstream scripts and model resources
        ├── sentiment/  ... upstream resources, unused by this experiment
        └── statement/  ... upstream resources, unused by this experiment
```

## Limitations and next steps

1. **Verify checkpoint reload integrity.** The saved training log reports missing LayerNorm `weight`/`bias` keys and unexpected `gamma`/`beta` keys during checkpoint reload. The recorded test scores do not establish that every selected-checkpoint parameter was restored correctly. Record library versions, investigate the warning, and compare predictions before saving and after a fresh load before claiming a reproducible model release.
2. **Measure actual truncation.** Audit WordPiece lengths and lost entity spans. The original-token percentiles do not prove that a 128-subword limit preserves more than 99% of sequences.
3. **Audit label quality.** Review malformed-label mappings, BIO consistency, and ORG boundaries; mapping a noisy label to `O` can discard useful supervision.
4. **Strengthen evaluation.** No multi-seed results, confidence intervals, baseline-model comparison, cross-split duplicate audit, or external-domain test is documented. Compare future changes on validation data; the current test set has already informed qualitative error analysis.
5. **Improve reproducibility and packaging.** Add validated dependency pins, an explicit seed setup before model initialization, a model card, and a verified reload/inference example. There is currently no deployed API or application in this repository.

IndoBERT comparison, loss reweighting, and contextual postprocessing are possible future experiments. Their performance gains have not been measured here.

## Attribution and references

Project notebook: **Gidion Depari**.

The corpus and bundled upstream resources are credited to **NERGRIT DEVELOPERS (2019)**. Preserve their [license](data_nergrit18/nergrit-corpus/LICENSE) and [full contributor credits](data_nergrit18/nergrit-corpus/Readme.md) when redistributing those materials. The corpus license does not establish a separate license for the project notebook; no project-level license file is currently present.

- [NERGrit archive distribution used by the notebook](https://github.com/cahya-wirawan/indonesian-language-models/blob/master/data/nergrit-corpus_20190726_corrected.tgz)
- [Multilingual BERT model card](https://huggingface.co/google-bert/bert-base-multilingual-cased)
- [Hugging Face token classification guide](https://huggingface.co/docs/transformers/tasks/token_classification)
- [Hugging Face Evaluate: seqeval metric](https://huggingface.co/spaces/evaluate-metric/seqeval/blob/main/README.md)

Documentation evidence: notebook blob `7ff4ee30ae323ee88f3f1f34f991da42647b1f31` and repository tree `731797f8920c35c89624e6840f3ee44ef6c4dc78`, inspected on 14 October 2026.
