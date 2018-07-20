import requests
from pyquery import PyQuery as pq

class invoice():
	def __init__(self, date):
		self.url = 'https://www.etax.nat.gov.tw/etw-main/web/ETW183W2_{}'.format(date)#10605
		self.req = requests.get(self.url)
	def getprize(self):
		if self.req.status_code == 200:
			self.req.encoding = 'utf-8'
			self.get = pq(self.req.text)
			self.tmpdict, self.tmpnum, self.invoiceDict = {}, 0, {}
		else:
			return {'status': 'error'}
		for x in self.get('tr')('td').items():
			tmpdict = {}
			content, headers = x.text(), x.attr('headers')
			self.tmpnum += 1
			if headers in ['specialPrize', 'grandPrize', 'firstPrize']:
				if self.tmpnum % 2 == 0:
					if '、' in content:
						content = content.split('、')
					store = dict(number=content)
					self.invoiceDict[headers] = store
				else:
					store = dict(desc=content)
				self.invoiceDict[headers].update(store)
			elif headers in ['twoPrize', 'threeAwards', 'fourPrizes', 'fivePrize', 'sixPrize', 'addSixPrize']:
				if headers == 'addSixPrize':
					if '、' in content:
						content = content.split('、')
					store = dict(number=content)
				else:
					store = dict(desc=content)
				self.invoiceDict[headers] = store
		return self.invoiceDict
