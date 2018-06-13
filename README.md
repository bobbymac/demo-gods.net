## demo-gods.net
Static DNS records for demos under the domain "Demo-Gods.net"


Sick of editing hosts files or using .localhost for in DNS records for demos?  Stop sacrificing VM’s to the Demo-Gods.   The Gods have answered with basic DNS for well know frame works in the RFC 1918 space.  I will be changing/adding to this is in near future to facilitate more frameworks including unique IP addrs in the range 10.0.0.0/8.  The current frame of mind is to offer 1, 3, 5 and 7 node frameworks including TXT records to explain.

Forward DNS is publicly resolvable and the appropriate reverse zone files can be added to your own bind server.

For reverse DNS,  add the following line to named.conf.  Change the SOA to reflect you DNS local server.

```zone "100.0.10.in-addr.arpa" IN { type master; file "100.0.10.in-addr.arpa.zone"; allow-update { none; }; };```

I am not going to go over all the bind syntax or how to configure named.conf but the current format is per /24.

#### Current records:  

Docker Enterprise uses the 10.0.100.0/24

	dtr 3660 IN A 10.0.100.6
	dtr-node1 3660 IN A 10.0.100.13
	dtr-node2 3660 IN A 10.0.100.14
	dtr-node3 3660 IN A 10.0.100.15
	dtr-node4 3660 IN A 10.0.100.16
	dtr-node5 3660 IN A 10.0.100.17
	ucp 3660 IN A 10.0.100.5
	ucp-node1 3660 IN A 10.0.100.10
	ucp-node2 3660 IN A 10.0.100.11
	ucp-node3 3660 IN A 10.0.100.12
	ucp-node4 3660 IN A 10.0.100.18
	ucp-node5 3660 IN A 10.0.100.19
	worker 3660 IN A 10.0.100.7
	worker2 3660 IN A 10.0.100.8
	worker3 3660 IN A 10.0.100.9
	worker4 3660 IN A 10.0.100.20
	worker5 3660 IN A 10.0.100.21
	worker6 3660 IN A 10.0.100.22
	worker7 3660 IN A 10.0.100.23
	worker8 3660 IN A 10.0.100.24
	worker9 3660 IN A 10.0.100.25
	worker10 3660 IN A 10.0.100.26
	worker11 3660 IN A 10.0.100.27
	worker12 3660 IN A 10.0.100.28
	worker13 3660 IN A 10.0.100.29
	worker14 3660 IN A 10.0.100.30
	worker15 3660 IN A 10.0.100.31
	worker16 3660 IN A 10.0.100.32
	worker17 3660 IN A 10.0.100.33
	worker18 3660 IN A 10.0.100.34
	worker19 3660 IN A 10.0.100.35
	worker20 3660 IN A 10.0.100.36


General

	haproxy 3660 IN A 172.28.128.30
	jenkins 3660 IN A 172.28.128.31
	nodeapp 3660 IN A 172.28.128.31
	visualizer 3660 IN A 172.28.128.31
	wordpress 3660 IN A 172.28.128.31

 Themes

	gilligan 3600 IN A 10.0.110.2
	skipper 3660 IN A 10.0.110.3
	mr-howel 3660 IN A 10.0.110.4
	mrs-howel 3660 IN A 10.0.110.5
	lovey 3600 IN CNAME mrs-howel
	ginger 3660 IN A 10.0.110.6
	maryann 3660 IN A 10.0.110.7
	professor 3660 IN A 10.0.110.8
	wrongway-feldman 3660 IN A 10.0.110.9
	dr-balinkoff 3660 IN A 10.0.110.10
	japanese-sailor 3660 IN A 10.0.110.11
	gorilla 3660 IN A 10.0.110.12
	minnow 3660 IN A 10.0.110.13
	island 3660 IN A 10.0.110.14
	tropic-port 3660 IN A 10.0.110.15
	2hour-tour 3660 IN A 10.0.110.16
	mosquitoes 3660 IN A 10.0.110.17
	bingo 3660 IN A 10.0.110.18
	bango 3660 IN A 10.0.110.19
	bongo 3660 IN A 10.0.110.20
	irving 3660 IN A 10.0.110.21
