import os

paths = [
    #'/eos/user/k/kmotaama/CRAB_PrivateMC/UpsilonPt9To30ToMuMuDstarToD0pi',
    #'/eos/user/k/kmotaama/CRAB_PrivateMC/UpsilonPt30To60ToMuMuDstarToD0pi',
    #'/eos/user/k/kmotaama/CRAB_PrivateMC/UpsilonPt60To120ToMuMuDstarToD0pi',
    #'/eos/user/k/kmotaama/CRAB_PrivateMC/UpsilonPt120ToMuMuDstarToD0pi',
    '/eos/user/k/kmotaama/CRAB_PrivateMC/Upsilon1SMapsePt60To120ToMuMuDstarToD0pi',
    '/eos/user/k/kmotaama/CRAB_PrivateMC/Upsilon1SPt60To120ToMuMuDstarToD0pi',
    ]
paths = [p + '/' + os.listdir(p)[0] for p in paths]
template = 'python/gentuple_template.py'

for path in paths:
    for p in os.listdir(path):
        PATH = path + '/' + p + '/'
        OUTNAME = path.split('/')[-2] + '_' + p
	run = True
	for f in os.listdir('.'):
	    if OUTNAME in f:
	        run = False
        with open(template, 'r') as f:
            new_file = f.read().replace('PATH', PATH)
            new_file = new_file.replace('OUTNAME', OUTNAME)

            nfilename = 'python/gentuple_' + p + ".py"
            with open(nfilename, 'w') as nf:
                nf.write(new_file)
        
	if run: os.system('cmsRun ' + nfilename)
        os.system('rm -rf ' + nfilename)
