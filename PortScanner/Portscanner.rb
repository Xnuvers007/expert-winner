require 'socket'
require 'timeout'

printf "====================\n"
print "XnuversXploitXen\n"
print "PORT SCANNER...\n"
print "===================="
print "\n"

print "Ip Address"
ip = gets.chomp

ports = 21, 22, 23, 25, 53, 80, 110, 143, 443, 465, 587, 993

ports.each do |scan|
  begin
    Timeout::timeout(10){TCPSocket.new("#{Ip}", scan)}
  rescue
    puts "closed : #{scan}"
  else
    puts "open : #{scan}"
  end
end

port = 1..1000

port.each do |scans|
  begin
    Timeout::timeout(10){TCPSocket.new("#{Ip}", scans)}
  rescue
    puts "closed : #{scans}"
    else
      puts "open : #{scans}"
    end
  end

sleep 4
