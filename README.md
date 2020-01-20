# This script is used to identify Structural Variant (SV) haplotypes in *Helianthus* SNP data.
### These scripts run on Python2.7, do NOT use Python3. 

The purpose of these scripts is to take a list of pre-determined SNPs that are diagnostic of certain structural variants (SVs) in the Helianthus genome, and check the diagnostic sites against sequenced samples with unknown SV haplotypes to identify which SVs your samples have. This script should work for both DNAseq and RNAseq data. The script uses two input files. A VCF of your samples, and a list of diagnostic sites for your SV. Diagnostic snp lists for each Helianthus SV have been previously generated and are [publicly available](https://github.com/owensgl/wild_gwas_2018/tree/master/MDS_outliers/Ha412HO).

There are multiple ways to run this script:
* You can run it to diagnose a single SV, or a list of SVs
* You can run it using either HanXRQ (recommended) or HaHO412 (results may be inaccurate using list diagnostic site lists generated in XRQ)

Files required to run the code are in: LINK TO CODE FOLDER
Test files can be found in:  LINK TO TEST FILE FOLDER

### How to run the code for a single SV haplotype:

To start the code, run the file "Run_Haplotypes.py"
* You will be prompted to input the name of a VCF file. For the test run, use "Test.vcf." Note that the code will fail in a few steps if the input name is misspelled.
* You will then be asked "Do you want to identify multiple structural variants (y/n)?" For a single haplotype test, enter n. 
* You will then be prompted to enter the name of the diagnostic site File. Use "Test_DS_sites.txt" for the test run. 
* Lastly, you'll be prompted for the reference genome. Choose HanXRQ (1) for the test file.

Assuming all went well, you should get an ouput that looks like this in the terminal:

###################################################
|                                                 |
|      sites in VCF: 101                          |
|      9.90 % of Diagnostic Sites match VCF       |
|      Non-Diagnostic VCF Sites: 91               |
|                                                 |
###################################################

* Line 1: how many sites were in the original VCF
* Line 2: what percentage of them were identified as diagnostic sites
* Line 3: the number of sites that were discarded (No match in the diagnostic site file).

Additionally, there should be a file in your working directory called "Test_DS_sites_HAPLOTYPES.txt." This file contains data on the analysis:

#Sample Name	INV0 Count	INV0 Probability	INV1 Count	Inv1 Probability	HET Count	HET Probability	NA Count	Total Sites	Most Likely Haplotype
#SAMPLE_1	7	69.9996536846	0	0.0	3	29.8170691995	0	10	INV0
#SAMPLE_2	0	0.0	3	29.8386669914	7	69.9996073231	0	10	HET
#SAMPLE_3	1	8.37095460012	8	79.9999146819	1	8.26357930227	0	10	INV1
#SAMPLE_4	4	39.9639071957	6	59.9979940047	0	0.0	0	10	INV1

* Column 1: Sample name
* Column 2: Number of diagnostic sites with haplotype 0 snps
* Column 3: Probability sample has haplotype 0.
* Column 4: Number of diagnostic sites with heterozygous snps
* Column 5: Probability sample is heterozygous.
* Column 6: Number of diagnostic sites with haplotype 2 snps
* Column 7: Probability sample has haplotype 2.
* Column 8: Count of diagnostic sites in the VCF that the sample has no data for.
* Column 9: Total diagnostic sites matched to VCF.
* Column 10: Prediction of most likely haplotype.

### How to run the script for multiple inversion haplotypes:

Run the script again, but this time select y/yes when it asks if you want to run multiple haplotypes.
* You will be prompted for a LIST of diagnostic file names, rather than a single diagnostic file. Use "list_of_DS_sites.txt" for the test files.
* This file contains the \n separated names of 3 other files in the folder:
  * test_DSfile_1.txt
  * test_DSfile_2.txt
  * test_DSfile_3.txt

* These are all the same file with a different name. They are also the same as the Test_DS_sites.txt file you input for the single haplotype code. The point is to check if they look the same.
* Everything else about the code runs the same way, except you should now have three output files instead of one.
