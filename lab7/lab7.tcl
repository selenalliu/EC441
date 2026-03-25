#Create a simulator object
set ns [new Simulator]

#Define different colors for data flows (for NAM)
$ns color 1 Red

#Open the NAM trace file
set nf [open out.nam w]
$ns namtrace-all $nf

#Open the trace files
set tf [open out.tr w]
$ns trace-all $tf

#Define a 'finish' procedure
proc finish {} {
	global ns nf tf
	$ns flush-trace
	#Close the trace files
	close $nf
	close $tf
	#Execute NAM on the trace file
	exec nam out.nam &
	exit 0
}

#Define a 'dump' procedure to record routing tables
proc dump {} { 
	global ns
	set now [$ns now] 
	puts "Routing table at time $now"
	$ns dump-routelogic-nh
        puts "Dumping Routing Table: Routing Table Information"
	$ns dump-routelogic-distance
}


#Create 7 nodes
set NodeNum 7

for {set i 0} {$i < $NodeNum} {incr i} {
set n($i) [$ns node]
}

#Create links between the nodes
for {set i 0} {$i < $NodeNum} {incr i} {
$ns duplex-link $n($i) $n([expr ($i+1)%$NodeNum]) 1.5Mb 10ms DropTail
}

#Define routing protocols, DV for distance vector, LS for link state, none for static
#$ns rtproto DV
#$ns rtproto LS

#Setup a UDP connection
set udp [new Agent/UDP]
$ns attach-agent $n(0) $udp
set null [new Agent/Null]
$ns attach-agent $n(4) $null
$ns connect $udp $null
$udp set fid_ 1

#Setup a CBR over UDP connection
set cbr [new Application/Traffic/CBR]
$cbr attach-agent $udp
$cbr set type_ CBR
$cbr set packet_size_ 1000
$cbr set rate_ 1Mb
$cbr set random_ false

#Schedule events for the CBR and FTP agents
$ns at 0.1 "$cbr start"
#$ns at 0.5 "dump"
$ns rtmodel-at 1.0 down $n(4) $n(5)
$ns rtmodel-at 3.0 up $n(4) $n(5)
$ns at 4.0 "$cbr stop"

#Call the finish procedure after 5 seconds of simulation time
$ns at 4.0 "finish"

#Run the simulation
$ns run
