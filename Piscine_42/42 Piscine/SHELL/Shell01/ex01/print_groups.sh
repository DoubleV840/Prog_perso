#!/bin/bash
# print_groups.sh

id -nG $FT_USER | tr ' ' ',' | tr -d '\n'
