#filters out0.tr trace file into overhead packets
#usage: awk -f filter.awk out0.tr

BEGIN{}
{
  if($1 == "\+"){
    if($3 == 0){
      i++
      if($5 == "rtProtoDV")
	j++
      if($5 == "rtProtoLS")
	k++
    }
    if($5 == "rtProtoDV"){
      l++
      print > "DVpackets.tr"
    }
    if($5 == "rtProtoLS"){
      m++
      print > "LSpackets.tr"
    }
  }
}
END{print "total data packets from source: "i-j-k "\nDV control packets from source: "j+0"\nLS control packets from source: "k+0 "\ntotal DV packets: "l+0"\ntotal LS packets: "m+0}
