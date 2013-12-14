#!/usr/bin/python

type_list = [ "char", "uchar", "short", "ushort", "int", "uint", "long", "ulong", "float", "double", ]
vec_list = [ "", "2", "3", "4", "8", "16", ]
sat_list = [ "", "_sat", ]
rounding_list = [ "", "_rte", "_rtz", "_rtp", "_rtn", ]

def build_description(dest_type, sat, rounding):
	description = "Explixit Type Conversion To " + dest_type
	if sat is "_sat":
		description += " Saturated"
	if rounding is "_rte":
		description += " Round To Nearest Even"
	if rounding is "_rtz":
		description += " Round Towards Zero"
	if rounding is "_rtp":
		description += " Round Toward Positive Infinity"
	if rounding is "_rtn":
		description += " Round Toward Nevagite Infinity"
	return description

def write_snippet(dest_type, sat, rounding):
	function = "convert_" + dest_type + sat + rounding
	description = build_description(dest_type, sat, rounding)
	f = open(function + ".sublime-snippet", "w")
	f.write("<snippet>\n\t<description>" + description + "</description>\n")
	f.write("\t<content><![CDATA[" + function + "(${1:x})]]></content>\n")
	f.write("\t<tabTrigger>" + function + "</tabTrigger>\n")
	f.write("\t<scope>source.opencl</scope>\n</snippet>\n")

for scalar_type in type_list:
	for vec in vec_list:
		dest_type = scalar_type + vec
		for sat in sat_list:
			for rounding in rounding_list:
				write_snippet(dest_type, sat, rounding)
