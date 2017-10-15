#!/bin/bash


cd ../
root_path=$(pwd)
echo "Project path: "$root_path
cd $root_path/thrift_files/tank_files
echo "generating python sources"
thrift --gen py tank.thrift

if [ -d $root_path/urrcp_ready/tank ]
then
rm -rf $root_path/urrcp_ready/tank/*
else
mkdir $root_path/urrcp_ready/tank
fi

echo "moving files"
cp $root_path/thrift_files/tank_files/gen-py/tank/* $root_path/urrcp_ready/tank/
cp $root_path/thrift_files/tank_files/tank_handler.py $root_path/urrcp_ready/tank/

echo "done."