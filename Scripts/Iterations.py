rg = input("Please indicate whether you are using the Ha412(0) or HanXRQ(1) reference genome (0/1): ")
iterations_script = "on" #don't ask each iteration which reference genome to use in the main script.
if rg ==1:#the two reference genome loci are contained in different columns of the input text file. This sets a global parameter based on the reference genome the user is working in:
    Ref_Genome_Chr_Col = 2#XRQ columns
    Ref_Genome_Pos_Col = 3
elif rg ==0:
    Ref_Genome_Chr_Col = 0#412 columns
    Ref_Genome_Pos_Col = 1
else:
    print "Fatal Error:", rg, "is not a recognized Option. Please try again."
    exit()

List_Of_Files = open(files_list, 'r')#input a file with the list of input DS site files to use. Uses the object defined by user input in the Run_Haplotypes.py file.
for line in List_Of_Files:#for each file name,
    line = line.strip()#strip the endline character
    t = str(line)#make a temporary object called t that represents the line-th row of the name list
    input_diagnostic_site_list = t#define the parameter "input_diagnostic_site_list" as the temporary line
    execfile("Main_Script.py")#execute the main script with that input file, then repeat for all lines