#!/usr/bin/python
# -*- coding: utf-8 -*-
import argparse
import pandas as pd
import json


def read_data(file_path):
	train = pd.read_csv(file_path, header=0, encoding='big5',\
                    			delimiter=',', quoting=3)
	data = []
	num = train['date'].size
	for i in xrange(0, num):
		if (train['isHoliday'][i].strip() == u'是') and \
			((train['holidayCategory'][i].strip() != u'星期六、星期日') and \
			(train['holidayCategory'][i].strip() != u'星期日')):
		
			if type(train['name'][i]) != float:
				name = train['name'][i].strip()
			else:
				name = train['holidayCategory'][i].strip()
			data.append({'date': train['date'][i].strip().decode('utf8'), \
						 'name': name.encode('utf8'), \
						 'is_holiday': train['isHoliday'][i].strip().encode('utf8')})
	return data


def run():
    parser = argparse.ArgumentParser(description='Print argument')
    parser.add_argument("-f", "--file", help="set path of file")
    args = parser.parse_args()
    data = read_data(args.file)

    with open('data.json', 'w') as json_file:
        json.dump(data, json_file, indent=4, ensure_ascii=False, encoding='utf-8')
    json_file.close()


if __name__ == '__main__':
    run()