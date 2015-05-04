#!/usr/bin/env python
import re


output = "DIR:/rocket/ms120513,1604:18114,1426:15710,1605:15911,1427:16414,1606:15912,1607:1827,1640:1697,1608:16414,1609:2148,1645:16617,1646:14512,1647:13910,1648:17713,1649:17012,1210:16716,1211:14810,1212:1685,1213:18414,1214:15514,1215:16312,1216:1588,1217:15716,1250:1629,1218:1509,1219:18213,1251:14913,1252:20117,1253:19515,1254:18422,1610:16511,1255:1577,1256:14614,1612:1698,1257:19618,1613:17110,1614:30316,1258:21614,1259:17823,1615:15913,1616:1659,1617:18413,1618:15711,1650:15611,1619:20710,1220:20112,1221:1589,1400:1647,1222:17716,1223:15712,1401:16313,1402:15213,1224:1296,1225:17512,1403:18213,1226:1617,1404:1517,1405:1616,1260:21026,1406:17517,1407:19215,1261:15410,1229:16712,1408:18212,1262:14519,1409:1709,1620:1449,false:4070376,1621:18811,1622:1589,1267:16614,1623:1628,1624:1657,1625:1738,1626:18415,1627:15313,1628:17811,1629:15610,1809:97487,1843:91182,1847:92986,1410:16912,1411:1656,1412:16315,1414:17512,1415:1375,1416:19017,1417:18011,1630:15814,1631:17212,1632:14113,1810:94488,1633:1646,1811:95490,1634:14611,1812:95466,1635:16511,1813:89074,1636:1468,1814:93482,1815:90387,1638:16712,1816:94581,1639:1407,1817:97585,1200:16911,1854:91894,1201:1713,1202:1579,1203:15612,1204:1468,1205:92743,1206:15816,1207:15915,1208:15415,1209:1759,1601:17214,1423:16020,1245:1428,1602:17313,1424:16615,1603:17012,1425:16618,1247:1589,,STAY:92744,MOVES:33704,NO_MOVE:18653"
print output

#def parse():
	#farm = output[0]
	#print "Farm Number", farm[14:18]
	#movement = output[-3:]
	#print movement

	#for farm_data in output:
	#	print farm_data
	#	foo = re.findall(r'(\d+):(\d+)' + u'\u0001' + '(\d+)', farm_data)
	#	print foo

#parse()

class Parser():
	""" Parses farm data """
	def __init__(self):
		self.data = dict()

	def getStay(self):
		return self.data['STAY']
	
	def getMove(self):
		return self.data['MOVES']

	def getNoMove(self):
		return self.data['NO_MOVE']

	def getFarms(self):
		return self.data['FARM']

	def parse(self, line):
		 match = re.search(r'STAY:(\d+),MOVES:(\d+),NO_MOVE:(\d+)', line)
		 self.data['STAY'] = match.group(1)
		 self.data['MOVES'] = match.group(2)
		 self.data['NO_MOVE'] = match.group(3)
		 match_farm = re.findall(r'(\d+):(\d+)' + u'\u0001' + '(\d+)', line)
		 self.data['FARM'] = match_farm
	
	def getTotalMoves(self):
		total = 0
		for i in self.getFarms():
			total += int(i[1])
		return total
	
	def getTotalNoMove(self):
		total = 0
		for i in self.getFarms():
			total += int(i[2])
		return total


if __name__ == '__main__':
	p = Parser()
	p.parse(output)
	print p.getStay()
	print p.getFarms()
	print p.getTotalMoves()
	print p.getTotalNoMove()
	pass
