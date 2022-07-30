from pyobigram.utils import sizeof_fmt,nice_time
import datetime
import time
import os

def text_progres(index,max):
	try:
		if max<1:
			max += 1
		porcent = index / max
		porcent *= 100
		porcent = round(porcent)
		make_text = ''
		index_make = 1
		make_text += '\n['
		while(index_make<21):
			if porcent >= index_make * 5: make_text+='▪'
			else: make_text+='▫'
			index_make+=1
		make_text += ']\n'
		return make_text
	except Exception as ex:
			return ''

def porcent(index,max):
    porcent = index / max
    porcent *= 100
    porcent = round(porcent)
    return porcent

def createDownloading(filename,totalBits,currentBits,speed,time,tid=''):
    msg = '💻Descargando_al_servidor💻 \n\n'
    msg+= '🧾NOMBRE🧾: ' + str(filename)+'\n'
    msg+= '💾TAMAÑO_TOTAL💾: ' + str(sizeof_fmt(totalBits))+'\n'
    msg+= '💽DESCARGADO💽: ' + str(sizeof_fmt(currentBits))+'\n'
    msg+= '✴️VELOCIDAD✴️: ' + str(sizeof_fmt(speed))+'/s\n'
    msg+= '🕐Tiempo: ' + str(datetime.timedelta(seconds=int(time))) +'\n\n'

    msg = '\n💻Descargando_al_servidor💻\n'
    msg += '🧾ARGUMENTO🧾: '+filename+'\n'
    msg += text_progres(currentBits,totalBits)+'\n'
    msg += '🤳PROGRESO🤳: '+str(porcent(currentBits,totalBits))+'%\n\n'
    msg += '💾TAMAÑO_TOTAL💾: '+sizeof_fmt(totalBits)+'\n\n'
    msg += '💽DESCARGADO💽: '+sizeof_fmt(currentBits)+'\n\n'
    msg += '✴️VELOCIDAD✴️: '+sizeof_fmt(speed)+'/s\n\n'
    msg += '🕐 Tiempo de Descarga: '+str(datetime.timedelta(seconds=int(time)))+'s\n\n'

    if tid!='':
        msg+= '/cancel_' + tid
    return msg
def createUploading(filename,totalBits,currentBits,speed,time,originalname=''):
    msg = '✅☁️SUBIENDO_A_LA_NUBE☁️✅\n\n'
    msg+= '🔖Nombre: ' + str(filename)+'\n'
    if originalname!='':
        msg = str(msg).replace(filename,originalname)
        msg+= '⏫Subiendo: ' + str(filename)+'\n'
    msg+= '💾TAMAÑO_TOTAL💾: ' + str(sizeof_fmt(totalBits))+'\n'
    msg+= '✅SUBIDO✅: ' + str(sizeof_fmt(currentBits))+'\n'
    msg+= ': ' + str(sizeof_fmt(speed))+'/s\n'
    msg+= '🕐Tiempo: ' + str(datetime.timedelta(seconds=int(time))) +'\n'

    msg = '✅☁️SUBIENDO_A_LA_NUBE☁️✅\n\n'
    msg += '🔖 Nombre: '+filename+'\n'
    if originalname!='':
        msg = str(msg).replace(filename,originalname)
        msg+= '🔖 Parte: ' + str(filename)+'\n'
    msg += text_progres(currentBits,totalBits)+'\n'
    msg += '🤳PROGRESO🤳: '+str(porcent(currentBits,totalBits))+'%\n\n'
    msg += '🗂 Total: '+sizeof_fmt(totalBits)+'\n\n'
    msg += '✅SUBIDO✅: '+sizeof_fmt(currentBits)+'\n\n'
    msg += '✴️VELOCIDAD✴️: '+sizeof_fmt(speed)+'/s\n\n'
    msg += '🕐 TIEMPO_DE_GRABACION: '+str(datetime.timedelta(seconds=int(time)))+'s\n\n'

    return msg
