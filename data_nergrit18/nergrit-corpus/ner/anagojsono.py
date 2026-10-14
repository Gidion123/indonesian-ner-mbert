#Global Vars
import json
from ast import literal_eval

per=[]
nor=[]
fac=[]
org=[]
gpe=[]
loc=[]
prd=[]
evt=[]
woa=[]
law=[]
lan=[]
dat=[]
tim=[]
prc=[]
mon=[]
qty=[]
ordi=[]
crd=[]
reg=[]

# for cleaning global vars
def varkosong():
	global per
	global nor
	global fac
	global org
	global gpe
	global loc
	global prd
	global evt
	global woa
	global law
	global lan
	global dat
	global tim
	global prc
	global mon
	global qty
	global ordi
	global crd
	global reg

	per=[]
	nor=[]
	fac=[]
	org=[]
	gpe=[]
	loc=[]
	prd=[]
	evt=[]
	woa=[]
	law=[]
	lan=[]
	dat=[]
	tim=[]
	prc=[]
	mon=[]
	qty=[]
	ordi=[]
	crd=[]
	reg=[]

	
# function json it!
def jsonkansaja(tulisan):
	global per
	global nor
	global fac
	global org
	global gpe
	global loc
	global prd
	global evt
	global woa
	global law
	global lan
	global dat
	global tim
	global prc
	global mon
	global qty
	global ordi
	global crd
	global reg
	tulisan = json.loads( tulisan )
	# convert text to tuple
	tp = literal_eval(tulisan)
	# count items in tuple
	i = len(tp)

	print (tp)
	print ("\n")


	varkosong()
	for x in range(0, i):

		if ( tp[x]['type'] == 'PER') :		
			varx = tp[x]['text']
			per.append(varx)
		if ( tp[x]['type'] == 'NOR') :		
			varx = tp[x]['text']
			nor.append(varx)
		if ( tp[x]['type'] == 'FAC') :		
			varx = tp[x]['text']
			fac.append(varx)
		if ( tp[x]['type'] == 'ORG') :		
			varx = tp[x]['text']
			org.append(varx)
		if ( tp[x]['type'] == 'GPE') :		
			varx = tp[x]['text']
			gpe.append(varx)
		if ( tp[x]['type'] == 'LOC') :		
			varx = tp[x]['text']
			loc.append(varx)
		if ( tp[x]['type'] == 'PRD') :		
			varx = tp[x]['text']
			prd.append(varx)
		if ( tp[x]['type'] == 'EVT') :		
			varx = tp[x]['text']
			evt.append(varx)
		if ( tp[x]['type'] == 'WOA') :		
			varx = tp[x]['text']
			woa.append(varx)
		if ( tp[x]['type'] == 'LAW') :		
			varx = tp[x]['text']
			law.append(varx)
		if ( tp[x]['type'] == 'LAN') :		
			varx = tp[x]['text']
			lan.append(varx)
		if ( tp[x]['type'] == 'DAT') :		
			varx = tp[x]['text']
			dat.append(varx)
		if ( tp[x]['type'] == 'TIM') :		
			varx = tp[x]['text']
			tim.append(varx)
		if ( tp[x]['type'] == 'PRC') :		
			varx = tp[x]['text']
			prc.append(varx)
		if ( tp[x]['type'] == 'MON') :		
			varx = tp[x]['text']
			mon.append(varx)
		if ( tp[x]['type'] == 'QTY') :		
			varx = tp[x]['text']
			qty.append(varx)
		if ( tp[x]['type'] == 'ORD') :		
			varx = tp[x]['text']
			ordi.append(varx)
		if ( tp[x]['type'] == 'crd') :		
			varx = tp[x]['text']
			crd.append(varx)
		if ( tp[x]['type'] == 'REG') :		
			varx = tp[x]['text']
			reg.append(varx)
	
	per = '{"Person": ' + json.dumps(per) + '}'
	nor = '{"PoliticalOrg": ' + json.dumps(nor) + '}'
	fac = '{"Facility": ' + json.dumps(fac) + '}'
	org = '{"Company": ' + json.dumps(org) + '}'
	gpe = '{"GeopoliticalEnt": ' + json.dumps(gpe) + '}'
	loc = '{"Location": ' + json.dumps(loc) + '}'
	prd = '{"Product": ' + json.dumps(prd) + '}'
	evt = '{"Event": ' + json.dumps(evt) + '}'
	woa = '{"WoArt": ' + json.dumps(woa) + '}'
	law = '{"Law": ' + json.dumps(law) + '}'
	lan = '{"Language": ' + json.dumps(lan) + '}'
	dat = '{"Date": ' + json.dumps(dat) + '}'
	tim = '{"Time": ' + json.dumps(tim) + '}'
	prc = '{"Percentage": ' + json.dumps(prc) + '}'
	mon = '{"Money": ' + json.dumps(mon) + '}'
	qty = '{"Quantity": ' + json.dumps(qty) + '}'
	ordi = '{"Ordinal": ' + json.dumps(ordi) + '}'
	crd = '{"Cardinal": ' + json.dumps(crd) + '}'
	reg = '{"Religion": ' + json.dumps(reg) + '}'		

	per = json.loads( per )
	nor = json.loads( nor )
	fac = json.loads( fac )
	org = json.loads( org )
	gpe = json.loads( gpe )
	loc = json.loads( loc )
	prd = json.loads( prd )
	evt = json.loads( evt )
	woa = json.loads( woa )
	law = json.loads( law )
	lan = json.loads( lan )
	dat = json.loads( dat )
	tim = json.loads( tim )
	prc = json.loads( prc )
	mon = json.loads( mon )
	qty = json.loads( qty )
	ordi = json.loads( ordi )
	crd = json.loads( crd )
	reg = json.loads( reg )
	
	
	res = {}
	res.update ( per )
	res.update ( nor )
	res.update ( fac )
	res.update ( org )
	res.update ( gpe )
	res.update ( loc )
	res.update ( prd )
	res.update ( evt )
	res.update ( woa )
	res.update ( law )
	res.update ( lan )
	res.update ( dat )
	res.update ( tim )
	res.update ( prc )
	res.update ( mon )
	res.update ( qty )
	res.update ( ordi )
	res.update ( crd )
	res.update ( reg )
	

	# Throw away escape encodings
	# Using json.dumps
	res = json.dumps( res )
	
	print ( res )
	return res

	#clear memory
	res=''
	esce=None
	esce2=None
	varkosong()