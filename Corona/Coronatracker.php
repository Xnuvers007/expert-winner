<!---XnuversXploitXen--->
<!---PHP PROGRAMMING--->

<?php

echo "__  __                              __  __      _       _ _  __  __          ";
echo "\ \/ /_ __  _   ___   _____ _ __ ___\ \/ /_ __ | | ___ (_) |_\ \/ /___ _ __  ";
echo " \  /| '_ \| | | \ \ / / _ \ '__/ __|\  /| '_ \| |/ _ \| | __|\  // _ \ '_ \ ";
echo " /  \| | | | |_| |\ V /  __/ |  \__ \/  \| |_) | | (_) | | |_ /  \  __/ | | |";
echo "/_/\_\_| |_|\__,_| \_/ \___|_|  |___/_/\_\ .__/|_|\___/|_|\__/_/\_\___|_| |_|";
echo "                                         |_|                                 ";

echo "|-------------------------------------|";
echo "| Author   : XNUVERS007               |";
echo "| You Tube : https://bit.ly/Xnuvers   |";
echo "| github   : https://bit.ly/Xnuvrs1   |";
echo "| Facebook : https://bit.ly/Fesbuck   |";
echo "| Instagram: https://bit.ly/Xnvrs13   |";
echo "| Site     : http://bit.ly/Mykingbee  |";
echo "|-------------------------------------|";
echo "\n";
  
echo "Sekarang (now) = ".date('l, d / M / y');
echo "Waktu  = ".date('H:i:s a');

$url = file_get_contents('https://api.kawalcorona.com/indonesia/');
$data = json_decode($url,true);

echo "Negara : " . $data[0]['name'] . "\n";
echo "Positif : " . $data[0]['positif'] . " Orang\n";
echo "Sembuh : " . $data[0]['sembuh'] . " Orang\n";
echo "Meninggal : " . $data[0]['meninggal'] . " Orang\n";

?>
