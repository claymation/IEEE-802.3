BEGIN {
	print("IDLE_BIT_TO_SYMBOL = {");
}

# Sample line: 'Idle/CarrExt 000000    0, 0, 0, 0        -             -             -'
$1 == "Idle/CarrExt" {
	printf("    0b%s: (%s),\n", $2, substr($0, 23, 11));
}

END {
	print("}")
}
