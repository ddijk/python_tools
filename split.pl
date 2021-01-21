
$regex=$ARGV[0];
$str = $ARGV[1];

@res = split(/$regex/, $str);
print "result is @res\n";

