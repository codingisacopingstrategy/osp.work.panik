#!/bin/bash

for f1 in *.*; do
 convert "$f1" pbm:- | potrace -s -o "`echo $f1 | sed 's/\(.*\)\..*/\1/'`.svg"
done
echo "stop"

