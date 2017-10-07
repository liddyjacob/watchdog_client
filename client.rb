require "socket"
s = TCPSocket.open('18.220.180.253', 50000)
while line = s.gets
	puts "received : #{line.chop}"
end
s.close
