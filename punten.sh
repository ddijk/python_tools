for i in {1..200}; do
    echo -n "iteration $i, ";
    date
    python3 knwu_punten.py herw 71
    sleep 3600;
done
