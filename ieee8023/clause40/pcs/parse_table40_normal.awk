BEGIN {
	print("NORMAL_BIT_TO_SYMBOL = {");
}

$1 == "=" && $3 == "=" && $5 == "=" && $7 == "=" {
	Sdn_6_8[1] = substr($2, 2, 3);
	Sdn_6_8[2] = substr($4, 2, 3);
	Sdn_6_8[3] = substr($6, 2, 3);
	Sdn_6_8[4] = substr($8, 2, 3);
}

# Sample line: '  Normal     000000    0, 0, 0, 0    0, 0,+1,+1    0,+1,+1, 0    0,+1, 0,+1'
$1 == "Normal" {
	printf("    0b%s%s: (%s),\n", Sdn_6_8[1], $2, substr($0, 23, 11));
	printf("    0b%s%s: (%s),\n", Sdn_6_8[2], $2, substr($0, 37, 11));
	printf("    0b%s%s: (%s),\n", Sdn_6_8[3], $2, substr($0, 51, 11));
	printf("    0b%s%s: (%s),\n", Sdn_6_8[4], $2, substr($0, 65, 11));
}

END {
	print("}")
}
