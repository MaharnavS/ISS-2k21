#!/bin/bash
grep . quotes.txt
echo ""
awk '!seen[$0]++' quotes.txt