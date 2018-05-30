import csv, os, re

def main():
	headers = ["id", "address", "speaker", "age", "b_date", "r_date", "turn_min_2", "turn_min_1", "turn", "turn_plus_1", "turn_plus_2", "speech_act", "consistency", "utterance_type", "answer", "intonation", "syn_level", "connective_meaning", "annotation"]

	and_annot = []

	filelist = os.listdir(".\\data\\and_annot")
	for f in filelist:
		fname = "\\".join([os.getcwd(), "data\\and_annot", f])
		with open(fname) as csvfile:
			reader = csv.reader(csvfile)
			next(reader)
			for row in reader:
				row.append("AND")
				and_annot.append(row)
	
	or_annot = []
	
	filelist = os.listdir(".\\data\\or_annot")
	for f in filelist:
		fname = "\\".join([os.getcwd(), "data\\or_annot", f])
		with open(fname) as csvfile:
			reader = csv.reader(csvfile)
			next(reader)
			for row in reader:
				row.append("OR")
				or_annot.append(row)
	
	common_annot = []
		
	for row in or_annot:
		id = row[0]
		address = row[1]
		speaker = row[2]
		age = row[3]
		b_date = row[4]
		r_date = row[5]
		turn_min_2 = row[8]
		turn_min_1 = row[9]
		turn = row[10]
		turn_plus_1 = row[11]
		turn_plus_2 = row[12]
		speech_act = row[14]
		utterance_type = row[18]
		answer = "N" if row[19] == "NA" else row[19]
		intonation = row[20]
		syn_level = row[22]
		connective_meaning = row[23]
		consistency = "inconsistent" if row[17] == "EXC" else ("consistent" if row[17] == "ELS" else "") # EXC = inconsistent, ELS = consistent
		annotation = row[26]
		common_annot.append([id, address, speaker, age, b_date, r_date, turn_min_2, turn_min_1, turn, turn_plus_1, turn_plus_2, speech_act, consistency, utterance_type, answer, intonation, syn_level, connective_meaning, annotation])	
		
	for row in and_annot:
		id = row[0]
		address = re.search("/(Providence.+)", row[1]).group(1) + "/" + re.search("line +([0-9]+)", row[2]).group(1)
		speaker = row[3]
		age = row[4]
		b_date = row[6]
		r_date = row[7]
		turn_min_2 = row[8]
		turn_min_1 = row[9]
		turn = row[10]
		turn_plus_1 = row[11]
		turn_plus_2 = row[12]
		speech_act = row[14]
		consistency = "inconsistent" if row[15] == "1" else ("consistent" if row[15] == "0" else "")  # 1 = inconsistent, 0 = consistent
		utterance_type = row[16]
		answer = "N" if row[17] == "NA" else row[17]
		intonation = row[18]
		syn_level = row[20]
		connective_meaning = row[21]
		annotation = row[23]
		common_annot.append([id, address, speaker, age, b_date, r_date, turn_min_2, turn_min_1, turn, turn_plus_1, turn_plus_2, speech_act, consistency, utterance_type, answer, intonation, syn_level, connective_meaning, annotation])	
	
	merged_file = "providence_merged.csv"
	
	clean_data = clean_unannotated(common_annot, headers)
	
	with open(merged_file, "wb") as writefile:
		writer = csv.writer(writefile)
		writer.writerow(headers)
		writer.writerows(clean_data)
	
	print "------------------------------"
	print "The tables have been combined.\nMerged table saved to: %s" %(merged_file)
	print "------------------------------"
	

def clean_unannotated(data, headers):
	problematic_rows = []
	clean = []
	
	for row in data:
		if "" in row[11:]:
			problematic_rows.append(row)
		else:
			clean.append(row)
	problems_file = "providence_problem_rows.csv"
	with open(problems_file, "wb") as writefile:
		writer = csv.writer(writefile)
		writer.writerow(headers)
		writer.writerows(problematic_rows)
	
	print "------------------------------"
	print "There are %d problematic rows.\nThey have been saved to: %s" % (len(problematic_rows), problems_file)
	print "------------------------------"
	
	return clean
	
if __name__ == "__main__":
	main()