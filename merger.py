import os, sys

def merge(path, out_file, n_files=50):
   file_list = open(path, 'r').read().splitlines()
   
   chunks = [file_list[x:x+n_files] for x in range(0, len(file_list), n_files)]

   for idx, c in enumerate(chunks):
      cmd = f'hadd -f {out_file}_{idx}.root'
      for s in c:
         cmd +=  " "+ s
      print(f'Merging file {idx}')
      os.system(cmd)
   
   print('DONE!!')

if __name__ == '__main__':
   if len(sys.argv) != 3:
      print("There should two arguments!!")
      sys.exit()
   
   merge(sys.argv[1], sys.argv[2])
   