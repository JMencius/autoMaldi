# -*- coding: utf-8 -*-
"""
Created on Wed Aug 19 14:28:54 2020

@author: nujiz
Original idea from ZYXyoudaoli
@Software name: Madli-TOF Oject-oriented Programming (MOOP) v5
@Developong software: Python3.7.3 in Spyder4
@Developing hardware: Microsoft Surface Pro 3  Intel Core i5-4300U 4G RAM
@If you have any question please contact: acemencius@gmail.com
"""

import os
import time

class Maldi_file:
    def __init__(self,name,peak):
        self.name = name
        self.peak = peak
    
    def read(self):
        line_count = 0
        m = 0
        m_p = 0
        with open(self.name,'r',errors="ignore") as f:
            for line in f:
                #Skip the appendix
                if line_count < 2:
                    line_count += 1
                    continue
            
                chop_line = line.split("\t")
                real_peak = float(chop_line[0])
                #pending range
                if (self.peak - 0.5) <= real_peak <= (self.peak + 0.5):
                    value = float(chop_line[1].strip("\n"))
                    if value > m:
                        m = value
                        m_p = real_peak
        return [m, m_p]

if __name__ == "__main__":

    #Check current folder
    all_file = os.listdir()
    filtered_file = []
    for i in all_file:
        if os.access(i, os.R_OK):
            print(i + " access granted.")
            if os.path.splitext(i)[1] != ".txt":
                print(i + " is not a txt file. Automatically removed")
            else:
                filtered_file.append(i)
        else:
            print(i + " access denied!!!")
            
    if len(filtered_file) == 0:
        print("No files. Please check the director!")
        leave = input("Press any key to leave")
        raise ValueError
    else:
        print("Total filenumber: " + str(len(filtered_file)))
    
    #input peak numbers
    peaks = []
    peak_numbers = int(eval(input("How many peaks: ")))
    print("Please input your peak one by one")
    i = 0
    while i < peak_numbers:
        try:
            a = eval(input("Peak please: "))
        except:
            print("Wrong number, please try again!")
        else:
            peaks.append(a)
            i += 1
    confirm_mark = input("Peaks are " + ','.join([str(i) for i in peaks]) + ' [Y/N]')
    if confirm_mark == 'N' or confirm_mark == 'n':
        leave = input("Press any key to leave and restart again.")
        raise ValueError
    elif confirm_mark != 'Y' and confirm_mark != 'y':
        leave = input("Key value error press any key to leave.")
        raise ValueError
    
    #Preparation
    start_time = time.time()
    summary = open("summmary.txt", 'w')
    exact_peak = open("Exact_peak.txt", 'w')
    
    summary.write("Filename")
    exact_peak.write("Filename")
    for i in peaks:
        summary.write("\t" + str(i))
        exact_peak.write("\t" + str(i))
    summary.write('\n')
    exact_peak.write('\n')
    
    #Analysis files and output
    for i in filtered_file:
        w1 = ""
        w2 = ""
        w1 += i.strip(".txt")
        w2 += i.strip(".txt")
        m1 = []
        m2 = []
        for j in peaks:
            r = Maldi_file(i, j).read()
            m1.append(r[0])
            m2.append(r[1])
        for c in m1:
            w1 += '\t' + str(c / sum(m1))
        for c in m2:
            w2 += '\t' + str(c)
        w1 += '\n'
        w2 += '\n'
        summary.write(w1)
        exact_peak.write(w2)
        
        print(i + " finish process and written to files.")
    summary.close()
    exact_peak.close()
    
    #Post-process
    end_time = time.time()
    total_time = (end_time - start_time)
    print("SUCCESS!!!")
    print("Total processing time: " + str(total_time) + ' s')
    leave = input("Press any key to leave")
            
        
        
    
    
            
        
            
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    