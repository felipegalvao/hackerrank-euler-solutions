<?php
  $_fp = fopen("php://stdin", "r");
  /* Enter your code here. Read input from STDIN. Print output to STDOUT */
  $t = fgets($_fp);
  for($i=0;$i<$t;$i++){
      $n = fgets($_fp);
      $height = 1;
      for($j=0;$j<$n;$j++) {
          if(($j == 0) or ($j % 2 == 0)) {
              $height = $height * 2;
          } else {
              $height = $height + 1;
          }
      }
      print $height . "\n";
  }
?>
