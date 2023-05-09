This is still a draft!

This is a dummy code to check the old work pipline at Mincs Lab, using codes written by Serge

it all the codes are copy-pasted from cytosim repo, with small modifications
1. dummy_code.cym.tpl is almost copy-paste from `bead.cym`
2. radom_analysis_code.py is a read-write code with nothing special
3. main.py is there to run a single code and it should do the rest. Not done yet! 
4. all the other scripts can be found on cytosim repo, or generated during the run 


the preconfig creates 15 different .cym files
1. there are three different values for cell radius
2. there are five different values for number of `particle` of radius 0.05
3. there is one value for balls which is two, Lol.
4. All the other parameters are fixed!

the go_sim.py & go_sim_lib.py 
1. reads `sim` file and the different config folders created in the last step
2. it runs each config file and create a folder for each one!

the scan.py
1. opens each directory
2. reads the command you give it
3. deals with each directory as working directory