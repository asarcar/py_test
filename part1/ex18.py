#!/usr/bin/python3

import sys

# non-standard library imports
from asarcar_package import file_exists


def secret_formula(sta_cnt, jb_mult, jar_div, crat_mod):
  jb = sta_cnt * jb_mult
  jars = sta_cnt / jar_div
  cra = sta_cnt % crat_mod
  return jb, jars, cra


def main():
  if (len(sys.argv) != 6):
    print("Usage: %s <dst_file> <start_count> <jellybeans_multiplier> <jars_divisor> <crates_modulus>" % sys.argv[0])
    sys.exit(1)
    
  scr, dst_file, st_cnt_str, jb_mul_str, jars_div_str, cra_mod_str = sys.argv

  if file_exists(dst_file):
    print("O/P file %s exists: aborting operation"%dst_file)
    sys.exit(1)
    
  st_cnt = int(st_cnt_str)
  jb_mul = int(jb_mul_str)
  jars_div = int(jars_div_str)
  cra_mod = int(cra_mod_str)

  if st_cnt <= 0 or jb_mul <= 0 or jars_div <= 0 or cra_mod <= 0:
    print("Bad numbers entered: \"st_cnt %d: jb_mul %d: jars_div %d: cra_mod %d\"" %(st_cnt, jb_mul, jars_div, cra_mod))
    sys.exit(1)

  numjellybeans, numjars, numcrates = secret_formula(st_cnt, jb_mul, jars_div, cra_mod)
  print("Start Count %d: Jelly Beans %d: Jars %d: Crates %d" %(st_cnt, numjellybeans, numjars, numcrates))

  st_cnt2 = st_cnt*2
  fobj = open(dst_file, "w")
  str1 = "Start Count %d: " %st_cnt2
  str1 += "Jelly Beans %d: Jars %d: Crates %d\n" %secret_formula(st_cnt2, jb_mul, jars_div, cra_mod) 
  fobj.write(str1)
  fobj.close()

  return

if __name__ == "__main__":
    main()
    

 
