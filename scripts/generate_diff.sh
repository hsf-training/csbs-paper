#!/usr/bin/env bash

# Script to generate a latexdiff comparing the current main version with the
# version from the first submission
# Kilian Lieret (kilian.lieret@posteo.de) Feb 2020
#
# Usage: ./generate_diff.sh <hash of previous version to compare to>

set -e
set +x

# Change to correct directory that contains the latex bits
pushd $(git rev-parse --show-toplevel)

# Check out old version of paper and copy it to new file
git checkout $1
cp main.tex _main.tex

# Go back to current version
git checkout main

# Generate diff
latexdiff _main.tex main.tex > diff.tex

# Build
mkdir -p build
pdflatex --output-directory build diff.tex
bibtex build/diff
pdflatex --output-directory build diff.tex
bibtex build/diff
pdflatex --output-directory build diff.tex

# Remove old version
rm _main.tex
rm diff.tex

# Jump back to the directory that we started from
popd
