##Input File
#This file directs the user directly to the haplotyping script if they're only using a single input file, or for those with many input files, to the haplotyping script through a script that iterates the haplotyping script for many input files.

input_VCF = raw_input("Name of input VCF: ")#allows the user to enter their VCF file name
start = raw_input("Do you want to identify multiple structural variants? (y/n): ")#which version of the script does the user want to run? A single haplotype (n), or many haplotypes (y)?
if start == "y" or start == "yes":#if yes, direct the user to the iterations script
    files_list = raw_input("Name of file containing diagnostic site files to run: ")#Input the list of DS site file names as "files_list"
    execfile("Iterations.py")#run the iterations.py file, which loops the haplotyping file for all inputs
elif start == "n" or start == "no":#if no, direct the user to the main script that only runs a single time
    input_diagnostic_site_file = raw_input("Name of Diagnostic Site File: ")#Prompt the diagnostic site file name
    iterations_script = "off"#set the iterations parameter to "off", so the use of iterations can be identified in the main script
    execfile("Main_Script.py")#run the haplotyping script a single time
else:
    print "Fatal Error:", start, "is not a recognized option.\n"#if the option is not y/yes or n/no, then the user will be ejected from the code. I tried to make this a loop that would prompt the user to keep trying, but it causes random bugs in other parts of the script and is generally very unweildy..
    exit()