# normalize_properties
Normalize bash-style variables in properties file

# input
een properties file met variablen, bijv. gemaakt door:
cat c.properties dd.properties > all.properties


# Usage:
# resolve alle variabelen:
python props.py -f  all.properties > dd.properties


# Output:
File 'dd.properties' waarin alle variabelen zijn resolved 

