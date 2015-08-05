<?php
$_fp = fopen("php://stdin", "r");
/* Enter your code here. Read input from STDIN. Print output to STDOUT */
$n = fgets($_fp);
$sticks = split(' ',trim(fgets($_fp)));
$sticks_cut = 0;
do {
    $size_sticks = sizeof($sticks);
    print $size_sticks . "\n";
    $min_stick = min($sticks);
    $sticks = array_values($sticks);
    for ($i=0;$i<$size_sticks;$i++) {
        $sticks[$i] = $sticks[$i] - $min_stick;
        if ($sticks[$i] == 0) {
            unset($sticks[$i]);
        }
    }
} while(sizeof($sticks) > 0)

?>
