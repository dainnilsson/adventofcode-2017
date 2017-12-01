#!/bin/bash

for i in {1..25};
do
  if [ -f "day$i.py" ]; then
    echo "Solutions for day $i:"
    cat input$i.txt | python3 day$i.py
  fi
done

