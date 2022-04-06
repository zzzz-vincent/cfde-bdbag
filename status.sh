#!/bin/bash

ASSAYS=(hubmap-3dimc-20211010.csv
hubmap-af-20210609.csv
hubmap-bulkatacseq-20210609.csv
hubmap-bulkrnaseq-20210609.csv
hubmap-codex-20210820.csv
hubmap-imc-20210823.csv
hubmap-lightsheet-20210820.csv
hubmap-maldi-ims-neg-20210820.csv
hubmap-maldi-ims-pos-20210820.csv
hubmap-pas-20210820.csv
hubmap-scrnaseq-20210609.csv
hubmap-slideseq-20211010.csv
hubmap-snatacseq-20210315.csv
hubmap-wgs-20210609.csv)

for ASSAY in "${ASSAYS[@]}"
do
	./status.py $ASSAY
done
