#!/bin/bash

##############
#File names
#-------------
#constants.py
#ttypes
#Urrcp.py
#Urrcp-remote
#-------------
##############

cd ../
root_path=$(pwd)
echo "Project path: "${root_path}
cd ${root_path}/thrift_files/

# --------------------------------------- #
echo "generating python sources"
thrift --gen py urrcp.thrift
# --------------------------------------- #

echo "copy files"
cp ${root_path}/thrift_files/gen-py/urrcp/* ${root_path}/

echo "done."