#!/usr/bin/python

#
# def percent(num1, num2,dp):
# 	var = ' ({0:.'+str(dp)+'%}'
# 	print(var)
# 	return var.format((num1 / num2))+str(")")
#
# print(percent(123,442,2))


import urllib
import xmltodict

def homepage(request):
    file = urllib.urlopen('https://clinicaltrials.gov/ct2/show/NCT01119859?displayxml=true')
    data = file.read()
    file.close()

    data = xmltodict.parse(data)
    return render_to_response('test_template.html', {'data': data})


# import ftplib
# f = ftplib.FTP()
# f.connect("localhost")
# f.login()
# ls = []
# f.retrlines('MLSD', ls.append)
# for entry in ls:
#     print entry