def createCompresing(filename,filesize,splitsize):
    msg = '🤜COMPRIMIENDO🤛 \n\n'
    msg+= '🔖Nombre: ' + str(filename)+'\n'
    msg+= '🗂Tamaño Total: ' + str(sizeof_fmt(filesize))+'\n'
    msg+= '📂Tamaño Partes: ' + str(sizeof_fmt(splitsize))+'\n'
    msg+= '💾Cantidad Partes: ' + str(round(int(filesize/splitsize)+1,1))+'\n\n'
    return msg
def createFinishUploading(filename,filesize,split_size,current,count,findex):
    msg = '✅ TAREAS TERMINADAS✅\n\n'
    msg+= '🧾NOMBRE🧾: ' + str(filename)+'\n'
    msg+= '💾TAMAÑO_TOTAL💾: ' + str(sizeof_fmt(filesize))+'\n'
    msg+= '🚦TAMAÑO_DE_ZIP🚦: ' + str(sizeof_fmt(split_size))+'\n'
    msg+= '📤PARTES_SUBIDAS📤: ' + str(current) + '/' + str(count) +'\n\n'
    msg+= '💢ELIMINAR_ARCHIVOS💢: ' + '/del_'+str(findex)
    return msg

def createFileMsg(filename,files):
    import urllib
    if len(files)>0:
        msg= '<b>☁️LINKS_DE_DESCARGA☁️</b>\n'
        for f in files:
            url = urllib.parse.unquote(f['directurl'],encoding='utf-8', errors='replace')
            #msg+= '<a href="'+f['url']+'">☁️' + f['name'] + '☁️</a>'
            msg+= "<a href='"+url+"'>☁️"+f['name']+'☁️</a>\n'
        return msg
    return ''

def createFilesMsg(evfiles):
    msg = '💸Archivos ('+str(len(evfiles))+')💸\n\n'
    i = 0
    for f in evfiles:
            try:
                fextarray = str(f['files'][0]['name']).split('.')
                fext = ''
                if len(fextarray)>=3:
                    fext = '.'+fextarray[-2]
                else:
                    fext = '.'+fextarray[-1]
                fname = f['name'] + fext
                msg+= '/txt_'+ str(i) + ' /del_'+ str(i) + '\n' + fname +'\n\n'
                i+=1
            except:pass
    return msg
def createStat(username,userdata,isadmin):
    from pyobigram.utils import sizeof_fmt
    msg = '🌟CONFIGURACION_ACTIVA🌟\n\n'
    msg+= '👤 USUARIO: @' + str(username)+'\n'
    msg+= '☁️User_nube: ' + str(userdata['moodle_user'])+'\n'
    msg+= '☁️Password_nube: ' + str(userdata['moodle_password']) +'\n'
    msg+= '🧭Host: ' + str(userdata['moodle_host'])+'\n'
    if userdata['cloudtype'] == 'moodle':
        msg+= '💽RepoID: ' + str(userdata['moodle_repo_id'])+'\n'
        msg+= '📟UpType: ' + str(userdata['uploadtype'])+'\n'
    msg += '🧾CloudType: ' + str(userdata['cloudtype']) + '\n'
    if userdata['cloudtype'] == 'cloud':
        msg+= '🏧Dir: /' + str(userdata['dir'])+'\n'
    msg+= 'TAMAÑO_DE_RARS : ' + sizeof_fmt(userdata['zips']*1024*1024) + '\n\n'
    msgAdmin = '❌'

    if isadmin:
        msgAdmin = '✅'
    msg+= '🦾Admin : ' + msgAdmin + '\n'
    proxy = '❌'
    if userdata['proxy'] !='':
       proxy = '✅'
    rename = '❌'
    if userdata['rename'] == 1:
       rename = '✅'
    msg+= '📝Rename : ' + rename + '\n'
    msg+= '🔌Proxy : ' + proxy + '\n'
    shorturl = (userdata['urlshort'] == 1)
    shortener = '❌'
    if shorturl:
       shortener = '✅'
    msg += '🔌ShortUrl : ' + shortener + '\n\n'
    msg+= '🀄NUBES AUTOCONFIGURADAS🀄: \n'
    msg+= 'EVA: /seteva\n'
    msg+= 'CURSOS: /setcursos\n'
    msg+= 'EDU: /setedu\n'
    msg+= 'UCLV: /setuclv\n'
    msg+= 'EVEA: /setevea\n\n'
    return msg