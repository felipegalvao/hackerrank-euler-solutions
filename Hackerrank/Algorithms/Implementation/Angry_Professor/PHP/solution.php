<?php
  $_fp = fopen("php://stdin", "r");
  /* Enter your code here. Read input from STDIN. Print output to STDOUT */
  $t = fgets($_fp);

  for($i=0;$i<$t;$i++) {
      $arguments = split(' ', fgets($_fp));
      $students_quantity = $arguments[0];
      $limit = $arguments[1];
      $students = split(' ', fgets($_fp));
      $students_on_time = 0;

      for($j=0;$j<$students_quantity;$j++){
          if ($students[$j] <= 0) {
              $students_on_time = $students_on_time + 1;
          }
      }

      if ($students_on_time < $limit) {
          print "YES\n";
      } else {
          print "NO\n";
      }
  }
?>
