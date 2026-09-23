#!/bin/bash

read -rp "Root folder name : " root
read -rp "Subfolder Count : " count

mkdir -p "$root"

for ((i=0; i<count; i++)); do
    printf -v subfolder "ex%02d" "$i"
    mkdir -p "$root/$subfolder"
done

echo "Created $count subfolders in '$root'"
