#!/usr/bin/env bash
for file in $(find . -name "*.py" -type f)
do echo '#!/usr/bin/python3' > $file && echo '"""Module for '"$(basename -s .py $file)"'."""' >> $file
done
