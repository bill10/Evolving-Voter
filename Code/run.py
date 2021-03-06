import numpy as np
import subprocess

# Path of igraph
# IGRAPH_INCLUDE='/usr/local/Cellar/igraph/0.7.1/include/igraph'#/usr/local/include/igraph
# IGRAPH_LIB='/usr/local/Cellar/igraph/0.7.1/lib'#/usr/local/lib
count=0;
node=1000; # number of nodes
edge=2000; # number of edges
dt=1; # save results every dt steps
degree=4;
smallworld=0.1 # rewiring probability in the Watts-Strogatz network
g=2; # number of opinions
U0=1.0/g*np.ones(g,); # list of initial densities
U0[-1]=1-sum(U0[:-1]);
#system('g++ main.cpp Dynamic_Voter.h Dynamic_Voter.cpp Node.cpp Edge.cpp Random1.cpp -O3 -Wall -I/usr/include/igraph -L/usr/lib/x86_64-linux-gnu -ligraph -o DynamicVoter');
#subprocess.call('g++ main.cpp Dynamic_Voter.cpp Node.cpp Edge.cpp Random1.cpp -O3 -Wall -o DynamicVoter', shell=True);
for realization in range(0,8):
    for mode in [1]: # 1-rewire to random. 2-rewire to same.
        for gamma in [0]:
            for alpha in [0.4]:
                    # cmd='LD_PRELOAD=/usr/lib/x86_64-linux-gnu/libigraph.so.0 ./src/DynamicVoter -n {} -m {} -a {} -r {} -g {} -u {}'.format(node,edge,alpha,mode,gamma,g);
                    cmd='./DynamicVoter -n {} -m {} -a {} -r {} -g {} -t {} -u {}'.format(node,edge,alpha,mode,gamma,dt,g);
                    for i in xrange(g):
                        cmd=cmd+' '+str(U0[i]);
                    print cmd
                    subprocess.call(cmd, shell=True);
                    count=count+1;

print str(count)+' files submitted.';
print 'Mission Complete!';
