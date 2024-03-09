#!/usr/bin/env bash
while find . -name "*.py" -type f | read file
do echo '#!/usr/bin/python3' > $file && echo '"""Module for '$(basename -s .py $file)'."""' >> $file
done
