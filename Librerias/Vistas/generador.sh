#!/bin/bash
# Generador de carpetas

for d in ./*ui;do
f="$(basename --suffix=.ui $d).py"
pyuic5 -x "$d" -o "$f"
done