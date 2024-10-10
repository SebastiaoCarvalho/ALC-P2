#!/bin/bash

run_command="python3 project1.py"
test_folder="public-tests"

declare -a file_base=("t01" "t02" "t03" "t04" "t05" "t06" "t07" "t08" "t09" "t10" "t11" "t12" "t13" "t14" "t15" "t16")

for file in "${file_base[@]}"; do
    file_in="${test_folder}/${file}.ttp"
    file_out="${test_folder}/${file}.out"
    file_out_test="${test_folder}/${file}.out.test"

    echo "Running test for ${file_in}"
    SECONDS=0    
    $run_command < $file_in > $file_out_test

    if diff $file_out $file_out_test > /dev/null; then
        duration=$SECONDS
        echo -e "\e[32mTEST PASSED\e[0m : $((duration / 60))m $((duration % 60))s"
    else
        duration=$SECONDS
        echo -e "\e[31mTEST FAILED\e[0m : $((duration / 60))m $((duration % 60))s"
    fi

done